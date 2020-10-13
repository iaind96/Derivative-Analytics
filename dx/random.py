import numpy as np


def sn_random_numbers(shape, antithetic=False, moment_matching=False, fixed_seed=False):

    if fixed_seed:
        np.random.seed(1000)

    dimensions = len(shape)

    if antithetic:
        antithetic_shape = [i for i in shape]
        if antithetic_shape[-1] % 2 != 0:
            raise(ValueError("Last dimension must be divisible by 2 for antithetic sampling!"))
        else:
            antithetic_shape[-1] = int(antithetic_shape[-1] / 2)
        ran = np.random.standard_normal(tuple(antithetic_shape))
        ran = np.concatenate((ran, -ran), axis=dimensions-1)
    else:
        ran = np.random.standard_normal(shape)

    if moment_matching:
        ran = ran - np.mean(ran)
        ran = ran / np.std(ran)

    return ran