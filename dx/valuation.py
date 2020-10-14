import numpy as np
from scipy.stats import norm

from dx.simulation import GeometricBrownianMotion


class Valuation:

    def __init__(self, mar_env, option):
        self.mar_env = mar_env
        self.option = option


class BSValuation(Valuation):

    def get_present_value(self):
        S = self.option.underlying.current_price
        vol = self.option.underlying.vol
        r = self.mar_env.get_curve("discount_curve").rate
        K = self.option.strike
        T = (self.option.expiry - self.mar_env.date).days / self.option.day_count

        d1 = (np.log(S / K) + (r - 0.5 * vol ** 2) * T) / (vol * np.sqrt(T))
        d2 = d1 - vol * np.sqrt(T)

        if self.option.type == "call":
            return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        elif self.option.type == "put":
            return - S * norm.cdf(-d1) + K * np.exp(-r * T) * norm.cdf(-d2)


class MCValuation(Valuation):

    def __init__(self, mar_env, option):
        super().__init__(mar_env, option)
        self.simulator = GeometricBrownianMotion("gbm_sim", mar_env)

    def get_present_value(self, n_paths=10000, ret_sim_objects=False, *args, **kwargs):
        paths = self.simulator.simulate_paths(self.option.expiry, n_paths, "B", *args, **kwargs)

        cash_flows = self.option.payoff(paths[self.option.underlying.name][-1, :])
        mean_cash_flow = np.mean(cash_flows)

        discount_curve = self.mar_env.get_curve("discount_curve")
        T = (self.option.expiry - self.mar_env.date).days / self.option.day_count
        df = np.exp(-T * discount_curve.rate)

        pv = df * mean_cash_flow

        if ret_sim_objects:
            return pv, paths
        else:
            return df * mean_cash_flow

