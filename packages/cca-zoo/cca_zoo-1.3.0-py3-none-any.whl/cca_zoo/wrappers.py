import copy
import itertools
from abc import abstractmethod
from typing import Tuple, List, Union

import numpy as np
import numpy.ma as ma
import pandas as pd
import tensorly as tl
from joblib import Parallel, delayed
from scipy.linalg import block_diag, eigh
from scipy.linalg import sqrtm
from sklearn.base import BaseEstimator
from sklearn.metrics.pairwise import pairwise_kernels
from tensorly.decomposition import parafac

import cca_zoo.data
import cca_zoo.innerloop
import cca_zoo.plot_utils


# from hyperopt import fmin, tpe, Trials

class _CCA_Base(BaseEstimator):
    """
    A class used as the base for methods in the package. Allows methods to inherit fit_transform, predict_corr, and gridsearch_fit
    when only fit (and transform where it is different to the default) is provided.

    :param latent_dims: number of latent dimensions to learn
    """

    @abstractmethod
    def __init__(self, latent_dims: int = 1):
        """
        Constructor for _CCA_Base

        """
        self.weights_list = None
        self.train_correlations = None
        self.latent_dims = latent_dims

    @abstractmethod
    def fit(self, *views: Tuple[np.ndarray, ...]):
        """
        Fits a given model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        """
        pass
        return self

    def transform(self, *views: Tuple[np.ndarray, ...], **kwargs):
        """
        Transforms data given a fit model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param kwargs: any additional keyword arguments required by the given model
        """
        transformed_views = []
        for i, view in enumerate(views):
            transformed_view = np.ma.array((view - self.view_means[i]) @ self.weights_list[i])
            transformed_views.append(transformed_view)
        return transformed_views

    def fit_transform(self, *views: Tuple[np.ndarray, ...], **kwargs):
        """
        Fits and then transforms the training data

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param kwargs: any additional keyword arguments required by the given model
        :rtype: Tuple[np.ndarray, ...]
        """
        return self.fit(*views).transform(*views, **kwargs)

    def predict_corr(self, *views: Tuple[np.ndarray, ...], **kwargs) -> np.ndarray:
        """
        Predicts the correlation for the given data using the fit model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param kwargs: any additional keyword arguments required by the given model
        :return: all_corrs: an array of the pairwise correlations (k,k,self.latent_dims) where k is the number of views
        :rtype: np.ndarray
        """
        # Takes two views and predicts their out of sample correlation using trained model
        transformed_views = self.transform(*views, **kwargs)
        all_corrs = []
        for x, y in itertools.product(transformed_views, repeat=2):
            all_corrs.append(np.diag(ma.corrcoef(x.T, y.T)[:self.latent_dims, self.latent_dims:]))
        all_corrs = np.array(all_corrs).reshape((len(views), len(views), self.latent_dims))
        return all_corrs

    def demean_data(self, *views: Tuple[np.ndarray, ...]):
        """
        Removes the mean of the training data for each view and stores it

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :return: train_views: the demeaned numpy arrays to be used to fit the model
        :rtype: Tuple[np.ndarray, ...]
        """
        train_views = []
        self.view_means = []
        for view in views:
            self.view_means.append(view.mean(axis=0))
            train_views.append(view - view.mean(axis=0))
        return train_views

    def gridsearch_fit(self, *views: Tuple[np.ndarray, ...], K=None, param_candidates=None, folds: int = 5,
                       verbose: bool = False,
                       jobs: int = 0,
                       plot: bool = False):
        """
        Implements a gridsearch over the parameters in param_candidates and returns a model fit with the optimal parameters
        in cross validation (measured by sum of correlations).

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param K: observation matrix which can be used by GCCA
        :param param_candidates:
        :param folds: number of cross-validation folds
        :param verbose: print results of training folds
        :param jobs: number of jobs. If jobs>1 then the function can use parallelism
        :param plot: produce a hyperparameter surface plot
        """
        if verbose:
            print('cross validation', flush=True)
            print('number of folds: ', folds, flush=True)

        # Set up an array for each set of hyperparameters
        assert (len(param_candidates) > 0)
        param_names = list(param_candidates.keys())
        param_values = list(param_candidates.values())
        param_combinations = list(itertools.product(*param_values))

        param_sets = []
        for param_set in param_combinations:
            param_dict = {}
            for i, param_name in enumerate(param_names):
                param_dict[param_name] = param_set[i]
            param_sets.append(param_dict)

        cv = _CrossValidate(self, folds=folds, verbose=verbose)

        if jobs > 0:
            out = Parallel(n_jobs=jobs)(delayed(cv.score)(*views, **param_set, K=K) for param_set in param_sets)
        else:
            out = [cv.score(*views, **param_set) for param_set in param_sets]
        cv_scores, cv_stds = zip(*out)
        max_index = cv_scores.index(max(cv_scores))

        if verbose:
            print('Best score : ', max(cv_scores), flush=True)
            print('Standard deviation : ', cv_stds[max_index], flush=True)
            print(param_sets[max_index], flush=True)

        self.cv_results_table = pd.DataFrame(zip(param_sets, cv_scores, cv_stds), columns=['params', 'scores', 'std'])
        self.cv_results_table = self.cv_results_table.join(pd.json_normalize(self.cv_results_table.params))
        self.cv_results_table.drop(columns=['params'], inplace=True)

        if plot:
            cca_zoo.plot_utils.cv_plot(cv_scores, param_sets, self.__class__.__name__)

        self.set_params(**param_sets[max_index])
        self.fit(*views)
        return self

    """
    def bayes_fit(self, *views: Tuple[np.ndarray, ...], space=None, folds: int = 5, verbose=True):
        :param views: numpy arrays separated by comma e.g. fit(view_1,view_2,view_3)
        :param space:
        :param folds: number of folds used for cross validation
        :param verbose: whether to return scores for each set of parameters
        :return: fit model with best parameters
        trials = Trials()

        cv = CrossValidate(self, folds=folds, verbose=verbose)

        best_params = fmin(
            fn=cv.score(*views),
            space=space,
            algo=tpe.suggest,
            max_evals=100,
            trials=trials,
        )
        self.set_params(**param_sets[max_index])
        self.fit(*views)
        return self
    """


class MCCA(_CCA_Base, BaseEstimator):
    """
    A class used to fit MCCA model. For more than 2 views, MCCA optimizes the sum of pairwise correlations.

    :Example:

    >>> from cca_zoo.wrappers import MCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = MCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None):
        """
        Constructor for MCCA

        :param latent_dims: number of latent dimensions
        :param c: list of regularisation parameters for each view (between 0:CCA and 1:PLS)
        """
        super().__init__(latent_dims=latent_dims)
        self.c = c

    def check_params(self):
        if self.c is None:
            self.c = [0] * self.n_views

    def fit(self, *views: Tuple[np.ndarray, ...], ):
        """
        Fits an MCCA model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        """
        self.n_views = len(views)
        self.check_params()
        assert (len(self.c) == len(views)), 'c requires as many values as #views'
        train_views, C, D = self.setup_gevp(*views)
        self.alphas = self.solve_gevp(C, D)
        self.score_list = [train_view @ eigvecs_ for train_view, eigvecs_ in zip(train_views, self.alphas)]
        self.weights_list = [weights / np.linalg.norm(score) for weights, score in zip(self.alphas, self.score_list)]
        self.score_list = [train_view @ weights for train_view, weights in zip(train_views, self.weights_list)]
        self.train_correlations = self.predict_corr(*views)
        return self

    def setup_gevp(self, *views: Tuple[np.ndarray, ...]):
        train_views = self.demean_data(*views)
        all_views = np.concatenate(train_views, axis=1)
        C = all_views.T @ all_views
        # Can regularise by adding to diagonal
        D = block_diag(*[(1 - self.c[i]) * m.T @ m + self.c[i] * np.eye(m.shape[1]) for i, m in enumerate(train_views)])
        C -= block_diag(*[view.T @ view for view in train_views]) - D
        self.splits = np.cumsum([0] + [view.shape[1] for view in train_views])
        return train_views, C, D

    def solve_gevp(self, C, D):
        n = D.shape[0]
        [eigvals, eigvecs] = eigh(C, D, subset_by_index=[n - self.latent_dims, n - 1])
        # sorting according to eigenvalue
        idx = np.argsort(eigvals, axis=0)[::-1][:self.latent_dims]
        eigvecs = eigvecs[:, idx].real
        eigvecs = [eigvecs[split:self.splits[i + 1]] for i, split in enumerate(self.splits[:-1])]
        return eigvecs


class KCCA(MCCA):
    """
    A class used to fit KCCA model.

    :Example:

    >>> from cca_zoo.wrappers import KCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = KCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, kernel: List[Union[float, callable]] = None,
                 gamma: List[float] = None,
                 degree: List[float] = None, coef0: List[float] = None,
                 kernel_params: List[dict] = None, eps=1e-3):
        """
        :param latent_dims: number of latent dimensions
        :param c: list of regularisation parameters for each view (between 0:CCA and 1:PLS)
        :param kernel: list of kernel mappings used internally. This parameter is directly passed to :class:`~sklearn.metrics.pairwise.pairwise_kernel`. If element of `kernel` is a string, it must be one of the metrics in `pairwise.PAIRWISE_KERNEL_FUNCTIONS`. Alternatively, if element of `kernel` is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two rows from X as input and return the corresponding kernel value as a single number. This means that callables from :mod:`sklearn.metrics.pairwise` are not allowed, as they operate on matrices, not single samples. Use the string identifying the kernel instead.
        :param gamma: list of gamma parameters for the RBF, laplacian, polynomial, exponential chi2 and sigmoid kernels. Interpretation of the default value is left to the kernel; see the documentation for sklearn.metrics.pairwise. Ignored by other kernels.
        :param degree: list of degree parameters of the polynomial kernel. Ignored by other kernels.
        :param coef0: list of zero coefficients for polynomial and sigmoid kernels. Ignored by other kernels.
        :param kernel_params: list of additional parameters (keyword arguments) for kernel function passed as callable object.
        :param eps: epsilon value to ensure stability
        """
        super().__init__(latent_dims=latent_dims)
        self.kernel_params = kernel_params
        self.gamma = gamma
        self.coef0 = coef0
        self.kernel = kernel
        self.degree = degree
        self.c = c
        self.eps = eps

    def check_params(self):
        if self.kernel is None:
            self.kernel = ['linear'] * self.n_views
        if self.gamma is None:
            self.gamma = [None] * self.n_views
        if self.coef0 is None:
            self.coef0 = [1] * self.n_views
        if self.degree is None:
            self.degree = [1] * self.n_views
        if self.c is None:
            self.c = [0] * self.n_views

    def _get_kernel(self, view, X, Y=None):
        if callable(self.kernel):
            params = self.kernel_params[view] or {}
        else:
            params = {"gamma": self.gamma[view],
                      "degree": self.degree[view],
                      "coef0": self.coef0[view]}
        return pairwise_kernels(X, Y, metric=self.kernel[view],
                                filter_params=True, **params)

    def setup_gevp(self, *views: Tuple[np.ndarray, ...]):
        """
        Generates the left and right hand sides of the generalized eigenvalue problem

        :param views:
        """
        self.train_views = self.demean_data(*views)
        kernels = [self._get_kernel(i, view) for i, view in enumerate(self.train_views)]
        C = np.hstack(kernels).T @ np.hstack(kernels)
        # Can regularise by adding to diagonal
        D = block_diag(
            *[(1 - self.c[i]) * kernel @ kernel.T + self.c[i] * kernel for i, kernel in enumerate(kernels)])
        C -= block_diag(*[k.T @ k for k in kernels]) - D
        D_smallest_eig = min(0, np.linalg.eigvalsh(D).min()) - self.eps
        D = D - D_smallest_eig * np.eye(D.shape[0])
        self.splits = np.cumsum([0] + [kernel.shape[1] for kernel in kernels])
        return kernels, C, D

    def transform(self, *views: Tuple[np.ndarray, ...], ):
        """
        Transforms data given a fit KCCA model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param kwargs: any additional keyword arguments required by the given model
        """
        Ktest = [self._get_kernel(i, train_view, Y=test_view - self.view_means[i]) for i, (train_view, test_view) in
                 enumerate(zip(self.train_views, views))]
        transformed_views = [test_kernel @ self.alphas[i] for i, test_kernel in enumerate(Ktest)]
        return transformed_views


class GCCA(_CCA_Base, BaseEstimator):
    """
    A class used to fit GCCA model. For more than 2 views, GCCA optimizes the sum of correlations with a shared auxiliary vector

    :Example:

    >>> from cca_zoo.wrappers import GCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = GCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, view_weights: Tuple[float, ...] = None):
        """
        Constructor for GCCA

        :param latent_dims: number of latent dimensions
        :param c: regularisation between 0 (CCA) and 1 (PLS)
        :param view_weights: list of weights of each view
        """
        super().__init__(latent_dims=latent_dims)
        self.c = c
        self.view_weights = view_weights

    def fit(self, *views: Tuple[np.ndarray, ...], K: np.ndarray = None):
        """
        Fits a GCCA model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param K: observation matrix. Binary array with (k,n) dimensions where k is the number of views and n is the number of samples 1 means the data is observed in the corresponding view and 0 means the data is unobserved in that view.
        """
        if self.c is None:
            self.c = [0] * len(views)
        assert (len(self.c) == len(views)), 'c requires as many values as #views'
        if self.view_weights is None:
            self.view_weights = [1] * len(views)
        if K is None:
            # just use identity when all rows are observed in all views.
            K = np.ones((len(views), views[0].shape[0]))
        train_views = self.demean_observed_data(*views, K=K)
        Q = []
        for i, (view, view_weight) in enumerate(zip(train_views, self.view_weights)):
            view_cov = view.T @ view
            view_cov = (1 - self.c[i]) * view_cov + self.c[i] * np.eye(view_cov.shape[0])
            Q.append(view_weight * view @ np.linalg.inv(view_cov) @ view.T)
        Q = np.sum(Q, axis=0)
        Q = np.diag(np.sqrt(np.sum(K, axis=0))) @ Q @ np.diag(np.sqrt(np.sum(K, axis=0)))
        n = Q.shape[0]
        [eigvals, eigvecs] = eigh(Q, subset_by_index=[n - self.latent_dims, n - 1])
        idx = np.argsort(eigvals, axis=0)[::-1]
        eigvecs = eigvecs[:, idx].real
        self.eigvals = eigvals[idx].real
        self.weights_list = [np.linalg.pinv(view) @ eigvecs[:, :self.latent_dims] for view in train_views]
        self.score_list = [view @ self.weights_list[i] for i, view in enumerate(train_views)]
        self.train_correlations = self.predict_corr(*views)
        return self

    def demean_observed_data(self, *views: Tuple[np.ndarray, ...], K):
        """
        Since most methods require zero-mean data, demean_data() is used to demean training data as well as to apply this
        demeaning transformation to out of sample data

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param K: observation matrix. Binary array with (k,n) dimensions where k is the number of views and n is the number of samples
        1 means the data is observed in the corresponding view and 0 means the data is unobserved in that view.
        """
        train_views = []
        self.view_means = []
        for i, (observations, view) in enumerate(zip(K, views)):
            observed = np.where(observations == 1)[0]
            self.view_means.append(view[observed].mean(axis=0))
            view[observed] = view[observed] - self.view_means[i]
            train_views.append(np.diag(observations) @ view)
        return train_views

    def transform(self, *views: Tuple[np.ndarray, ...], K=None):
        """
        Transforms data given a fit GCCA model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param K: observation matrix. Binary array with (k,n) dimensions where k is the number of views and n is the number of samples
        1 means the data is observed in the corresponding view and 0 means the data is unobserved in that view.
        """
        transformed_views = []
        for i, view in enumerate(views):
            transformed_view = np.ma.array((view - self.view_means[i]) @ self.weights_list[i])
            if K is not None:
                transformed_view.mask[np.where(K[i]) == 1] = True
            transformed_views.append(transformed_view)
        return transformed_views


def _pca_data(*views: Tuple[np.ndarray, ...]):
    """
    Since most methods require zero-mean data, demean_data() is used to demean training data as well as to apply this
    demeaning transformation to out of sample data

    :param views: numpy arrays with the same number of rows (samples) separated by commas
    """
    views_U = []
    views_S = []
    views_Vt = []
    for i, view in enumerate(views):
        U, S, Vt = np.linalg.svd(view, full_matrices=False)
        views_U.append(U)
        views_S.append(S)
        views_Vt.append(Vt)
    return views_U, views_S, views_Vt


class rCCA(_CCA_Base, BaseEstimator):
    """
    A class used to fit Regularised CCA (canonical ridge) model. Uses PCA to perform the optimization efficiently for high dimensional data.

    :Example:

    >>> from cca_zoo.wrappers import rCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = rCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None):
        """
        Constructor for rCCA

        :param latent_dims: number of latent dimensions
        :param c: regularisation between 0 (CCA) and 1 (PLS)
        """
        super().__init__(latent_dims=latent_dims)
        self.c = c

    def fit(self, *views: Tuple[np.ndarray, ...]):
        """
        Fits a regularised CCA (canonical ridge) model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        """
        if self.c is None:
            self.c = [0] * len(views)
        assert (len(self.c) == len(views)), 'c requires as many values as #views'
        train_views = self.demean_data(*views)
        U_list, S_list, Vt_list = _pca_data(*train_views)
        if len(views) == 2:
            self.two_view_fit(U_list, S_list, Vt_list)
        else:
            self.multi_view_fit(U_list, S_list, Vt_list)
        if self.weights_list[0].shape[1] == 0:
            self.two_view_fit(U_list, S_list, Vt_list)
        self.score_list = [view @ self.weights_list[i] for i, view in enumerate(train_views)]
        if self.weights_list[0].shape[1] == 0:
            self.two_view_fit(U_list, S_list, Vt_list)
        self.train_correlations = self.predict_corr(*views)
        self.predict_corr(*views)
        return self

    def two_view_fit(self, U_list, S_list, Vt_list):
        B_list = [(1 - self.c[i]) * S * S + self.c[i] for i, S in
                  enumerate(S_list)]
        R_list = [U @ np.diag(S) for U, S in zip(U_list, S_list)]
        R_12 = R_list[0].T @ R_list[1]
        M = np.diag(1 / np.sqrt(B_list[1])) @ R_12.T @ np.diag(1 / B_list[0]) @ R_12 @ np.diag(1 / np.sqrt(B_list[1]))
        n = M.shape[0]
        [eigvals, eigvecs] = eigh(M, subset_by_index=[n - 1 - self.latent_dims, n - 1])
        idx = np.argsort(eigvals, axis=0)[::-1]
        eigvecs = eigvecs[:, idx].real
        eigvals = np.real(np.sqrt(eigvals))[idx][:self.latent_dims]
        w_y = Vt_list[1].T @ np.diag(1 / np.sqrt(B_list[1])) @ eigvecs[:, :self.latent_dims].real
        w_x = Vt_list[0].T @ np.diag(1 / B_list[0]) @ R_12 @ np.diag(1 / np.sqrt(B_list[1])) @ eigvecs[:,
                                                                                               :self.latent_dims].real / eigvals
        self.weights_list = [w_x, w_y]

    def multi_view_fit(self, U_list, S_list, Vt_list):
        B_list = [(1 - self.c[i]) * S * S + self.c[i] for i, S in
                  enumerate(S_list)]
        D = block_diag(*[np.diag((1 - self.c[i]) * S * S + self.c[i]) for i, S in
                         enumerate(S_list)])
        C = np.concatenate([U @ np.diag(S) for U, S in zip(U_list, S_list)], axis=1)
        C = C.T @ C
        C -= block_diag(*[np.diag(S ** 2) for U, S in zip(U_list, S_list)]) - D
        n = C.shape[0]
        [eigvals, eigvecs] = eigh(C, D, subset_by_index=[n - self.latent_dims, n - 1])
        idx = np.argsort(eigvals, axis=0)[::-1]
        eigvecs = eigvecs[:, idx].real
        splits = np.cumsum([0] + [U.shape[1] for U in U_list])
        self.weights_list = [Vt.T @ np.diag(1 / np.sqrt(B)) @ eigvecs[split:splits[i + 1], :self.latent_dims] for
                             i, (split, Vt, B) in enumerate(zip(splits[:-1], Vt_list, B_list))]


class CCA(rCCA):
    """
    A class used to fit a simple CCA model

    Implements CCA by inheriting regularised CCA with 0 regularisation

    :Example:

    >>> from cca_zoo.wrappers import CCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = CCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1):
        """
        Constructor for CCA

        :param latent_dims: number of latent dimensions to learn
        """
        super().__init__(latent_dims=latent_dims, c=[0.0, 0.0])


class _Iterative(_CCA_Base):
    """
    A class used as the base for iterative CCA methods i.e. those that optimize for each dimension one at a time with deflation.

    """

    def __init__(self, latent_dims: int = 1, deflation='cca', max_iter: int = 100, generalized: bool = False,
                 initialization: str = 'unregularized', tol: float = 1e-5):
        """
        Constructor for _Iterative

        :param latent_dims: number of latent dimensions
        :param deflation: the type of deflation.
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights)
        or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        super().__init__(latent_dims=latent_dims)
        self.max_iter = max_iter
        self.generalized = generalized
        self.initialization = initialization
        self.tol = tol
        self.deflation = deflation

    def fit(self, *views: Tuple[np.ndarray, ...], ):
        """
        Fits the model by running an inner loop to convergence and then using deflation (currently only supports CCA deflation)

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        """
        self._set_loop_params()
        train_views = self.demean_data(*views)
        n = train_views[0].shape[0]
        p = [view.shape[1] for view in train_views]
        # list of d: p x k
        self.weights_list = [np.zeros((p_, self.latent_dims)) for p_ in p]

        # list of d: n x k
        self.score_list = [np.zeros((n, self.latent_dims)) for _ in train_views]

        residuals = copy.deepcopy(list(train_views))

        self.objective = []
        # For each of the dimensions
        for k in range(self.latent_dims):
            self.loop = self.loop.fit(*residuals)
            for i, residual in enumerate(residuals):
                self.weights_list[i][:, k] = self.loop.weights[i]
                self.score_list[i][:, k] = self.loop.scores[i]
                # TODO This is CCA deflation (https://ars.els-cdn.com/content/image/1-s2.0-S0006322319319183-mmc1.pdf)
                # but in principle we could apply any form of deflation here
                # residuals[i] = residuals[i] - np.outer(self.score_list[i][:, k], self.score_list[i][:, k]) @ residuals[
                #    i] / np.dot(self.score_list[i][:, k], self.score_list[i][:, k]).item()
                residuals[i] = self.deflate(residuals[i], self.score_list[i][:, k])
            self.objective.append(self.loop.track_objective)
        self.train_correlations = self.predict_corr(*views)
        return self

    def deflate(self, residual, score):
        """
        Deflate view residual by CCA deflation (https://ars.els-cdn.com/content/image/1-s2.0-S0006322319319183-mmc1.pdf)

        :param residual:
        :param score:

        """
        if self.deflation == 'cca':
            return residual - np.outer(score, score) @ residual / np.dot(score, score).item()

    @abstractmethod
    def _set_loop_params(self):
        """
        Sets up the inner optimization loop for the method. By default uses the PLS inner loop.
        """
        self.loop = cca_zoo.innerloop.PLSInnerLoop(max_iter=self.max_iter, generalized=self.generalized,
                                                   initialization=self.initialization)


class PLS(_Iterative):
    """
    A class used to fit a PLS model

    Fits a partial least squares model with CCA deflation by NIPALS algorithm

    :Example:

    >>> from cca_zoo.wrappers import PLS
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = PLS()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, max_iter: int = 100, generalized: bool = False,
                 initialization: str = 'unregularized', tol: float = 1e-5):
        """
        Constructor for PLS

        :param latent_dims: number of latent dimensions
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights) or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol)

    def _set_loop_params(self):
        self.loop = cca_zoo.innerloop.PLSInnerLoop(max_iter=self.max_iter, generalized=self.generalized,
                                                   initialization=self.initialization, tol=self.tol)


class ElasticCCA(_Iterative, BaseEstimator):
    """
    Fits an elastic CCA by iterative rescaled elastic net regression

    :Example:

    >>> from cca_zoo.wrappers import ElasticCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = ElasticCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: Union[List[float], float] = None,
                 l1_ratio: Union[List[float], float] = None,
                 constrained: bool = False, max_iter: int = 100,
                 generalized: bool = False,
                 initialization: str = 'unregularized', tol: float = 1e-5, stochastic=False):
        """
        Constructor for ElasticCCA

        :param latent_dims: Number of latent dimensions
        :param c: lasso alpha
        :param l1_ratio: l1 ratio in lasso subproblems
        :param max_iter: Maximum number of iterations
        """
        self.c = c
        self.l1_ratio = l1_ratio
        self.constrained = constrained
        self.stochastic = stochastic
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol)

    def _set_loop_params(self):
        self.loop = cca_zoo.innerloop.ElasticInnerLoop(max_iter=self.max_iter, c=self.c, l1_ratio=self.l1_ratio,
                                                       generalized=self.generalized, initialization=self.initialization,
                                                       tol=self.tol, constrained=self.constrained,
                                                       stochastic=self.stochastic)


class CCA_ALS(ElasticCCA):
    """
    Fits a CCA model with CCA deflation by NIPALS algorithm. Implemented by ElasticCCA with 0 regularisation

    :Example:

    >>> from cca_zoo.wrappers import CCA_ALS
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = CCA_ALS()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, max_iter: int = 100, generalized: bool = False,
                 initialization: str = 'random', tol: float = 1e-5, stochastic=True):
        """
        Constructor for CCA_ALS

        :param latent_dims: number of latent dimensions
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights) or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol, constrained=False, stochastic=stochastic)


class SCCA(ElasticCCA):
    """
    Fits a sparse CCA model by iterative rescaled lasso regression. Implemented by ElasticCCA with l1 ratio=1

    :Example:

    >>> from cca_zoo.wrappers import SCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = SCCA(c=[0.001,0.001])
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, max_iter: int = 100,
                 generalized: bool = False,
                 initialization: str = 'unregularized', tol: float = 1e-5, stochastic=False):
        """
        Constructor for SCCA

        :param latent_dims: number of latent dimensions
        :param c: l1 regularisation parameter
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights) or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol, c=c, l1_ratio=1, constrained=False,
                         stochastic=stochastic)


class PMD(_Iterative, BaseEstimator):
    """
    Fits a Sparse CCA (Penalized Matrix Decomposition) model.

    :Example:

    >>> from cca_zoo.wrappers import PMD
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = PMD(c=[1,1])
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, max_iter: int = 100,
                 generalized: bool = False, initialization: str = 'unregularized', tol: float = 1e-5):
        """
        Constructor for PMD

        :param latent_dims: number of latent dimensions
        :param c: l1 regularisation parameter between 1 and sqrt(number of features) for each view
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights) or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        self.c = c
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol)

    def _set_loop_params(self):
        self.loop = cca_zoo.innerloop.PMDInnerLoop(max_iter=self.max_iter, c=self.c, generalized=self.generalized,
                                                   initialization=self.initialization, tol=self.tol)


class ParkhomenkoCCA(_Iterative, BaseEstimator):
    """
    Fits a sparse CCA (penalized CCA) model

    :Example:

    >>> from cca_zoo.wrappers import ParkhomenkoCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = ParkhomenkoCCA(c=[0.001,0.001])
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, max_iter: int = 100,
                 generalized: bool = False, initialization: str = 'unregularized', tol: float = 1e-5):
        """
        Constructor for ParkhomenkoCCA

        :param latent_dims: number of latent dimensions
        :param c: l1 regularisation parameter
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights) or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        self.c = c
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol)

    def _set_loop_params(self):
        self.loop = cca_zoo.innerloop.ParkhomenkoInnerLoop(max_iter=self.max_iter, c=self.c,
                                                           generalized=self.generalized,
                                                           initialization=self.initialization, tol=self.tol)


class SCCA_ADMM(_Iterative, BaseEstimator):
    """
    Fits a sparse CCA model by alternating ADMM

    :Example:

    >>> from cca_zoo.wrappers import SCCA_ADMM
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = SCCA_ADMM()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, mu: List[float] = None, lam: List[float] = None,
                 eta: List[float] = None,
                 max_iter: int = 100,
                 generalized: bool = False, initialization: str = 'unregularized', tol: float = 1e-5):
        """
        Constructor for SCCA_ADMM

        :param latent_dims: number of latent dimensions
        :param c: l1 regularisation parameter
        :param mu:
        :param lam:
        :param: eta:
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param generalized:
        :param initialization: the initialization for the inner loop either 'unregularized' (initializes with PLS scores and weights) or 'random'.
        :param tol: if the cosine similarity of the weights between subsequent iterations is greater than 1-tol the loop is considered converged
        """
        self.c = c
        self.mu = mu
        self.lam = lam
        self.eta = eta
        super().__init__(latent_dims=latent_dims, max_iter=max_iter, generalized=generalized,
                         initialization=initialization, tol=tol)

    def _set_loop_params(self):
        self.loop = cca_zoo.innerloop.ADMMInnerLoop(max_iter=self.max_iter, c=self.c, mu=self.mu, lam=self.lam,
                                                    eta=self.eta, generalized=self.generalized,
                                                    initialization=self.initialization, tol=self.tol)


class TCCA(_CCA_Base):
    """
    Fits a Tensor CCA model. Tensor CCA maximises higher order correlations

    My own port from https://github.com/rciszek/mdr_tcca

    :param latent_dims:
    :param c: regularisation between 0 (CCA) and 1 (PLS)

    :Example:

    >>> from cca_zoo.wrappers import TCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = TCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None):
        """
        Constructor for TCCA

        :param latent_dims:
        :param c: regularisation between 0 (CCA) and 1 (PLS)
        """
        super().__init__(latent_dims)
        self.c = c

    def check_params(self):
        if self.c is None:
            self.c = [0] * self.n_views

    def fit(self, *views: Tuple[np.ndarray, ...], ):
        self.n_views = len(views)
        self.check_params()
        assert (len(self.c) == len(views)), 'c requires as many values as #views'
        train_views, covs_invsqrt = self.setup_tensor(*views)
        for i, el in enumerate(train_views):
            if i == 0:
                M = el
            else:
                for _ in range(len(M.shape) - 1):
                    el = np.expand_dims(el, 1)
                M = np.expand_dims(M, -1) @ el
        M = np.mean(M, 0)
        tl.set_backend('numpy')
        M_parafac = parafac(M, self.latent_dims, verbose=True)
        self.alphas = [cov_invsqrt @ fac for i, (view, cov_invsqrt, fac) in
                       enumerate(zip(train_views, covs_invsqrt, M_parafac.factors))]
        self.score_list = [view @ self.alphas[i] for i, view in enumerate(train_views)]
        self.weights_list = [weights / np.linalg.norm(score) for weights, score in
                             zip(self.alphas, self.score_list)]
        self.score_list = [view @ self.weights_list[i] for i, view in enumerate(train_views)]
        self.train_correlations = self.predict_corr(*views)
        return self

    def setup_tensor(self, *views: Tuple[np.ndarray, ...]):
        train_views = self.demean_data(*views)
        n = train_views[0].shape[0]
        covs = [(1 - self.c[i]) * view.T @ view + self.c[i] * np.eye(view.shape[1]) for i, view in
                enumerate(train_views)]
        covs_invsqrt = [np.linalg.inv(sqrtm(cov)) for cov in covs]
        train_views = [train_view @ cov_invsqrt for train_view, cov_invsqrt in zip(train_views, covs_invsqrt)]
        return train_views, covs_invsqrt


class KTCCA(TCCA):
    """
    Fits a Kernel Tensor CCA model. Tensor CCA maximises higher order correlations

    My own port from https://github.com/rciszek/mdr_tcca

    :param latent_dims:
    :param c: regularisation between 0 (CCA) and 1 (PLS)

    :Example:

    >>> from cca_zoo.wrappers import KTCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> model = KTCCA()
    >>> model.fit(X1,X2)
    """

    def __init__(self, latent_dims: int = 1, c: List[float] = None, kernel: List[Union[float, callable]] = None,
                 gamma: List[float] = None,
                 degree: List[float] = None, coef0: List[float] = None,
                 kernel_params: List[dict] = None, eps=1e-3):
        """
        :param latent_dims: number of latent dimensions
        :param c: list of regularisation parameters for each view (between 0:CCA and 1:PLS)
        :param kernel: list of kernel mappings used internally. This parameter is directly passed to :class:`~sklearn.metrics.pairwise.pairwise_kernel`. If element of `kernel` is a string, it must be one of the metrics in `pairwise.PAIRWISE_KERNEL_FUNCTIONS`. Alternatively, if element of `kernel` is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two rows from X as input and return the corresponding kernel value as a single number. This means that callables from :mod:`sklearn.metrics.pairwise` are not allowed, as they operate on matrices, not single samples. Use the string identifying the kernel instead.
        :param gamma: list of gamma parameters for the RBF, laplacian, polynomial, exponential chi2 and sigmoid kernels. Interpretation of the default value is left to the kernel; see the documentation for sklearn.metrics.pairwise. Ignored by other kernels.
        :param degree: list of degree parameters of the polynomial kernel. Ignored by other kernels.
        :param coef0: list of zero coefficients for polynomial and sigmoid kernels. Ignored by other kernels.
        :param kernel_params: list of additional parameters (keyword arguments) for kernel function passed as callable object.
        :param eps: epsilon value to ensure stability
        """
        super().__init__(latent_dims=latent_dims)
        self.kernel_params = kernel_params
        self.gamma = gamma
        self.coef0 = coef0
        self.kernel = kernel
        self.degree = degree
        self.c = c
        self.eps = eps

    def check_params(self):
        if self.kernel is None:
            self.kernel = ['linear'] * self.n_views
        if self.gamma is None:
            self.gamma = [None] * self.n_views
        if self.coef0 is None:
            self.coef0 = [1] * self.n_views
        if self.degree is None:
            self.degree = [1] * self.n_views
        if self.c is None:
            self.c = [0] * self.n_views

    def _get_kernel(self, view, X, Y=None):
        if callable(self.kernel):
            params = self.kernel_params[view] or {}
        else:
            params = {"gamma": self.gamma[view],
                      "degree": self.degree[view],
                      "coef0": self.coef0[view]}
        return pairwise_kernels(X, Y, metric=self.kernel[view],
                                filter_params=True, **params)

    def setup_tensor(self, *views: Tuple[np.ndarray, ...]):
        self.train_views = self.demean_data(*views)
        train_views = [self._get_kernel(i, view) for i, view in enumerate(self.train_views)]
        n = train_views[0].shape[0]
        covs = [(1 - self.c[i]) * kernel @ kernel.T + self.c[i] * kernel for i, kernel in enumerate(train_views)]
        smallest_eigs = [min(0, np.linalg.eigvalsh(cov).min()) - self.eps for cov in covs]
        covs = [cov - smallest_eig * np.eye(cov.shape[0]) for cov, smallest_eig in zip(covs, smallest_eigs)]
        self.covs_invsqrt = [np.linalg.inv(sqrtm(cov)).real for cov in covs]
        train_views = [train_view @ cov_invsqrt for train_view, cov_invsqrt in zip(train_views, self.covs_invsqrt)]
        return train_views, self.covs_invsqrt

    def transform(self, *views: Tuple[np.ndarray, ...], ):
        """
        Transforms data given a fit k=KCCA model

        :param views: numpy arrays with the same number of rows (samples) separated by commas
        :param kwargs: any additional keyword arguments required by the given model
        """
        Ktest = [self._get_kernel(i, train_view, Y=test_view - self.view_means[i]) for i, (train_view, test_view) in
                 enumerate(zip(self.train_views, views))]
        transformed_views = [test_kernel @ cov_invsqrt @ self.alphas[i] for i, (test_kernel, cov_invsqrt) in
                             enumerate(zip(Ktest, self.covs_invsqrt))]
        return transformed_views


class _CrossValidate:
    """
    Base class used for cross validation
    """

    def __init__(self, model, folds: int = 5, verbose: bool = True):
        self.folds = folds
        self.verbose = verbose
        self.model = model

    def score(self, *views: Tuple[np.ndarray, ...], K=None, **cvparams):
        scores = np.zeros(self.folds)
        inds = np.arange(views[0].shape[0])
        np.random.shuffle(inds)
        if self.folds == 1:
            # If 1 fold do an 80:20 split
            fold_inds = np.array_split(inds, 5)
        else:
            fold_inds = np.array_split(inds, self.folds)
        for fold in range(self.folds):
            train_sets = [np.delete(view, fold_inds[fold], axis=0) for view in views]
            val_sets = [view[fold_inds[fold], :] for view in views]
            if K is not None:
                train_obs = np.delete(K, fold_inds[fold], axis=1)
                val_obs = K[:, fold_inds[fold]]
                scores[fold] = self.model.set_params(**cvparams).fit(
                    *train_sets, K=train_obs).predict_corr(
                    *val_sets).sum(axis=-1)[np.triu_indices(len(views), 1)].sum()
            else:
                self.model.set_params(**cvparams).fit(
                    *train_sets)
                scores[fold] = self.model.predict_corr(
                    *val_sets).sum(axis=-1)[np.triu_indices(len(views), 1)].sum()
        metric = scores.sum(axis=0) / self.folds
        std = scores.std(axis=0)
        if np.isnan(metric):
            metric = 0
        if self.verbose:
            print(cvparams)
            print(metric)
            print(std)
        return metric, std
