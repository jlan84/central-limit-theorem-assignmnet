import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def make_draws(dist, params, size=200):
    """
    Draw a sample from a specified distribution
    with given parameters and return these in an array.

    Parameters
    ----------

    dist: scipy.stats distribution object:
      Distribution object from scipy.stats, must have a .rvs method

    params: dict:
      Parameters needed to define the distribution dist.
    For example, if dist = scipy.stats.binom, then params could be

          {'n': 100, 'p': 0.25}

    size: int:
      The number of values to draw

    Returns
    -------
    sample: np.array, shape (size, )
      An i.i.d sample from the specified distribution.
    """
    return dist(**params).rvs(size)

def plot_means(ax, dist, params, repeat=10, size=200, title=None):
    mean_lst = [np.max(make_draws(dist, params, size=size)) for i in range(repeat)]
    ax.hist(mean_lst, bins=40)
    ax.set_title(title)


if __name__ == "__main__":
    fig, axs = plt.subplots(5,1, figsize=(4,10))
    params = {'n':100, 'p': 0.25}
    params = [{'n':100, 'p': 0.25}, {'mu': 3}, {'loc':2}, {'p': 0.2},
              {'loc':0, 'scale':10}]
    titles = ('Binomial', 'Poisson', 'Exponential', 'Geometric', 'Uniform')
    models = ['stats.binom','stats.poisson', 'stats.expon', 'stats.geom',
              'stats.uniform']
    d = dict(zip(models, params))
        
    for title, model, param, ax in zip(titles, models, params, axs.flatten()):
        plot_means(ax, dist=eval(model), params=param, size = 10,repeat=1000, title=title)
    plt.tight_layout()
    plt.show()
    
