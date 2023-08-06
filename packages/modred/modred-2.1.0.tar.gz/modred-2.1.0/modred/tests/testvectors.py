#!/usr/bin/env python
"""Test vectors module"""
import unittest
import os
from os.path import join
from shutil import rmtree

import numpy as np

from modred import vectors as vcs, parallel


@unittest.skipIf(parallel.is_distributed(), 'No need to test in parallel')
class TestVectors(unittest.TestCase):
    """Test the vector methods """
    def setUp(self):
        self.test_dir = 'files_vectors_DELETE_ME'
        if not os.access('.', os.W_OK):
            raise RuntimeError('Cannot write to current directory')
        if not os.path.isdir(self.test_dir) and parallel.is_rank_zero():
            os.mkdir(self.test_dir)
        parallel.barrier()
        self.mode_nums = [2, 4, 3, 6, 9, 8, 10, 11, 30]
        self.num_vecs = 40
        self.num_states = 100
        self.index_from = 2


    def tearDown(self):
        parallel.barrier()
        if parallel.is_rank_zero():
            rmtree(self.test_dir, ignore_errors=True)
        parallel.barrier()


    #@unittest.skip('Testing something else.')
    def test_in_memory_handle(self):
        """Test in memory and base class vector handles"""
        # Test real and complex data
        for is_complex in [True, False]:
            base_vec1 = np.random.random((3, 4))
            base_vec2 = np.random.random((3, 4))
            vec_true = np.random.random((3, 4))
            scale = np.random.random()
            if is_complex:
                base_vec1 = base_vec1 + 1j * base_vec1
                base_vec2 = base_vec2 - 1j * base_vec2
                vec_true = vec_true + 2j * vec_true
                scale = scale - 3j * scale

            # Test base class functionality
            vec_handle = vcs.VecHandleInMemory(
                vec=vec_true,
                base_vec_handle=vcs.VecHandleInMemory(vec=base_vec1),
                scale=scale)
            vec_val = vec_handle.get()
            np.testing.assert_equal(vec_val, scale * (vec_true - base_vec1))

            vec_handle = vcs.VecHandleInMemory(
                vec=vec_true,
                base_vec_handle=vcs.VecHandleInMemory(vec=base_vec2),
                scale=scale)
            vec_val = vec_handle.get()
            np.testing.assert_equal(vec_val, scale * (vec_true - base_vec2))

            vec_handle = vcs.VecHandleInMemory(
                vec=vec_true,
                base_vec_handle=vcs.VecHandleInMemory(vec=base_vec1))
            vec_val = vec_handle.get()
            np.testing.assert_equal(vec_val, vec_true - base_vec1)

            vec_handle = vcs.VecHandleInMemory(vec=vec_true)
            vec_val = vec_handle.get()
            np.testing.assert_equal(vec_val, vec_true)

            # Test put
            vec_handle = vcs.VecHandleInMemory()
            vec_handle.put(vec_true)
            np.testing.assert_equal(vec_handle.vec, vec_true)

            # Test __eq__ operator
            vec_handle1 = vcs.VecHandleInMemory(vec=np.ones(2))
            vec_handle2 = vcs.VecHandleInMemory(vec=np.ones(2))
            vec_handle3 = vcs.VecHandleInMemory(vec=np.ones(3))
            vec_handle4 = vcs.VecHandleInMemory(vec=np.zeros(2))
            self.assertEqual(vec_handle1, vec_handle1)
            self.assertEqual(vec_handle1, vec_handle2)
            self.assertNotEqual(vec_handle1, vec_handle3)
            self.assertNotEqual(vec_handle1, vec_handle4)


    #@unittest.skip('Testing something else.')
    def test_handles_that_save(self):
        """Test handles whose get/put load/save from file"""
        # Test real and complex data
        for is_complex in [True, False]:
            base_vec1 = np.random.random((3, 4))
            base_vec2 = np.random.random((3, 4))
            vec_true = np.random.random((3, 4))
            if is_complex:
                base_vec1 = base_vec1 + 1j * base_vec1
                base_vec2 = base_vec2 - 1j * base_vec2
                vec_true = vec_true + 2j * vec_true

            # Define paths for saving data
            vec_true_path = join(self.test_dir, 'test_vec')
            vec_saved_path = join(self.test_dir, 'put_vec')
            base_path1 = join(self.test_dir, 'base_vec1')
            base_path2 = join(self.test_dir, 'base_vec2')

            # Test different handle types
            for VecHandle in [vcs.VecHandleArrayText, vcs.VecHandlePickle]:

                # Save data to disk
                VecHandle(base_path1).put(base_vec1)
                VecHandle(base_path2).put(base_vec2)
                VecHandle(vec_true_path).put(vec_true)

                # Test get (VecHandleArrayText needs to know if it is loading
                # complex data, so try both)
                try:
                    vec_handle = VecHandle(vec_true_path, is_complex=is_complex)
                except:
                    vec_handle = VecHandle(vec_true_path)
                vec_val = vec_handle.get()
                np.testing.assert_allclose(vec_val, vec_true)

                # Test put (VecHandleArrayText needs to know if it is loading
                # complex data, so try both)
                try:
                    vec_handle = VecHandle(
                        vec_saved_path, is_complex=is_complex)
                except:
                    vec_handle = VecHandle(vec_saved_path)
                vec_handle.put(vec_true)
                np.testing.assert_equal(vec_handle.get(), vec_true)

                # Test __eq__ operator
                vec_handle1 = VecHandle('a')
                vec_handle2 = VecHandle('a')
                vec_handle3 = VecHandle('aa')
                vec_handle4 = VecHandle('b')
                self.assertEqual(vec_handle1, vec_handle1)
                self.assertEqual(vec_handle1, vec_handle2)
                self.assertNotEqual(vec_handle1, vec_handle3)
                self.assertNotEqual(vec_handle1, vec_handle4)


    #@unittest.skip('Testing something else.')
    def test_IP_trapz(self):
        """Test trapezoidal rule inner product for 2nd-order convergence"""
        # Known inner product of x ** 2 + 1.2 * y ** 2 and x ** 2 over interval
        # -1 < x < 1 and -2 < y < 2.
        ip_true = 5.8666666
        ip_error = []
        num_points_list = [20, 100]
        for num_points in num_points_list:
            x_grid = np.cos(np.linspace(0, np.pi, num_points))[::-1]
            y_grid = 2*np.cos(np.linspace(0, np.pi, num_points+1))[::-1]

            # Notice order is reversed. This gives dimensions [nx, ny]
            # instead of [ny, nx]. See np.meshgrid documentation.
            Y, X = np.meshgrid(y_grid, x_grid)
            v1 = X ** 2 + 1.2 * Y ** 2
            v2 = X ** 2
            ip_comp = vcs.InnerProductTrapz(x_grid, y_grid)(v1, v2)
            ip_error.append(np.abs(ip_comp - ip_true))
        convergence = (
            (np.log(ip_error[1]) - np.log(ip_error[0])) /
            (np.log(num_points_list[1]) - np.log(num_points_list[0])))
        self.assertTrue(convergence < -1.9)


if __name__ == '__main__':
    unittest.main()
