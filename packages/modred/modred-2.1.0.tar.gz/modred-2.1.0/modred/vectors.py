""" Vectors, handles, and inner products.

We recommend using these functions and classes when possible.
Otherwise, you can write your own vector class and/or vector handle,
see documentation :ref:`sec_details`.
"""
import pickle

import numpy as np

from . import util


class VecHandle(object):
    """Recommended base class for vector handles (not required)."""
    cached_base_vec_handle = None
    cached_base_vec = None


    def __init__(self, base_vec_handle=None, scale=None):
        self.__base_vec_handle = base_vec_handle
        self.scale = scale


    def get(self):
        """Get a vector, using the private (user-overwritten) ``_get``
        function.  If available, the base vector will be subtracted from the
        specified vector.  Then, if a scale factor is specified, the
        base-subtracted vector will be scaled.  The scaled, base-subtracted
        vector is then returned."""
        vec = self._get()
        if self.__base_vec_handle is None:
            return self.__scale_vec(vec)
        if self.__base_vec_handle == VecHandle.cached_base_vec_handle:
            base_vec = VecHandle.cached_base_vec
        else:
            base_vec = self.__base_vec_handle.get()
            VecHandle.cached_base_vec_handle = self.__base_vec_handle
            VecHandle.cached_base_vec = base_vec
        return self.__scale_vec(vec - base_vec)


    def put(self, vec):
        """Put a vector to file or memory using the private (user-overwritten)
        ``_put`` function."""
        return self._put(vec)


    def _get(self):
        """Subclass must overwrite, retrieves a vector."""
        raise NotImplementedError("must be implemented by subclasses")


    def _put(self, vec):
        """Subclass must overwrite, puts a vector."""
        raise NotImplementedError("must be implemented by subclasses")


    def __scale_vec(self, vec):
        """Scales the vector by a scalar."""
        if self.scale is not None:
            return vec*self.scale
        return vec


class VecHandleInMemory(VecHandle):
    """Gets and puts vectors from/in memory."""
    def __init__(self, vec=None, base_vec_handle=None, scale=None):
        VecHandle.__init__(self, base_vec_handle, scale)
        self.vec = vec


    def _get(self):
        """Returns the vector."""
        return self.vec


    def _put(self, vec):
        """Stores the vector, ``vec``."""
        self.vec = vec


    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return util.smart_eq(self.vec, other.vec)


class VecHandleArrayText(VecHandle):
    """Gets and puts array vector objects from/in text files."""
    def __init__(
        self, vec_path, base_vec_handle=None, scale=None, is_complex=False):
        VecHandle.__init__(self, base_vec_handle, scale)
        self.vec_path = vec_path
        self.is_complex = is_complex


    def _get(self):
        """Loads vector from path."""
        return util.load_array_text(self.vec_path, is_complex=self.is_complex)


    def _put(self, vec):
        """Saves vector to path."""
        util.save_array_text(vec, self.vec_path)


    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.vec_path == other.vec_path


class VecHandlePickle(VecHandle):
    """Gets and puts any vector object from/in pickle files."""
    def __init__(self, vec_path, base_vec_handle=None, scale=None):
        VecHandle.__init__(self, base_vec_handle, scale)
        self.vec_path = vec_path

    def _get(self):
        """Loads vector from path."""
        with open(self.vec_path, 'rb') as file_obj:
            to_return = pickle.load(file_obj)
        return to_return

    def _put(self, vec):
        """Saves vector to path."""
        with open(self.vec_path, 'wb') as file_obj:
            pickle.dump(vec, file_obj)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.vec_path == other.vec_path


def inner_product_array_uniform(vec1, vec2):
    """Takes inner product of numpy arrays without weighting. The first element
    is conjugated, i.e., IP = np.dot(vec1.conj().T, v2)
    """
    return np.vdot(vec1, vec2)


class InnerProductTrapz(object):
    """Callable that computes inner product of n-dimensional arrays defined on
    a spatial grid, using the trapezoidal rule.

    Args:
        ``*grids``: 1D arrays of grid points, in the order of the spatial
        dimensions.

    Usage::

      nx = 10
      ny = 11
      x_grid = 1 - np.cos(np.linspace(0, np.pi, nx))
      y_grid = np.linspace(0, 1.0, ny)**2
      my_trapz = InnerProductTrapz(x_grid, y_grid)

      v1 = np.random.random((nx,ny))
      v2 = np.random.random((nx,ny))
      IP_v1_v2 = my_trapz(v1, v2)
    """
    def __init__(self, *grids):
        if len(grids) == 0:
            raise ValueError('Must supply at least one 1D grid array')
        for gidx, g in enumerate(grids):
            if not isinstance(g, np.ndarray):
                raise TypeError(
                    'Grid {:d} of {:d} is a {}, not a numpy array'.format(
                        gidx + 1, len(grids), type(g)))
        self.grids = grids
        self.grid_shape = tuple(g.size for g in grids)


    def __call__(self, vec1, vec2):
        return self.inner_product(vec1, vec2)


    def inner_product(self, vec1, vec2):
        """Computes inner product."""
        if vec1.shape != self.grid_shape:
            raise TypeError(
                'Vector 1 shape does not match grid shape: '
                '{} != {}'.format(vec1.shape, self.grid_shape))
        if vec2.shape != self.grid_shape:
            raise TypeError(
                'Vector 2 shape does not match grid shape: '
                '{} != {}'.format(vec2.shape, self.grid_shape))
        # IP starts as an array of shape vec1 (=vec2) and the subsequent
        # loop over the grids collapses each dimension after integrating
        # over that dimension until IP is a scalar by the end of the loop
        # over the grids.
        IP = vec1.conj() * vec2
        for grid in reversed(self.grids):
            IP = np.trapz(IP, x=grid)
        return IP


class Vector(object):
    """Recommended base class for vector objects (not required)."""
    def __init__(self):
        """Must overwrite"""
        raise NotImplementedError('constructor must be implemented by subclass')


    def __add__(self, other):
        raise NotImplementedError('addition must be implemented by subclass')


    def __mul__(self, scalar):
        raise NotImplementedError('multiplication must be implemented by '
            'subclass')


    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    def __lmul__(self, scalar):
        return self.__mul__(scalar)


    def __sub__(self, other):
        return self + (-1 * other)
