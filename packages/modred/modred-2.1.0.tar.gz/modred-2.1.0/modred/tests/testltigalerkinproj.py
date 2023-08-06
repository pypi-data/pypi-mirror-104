#!/usr/bin/env python
"""Test ltigalerkinproj module"""
import unittest
import os
from os.path import join
from shutil import rmtree

import numpy as np

from modred import ltigalerkinproj as lgp, parallel, util
from modred import util
from modred.py2to3 import range
from modred.vectors import VecHandlePickle


#@unittest.skip('Testing something else.')
class TestLTIGalerkinProjectionBase(unittest.TestCase):
    def setUp(self):
        if not os.access('.', os.W_OK):
            raise RuntimeError('Cannot write to current directory')
        self.test_dir ='files_LTIGalerkinProj_DELETE_ME'
        if parallel.is_rank_zero() and not os.path.exists(self.test_dir):
            os.mkdir(self.test_dir)
        parallel.barrier()


    def tearDown(self):
        parallel.barrier()
        parallel.call_from_rank_zero(rmtree, self.test_dir, ignore_errors=True)
        parallel.barrier()


    def test_put_reduced_arrays(self):
        """Test putting reduced mats"""
        A_reduced_path = join(self.test_dir, 'A.txt')
        B_reduced_path = join(self.test_dir, 'B.txt')
        C_reduced_path = join(self.test_dir, 'C.txt')
        A = parallel.call_and_bcast(np.random.random, ((10, 10)))
        B = parallel.call_and_bcast(np.random.random, ((1, 10)))
        C = parallel.call_and_bcast(np.random.random, ((10, 2)))
        LTI_proj = lgp.LTIGalerkinProjectionBase()
        LTI_proj.A_reduced = A.copy()
        LTI_proj.B_reduced = B.copy()
        LTI_proj.C_reduced = C.copy()
        LTI_proj.put_model(A_reduced_path, B_reduced_path, C_reduced_path)
        np.testing.assert_equal(util.load_array_text(A_reduced_path), A)
        np.testing.assert_equal(util.load_array_text(B_reduced_path), B)
        np.testing.assert_equal(util.load_array_text(C_reduced_path), C)


#@unittest.skip('Testing something else.')
@unittest.skipIf(parallel.is_distributed(), 'Serial only')
class TestLTIGalerkinProjectionArrays(unittest.TestCase):
    """Tests that can find the correct A, B, and C arrays."""
    def setUp(self):
        self.num_basis_vecs = 10
        self.num_adjoint_basis_vecs = 10
        self.num_states = 11
        self.num_inputs = 3
        self.num_outputs = 2

        self.generate_data_set(
            self.num_basis_vecs, self.num_adjoint_basis_vecs,
            self.num_states, self.num_inputs, self.num_outputs)

        self.LTI_proj = lgp.LTIGalerkinProjectionArrays(
            self.basis_vecs, adjoint_basis_vecs=self.adjoint_basis_vecs,
            is_basis_orthonormal=True)


    def tearDown(self):
        pass


    def test_init(self):
        """ """
        pass


    def generate_data_set(
        self, num_basis_vecs, num_adjoint_basis_vecs,
        num_states, num_inputs, num_outputs):
        """Generates random data, saves, and computes true reduced A, B, C."""
        self.basis_vecs = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_basis_vecs)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_basis_vecs)))
        self.adjoint_basis_vecs =(
            parallel.call_and_bcast(
                np.random.random, (num_states, num_basis_vecs)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_basis_vecs)))
        self.A_array = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_states)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_states)))
        self.B_array = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_inputs)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_inputs)))
        self.C_array = (
            parallel.call_and_bcast(
                np.random.random, (num_outputs, num_states)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_outputs, num_states)))

        self.A_on_basis_vecs = self.A_array.dot(self.basis_vecs)
        self.B_on_standard_basis_array = self.B_array
        self.C_on_basis_vecs = self.C_array.dot(self.basis_vecs).squeeze()

        parallel.barrier()

        self.A_true = self.adjoint_basis_vecs.conj().T.dot(
            self.A_array.dot(
                self.basis_vecs))
        self.B_true = self.adjoint_basis_vecs.conj().T.dot(self.B_array)
        self.C_true = self.C_array.dot(self.basis_vecs)
        self.proj_array = np.linalg.inv(
            self.adjoint_basis_vecs.conj().T.dot(self.basis_vecs))
        self.A_true_non_orth = self.proj_array.dot(self.A_true)
        self.B_true_non_orth = self.proj_array.dot(self.B_true)


    #@unittest.skip('Testing something else')
    def test_reduce_A(self):
        """Reduction of A array for Array, LookUp operators and in_memory."""
        A_returned = self.LTI_proj.reduce_A(self.A_on_basis_vecs)
        np.testing.assert_equal(A_returned, self.A_true)

        LTI_proj = lgp.LTIGalerkinProjectionArrays(
            self.basis_vecs, adjoint_basis_vecs=self.adjoint_basis_vecs,
            is_basis_orthonormal=False)
        A_returned = LTI_proj.reduce_A(self.A_on_basis_vecs)
        np.testing.assert_equal(LTI_proj._proj_array, self.proj_array)
        np.testing.assert_equal(A_returned, self.A_true_non_orth)


    #@unittest.skip('Testing something else')
    def test_reduce_B(self):
        """Given modes, test reduced B array"""
        B_returned = self.LTI_proj.reduce_B(self.B_on_standard_basis_array)
        np.testing.assert_equal(B_returned, self.B_true)

        LTI_proj = lgp.LTIGalerkinProjectionArrays(
            self.basis_vecs, adjoint_basis_vecs=self.adjoint_basis_vecs,
            is_basis_orthonormal=False)
        B_returned = LTI_proj.reduce_B(self.B_on_standard_basis_array)
        np.testing.assert_allclose(B_returned, self.B_true_non_orth)


    #@unittest.skip('Testing something else')
    def test_reduce_C(self):
        """Test that, given modes, can find correct C array"""
        C_returned = self.LTI_proj.reduce_C(self.C_on_basis_vecs)
        np.testing.assert_equal(C_returned, self.C_true)


    #@unittest.skip('Testing something else')
    def test_compute_model(self):
        # No test; just check it runs. Results are checked in other tests.
        A, B, C = self.LTI_proj.compute_model(
            self.A_on_basis_vecs, self.B_on_standard_basis_array,
            self.C_on_basis_vecs)


    #@unittest.skip('Testing something else')
    def test_adjoint_basis_vec_optional(self):
        """Test that adjoint modes default to direct modes"""
        no_adjoints_LTI_proj = lgp.LTIGalerkinProjectionArrays(
            self.basis_vecs, is_basis_orthonormal=True)
        np.testing.assert_equal(
            no_adjoints_LTI_proj.adjoint_basis_vecs,
            self.basis_vecs)


#@unittest.skip('Testing something else.')
#@unittest.skipIf(parallel.is_distributed(), 'Only test in serial')
class TestLTIGalerkinProjectionHandles(unittest.TestCase):
    """Tests that can find the correct A, B, and C arrays from modes."""
    def setUp(self):
        if not os.access('.', os.W_OK):
            raise RuntimeError('Cannot write to current directory')

        self.test_dir ='file_LTIGalerkinProj_DELETE_ME'
        if parallel.is_rank_zero() and not os.path.exists(self.test_dir):
            os.mkdir(self.test_dir)
        parallel.barrier()

        self.basis_vec_path = join(self.test_dir, 'basis_vec_%02d.txt')
        self.adjoint_basis_vec_path = join(
            self.test_dir, 'adjoint_basis_vec_%02d.txt')
        self.A_on_basis_vec_path = join(self.test_dir, 'A_on_mode_%02d.txt')
        self.B_on_basis_path = join(self.test_dir, 'B_on_basis_%02d.txt')
        self.C_on_basis_vec_path = join(self.test_dir, 'C_on_mode_%02d.txt')

        self.num_basis_vecs = 10
        self.num_adjoint_basis_vecs = 10
        self.num_states = 11
        self.num_inputs = 3
        self.num_outputs = 2

        self.generate_data_set(
            self.num_basis_vecs, self.num_adjoint_basis_vecs,
            self.num_states, self.num_inputs, self.num_outputs)

        self.LTI_proj = lgp.LTIGalerkinProjectionHandles(
            np.vdot, self.basis_vec_handles,
            adjoint_basis_vec_handles=self.adjoint_basis_vec_handles,
            is_basis_orthonormal=True, verbosity=0)


    def tearDown(self):
        parallel.barrier()
        if parallel.is_rank_zero():
            rmtree(self.test_dir, ignore_errors=True)
        parallel.barrier()


    def test_init(self):
        """ """
        pass


    def generate_data_set(self, num_basis_vecs, num_adjoint_basis_vecs,
        num_states, num_inputs, num_outputs):
        """Generates random data, saves, and computes true reduced A,B,C."""
        self.basis_vec_handles = [
            VecHandlePickle(self.basis_vec_path % i)
            for i in range(self.num_basis_vecs)]
        self.adjoint_basis_vec_handles = [
            VecHandlePickle(self.adjoint_basis_vec_path % i)
            for i in range(self.num_adjoint_basis_vecs)]
        self.A_on_basis_vec_handles = [
            VecHandlePickle(self.A_on_basis_vec_path % i)
            for i in range(self.num_basis_vecs)]
        self.B_on_standard_basis_handles = [
            VecHandlePickle(self.B_on_basis_path % i)
            for i in range(self.num_inputs)]
        self.C_on_basis_vec_handles = [
            VecHandlePickle(self.C_on_basis_vec_path % i)
            for i in range(self.num_basis_vecs)]

        self.basis_vec_array = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_basis_vecs)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_basis_vecs)))
        self.adjoint_basis_vec_array = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_adjoint_basis_vecs)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_adjoint_basis_vecs)))
        self.A_array = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_states)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_states)))
        self.B_array = (
            parallel.call_and_bcast(
                np.random.random, (num_states, num_inputs)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_states, num_inputs)))
        self.C_array = (
            parallel.call_and_bcast(
                np.random.random, (num_outputs, num_states)) +
            1j * parallel.call_and_bcast(
                np.random.random, (num_outputs, num_states)))

        self.basis_vecs = [
            self.basis_vec_array[:, i].squeeze() for i in range(num_basis_vecs)]
        self.adjoint_basis_vecs = [
            self.adjoint_basis_vec_array[:, i].squeeze()
            for i in range(num_adjoint_basis_vecs)]
        self.A_on_basis_vecs = [
            self.A_array.dot(basis_vec).squeeze()
            for basis_vec in self.basis_vecs]
        self.B_on_basis = [
            self.B_array[:, i].squeeze() for i in range(self.num_inputs)]
        self.C_on_basis_vecs = [
            np.array(self.C_array.dot(basis_vec).squeeze(), ndmin=1)
            for basis_vec in self.basis_vecs]

        if parallel.is_rank_zero():
            for handle,vec in zip(self.basis_vec_handles, self.basis_vecs):
                handle.put(vec)
            for handle,vec in zip(
                self.adjoint_basis_vec_handles, self.adjoint_basis_vecs):
                handle.put(vec)
            for handle,vec in zip(
                self.A_on_basis_vec_handles, self.A_on_basis_vecs):
                handle.put(vec)
            for handle,vec in zip(
                self.B_on_standard_basis_handles, self.B_on_basis):
                handle.put(vec)
            for handle,vec in zip(
                self.C_on_basis_vec_handles, self.C_on_basis_vecs):
                handle.put(vec)
        parallel.barrier()

        self.A_true = self.adjoint_basis_vec_array.conj().T.dot(
            self.A_array.dot(self.basis_vec_array))
        self.B_true = self.adjoint_basis_vec_array.conj().T.dot(self.B_array)
        self.C_true = self.C_array.dot(self.basis_vec_array)
        self.proj_array = np.linalg.inv(
            self.adjoint_basis_vec_array.conj().T.dot(self.basis_vec_array))
        self.A_true_non_orth = self.proj_array.dot(self.A_true)
        self.B_true_non_orth = self.proj_array.dot(self.B_true)


    #@unittest.skip('Testing something else')
    def test_derivs(self):
        """Test can take derivs"""
        dt = 0.1
        true_derivs = []
        num_vecs = len(self.basis_vec_handles)
        for i in range(num_vecs):
            true_derivs.append((
                self.A_on_basis_vec_handles[i].get() -
                self.basis_vec_handles[i].get()).squeeze() / dt)
        deriv_handles = [
            VecHandlePickle(join(self.test_dir, 'deriv_test%d' % i))
            for i in range(num_vecs)]
        lgp.compute_derivs_handles(
            self.basis_vec_handles, self.A_on_basis_vec_handles,
            deriv_handles, dt)
        derivs_loaded = [v.get() for v in deriv_handles]
        derivs_loaded = list(map(np.squeeze, derivs_loaded))
        list(map(np.testing.assert_allclose, derivs_loaded, true_derivs))


    #@unittest.skip('Testing something else')
    def test_reduce_A(self):
        """Reduction of A array for Array, LookUp operators and in_memory."""
        A_returned = self.LTI_proj.reduce_A(self.A_on_basis_vec_handles)
        np.testing.assert_allclose(A_returned, self.A_true)

        LTI_proj = lgp.LTIGalerkinProjectionHandles(
            np.vdot, self.basis_vec_handles,
            adjoint_basis_vec_handles=self.adjoint_basis_vec_handles,
            is_basis_orthonormal=False, verbosity=0)
        A_returned = LTI_proj.reduce_A(self.A_on_basis_vec_handles)
        np.testing.assert_allclose(LTI_proj._proj_array, self.proj_array)
        np.testing.assert_allclose(A_returned, self.A_true_non_orth)


    #@unittest.skip('Testing something else')
    def test_reduce_B(self):
        """Given modes, test reduced B array, orthogonal and non-orthogonal."""
        B_returned = self.LTI_proj.reduce_B(self.B_on_standard_basis_handles)
        np.testing.assert_allclose(B_returned, self.B_true)

        LTI_proj = lgp.LTIGalerkinProjectionHandles(
            np.vdot, self.basis_vec_handles,
            adjoint_basis_vec_handles=self.adjoint_basis_vec_handles,
            is_basis_orthonormal=False, verbosity=0)
        B_returned = LTI_proj.reduce_B(self.B_on_standard_basis_handles)
        np.testing.assert_allclose(B_returned, self.B_true_non_orth)


    #@unittest.skip('Testing something else')
    def test_reduce_C(self):
        """Test that, given modes, can find correct C array"""
        C_returned = self.LTI_proj.reduce_C(self.C_on_basis_vecs)
        np.testing.assert_allclose(C_returned, self.C_true)


    #@unittest.skip('Testing something else')
    def test_adjoint_basis_vec_optional(self):
        """Test that adjoint modes default to direct modes"""
        no_adjoints_LTI_proj = lgp.LTIGalerkinProjectionHandles(
            np.vdot, self.basis_vec_handles, is_basis_orthonormal=True,
            verbosity=0)
        np.testing.assert_equal(
            no_adjoints_LTI_proj.adjoint_basis_vec_handles,
            self.basis_vec_handles)


if __name__ == '__main__':
    unittest.main()
