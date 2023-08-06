#!/usr/bin/env python
"""Test dmd module"""
import copy
import unittest
import os
from os.path import join
from shutil import rmtree

import numpy as np

from modred import dmd, parallel, util
from modred.py2to3 import range
from modred.vectorspace import VectorSpaceArrays, VectorSpaceHandles
from modred.vectors import VecHandlePickle


#@unittest.skip('Testing something else.')
@unittest.skipIf(parallel.is_distributed(), 'Serial only.')
class TestDMDArraysFunctions(unittest.TestCase):
    def setUp(self):
        self.num_states = 30
        self.num_vecs = 10


    def test_all(self):
        rtol = 1e-10
        atol = 1e-12

        # Generate weights to test different inner products.
        weights_1D = np.random.random(self.num_states)
        weights_2D = np.identity(self.num_states, dtype=np.complex)
        weights_2D[0, 0] = 2.
        weights_2D[2, 1] = 0.3j
        weights_2D[1, 2] = weights_2D[2, 1].conj()

        # Generate random snapshot data
        vecs_array = (
            np.random.random((self.num_states, self.num_vecs)) +
            1j * np.random.random((self.num_states, self.num_vecs)))
        adv_vecs_array = (
            np.random.random((self.num_states, self.num_vecs)) +
            1j * np.random.random((self.num_states, self.num_vecs)))

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [vecs_array, vecs_array],
            [None, adv_vecs_array],
            [vecs_array[:, :-1], vecs_array],
            [vecs_array[:, 1:], adv_vecs_array]):

            # Test both method of snapshots and direct method
            for method in ['snaps', 'direct']:
                if method == 'snaps':
                    compute_DMD = dmd.compute_DMD_arrays_snaps_method
                elif method == 'direct':
                    compute_DMD = dmd.compute_DMD_arrays_direct_method
                else:
                    raise ValueError('Invalid method choice.')

                # Consider different inner product weights
                for weights in [None, weights_1D, weights_2D]:
                    IP = VectorSpaceArrays(
                        weights=weights).compute_inner_product_array

                    # Test that results hold for truncated or untruncated DMD
                    # (i.e., whether or not the underlying POD basis is
                    # truncated).
                    for max_num_eigvals in [None, self.num_vecs // 2]:

                        # Compute DMD
                        DMD_res = compute_DMD(
                            vecs_arg, adv_vecs=adv_vecs_arg,
                            inner_product_weights=weights,
                            max_num_eigvals=max_num_eigvals)

                        # For method of snapshots, test correlation array values
                        # by simply recomputing them.
                        if method == 'snaps':
                            np.testing.assert_allclose(
                                IP(vecs_vals, vecs_vals),
                                DMD_res.correlation_array,
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                IP(vecs_vals, adv_vecs_vals),
                                DMD_res.cross_correlation_array,
                                rtol=rtol, atol=atol)

                        # Test correlation array eigenvalues and eigenvectors.
                        np.testing.assert_allclose(
                            IP(vecs_vals, vecs_vals).dot(
                                DMD_res.correlation_array_eigvecs),
                            DMD_res.correlation_array_eigvecs.dot(
                                np.diag(DMD_res.correlation_array_eigvals)),
                            rtol=rtol, atol=atol)

                        # Compute the approximating linear operator relating the
                        # vecs to the adv_vecs.  To do this, use the
                        # eigendecomposition of the correlation array.
                        vecs_POD_build_coeffs = (
                            DMD_res.correlation_array_eigvecs.dot(
                                np.diag(
                                    DMD_res.correlation_array_eigvals ** -0.5)))
                        vecs_POD_modes = vecs_vals.dot(vecs_POD_build_coeffs)
                        approx_linear_op = adv_vecs_vals.dot(
                            DMD_res.correlation_array_eigvecs.dot(
                                np.diag(
                                    DMD_res.correlation_array_eigvals ** -0.5)
                            ).dot(vecs_POD_modes.conj().T))
                        low_order_linear_op = IP(
                            vecs_POD_modes,
                            IP(approx_linear_op.conj().T, vecs_POD_modes))

                        # Test the left and right eigenvectors of the low-order
                        # (projected) approximating linear operator.
                        np.testing.assert_allclose(
                            low_order_linear_op.dot(
                                DMD_res.R_low_order_eigvecs),
                            DMD_res.R_low_order_eigvecs.dot(np.diag(
                                DMD_res.eigvals)),
                            rtol=rtol, atol=atol)
                        np.testing.assert_allclose(
                            DMD_res.L_low_order_eigvecs.conj().T.dot(
                                low_order_linear_op),
                            np.diag(DMD_res.eigvals).dot(
                                DMD_res.L_low_order_eigvecs.conj().T),
                            rtol=rtol, atol=atol)

                        # Test the exact modes, which are eigenvectors of the
                        # approximating linear operator.
                        np.testing.assert_allclose(
                            IP(approx_linear_op.conj().T, DMD_res.exact_modes),
                            DMD_res.exact_modes.dot(np.diag(DMD_res.eigvals)),
                            rtol=rtol, atol=atol)

                        # Test the projected modes, which are eigenvectors of
                        # the approximating linear operator projected onto the
                        # POD modes of the vecs.
                        np.testing.assert_allclose(
                            vecs_POD_modes.dot(IP(
                                vecs_POD_modes,
                                IP(
                                    approx_linear_op.conj().T,
                                    DMD_res.proj_modes))),
                            DMD_res.proj_modes.dot(
                                np.diag(DMD_res.eigvals)),
                            rtol=rtol, atol=atol)

                        # Test the adjoint modes, which are left eigenvectors of
                        # the approximating linear operator.
                        np.testing.assert_allclose(
                            IP(approx_linear_op, DMD_res.adjoint_modes),
                            DMD_res.adjoint_modes.dot(
                                np.diag(DMD_res.eigvals.conj().T)),
                            rtol=rtol, atol=atol)

                        # Test spectral coefficients against an explicit
                        # projection using the adjoint DMD modes.
                        np.testing.assert_allclose(
                            DMD_res.spectral_coeffs,
                            np.abs(IP(
                                DMD_res.adjoint_modes,
                                vecs_vals[:, 0])).squeeze(),
                            rtol=rtol, atol=atol)

                        # Test projection coefficients against an explicit
                        # projection using the adjoint DMD modes.
                        np.testing.assert_allclose(
                            DMD_res.proj_coeffs,
                            IP(DMD_res.adjoint_modes, vecs_vals),
                            rtol=rtol, atol=atol)
                        np.testing.assert_allclose(
                            DMD_res.adv_proj_coeffs,
                            IP(DMD_res.adjoint_modes, adv_vecs_vals),
                            rtol=rtol, atol=atol)

                        # Choose subset of modes to compute, for testing mode
                        # indices argument. Test both an explicit selection of
                        # mode indices and a None argument.
                        mode_indices_trunc = np.unique(np.random.randint(
                            0, high=DMD_res.eigvals.size,
                            size=DMD_res.eigvals.size // 2))
                        for mode_idxs_arg, mode_idxs_vals in zip(
                            [None, mode_indices_trunc],
                            [range(DMD_res.eigvals.size), mode_indices_trunc]):

                            # Compute DMD
                            DMD_res_sliced = compute_DMD(
                                vecs_arg, adv_vecs=adv_vecs_arg,
                                mode_indices=mode_idxs_arg,
                                inner_product_weights=weights,
                                max_num_eigvals=max_num_eigvals)

                            # Test that use of mode indices argument returns
                            # correct subset of modes
                            np.testing.assert_allclose(
                                DMD_res_sliced.exact_modes,
                                DMD_res.exact_modes[:, mode_idxs_vals],
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                DMD_res_sliced.proj_modes,
                                DMD_res.proj_modes[:, mode_idxs_vals],
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                DMD_res_sliced.adjoint_modes,
                                DMD_res.adjoint_modes[:, mode_idxs_vals],
                                rtol=rtol, atol=atol)


#@unittest.skip('Testing something else.')
class TestDMDHandles(unittest.TestCase):
    def setUp(self):
        # Specify output locations
        if not os.access('.', os.W_OK):
            raise RuntimeError('Cannot write to current directory')
        self.test_dir = 'files_DMD_DELETE_ME'
        if not os.path.isdir(self.test_dir):
            parallel.call_from_rank_zero(os.mkdir, self.test_dir)
        self.vec_path = join(self.test_dir, 'dmd_vec_%03d.pkl')
        self.adv_vec_path = join(self.test_dir, 'dmd_adv_vec_%03d.pkl')
        self.exact_mode_path = join(self.test_dir, 'dmd_exactmode_%03d.pkl')
        self.proj_mode_path = join(self.test_dir, 'dmd_projmode_%03d.pkl')
        self.adjoint_mode_path = join(self.test_dir, 'dmd_adjmode_%03d.pkl')

        # Specify data dimensions
        self.num_states = 30
        self.num_vecs = 10

        # Generate random data and write to disk using handles
        self.vecs_array = (
            parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs))
            + 1j * parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs)))
        self.adv_vecs_array = (
            parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs))
            + 1j * parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs)))
        self.vec_handles = [
            VecHandlePickle(self.vec_path % i) for i in range(self.num_vecs)]
        self.adv_vec_handles = [
            VecHandlePickle(self.adv_vec_path % i)
            for i in range(self.num_vecs)]
        for idx, (hdl, adv_hdl) in enumerate(
            zip(self.vec_handles, self.adv_vec_handles)):
            hdl.put(self.vecs_array[:, idx])
            adv_hdl.put(self.adv_vecs_array[:, idx])

        parallel.barrier()


    def tearDown(self):
        parallel.barrier()
        parallel.call_from_rank_zero(rmtree, self.test_dir, ignore_errors=True)
        parallel.barrier()


    #@unittest.skip('Testing something else.')
    def test_init(self):
        """Test arguments passed to the constructor are assigned properly"""
        # Get default data member values
        # Set verbosity to false, to avoid printing warnings during tests
        def my_load(fname): pass
        def my_save(data, fname): pass
        def my_IP(vec1, vec2): pass

        data_members_default = {
            'put_array': util.save_array_text,
            'get_array': util.load_array_text,
            'verbosity': 0, 'eigvals': None, 'correlation_array': None,
            'cross_correlation_array': None, 'correlation_array_eigvals': None,
            'correlation_array_eigvecs': None, 'low_order_linear_map': None,
            'L_low_order_eigvecs': None, 'R_low_order_eigvecs': None,
            'spectral_coeffs': None, 'proj_coeffs': None, 'adv_proj_coeffs':
            None, 'vec_handles': None, 'adv_vec_handles': None, 'vec_space':
            VectorSpaceHandles(inner_product=my_IP, verbosity=0)}

        # Get default data member values
        for k,v in util.get_data_members(
            dmd.DMDHandles(inner_product=my_IP, verbosity=0)).items():
            self.assertEqual(v, data_members_default[k])

        my_DMD = dmd.DMDHandles(inner_product=my_IP, verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['vec_space'] = VectorSpaceHandles(
            inner_product=my_IP, verbosity=0)
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])

        my_DMD = dmd.DMDHandles(
            inner_product=my_IP, get_array=my_load, verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['get_array'] = my_load
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])

        my_DMD = dmd.DMDHandles(
            inner_product=my_IP, put_array=my_save, verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['put_array'] = my_save
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])

        max_vecs_per_node = 500
        my_DMD = dmd.DMDHandles(
            inner_product=my_IP, max_vecs_per_node=max_vecs_per_node,
            verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['vec_space'].max_vecs_per_node = max_vecs_per_node
        data_members_modified['vec_space'].max_vecs_per_proc = (
            max_vecs_per_node *
            parallel.get_num_nodes() /
            parallel.get_num_procs())
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])


    #@unittest.skip('Testing something else.')
    def test_puts_gets(self):
        """Test get and put functions"""
        # Generate some random data
        eigvals = parallel.call_and_bcast(np.random.random, 5)
        R_low_order_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        L_low_order_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        correlation_array_eigvals = parallel.call_and_bcast(np.random.random, 5)
        correlation_array_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        correlation_array = parallel.call_and_bcast(np.random.random, (10, 10))
        cross_correlation_array = parallel.call_and_bcast(
            np.random.random, (10, 10))
        spectral_coeffs = parallel.call_and_bcast(np.random.random, 5)
        proj_coeffs = parallel.call_and_bcast(np.random.random, (5, 5))
        adv_proj_coeffs = parallel.call_and_bcast(np.random.random, (5, 5))

        # Create a DMD object and store the data in it
        DMD_save = dmd.DMDHandles(verbosity=0)
        DMD_save.eigvals = eigvals
        DMD_save.R_low_order_eigvecs = R_low_order_eigvecs
        DMD_save.L_low_order_eigvecs = L_low_order_eigvecs
        DMD_save.correlation_array_eigvals = correlation_array_eigvals
        DMD_save.correlation_array_eigvecs = correlation_array_eigvecs
        DMD_save.correlation_array = correlation_array
        DMD_save.cross_correlation_array = cross_correlation_array
        DMD_save.spectral_coeffs = spectral_coeffs
        DMD_save.proj_coeffs = proj_coeffs
        DMD_save.adv_proj_coeffs = adv_proj_coeffs

        # Write the data to disk
        eigvals_path = join(self.test_dir, 'dmd_eigvals.txt')
        R_low_order_eigvecs_path = join(
            self.test_dir, 'dmd_R_low_order_eigvecs.txt')
        L_low_order_eigvecs_path = join(
            self.test_dir, 'dmd_L_low_order_eigvecs.txt')
        correlation_array_eigvals_path = join(
            self.test_dir, 'dmd_corr_array_eigvals.txt')
        correlation_array_eigvecs_path = join(
            self.test_dir, 'dmd_corr_array_eigvecs.txt')
        correlation_array_path = join(self.test_dir, 'dmd_corr_array.txt')
        cross_correlation_array_path = join(
            self.test_dir, 'dmd_cross_corr_array.txt')
        spectral_coeffs_path = join(self.test_dir, 'dmd_spectral_coeffs.txt')
        proj_coeffs_path = join(self.test_dir, 'dmd_proj_coeffs.txt')
        adv_proj_coeffs_path = join(self.test_dir, 'dmd_adv_proj_coeffs.txt')
        DMD_save.put_decomp(
            eigvals_path, R_low_order_eigvecs_path, L_low_order_eigvecs_path,
            correlation_array_eigvals_path , correlation_array_eigvecs_path)
        DMD_save.put_correlation_array(correlation_array_path)
        DMD_save.put_cross_correlation_array(cross_correlation_array_path)
        DMD_save.put_spectral_coeffs(spectral_coeffs_path)
        DMD_save.put_proj_coeffs(proj_coeffs_path, adv_proj_coeffs_path)
        parallel.barrier()

        # Create a new DMD object and use it to load data
        DMD_load = dmd.DMDHandles(verbosity=0)
        DMD_load.get_decomp(
            eigvals_path, R_low_order_eigvecs_path, L_low_order_eigvecs_path,
            correlation_array_eigvals_path, correlation_array_eigvecs_path)
        DMD_load.get_correlation_array(correlation_array_path)
        DMD_load.get_cross_correlation_array(cross_correlation_array_path)
        DMD_load.get_spectral_coeffs(spectral_coeffs_path)
        DMD_load.get_proj_coeffs(proj_coeffs_path, adv_proj_coeffs_path)

        # Check that the loaded data is correct
        np.testing.assert_equal(DMD_load.eigvals, eigvals)
        np.testing.assert_equal(
            DMD_load.L_low_order_eigvecs, L_low_order_eigvecs)
        np.testing.assert_equal(
            DMD_load.R_low_order_eigvecs, R_low_order_eigvecs)
        np.testing.assert_equal(
            DMD_load.correlation_array_eigvals, correlation_array_eigvals)
        np.testing.assert_equal(
            DMD_load.correlation_array_eigvecs, correlation_array_eigvecs)
        np.testing.assert_equal(DMD_load.correlation_array, correlation_array)
        np.testing.assert_equal(
            DMD_load.cross_correlation_array, cross_correlation_array)
        np.testing.assert_equal(
            np.array(DMD_load.spectral_coeffs).squeeze(), spectral_coeffs)
        np.testing.assert_equal(DMD_load.proj_coeffs, proj_coeffs)
        np.testing.assert_equal(DMD_load.adv_proj_coeffs, adv_proj_coeffs)


    #@unittest.skip('Testing something else.')
    def test_compute_decomp(self):
        """Test DMD decomposition"""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated DMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute DMD using modred
                DMD = dmd.DMDHandles(inner_product=np.vdot, verbosity=0)
                (eigvals, R_low_order_eigvecs, L_low_order_eigvecs,
                correlation_array_eigvals, correlation_array_eigvecs) =\
                DMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Test correlation array values by simply recomputing them.
                # Here compute the full inner product array, rather than
                # assuming it is symmetric.
                np.testing.assert_allclose(
                    DMD.vec_space.compute_inner_product_array(
                        vecs_vals, vecs_vals),
                    DMD.correlation_array,
                    rtol=rtol, atol=atol)
                np.testing.assert_allclose(
                    DMD.vec_space.compute_inner_product_array(
                        vecs_vals, adv_vecs_vals),
                    DMD.cross_correlation_array,
                    rtol=rtol, atol=atol)

                # Test correlation array eigenvalues and eigenvectors.
                np.testing.assert_allclose(
                    DMD.correlation_array.dot(correlation_array_eigvecs),
                    correlation_array_eigvecs.dot(
                        np.diag(correlation_array_eigvals)),
                    rtol=rtol, atol=atol)

                # Compute the projection of the approximating linear operator
                # relating the vecs to the adv_vecs.  To do this, compute the
                # POD modes of the vecs using the eigendecomposition of the
                # correlation array.
                POD_build_coeffs = correlation_array_eigvecs.dot(
                    np.diag(correlation_array_eigvals ** -0.5))
                POD_mode_path = join(self.test_dir, 'pod_mode_%03d.txt')
                POD_mode_handles = [
                    VecHandlePickle(POD_mode_path % i)
                    for i in range(correlation_array_eigvals.size)]
                DMD.vec_space.lin_combine(
                    POD_mode_handles, vecs_vals, POD_build_coeffs)
                low_order_linear_op = DMD.vec_space.compute_inner_product_array(
                    POD_mode_handles, adv_vecs_vals).dot(
                        correlation_array_eigvecs.dot(
                            np.diag(correlation_array_eigvals ** -0.5)))

                # Test the left and right eigenvectors of the low-order
                # (projected) approximating linear operator.
                np.testing.assert_allclose(
                    low_order_linear_op.dot(R_low_order_eigvecs),
                    R_low_order_eigvecs.dot(np.diag(eigvals)),
                    rtol=rtol, atol=atol)
                np.testing.assert_allclose(
                    L_low_order_eigvecs.conj().T.dot(low_order_linear_op),
                    np.diag(eigvals).dot(L_low_order_eigvecs.conj().T),
                    rtol=rtol, atol=atol)

                # Check that returned values match internal values
                np.testing.assert_equal(eigvals, DMD.eigvals)
                np.testing.assert_equal(
                    R_low_order_eigvecs, DMD.R_low_order_eigvecs)
                np.testing.assert_equal(
                    L_low_order_eigvecs, DMD.L_low_order_eigvecs)
                np.testing.assert_equal(
                    correlation_array_eigvals, DMD.correlation_array_eigvals)
                np.testing.assert_equal(
                    correlation_array_eigvecs, DMD.correlation_array_eigvecs)

        # Check that if mismatched sets of handles are passed in, an error is
        # raised.
        DMD = dmd.DMDHandles(inner_product=np.vdot, verbosity=0)
        self.assertRaises(
            ValueError, DMD.compute_decomp, self.vec_handles,
            self.adv_vec_handles[:-1])


    #@unittest.skip('Testing something else.')
    def test_compute_modes(self):
        """Test building of modes."""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated DMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute DMD using modred.  (The properties defining a DMD mode
                # require manipulations involving the correct decomposition, so
                # we cannot isolate the mode computation from the decomposition
                # step.
                DMD = dmd.DMDHandles(inner_product=np.vdot, verbosity=0)
                DMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Compute the projection of the approximating linear operator
                # relating the projected vecs to the projected adv_vecs.  To do
                # this, compute the POD modes of the projected vecs using the
                # eigendecomposition of the projected correlation array.
                POD_build_coeffs = DMD.correlation_array_eigvecs.dot(
                    np.diag(DMD.correlation_array_eigvals ** -0.5))
                POD_mode_path = join(self.test_dir, 'pod_mode_%03d.txt')
                POD_mode_handles = [
                    VecHandlePickle(POD_mode_path % i)
                    for i in range(DMD.correlation_array_eigvals.size)]
                DMD.vec_space.lin_combine(
                    POD_mode_handles, vecs_vals, POD_build_coeffs)

                # Select a subset of modes to compute.  Compute at least half
                # the modes, and up to all of them.  Make sure to use unique
                # values.  (This may reduce the number of modes computed.)
                num_modes = parallel.call_and_bcast(
                    np.random.randint,
                    DMD.eigvals.size // 2, DMD.eigvals.size + 1)
                mode_idxs = np.unique(parallel.call_and_bcast(
                    np.random.randint,
                    0, DMD.eigvals.size, num_modes))

                # Create handles for the modes
                DMD_exact_mode_handles = [
                    VecHandlePickle(self.exact_mode_path % i)
                    for i in mode_idxs]
                DMD_proj_mode_handles = [
                    VecHandlePickle(self.proj_mode_path % i)
                    for i in mode_idxs]
                DMD_adjoint_mode_handles = [
                    VecHandlePickle(self.adjoint_mode_path % i)
                    for i in mode_idxs]

                # Compute modes
                DMD.compute_exact_modes(mode_idxs, DMD_exact_mode_handles)
                DMD.compute_proj_modes(mode_idxs, DMD_proj_mode_handles)
                DMD.compute_adjoint_modes(mode_idxs, DMD_adjoint_mode_handles)

                # Test that exact modes are eigenvectors of the approximating
                # linear operator by checking A \Phi = \Phi \Lambda.  Do this
                # using handles, i.e. check mode by mode.  Note that since
                # np.vdot takes the conjugate of its second argument, whereas
                # modred assumes a conjugate is taken on the first inner product
                # argument, the inner product array in the LHS computation must
                # be conjugated.
                LHS_path = join(self.test_dir, 'LHS_%03d.pkl')
                LHS_handles = [
                    VecHandlePickle(LHS_path % i) for i in mode_idxs]
                RHS_path = join(self.test_dir, 'RHS_%03d.pkl')
                RHS_handles = [
                    VecHandlePickle(RHS_path % i) for i in mode_idxs]
                DMD.vec_space.lin_combine(
                    LHS_handles,
                    adv_vecs_vals,
                    DMD.correlation_array_eigvecs.dot(
                        np.diag(DMD.correlation_array_eigvals ** -0.5)).dot(
                            DMD.vec_space.compute_inner_product_array(
                                POD_mode_handles, DMD_exact_mode_handles)))
                DMD.vec_space.lin_combine(
                    RHS_handles,
                    DMD_exact_mode_handles,
                    np.diag(DMD.eigvals[mode_idxs]))
                for LHS, RHS in zip(LHS_handles, RHS_handles):
                    np.testing.assert_allclose(
                        LHS.get(), RHS.get(), rtol=rtol, atol=atol)

                # Test that projected modes are eigenvectors of the projection
                # of the approximating linear operator by checking
                # U U^* A \Phi = \Phi \Lambda.  As above, check this using
                # handles, and be careful about the order of arguments when
                # taking inner products.
                LHS_path = join(self.test_dir, 'LHS_%03d.pkl')
                LHS_handles = [
                    VecHandlePickle(LHS_path % i) for i in mode_idxs]
                RHS_path = join(self.test_dir, 'RHS_%03d.pkl')
                RHS_handles = [
                    VecHandlePickle(RHS_path % i) for i in mode_idxs]
                DMD.vec_space.lin_combine(
                    LHS_handles,
                    POD_mode_handles,
                    DMD.vec_space.compute_inner_product_array(
                        POD_mode_handles, adv_vecs_vals).dot(
                            DMD.correlation_array_eigvecs.dot(np.diag(
                                DMD.correlation_array_eigvals ** -0.5).dot(
                                    DMD.vec_space.compute_inner_product_array(
                                        POD_mode_handles,
                                        DMD_proj_mode_handles)))))
                DMD.vec_space.lin_combine(
                    RHS_handles,
                    DMD_proj_mode_handles,
                    np.diag(DMD.eigvals[mode_idxs]))
                for LHS, RHS in zip(LHS_handles, RHS_handles):
                    np.testing.assert_allclose(
                        LHS.get(), RHS.get(), rtol=rtol, atol=atol)

                # Test that adjoint modes are eigenvectors of the conjugate
                # transpose of approximating linear operator by checking
                # A^* \Phi = \Phi \Lambda^*.  Do this using handles, i.e. check
                # mode by mode.  Note that since np.vdot takes the conjugate of
                # its second argument, whereas modred assumes a conjugate is
                # taken on the first inner product argument, the inner product
                # array in the LHS computation must be conjugated.
                LHS_path = join(self.test_dir, 'LHS_%03d.pkl')
                LHS_handles = [
                    VecHandlePickle(LHS_path % i) for i in mode_idxs]
                RHS_path = join(self.test_dir, 'RHS_%03d.pkl')
                RHS_handles = [
                    VecHandlePickle(RHS_path % i) for i in mode_idxs]
                DMD.vec_space.lin_combine(
                    LHS_handles,
                    POD_mode_handles,
                    np.diag(DMD.correlation_array_eigvals ** -0.5).dot(
                        DMD.correlation_array_eigvecs.conj().T.dot(
                            DMD.vec_space.compute_inner_product_array(
                                adv_vecs_vals, DMD_adjoint_mode_handles))))
                DMD.vec_space.lin_combine(
                    RHS_handles,
                    DMD_adjoint_mode_handles,
                    np.diag(DMD.eigvals[mode_idxs]).conj().T)
                for LHS, RHS in zip(LHS_handles, RHS_handles):
                    np.testing.assert_allclose(
                        LHS.get(), RHS.get(), rtol=rtol, atol=atol)


    #@unittest.skip('Testing something else.')
    def test_compute_spectrum(self):
        """Test DMD spectrum"""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated DMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute DMD using modred.  (The DMD spectral coefficients are
                # defined by a projection onto DMD modes.  As such, testing them
                # requires manipulations involving the correct decomposition and
                # modes, so we cannot isolate the spectral coefficient
                # computation from those computations.)
                DMD = dmd.DMDHandles(inner_product=np.vdot, verbosity=0)
                DMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Test by checking a least-squares projection onto the projected
                # modes, which is analytically equivalent to a biorthogonal
                # projection onto the exact modes.  The latter is implemented
                # (using various identities) in modred.  Here, test using the
                # former approach, as it doesn't require adjoint modes.
                mode_idxs = range(DMD.eigvals.size)
                proj_mode_handles = [
                    VecHandlePickle(self.proj_mode_path % i)
                    for i in mode_idxs]
                DMD.compute_proj_modes(mode_idxs, proj_mode_handles)
                spectral_coeffs_true = np.abs(
                    np.linalg.inv(
                        DMD.vec_space.compute_symm_inner_product_array(
                            proj_mode_handles)).dot(
                                DMD.vec_space.compute_inner_product_array(
                                    proj_mode_handles, vecs_vals[0]))).squeeze()
                spectral_coeffs = DMD.compute_spectrum()
                np.testing.assert_allclose(
                    spectral_coeffs, spectral_coeffs_true, rtol=rtol, atol=atol)


    #@unittest.skip('Testing something else.')
    def test_compute_proj_coeffs(self):
        """Test projection coefficients"""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated DMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute DMD using modred.  (Testing the DMD projection
                # coefficients requires the correct DMD decomposition and modes,
                # so we cannot isolate the projection coefficient computation
                # from those computations.)
                DMD = dmd.DMDHandles(inner_product=np.vdot, verbosity=0)
                DMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Test by checking a least-squares projection onto the projected
                # modes, which is analytically equivalent to a biorthogonal
                # projection onto the exact modes.  The latter is implemented
                # (using various identities) in modred.  Here, test using the
                # former approach, as it doesn't require adjoint modes.
                mode_idxs = range(DMD.eigvals.size)
                proj_mode_handles = [
                    VecHandlePickle(self.proj_mode_path % i)
                    for i in mode_idxs]
                DMD.compute_proj_modes(mode_idxs, proj_mode_handles)
                proj_coeffs_true = np.linalg.inv(
                    DMD.vec_space.compute_symm_inner_product_array(
                        proj_mode_handles)).dot(
                            DMD.vec_space.compute_inner_product_array(
                                proj_mode_handles, vecs_vals))
                adv_proj_coeffs_true = np.linalg.inv(
                    DMD.vec_space.compute_symm_inner_product_array(
                        proj_mode_handles)).dot(
                            DMD.vec_space.compute_inner_product_array(
                                proj_mode_handles, adv_vecs_vals))
                proj_coeffs, adv_proj_coeffs = DMD.compute_proj_coeffs()
                np.testing.assert_allclose(
                    proj_coeffs, proj_coeffs_true, rtol=rtol, atol=atol)
                np.testing.assert_allclose(
                    adv_proj_coeffs, adv_proj_coeffs_true, rtol=rtol, atol=atol)


#@unittest.skip('Testing something else.')
@unittest.skipIf(parallel.is_distributed(), 'Serial only.')
class TestTLSqrDMDArraysFunctions(unittest.TestCase):
    def setUp(self):
        # Specify data dimensions
        self.num_vecs = 30
        self.num_states = 10
        self.max_num_eigvals = int(np.round(self.num_states / 2))


    def test_all(self):
        rtol = 1e-10
        atol = 1e-12

        # Generate weights to test different inner products.
        ws = np.identity(self.num_states)
        ws[0, 0] = 2.
        ws[2, 1] = 0.3
        ws[1, 2] = 0.3
        weights_list = [None, np.random.random(self.num_states), ws]

        # Generate random snapshot data
        vecs_array = (
            np.random.random((self.num_states, self.num_vecs)) +
            1j * np.random.random((self.num_states, self.num_vecs)))
        adv_vecs_array =(
            np.random.random((self.num_states, self.num_vecs)) +
            1j * np.random.random((self.num_states, self.num_vecs)))

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to
        # a sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [vecs_array, vecs_array],
            [None, adv_vecs_array],
            [vecs_array[:, :-1], vecs_array],
            [vecs_array[:, 1:], adv_vecs_array]):

            # Stack the data arrays, for doing total-least squares
            stacked_vecs_array = np.vstack((vecs_vals, adv_vecs_vals))

            # Test both method of snapshots and direct method
            for method in ['snaps', 'direct']:
                if method == 'snaps':
                    compute_TLSqrDMD = dmd.compute_TLSqrDMD_arrays_snaps_method
                elif method == 'direct':
                    compute_TLSqrDMD = dmd.compute_TLSqrDMD_arrays_direct_method
                else:
                    raise ValueError('Invalid method choice.')

                # Consider different inner product weights
                for weights in weights_list:
                    IP = VectorSpaceArrays(
                        weights=weights).compute_inner_product_array
                    symm_IP = VectorSpaceArrays(
                        weights=weights).compute_symm_inner_product_array

                    # Define inner product for stacked vectors
                    if weights is None:
                        stacked_weights = None
                    elif len(weights.shape) == 1:
                        stacked_weights = np.hstack((weights, weights))
                    elif len(weights.shape) == 2:
                        stacked_weights = np.vstack((
                            np.hstack((weights, 0. * weights)),
                            np.hstack((0. * weights, weights))))
                    else:
                        raise ValueError('Invalid inner product weights.')
                    stacked_IP = VectorSpaceArrays(
                        weights=stacked_weights).compute_inner_product_array

                    # Test that results hold for truncated or untruncated DMD
                    # (i.e., whether or not the underlying POD basis is
                    # truncated).
                    for max_num_eigvals in [None, self.num_states // 2]:

                        # Compute DMD
                        DMD_res = compute_TLSqrDMD(
                            vecs_arg, adv_vecs=adv_vecs_arg,
                            inner_product_weights=weights,
                            max_num_eigvals=max_num_eigvals)

                        # For method of snapshots, test correlation arrays
                        # values by simply recomputing them.
                        if method == 'snaps':
                            np.testing.assert_allclose(
                                IP(vecs_vals, vecs_vals),
                                DMD_res.correlation_array,
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                IP(vecs_vals, adv_vecs_vals),
                                DMD_res.cross_correlation_array,
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                IP(adv_vecs_vals, adv_vecs_vals),
                                DMD_res.adv_correlation_array,
                                rtol=rtol, atol=atol)

                        # Test summed correlation array eigenvalues and
                        # eigenvectors
                        np.testing.assert_allclose((
                            IP(vecs_vals, vecs_vals) +
                            IP(adv_vecs_vals, adv_vecs_vals)).dot(
                                DMD_res.sum_correlation_array_eigvecs),
                            DMD_res.sum_correlation_array_eigvecs.dot(np.diag(
                                DMD_res.sum_correlation_array_eigvals)),
                            rtol=rtol, atol=atol)

                        # Test projected correlation array eigenvalues and
                        # eigenvectors
                        proj_vecs_vals = vecs_vals.dot(
                            DMD_res.sum_correlation_array_eigvecs.dot(
                                DMD_res.sum_correlation_array_eigvecs.conj().T))
                        proj_adv_vecs_vals = adv_vecs_vals.dot(
                            DMD_res.sum_correlation_array_eigvecs.dot(
                                DMD_res.sum_correlation_array_eigvecs.conj().T))
                        np.testing.assert_allclose(
                            IP(proj_vecs_vals, proj_vecs_vals).dot(
                                DMD_res.proj_correlation_array_eigvecs),
                            DMD_res.proj_correlation_array_eigvecs.dot(np.diag(
                                DMD_res.proj_correlation_array_eigvals)),
                            rtol=rtol, atol=atol)

                        # Compute the approximating linear operator relating the
                        # projected vecs to the projected adv_vecs.  To do this,
                        # compute the POD of the projected vecs using the
                        # eigendecomposition of the projected correlation array.
                        proj_vecs_POD_build_coeffs = (
                            DMD_res.proj_correlation_array_eigvecs.dot(np.diag(
                                DMD_res.proj_correlation_array_eigvals ** -0.5
                            )))
                        proj_vecs_POD_modes = proj_vecs_vals.dot(
                            proj_vecs_POD_build_coeffs)
                        approx_linear_op = proj_adv_vecs_vals.dot(
                            DMD_res.proj_correlation_array_eigvecs.dot(np.diag(
                                DMD_res.proj_correlation_array_eigvals ** -0.5
                            )).dot(
                                proj_vecs_POD_modes.conj().T))
                        low_order_linear_op = IP(
                            proj_vecs_POD_modes,
                            IP(approx_linear_op.conj().T, proj_vecs_POD_modes))

                        # Test the left and right eigenvectors of the low-order
                        # (projected) approximating linear operator.
                        np.testing.assert_allclose(
                            low_order_linear_op.dot(
                                DMD_res.R_low_order_eigvecs),
                            DMD_res.R_low_order_eigvecs.dot(
                                np.diag(DMD_res.eigvals)),
                            rtol=rtol, atol=atol)
                        np.testing.assert_allclose(
                            DMD_res.L_low_order_eigvecs.conj().T.dot(
                                low_order_linear_op),
                            np.diag(DMD_res.eigvals).dot(
                                DMD_res.L_low_order_eigvecs.conj().T),
                            rtol=rtol, atol=atol)

                        # Test the exact modes, which are eigenvectors of the
                        # approximating linear operator.
                        np.testing.assert_allclose(
                            IP(approx_linear_op.conj().T, DMD_res.exact_modes),
                            DMD_res.exact_modes.dot(
                                np.diag(DMD_res.eigvals)),
                            rtol=rtol, atol=atol)

                        # Test the projected modes, which are eigenvectors of
                        # the approximating linear operator projected onto the
                        # POD modes of the vecs.
                        np.testing.assert_allclose(
                            proj_vecs_POD_modes.dot(IP(
                                proj_vecs_POD_modes,
                                IP(
                                    approx_linear_op.conj().T,
                                    DMD_res.proj_modes))),
                            DMD_res.proj_modes.dot(
                                np.diag(DMD_res.eigvals)),
                            rtol=rtol, atol=atol)

                        # Test the adjoint modes, which are left eigenvectors of
                        # the approximating linear operator.
                        np.testing.assert_allclose(
                            IP(approx_linear_op, DMD_res.adjoint_modes),
                            DMD_res.adjoint_modes.dot(
                                np.diag(DMD_res.eigvals.conj().T)),
                            rtol=rtol, atol=atol)

                        # Test spectral coefficients against an explicit
                        # projection using the adjoint DMD modes.
                        np.testing.assert_allclose(
                            DMD_res.spectral_coeffs,
                            np.abs(IP(
                                DMD_res.adjoint_modes,
                                proj_vecs_vals[:, 0])).squeeze(),
                            rtol=rtol, atol=atol)

                        # Test projection coefficients against an explicit
                        # projection using the adjoint DMD modes.
                        np.testing.assert_allclose(
                            DMD_res.proj_coeffs,
                            IP(DMD_res.adjoint_modes, proj_vecs_vals),
                            rtol=rtol, atol=atol)
                        np.testing.assert_allclose(
                            DMD_res.adv_proj_coeffs,
                            IP(DMD_res.adjoint_modes, proj_adv_vecs_vals),
                            rtol=rtol, atol=atol)

                        # Choose subset of modes to compute, for testing mode
                        # indices argument. Test both an explicit selection of
                        # mode indices and a None argument.
                        mode_indices_trunc = np.unique(np.random.randint(
                            0, high=DMD_res.eigvals.size,
                            size=DMD_res.eigvals.size // 2))
                        for mode_idxs_arg, mode_idxs_vals in zip(
                            [None, mode_indices_trunc],
                            [range(DMD_res.eigvals.size), mode_indices_trunc]):

                            # Compute DMD
                            DMD_res_sliced = compute_TLSqrDMD(
                                vecs_arg, adv_vecs=adv_vecs_arg,
                                mode_indices=mode_idxs_arg,
                                inner_product_weights=weights,
                                max_num_eigvals=max_num_eigvals)

                            # Test that use of mode indices argument returns
                            # correct subset of modes
                            np.testing.assert_allclose(
                                DMD_res_sliced.exact_modes,
                                DMD_res.exact_modes[:, mode_idxs_vals],
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                DMD_res_sliced.proj_modes,
                                DMD_res.proj_modes[:, mode_idxs_vals],
                                rtol=rtol, atol=atol)
                            np.testing.assert_allclose(
                                DMD_res_sliced.adjoint_modes,
                                DMD_res.adjoint_modes[:, mode_idxs_vals],
                                rtol=rtol, atol=atol)


#@unittest.skip('Testing something else.')
class TestTLSqrDMDHandles(unittest.TestCase):
    def setUp(self):
        if not os.access('.', os.W_OK):
            raise RuntimeError('Cannot write to current directory')
        self.test_dir = 'files_TLSqrDMD_DELETE_ME'
        if not os.path.isdir(self.test_dir):
            parallel.call_from_rank_zero(os.mkdir, self.test_dir)
        self.vec_path = join(self.test_dir, 'tlsqrdmd_vec_%03d.pkl')
        self.adv_vec_path = join(self.test_dir, 'tlsqrdmd_adv_vec_%03d.pkl')
        self.exact_mode_path = join(
            self.test_dir, 'tlsqrdmd_exactmode_%03d.pkl')
        self.proj_mode_path = join(self.test_dir, 'tlsqrdmd_projmode_%03d.pkl')
        self.adjoint_mode_path = join(
            self.test_dir, 'tlsqrdmd_adjmode_%03d.pkl')

        # Specify data dimensions
        self.num_states = 30
        self.num_vecs = 10

        # Generate random data and write to disk using handles
        self.vecs_array = (
            parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs)) +
            + 1j * parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs)))
        self.adv_vecs_array = (
            parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs)) +
            + 1j * parallel.call_and_bcast(
                np.random.random, (self.num_states, self.num_vecs)))
        self.vec_handles = [
            VecHandlePickle(self.vec_path % i) for i in range(self.num_vecs)]
        self.adv_vec_handles = [
            VecHandlePickle(self.adv_vec_path % i)
            for i in range(self.num_vecs)]
        for idx, (hdl, adv_hdl) in enumerate(
            zip(self.vec_handles, self.adv_vec_handles)):
            hdl.put(self.vecs_array[:, idx])
            adv_hdl.put(self.adv_vecs_array[:, idx])

        # Path for saving projected (de-noised) vecs and advanced vecs to disk
        # later.
        self.proj_vec_path = join(
            self.test_dir, 'tlsqrdmd_proj_vec_%03d.pkl')
        self.proj_adv_vec_path = join(
            self.test_dir, 'tlsqrdmd_proj_adv_vec_%03d.pkl')

        parallel.barrier()


    def tearDown(self):
        parallel.barrier()
        parallel.call_from_rank_zero(rmtree, self.test_dir, ignore_errors=True)
        parallel.barrier()


    #@unittest.skip('Testing something else.')
    def test_init(self):
        """Test arguments passed to the constructor are assigned properly"""
        # Get default data member values
        # Set verbosity to false, to avoid printing warnings during tests
        def my_load(fname): pass
        def my_save(data, fname): pass
        def my_IP(vec1, vec2): pass

        data_members_default = {
            'put_array': util.save_array_text,
            'get_array': util.load_array_text,
            'verbosity': 0, 'eigvals': None, 'correlation_array': None,
            'cross_correlation_array': None, 'adv_correlation_array': None,
            'sum_correlation_array': None, 'proj_correlation_array': None,
            'sum_correlation_array_eigvals': None,
            'sum_correlation_array_eigvecs': None,
            'proj_correlation_array_eigvals': None,
            'proj_correlation_array_eigvecs': None,
            'low_order_linear_map': None,
            'L_low_order_eigvecs': None, 'R_low_order_eigvecs': None,
            'spectral_coeffs': None, 'proj_coeffs': None, 'adv_proj_coeffs':
            None, 'vec_handles': None, 'adv_vec_handles': None, 'vec_space':
            VectorSpaceHandles(inner_product=my_IP, verbosity=0)}

        # Get default data member values
        for k,v in util.get_data_members(
            dmd.TLSqrDMDHandles(inner_product=my_IP, verbosity=0)).items():
            self.assertEqual(v, data_members_default[k])

        my_DMD = dmd.TLSqrDMDHandles(inner_product=my_IP, verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['vec_space'] = VectorSpaceHandles(
            inner_product=my_IP, verbosity=0)
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])

        my_DMD = dmd.TLSqrDMDHandles(
            inner_product=my_IP, get_array=my_load, verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['get_array'] = my_load
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])

        my_DMD = dmd.TLSqrDMDHandles(
            inner_product=my_IP, put_array=my_save, verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['put_array'] = my_save
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])

        max_vecs_per_node = 500
        my_DMD = dmd.TLSqrDMDHandles(
            inner_product=my_IP, max_vecs_per_node=max_vecs_per_node,
            verbosity=0)
        data_members_modified = copy.deepcopy(data_members_default)
        data_members_modified['vec_space'].max_vecs_per_node = max_vecs_per_node
        data_members_modified['vec_space'].max_vecs_per_proc = (
            max_vecs_per_node * parallel.get_num_nodes() /
            parallel.get_num_procs())
        for k,v in util.get_data_members(my_DMD).items():
            self.assertEqual(v, data_members_modified[k])


    #@unittest.skip('Testing something else.')
    def test_puts_gets(self):
        """Test get and put functions"""
        # Generate some random data
        eigvals = parallel.call_and_bcast(np.random.random, 5)
        R_low_order_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        L_low_order_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        sum_correlation_array_eigvals = parallel.call_and_bcast(
            np.random.random, 5)
        sum_correlation_array_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        proj_correlation_array_eigvals = parallel.call_and_bcast(
            np.random.random, 5)
        proj_correlation_array_eigvecs = parallel.call_and_bcast(
            np.random.random, (10, 10))
        correlation_array = parallel.call_and_bcast(np.random.random, (10, 10))
        cross_correlation_array = parallel.call_and_bcast(
            np.random.random, (10, 10))
        adv_correlation_array = parallel.call_and_bcast(
            np.random.random, (10, 10))
        sum_correlation_array = parallel.call_and_bcast(
            np.random.random, (10, 10))
        proj_correlation_array = parallel.call_and_bcast(
            np.random.random, (10, 10))
        spectral_coeffs = parallel.call_and_bcast(np.random.random, 5)
        proj_coeffs = parallel.call_and_bcast(np.random.random, (5, 5))
        adv_proj_coeffs = parallel.call_and_bcast(np.random.random, (5, 5))

        # Create a DMD object and store the data in it
        TLSqrDMD_save = dmd.TLSqrDMDHandles(verbosity=0)
        TLSqrDMD_save.eigvals = eigvals
        TLSqrDMD_save.R_low_order_eigvecs = R_low_order_eigvecs
        TLSqrDMD_save.L_low_order_eigvecs = L_low_order_eigvecs
        TLSqrDMD_save.sum_correlation_array_eigvals =\
            sum_correlation_array_eigvals
        TLSqrDMD_save.sum_correlation_array_eigvecs =\
            sum_correlation_array_eigvecs
        TLSqrDMD_save.proj_correlation_array_eigvals =\
            proj_correlation_array_eigvals
        TLSqrDMD_save.proj_correlation_array_eigvecs =\
            proj_correlation_array_eigvecs
        TLSqrDMD_save.correlation_array = correlation_array
        TLSqrDMD_save.cross_correlation_array = cross_correlation_array
        TLSqrDMD_save.adv_correlation_array = adv_correlation_array
        TLSqrDMD_save.sum_correlation_array = sum_correlation_array
        TLSqrDMD_save.proj_correlation_array = proj_correlation_array
        TLSqrDMD_save.spectral_coeffs = spectral_coeffs
        TLSqrDMD_save.proj_coeffs = proj_coeffs
        TLSqrDMD_save.adv_proj_coeffs = adv_proj_coeffs

        # Write the data to disk
        eigvals_path = join(self.test_dir, 'tlsqrdmd_eigvals.txt')
        R_low_order_eigvecs_path = join(
            self.test_dir, 'tlsqrdmd_R_low_order_eigvecs.txt')
        L_low_order_eigvecs_path = join(
            self.test_dir, 'tlsqrdmd_L_low_order_eigvecs.txt')
        sum_correlation_array_eigvals_path = join(
            self.test_dir, 'tlsqrdmd_sum_corr_array_eigvals.txt')
        sum_correlation_array_eigvecs_path = join(
            self.test_dir, 'tlsqrdmd_sum_corr_array_eigvecs.txt')
        proj_correlation_array_eigvals_path = join(
            self.test_dir, 'tlsqrdmd_proj_corr_array_eigvals.txt')
        proj_correlation_array_eigvecs_path = join(
            self.test_dir, 'tlsqrdmd_proj_corr_array_eigvecs.txt')
        correlation_array_path = join(self.test_dir, 'tlsqrdmd_corr_array.txt')
        cross_correlation_array_path = join(
            self.test_dir, 'tlsqrdmd_cross_corr_array.txt')
        adv_correlation_array_path = join(
            self.test_dir, 'tlsqrdmd_adv_corr_array.txt')
        sum_correlation_array_path = join(
            self.test_dir, 'tlsqrdmd_sum_corr_array.txt')
        proj_correlation_array_path = join(
            self.test_dir, 'tlsqrdmd_proj_corr_array.txt')
        spectral_coeffs_path = join(
            self.test_dir, 'tlsqrdmd_spectral_coeffs.txt')
        proj_coeffs_path = join(self.test_dir, 'tlsqrdmd_proj_coeffs.txt')
        adv_proj_coeffs_path = join(
            self.test_dir, 'tlsqrdmd_adv_proj_coeffs.txt')
        TLSqrDMD_save.put_decomp(
            eigvals_path, R_low_order_eigvecs_path, L_low_order_eigvecs_path,
            sum_correlation_array_eigvals_path,
            sum_correlation_array_eigvecs_path,
            proj_correlation_array_eigvals_path ,
            proj_correlation_array_eigvecs_path)
        TLSqrDMD_save.put_correlation_array(correlation_array_path)
        TLSqrDMD_save.put_cross_correlation_array(cross_correlation_array_path)
        TLSqrDMD_save.put_adv_correlation_array(adv_correlation_array_path)
        TLSqrDMD_save.put_sum_correlation_array(sum_correlation_array_path)
        TLSqrDMD_save.put_proj_correlation_array(proj_correlation_array_path)
        TLSqrDMD_save.put_spectral_coeffs(spectral_coeffs_path)
        TLSqrDMD_save.put_proj_coeffs(proj_coeffs_path, adv_proj_coeffs_path)
        parallel.barrier()

        # Create a new TLSqrDMD object and use it to load data
        TLSqrDMD_load = dmd.TLSqrDMDHandles(verbosity=0)
        TLSqrDMD_load.get_decomp(
            eigvals_path, R_low_order_eigvecs_path, L_low_order_eigvecs_path,
            sum_correlation_array_eigvals_path,
            sum_correlation_array_eigvecs_path,
            proj_correlation_array_eigvals_path,
            proj_correlation_array_eigvecs_path)
        TLSqrDMD_load.get_correlation_array(correlation_array_path)
        TLSqrDMD_load.get_cross_correlation_array(cross_correlation_array_path)
        TLSqrDMD_load.get_adv_correlation_array(adv_correlation_array_path)
        TLSqrDMD_load.get_sum_correlation_array(sum_correlation_array_path)
        TLSqrDMD_load.get_proj_correlation_array(proj_correlation_array_path)
        TLSqrDMD_load.get_spectral_coeffs(spectral_coeffs_path)
        TLSqrDMD_load.get_proj_coeffs(proj_coeffs_path, adv_proj_coeffs_path)

        # Check that the loaded data is correct
        np.testing.assert_equal(TLSqrDMD_load.eigvals, eigvals)
        np.testing.assert_equal(
            TLSqrDMD_load.R_low_order_eigvecs, R_low_order_eigvecs)
        np.testing.assert_equal(
            TLSqrDMD_load.L_low_order_eigvecs, L_low_order_eigvecs)
        np.testing.assert_equal(
            TLSqrDMD_load.sum_correlation_array_eigvals,
            sum_correlation_array_eigvals)
        np.testing.assert_equal(
            TLSqrDMD_load.sum_correlation_array_eigvecs,
            sum_correlation_array_eigvecs)
        np.testing.assert_equal(
            TLSqrDMD_load.proj_correlation_array_eigvals,
            proj_correlation_array_eigvals)
        np.testing.assert_equal(
            TLSqrDMD_load.proj_correlation_array_eigvecs,
            proj_correlation_array_eigvecs)
        np.testing.assert_equal(
            TLSqrDMD_load.correlation_array, correlation_array)
        np.testing.assert_equal(
            TLSqrDMD_load.cross_correlation_array, cross_correlation_array)
        np.testing.assert_equal(
            TLSqrDMD_load.adv_correlation_array, adv_correlation_array)
        np.testing.assert_equal(
            TLSqrDMD_load.sum_correlation_array, sum_correlation_array)
        np.testing.assert_equal(
            TLSqrDMD_load.proj_correlation_array, proj_correlation_array)
        np.testing.assert_equal(
            np.array(TLSqrDMD_load.spectral_coeffs).squeeze(), spectral_coeffs)
        np.testing.assert_equal(
            TLSqrDMD_load.proj_coeffs, proj_coeffs)
        np.testing.assert_equal(
            TLSqrDMD_load.adv_proj_coeffs, adv_proj_coeffs)


    #@unittest.skip('Testing something else.')
    def test_compute_decomp(self):
        """Test TLSqrDMD decomposition"""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated TLSqrDMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute DMD using modred
                TLSqrDMD = dmd.TLSqrDMDHandles(
                    inner_product=np.vdot, verbosity=0)
                (eigvals, R_low_order_eigvecs, L_low_order_eigvecs,
                sum_correlation_array_eigvals,
                sum_correlation_array_eigvecs,
                proj_correlation_array_eigvals,
                proj_correlation_array_eigvecs) = TLSqrDMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Test correlation array values by simply recomputing them.
                # Here compute the full inner product array, rather than
                # assuming it is symmetric.
                np.testing.assert_allclose(
                    TLSqrDMD.vec_space.compute_inner_product_array(
                        vecs_vals, vecs_vals),
                    TLSqrDMD.correlation_array,
                    rtol=rtol, atol=atol)
                np.testing.assert_allclose(
                    TLSqrDMD.vec_space.compute_inner_product_array(
                        vecs_vals, adv_vecs_vals),
                    TLSqrDMD.cross_correlation_array,
                    rtol=rtol, atol=atol)
                np.testing.assert_allclose(
                    TLSqrDMD.vec_space.compute_inner_product_array(
                        adv_vecs_vals, adv_vecs_vals),
                    TLSqrDMD.adv_correlation_array,
                    rtol=rtol, atol=atol)

                # Test sum correlation array values by adding together
                # correlation arrays.
                np.testing.assert_allclose(
                    TLSqrDMD.correlation_array +
                    TLSqrDMD.adv_correlation_array,
                    TLSqrDMD.sum_correlation_array,
                    rtol=rtol, atol=atol)

                # Test sum correlation array eigenvalues and eigenvectors.
                np.testing.assert_allclose(
                    TLSqrDMD.sum_correlation_array.dot(
                        sum_correlation_array_eigvecs),
                    sum_correlation_array_eigvecs.dot(
                        np.diag(sum_correlation_array_eigvals)),
                    rtol=rtol, atol=atol)

                # Test projected correlation array values by projecting the raw
                # data, saving them to disk using handles, and then
                # computing the correlation array of the projected vectors.
                proj_array = TLSqrDMD.sum_correlation_array_eigvecs.dot(
                    TLSqrDMD.sum_correlation_array_eigvecs.conj().T)
                proj_vec_path = join(
                    self.test_dir, 'tlsqrdmd_proj_vec_%03d.pkl')
                proj_vecs_handles = [
                    VecHandlePickle(proj_vec_path % i)
                    for i in range(len(vecs_vals))]
                TLSqrDMD.vec_space.lin_combine(
                    proj_vecs_handles, vecs_vals, proj_array)
                np.testing.assert_allclose(
                    TLSqrDMD.vec_space.compute_inner_product_array(
                        proj_vecs_handles, proj_vecs_handles),
                    TLSqrDMD.proj_correlation_array,
                    rtol=rtol, atol=atol)

                # Test projected correlation array eigenvalues and eigenvectors.
                np.testing.assert_allclose(
                    TLSqrDMD.proj_correlation_array.dot(
                        proj_correlation_array_eigvecs),
                    proj_correlation_array_eigvecs.dot(
                        np.diag(proj_correlation_array_eigvals)),
                    rtol=rtol, atol=atol)

                # Compute the projection of the approximating linear operator
                # relating the projected vecs to the projected adv_vecs.  To do
                # this, compute the POD modes of the projected vecs using the
                # eigendecomposition of the projected correlation array.
                proj_POD_build_coeffs = proj_correlation_array_eigvecs.dot(
                    np.diag(proj_correlation_array_eigvals ** -0.5))
                proj_POD_mode_path = join(
                    self.test_dir, 'proj_pod_mode_%03d.txt')
                proj_POD_mode_handles = [
                    VecHandlePickle(proj_POD_mode_path % i)
                    for i in range(proj_correlation_array_eigvals.size)]
                TLSqrDMD.vec_space.lin_combine(
                    proj_POD_mode_handles, vecs_vals, proj_POD_build_coeffs)
                low_order_linear_op = (
                    TLSqrDMD.vec_space.compute_inner_product_array(
                        proj_POD_mode_handles, adv_vecs_vals).dot(
                            proj_correlation_array_eigvecs.dot(
                                np.diag(proj_correlation_array_eigvals ** -0.5
                                ))))

                # Test the left and right eigenvectors of the low-order
                # (projected) approximating linear operator.
                np.testing.assert_allclose(
                    low_order_linear_op.dot(R_low_order_eigvecs),
                    R_low_order_eigvecs.dot(np.diag(eigvals)),
                    rtol=rtol, atol=atol)
                np.testing.assert_allclose(
                    L_low_order_eigvecs.conj().T.dot(low_order_linear_op),
                    np.diag(eigvals).dot(L_low_order_eigvecs.conj().T),
                    rtol=rtol, atol=atol)

                # Check that returned values match internal values
                np.testing.assert_equal(eigvals, TLSqrDMD.eigvals)
                np.testing.assert_equal(
                    R_low_order_eigvecs, TLSqrDMD.R_low_order_eigvecs)
                np.testing.assert_equal(
                    L_low_order_eigvecs, TLSqrDMD.L_low_order_eigvecs)
                np.testing.assert_equal(
                    sum_correlation_array_eigvals,
                    TLSqrDMD.sum_correlation_array_eigvals)
                np.testing.assert_equal(
                    sum_correlation_array_eigvecs,
                    TLSqrDMD.sum_correlation_array_eigvecs)
                np.testing.assert_equal(
                    proj_correlation_array_eigvals,
                    TLSqrDMD.proj_correlation_array_eigvals)
                np.testing.assert_equal(
                    proj_correlation_array_eigvecs,
                    TLSqrDMD.proj_correlation_array_eigvecs)

        # Check that if mismatched sets of handles are passed in, an error is
        # raised.
        TLSqrDMD = dmd.TLSqrDMDHandles(inner_product=np.vdot, verbosity=0)
        self.assertRaises(
            ValueError, TLSqrDMD.compute_decomp, self.vec_handles,
            self.adv_vec_handles[:-1])


    #@unittest.skip('Testing something else.')
    def test_compute_modes(self):
        """Test building of modes."""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated TLSqrDMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute TLSqrDMD using modred.  (The properties defining a
                # TLSqrDMD mode require manipulations involving the correct
                # decomposition, so we cannot isolate the mode computation from
                # the decomposition step.)
                TLSqrDMD = dmd.TLSqrDMDHandles(
                    inner_product=np.vdot, verbosity=0)
                TLSqrDMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Compute the projection of the approximating linear operator
                # relating the projected vecs to the projected adv_vecs.  To do
                # this, compute the POD modes of the projected vecs using the
                # eigendecomposition of the projected correlation array.
                proj_POD_build_coeffs = (
                    TLSqrDMD.proj_correlation_array_eigvecs.dot(
                        np.diag(TLSqrDMD.proj_correlation_array_eigvals ** -0.5
                        )))
                proj_POD_mode_path = join(
                    self.test_dir, 'proj_pod_mode_%03d.txt')
                proj_POD_mode_handles = [
                    VecHandlePickle(proj_POD_mode_path % i) for i in
                    range(TLSqrDMD.proj_correlation_array_eigvals.size)]
                TLSqrDMD.vec_space.lin_combine(
                    proj_POD_mode_handles, vecs_vals, proj_POD_build_coeffs)

                # Select a subset of modes to compute.  Compute at least half
                # the modes, and up to all of them.  Make sure to use unique
                # values.  (This may reduce the number of modes computed.)
                num_modes = parallel.call_and_bcast(
                    np.random.randint,
                    TLSqrDMD.eigvals.size // 2, TLSqrDMD.eigvals.size + 1)
                mode_idxs = np.unique(parallel.call_and_bcast(
                    np.random.randint,
                    0, TLSqrDMD.eigvals.size, num_modes))

                # Create handles for the modes
                TLSqrDMD_exact_mode_handles = [
                    VecHandlePickle(self.exact_mode_path % i)
                    for i in mode_idxs]
                TLSqrDMD_proj_mode_handles = [
                    VecHandlePickle(self.proj_mode_path % i)
                    for i in mode_idxs]
                TLSqrDMD_adjoint_mode_handles = [
                    VecHandlePickle(self.adjoint_mode_path % i)
                    for i in mode_idxs]

                # Compute modes
                TLSqrDMD.compute_exact_modes(
                    mode_idxs, TLSqrDMD_exact_mode_handles)
                TLSqrDMD.compute_proj_modes(
                    mode_idxs, TLSqrDMD_proj_mode_handles)
                TLSqrDMD.compute_adjoint_modes(
                    mode_idxs, TLSqrDMD_adjoint_mode_handles)

                # Test that exact modes are eigenvectors of the approximating
                # linear operator by checking A \Phi = \Phi \Lambda.  Do this
                # using handles, i.e. check mode by mode.  Note that since
                # np.vdot takes the conjugate of its second argument, whereas
                # modred assumes a conjugate is taken on the first inner product
                # argument, the inner product array in the LHS computation must
                # be conjugated.
                LHS_path = join(self.test_dir, 'LHS_%03d.pkl')
                LHS_handles = [
                    VecHandlePickle(LHS_path % i) for i in mode_idxs]
                RHS_path = join(self.test_dir, 'RHS_%03d.pkl')
                RHS_handles = [
                    VecHandlePickle(RHS_path % i) for i in mode_idxs]
                TLSqrDMD.vec_space.lin_combine(
                    LHS_handles,
                    adv_vecs_vals,
                    TLSqrDMD.proj_correlation_array_eigvecs.dot(np.diag(
                        TLSqrDMD.proj_correlation_array_eigvals ** -0.5).dot(
                            TLSqrDMD.vec_space.compute_inner_product_array(
                                proj_POD_mode_handles,
                                TLSqrDMD_exact_mode_handles))))
                TLSqrDMD.vec_space.lin_combine(
                    RHS_handles,
                    TLSqrDMD_exact_mode_handles,
                    np.diag(TLSqrDMD.eigvals[mode_idxs]))
                for LHS, RHS in zip(LHS_handles, RHS_handles):
                    np.testing.assert_allclose(
                        LHS.get(), RHS.get(), rtol=rtol, atol=atol)

                # Test that projected modes are eigenvectors of the projection
                # of the approximating linear operator by checking
                # U U^* A \Phi = \Phi \Lambda.  As above, check this using
                # handles, and be careful about the order of arguments when
                # taking inner products.
                LHS_path = join(self.test_dir, 'LHS_%03d.pkl')
                LHS_handles = [
                    VecHandlePickle(LHS_path % i) for i in mode_idxs]
                RHS_path = join(self.test_dir, 'RHS_%03d.pkl')
                RHS_handles = [
                    VecHandlePickle(RHS_path % i) for i in mode_idxs]
                TLSqrDMD.vec_space.lin_combine(
                    LHS_handles,
                    proj_POD_mode_handles,
                    TLSqrDMD.vec_space.compute_inner_product_array(
                        proj_POD_mode_handles, adv_vecs_vals).dot(
                            TLSqrDMD.proj_correlation_array_eigvecs.dot(np.diag(
                                TLSqrDMD.proj_correlation_array_eigvals ** -0.5
                            ).dot(
                                TLSqrDMD.vec_space.compute_inner_product_array(
                                    proj_POD_mode_handles,
                                    TLSqrDMD_proj_mode_handles)))))
                TLSqrDMD.vec_space.lin_combine(
                    RHS_handles,
                    TLSqrDMD_proj_mode_handles,
                    np.diag(TLSqrDMD.eigvals[mode_idxs]))
                for LHS, RHS in zip(LHS_handles, RHS_handles):
                    np.testing.assert_allclose(
                        LHS.get(), RHS.get(), rtol=rtol, atol=atol)

                # Test that adjoint modes are eigenvectors of the conjugate
                # transpose of approximating linear operator by checking
                # A^* \Phi = \Phi \Lambda^*.  Do this using handles, i.e. check
                # mode by mode.  Note that since np.vdot takes the conjugate of
                # its second argument, whereas modred assumes a conjugate is
                # taken on the first inner product argument, the inner product
                # array in the LHS computation must be conjugated.
                LHS_path = join(self.test_dir, 'LHS_%03d.pkl')
                LHS_handles = [
                    VecHandlePickle(LHS_path % i) for i in mode_idxs]
                RHS_path = join(self.test_dir, 'RHS_%03d.pkl')
                RHS_handles = [
                    VecHandlePickle(RHS_path % i) for i in mode_idxs]
                TLSqrDMD.vec_space.lin_combine(
                    LHS_handles,
                    proj_POD_mode_handles,
                    np.diag(
                        TLSqrDMD.proj_correlation_array_eigvals ** -0.5).dot(
                            TLSqrDMD.proj_correlation_array_eigvecs.\
                            conj().T.dot(
                                TLSqrDMD.vec_space.compute_inner_product_array(
                                    adv_vecs_vals,
                                    TLSqrDMD_adjoint_mode_handles))))
                TLSqrDMD.vec_space.lin_combine(
                    RHS_handles,
                    TLSqrDMD_adjoint_mode_handles,
                    np.diag(TLSqrDMD.eigvals[mode_idxs]).conj().T)
                for LHS, RHS in zip(LHS_handles, RHS_handles):
                    np.testing.assert_allclose(
                        LHS.get(), RHS.get(), rtol=rtol, atol=atol)


    #@unittest.skip('Testing something else.')
    def test_compute_spectrum(self):
        """Test TLSqrDMD spectrum"""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated DMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute TLSqrDMD using modred.  (The TLSqrDMD spectral
                # coefficients are defined by a projection onto TLSqrDMD modes.
                # As such, testing them requires manipulations involving the
                # correct decomposition and modes, so we cannot isolate the
                # spectral coefficient computation from those computations.)
                TLSqrDMD = dmd.TLSqrDMDHandles(
                    inner_product=np.vdot, verbosity=0)
                TLSqrDMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Compute the projection of the vecs.
                proj_array = TLSqrDMD.sum_correlation_array_eigvecs.dot(
                    TLSqrDMD.sum_correlation_array_eigvecs.conj().T)
                proj_vecs_handles = [
                    VecHandlePickle(self.proj_vec_path % i)
                    for i in range(len(vecs_vals))]
                TLSqrDMD.vec_space.lin_combine(
                    proj_vecs_handles, vecs_vals, proj_array)

                # Test by checking a least-squares projection (of the projected
                # vecs) onto the projected modes, which is analytically
                # equivalent to a biorthogonal projection onto the exact modes.
                # The latter is implemented (using various identities) in
                # modred.  Here, test using the former approach, as it doesn't
                # require adjoint modes.
                mode_idxs = range(TLSqrDMD.eigvals.size)
                proj_mode_handles = [
                    VecHandlePickle(self.proj_mode_path % i)
                    for i in mode_idxs]
                TLSqrDMD.compute_proj_modes(mode_idxs, proj_mode_handles)
                spectral_coeffs_true = np.abs(np.linalg.inv(
                    TLSqrDMD.vec_space.compute_symm_inner_product_array(
                        proj_mode_handles)).dot(
                            TLSqrDMD.vec_space.compute_inner_product_array(
                                proj_mode_handles,
                                proj_vecs_handles[0]))).squeeze()
                spectral_coeffs = TLSqrDMD.compute_spectrum()
                np.testing.assert_allclose(
                    spectral_coeffs, spectral_coeffs_true, rtol=rtol, atol=atol)


    #@unittest.skip('Testing something else.')
    def test_compute_proj_coeffs(self):
        """Test projection coefficients"""
        rtol = 1e-10
        atol = 1e-12

        # Consider sequential time series as well as non-sequential.  In the
        # below for loop, the first elements of each zipped list correspond to a
        # sequential time series.  The second elements correspond to a
        # non-sequential time series.
        for vecs_arg, adv_vecs_arg, vecs_vals, adv_vecs_vals in zip(
            [self.vec_handles, self.vec_handles],
            [None, self.adv_vec_handles],
            [self.vec_handles[:-1], self.vec_handles],
            [self.vec_handles[1:], self.adv_vec_handles]):

            # Test that results hold for truncated or untruncated DMD
            # (i.e., whether or not the underlying POD basis is
            # truncated).
            for max_num_eigvals in [None, self.num_vecs // 2]:

                # Compute TLSqrDMD using modred.  (Testing the TLSqrDMD
                # projection coefficients requires the correct TLSqrDMD
                # decomposition and modes, so we cannot isolate the projection
                # coefficient computation from those computations.)
                TLSqrDMD = dmd.TLSqrDMDHandles(
                    inner_product=np.vdot, verbosity=0)
                TLSqrDMD.compute_decomp(
                    vecs_arg, adv_vec_handles=adv_vecs_arg,
                    max_num_eigvals=max_num_eigvals)

                # Compute the projection of the vecs and advanced vecs.
                proj_array = TLSqrDMD.sum_correlation_array_eigvecs.dot(
                    TLSqrDMD.sum_correlation_array_eigvecs.conj().T)
                proj_vecs_handles = [
                    VecHandlePickle(self.proj_vec_path % i)
                    for i in range(len(vecs_vals))]
                proj_adv_vecs_handles = [
                    VecHandlePickle(self.proj_adv_vec_path % i)
                    for i in range(len(vecs_vals))]
                TLSqrDMD.vec_space.lin_combine(
                    proj_vecs_handles, vecs_vals, proj_array)
                TLSqrDMD.vec_space.lin_combine(
                    proj_adv_vecs_handles, adv_vecs_vals, proj_array)

                # Test by checking a least-squares projection (of the projected
                # vecs) onto the projected modes, which is analytically
                # equivalent to a biorthogonal projection onto the exact modes.
                # The latter is implemented (using various identities) in
                # modred.  Here, test using the former approach, as it doesn't
                # require adjoint modes.
                mode_idxs = range(TLSqrDMD.eigvals.size)
                proj_mode_handles = [
                    VecHandlePickle(self.proj_mode_path % i)
                    for i in mode_idxs]
                TLSqrDMD.compute_proj_modes(mode_idxs, proj_mode_handles)
                proj_coeffs_true = np.linalg.inv(
                    TLSqrDMD.vec_space.compute_symm_inner_product_array(
                        proj_mode_handles)).dot(
                            TLSqrDMD.vec_space.compute_inner_product_array(
                                proj_mode_handles, proj_vecs_handles))
                adv_proj_coeffs_true = np.linalg.inv(
                    TLSqrDMD.vec_space.compute_symm_inner_product_array(
                        proj_mode_handles)).dot(
                            TLSqrDMD.vec_space.compute_inner_product_array(
                                proj_mode_handles, proj_adv_vecs_handles))
                proj_coeffs, adv_proj_coeffs = TLSqrDMD.compute_proj_coeffs()
                np.testing.assert_allclose(
                    proj_coeffs, proj_coeffs_true, rtol=rtol, atol=atol)


if __name__ == '__main__':
    unittest.main()
