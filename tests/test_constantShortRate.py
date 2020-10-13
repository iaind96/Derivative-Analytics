from unittest import TestCase
import datetime as dt
import numpy as np
from numpy.testing import assert_array_equal

from dx.instruments import ConstantShortRate
from dx.utils import get_year_deltas


class TestConstantShortRate(TestCase):

    def test_rate(self):
        csr = ConstantShortRate("rate", 0.05)

        self.assertEqual(csr.rate, 0.05)

        with self.assertRaises(ValueError):
            csr.rate = -0.05

    def test_get_discount_factors(self):
        csr = ConstantShortRate("rate", 0.05)
        deltas = np.array([0, 0.5, 1])

        assert_array_equal(csr.get_discount_factors(deltas, dt_objects=False), np.array([deltas, np.exp(-0.05 * deltas)]).T)

        dates = np.array([dt.datetime(2020, 1, 1), dt.datetime(2020, 7, 1), dt.datetime(2021, 1, 1)])
        deltas = get_year_deltas(dates)

        assert_array_equal(csr.get_discount_factors(dates, dt_objects=True), np.array([deltas, np.exp(-0.05 * deltas)]).T)
