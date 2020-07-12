import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


# plt.style.use('ggplot')
# lunch = stats.norm(loc=2, scale=0.5)
# x = np.linspace(0.5, 3.5, num=100)
# print(lunch.ppf(.998))
# fig, ax = plt.subplots(figsize=(6,4))
# ax.plot(x, lunch.pdf(x), c='black', label='distribution')
# ax.set_title('Google lunch distribution')
# ax.set_ylabel('pdf')
# ax.set_xlabel('time taken for lunch')

# ax.axvline(lunch.ppf(.025), c="red",linestyle="--", linewidth=1)
# ax.axvline(lunch.ppf(.975),c="red", linestyle="--", linewidth=1)
# x1 = lunch.ppf(.025)
# x2 = lunch.ppf(.975)
# x = np.linspace(x1, x2, num=100)
# ax.fill_between(x=x, y1=lunch.pdf(x), alpha=.2, label='Middle 95%')
# ax.legend()
# plt.show()

# p = 0.5
# n = 10000
# binomial = stats.binom(10000, 0.5)
# prob_binom = binomial.cdf(5100) - binomial.cdf(4999)

# std = np.sqrt(n*p*(1-p))
# mu = n*p
# normal = stats.norm(loc=mu, scale=std)
# prob_norm = normal.cdf(5100) - normal.cdf(5000)

# print(prob_binom)
# print(prob_norm)

#1  

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

def plot_means(dist, params, ax, repeat, size=200):
  meansList = []
  for i in range(repeat):
    meansList.append(np.mean(make_draws(dist, params, size=size)))
  ax.hist(meansList)

sizeList = [100, 1000, 10000, 20000]

fig, axs = plt.subplots(2,2, figsize=(12,12))
for size, ax in zip(sizeList, axs.flatten()):
  plot_means(stats.binom, {'n':30, 'p': 0.5}, ax, repeat=size)


plt.show()






# if __name__=="__main__":
#     # binomial_samp = make_draws(stats.binom, {'n': 100, 'p':0.25}, size=200)
#     fig, ax = plt.subplots(figsize=(5,5))
#     plot_means(stats.binom, {'n':1000, 'p': 0.5}, ax, repeat=1000)
#     stats.uniform()