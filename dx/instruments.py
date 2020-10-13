import numpy as np

from dx.utils import get_year_deltas


class FinancialInstrument:

    def __init__(self, name, day_count):
        self.name = name
        self.day_count = day_count


class Stock(FinancialInstrument):

    def __init__(self, name, current_price, vol, day_count=365):
        super().__init__(name, day_count)
        self.current_price = current_price
        self.vol = vol


class ConstantShortRate(FinancialInstrument):

    def __init__(self, name, rate, day_count=365):
        super().__init__(name, day_count)
        self.rate = rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if rate >= 0.0:
            self._rate = rate
        else:
            raise ValueError("Short rate cannot be negative!")

    def get_discount_factors(self, date_list, dt_objects=True):
        if dt_objects:
            deltas = get_year_deltas(date_list, self.day_count)
        else:
            deltas = date_list
        dfs = np.exp(-self.rate * deltas)
        return np.array([deltas, dfs]).T