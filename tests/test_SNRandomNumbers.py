from unittest import TestCase
import numpy as np
from numpy.testing import assert_array_equal

from dx.random import sn_random_numbers


class TestSNRandomNumbers(TestCase):

    def test_sn_random_numbers(self):
        rns = sn_random_numbers((2, 2), antithetic=False, moment_matching=False)

        self.assertTupleEqual(rns.shape, (2, 2))

        rns = sn_random_numbers((2, 2, 2), antithetic=False, moment_matching=False)

        self.assertTupleEqual(rns.shape, (2, 2, 2))

    def test_sn_random_numbers_antithetic(self):
        rns = sn_random_numbers((2, 2, 2), antithetic=True)

        self.assertTupleEqual(rns.shape, (2, 2, 2))
        assert_array_equal(rns[:, :, 0], -rns[:, :, 1])

        with self.assertRaises(ValueError):
            sn_random_numbers((2, 2, 3), antithetic=True)

    def test_sn_random_numbers_moment_matching(self):
        rns = sn_random_numbers((2, 2, 2), moment_matching=True)

        self.assertAlmostEqual(np.mean(rns), 0.0, places=10)
        self.assertAlmostEqual(np.std(rns), 1.0, places=10)

    def test_sn_random_numbers_fixed_seed(self):
        rns = sn_random_numbers((2, 2, 2), fixed_seed=True)
        rns2 = sn_random_numbers((2, 2, 2), fixed_seed=True)

        assert_array_equal(rns, rns2)