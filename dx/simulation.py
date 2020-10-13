import pandas as pd
import numpy as np

from dx.random import sn_random_numbers


class Simulator:

    def __init__(self, name, mar_env):
        self.name = name
        self.mar_env = mar_env

    def generate_time_grid(self, end_date, freq):
        start_date = self.mar_env.date

        time_grid = pd.date_range(start=start_date, end=end_date, freq=freq).to_pydatetime()

        if start_date not in time_grid:
            time_grid = np.insert(time_grid, 0, start_date)
        if end_date not in time_grid:
            time_grid = np.append(time_grid, end_date)

        return time_grid


class GeometricBrownianMotion(Simulator):

    def __init__(self, name, mar_env):
        super().__init__(name, mar_env)

    def simulate_paths(self, end_date, n_paths, freq, *args, **kwargs):
        time_grid = self.generate_time_grid(end_date, freq)
        n_steps = len(time_grid)

        discount_curve = self.mar_env.get_curve("discount_curve")

        paths = {}
        for instrument in self.mar_env.instruments:

            instrument = self.mar_env.get_instrument(instrument)

            rns = sn_random_numbers((n_steps, n_paths), *args, **kwargs)

            paths_tmp = np.zeros((n_steps, n_paths))
            S0 = instrument.current_price
            vol = instrument.vol
            day_count = instrument.day_count
            r = discount_curve.rate

            paths_tmp[0] = S0

            for t in range(1, n_steps):
                dt = (time_grid[t] - time_grid[t-1]).days / day_count
                paths_tmp[t] = paths_tmp[t-1] * np.exp((r - 0.5 * vol ** 2) * dt + vol * np.sqrt(dt) * rns[t])

            paths[instrument.name] = paths_tmp

        return paths