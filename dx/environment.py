

class MarketEnvironment:

    def __init__(self, name, date):
        self.name = name
        self.date = date
        # self.constants = {}
        # self.lists = {}
        self.curves = {}
        self.instruments = {}

    # def add_constant(self, key, constant):
    #     self.constants[key] = constant
    #
    # def get_constant(self, key):
    #     return self.constants[key]
    #
    # def add_list(self, key, ls):
    #     self.lists[key] = ls
    #
    # def get_list(self, key):
    #     return self.lists[key]

    def add_curve(self, key, curve):
        self.curves[key] = curve

    def get_curve(self, key):
        return self.curves[key]

    def add_instrument(self, key, instrument):
        self.instruments[key] = instrument

    def get_instrument(self, key):
        return self.instruments[key]

    def add_environment(self, env):
        self.curves.update(env.curves)
        self.instruments.update(env.instruments)



