import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import norm, expon, poisson, binom, chisquare, kstest
from sklearn.preprocessing import MinMaxScaler


def show_distributions(sample_size: int = 1000):
    np.random.seed(123)

    data = {
        "Normal": np.random.normal(loc=0, scale=1, size=sample_size),
        "Binomial": np.random.binomial(n=10, p=0.5, size=sample_size),
        "Poisson": np.random.poisson(lam=3, size=sample_size),
        "Exponential": np.random.exponential(scale=1.0, size=sample_size)
    }

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    for ax, (name, dist) in zip(axs.flat, data.items()):
        sns.histplot(dist, kde=True, stat="density", ax=ax, bins=30)
        ax.set_title(f"{name} Distribution")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Distributions as main file.")

    #Uncomment to show some basic distributions.
    #show_distributions()
