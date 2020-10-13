from unittest import TestCase
import datetime as dt
import numpy as np
from numpy.testing import assert_array_equal

from dx.utils import get_year_deltas


class TestGetYearDeltas(TestCase):

    def test_get_year_deltas(self):
        dates = np.array([dt.datetime(2020, 1, 1), dt.datetime(2020, 7, 1), dt.datetime(2021, 1, 1)])

        true_deltas = np.array([0.0, 182.0, 366.0]) / 365

        assert_array_equal(get_year_deltas(dates), true_deltas)