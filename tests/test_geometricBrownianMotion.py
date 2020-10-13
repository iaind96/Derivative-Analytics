from unittest import TestCase
import datetime as dt

from dx.simulation import GeometricBrownianMotion
from dx.environment import MarketEnvironment
from dx.instruments import Stock, ConstantShortRate


class TestGeometricBrownianMotion(TestCase):

    def test_simulate_paths(self):
        discount_curve = ConstantShortRate("discount_curve", 0.03)
        stock = Stock("stock", 100.0, 0.2)

        mar_env = MarketEnvironment("market", dt.datetime(2020, 1, 1))
        mar_env.add_curve("discount_curve", discount_curve)
        mar_env.add_instrument("stock", stock)

        gbm_sim = GeometricBrownianMotion("gbm_sim", mar_env)

        paths = gbm_sim.simulate_paths(dt.datetime(2020, 12, 31), 100, "B")

        self.assertTupleEqual(paths["stock"].shape, (262, 100))

    # def test_market_environment_completeness(self):
    #     mar_env = MarketEnvironment("market", dt.datetime(2020, 1, 1))
    #
    #     gbm_sim = GeometricBrownianMotion("gbm_sim", mar_env)
    #
    #     with self.assertRaises(KeyError):
    #         gbm_sim.simulate_paths(dt.datetime(2020, 12, 31), 100, "B")
    #     # gbm_sim.simulate_paths(dt.datetime(2020, 12, 31), 100, "B")
    #     # self.assertTupleEqual(paths["stock"].shape, (262, 100))