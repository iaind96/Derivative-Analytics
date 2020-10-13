import matplotlib.pyplot as plt


def plot_mc_paths(paths, n_paths=None, ax=None, *args, **kwargs):

    if n_paths is None:
        n_paths = paths.shape[1]

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(paths[:, :n_paths], *args, **kwargs)
    ax.set_ylabel("Instrument price")
    ax.set_xlabel("Time")