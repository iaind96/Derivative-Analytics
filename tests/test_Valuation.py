from unittest import TestCase
import datetime as dt
import numpy as np

from dx.valuation import MCValuation, BSValuation
from dx.instruments import Stock, ConstantShortRate, VanillaOption
from dx.environment import MarketEnvironment


class TestBSValuation(TestCase):

    def test_get_present_value(self):
        discount_curve = ConstantShortRate("discount_curve", 0.03)
        stock = Stock("stock", 100.0, 0.2)

        mar_env = MarketEnvironment("market", dt.datetime(2020, 1, 1))
        mar_env.add_curve("discount_curve", discount_curve)
        mar_env.add_instrument("stock", stock)

        option = VanillaOption("option", stock, 110.0, dt.datetime(2020, 7, 1), "call")
        valuation = BSValuation(mar_env, option)
        pv_call = valuation.get_present_value()

        option = VanillaOption("option", stock, 110.0, dt.datetime(2020, 7, 1), "put")
        valuation = BSValuation(mar_env, option)
        pv_put = valuation.get_present_value()

        T = (dt.datetime(2020, 7, 1) - dt.datetime(2020, 1, 1)).days / 365

        # test put-call parity is satisfied
        self.assertAlmostEqual(pv_call - pv_put, 100.0 - np.exp(-0.03 * T) * 110.0, places=10)


class TestMCValuation(TestCase):

    def test_get_present_value(self):
        discount_curve = ConstantShortRate("discount_curve", 0.03)
        stock = Stock("stock", 100.0, 0.2)

        mar_env = MarketEnvironment("market", dt.datetime(2020, 1, 1))
        mar_env.add_curve("discount_curve", discount_curve)
        mar_env.add_instrument("stock", stock)

        option = VanillaOption("option", stock, 110.0, dt.datetime(2020, 7, 1), "call")
        valuation = MCValuation(mar_env, option)
        pv_mc = valuation.get_present_value(100000)

