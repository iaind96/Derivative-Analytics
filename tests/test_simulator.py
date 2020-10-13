from unittest import TestCase
import datetime as dt
import numpy as np
from numpy.testing import assert_array_equal

from dx.simulation import Simulator
from dx.environment import MarketEnvironment


class TestSimulator(TestCase):

    def test_generate_time_grid(self):
        mar_env = MarketEnvironment("env", dt.datetime(2020, 1, 1))
        simulator = Simulator("simulator", mar_env)

        true_time_grid = np.array([dt.datetime(2020, 1, i) for i in range(1, 11)])

        assert_array_equal(simulator.generate_time_grid(dt.datetime(2020, 1, 10), "D"), true_time_grid)

        mar_env.date = dt.datetime(2020, 1, 5)
        true_time_grid = np.array([dt.datetime(2020, 1, i) for i in [5, 6, 7, 8, 9, 10, 11]])

        assert_array_equal(simulator.generate_time_grid(dt.datetime(2020, 1, 11), "B"), true_time_grid)



