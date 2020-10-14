from unittest import TestCase
import datetime as dt
import numpy as np
from numpy.testing import assert_array_equal

from dx.instruments import VanillaOption, Stock


class TestVanillaOption(TestCase):

    def test_payoff(self):
        stock = Stock("stock", 100.0, 0.3)
        call_option = VanillaOption("call_option", stock, 110.0, dt.datetime(2020, 7, 1), "call")

        S = np.array([120.0, 110.0, 100.0])
        assert_array_equal(call_option.payoff(S), np.array([10.0, 0.0, 0.0]))

        put_option = VanillaOption("put_option", stock, 110.0, dt.datetime(2020, 7, 1), "put")
        assert_array_equal(put_option.payoff(S), np.array([0.0, 0.0, 10.0]))

