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


def pdf_vs_cdf():
    normal_data = np.random.normal(size=1000)
    sorted_data = np.sort(normal_data)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    sns.histplot(normal_data, kde=True, stat="density", bins=30, color='skyblue', label="PDF")
    plt.title("PDF - Probability Density Function")
    plt.legend()

    plt.subplot(1, 2, 2)
    cdf = np.arange(len(sorted_data)) / float(len(sorted_data))
    plt.plot(sorted_data, cdf, marker=".", linestyle="none", label="Empirical CDF")
    plt.title("CDF - Cumulative Distribution Function")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Distributions as main file.")

    #Uncomment to show some basic distributions.
    #show_distributions()

    #Uncomment tp show the differences between PDF and CDF.
    #pdf_vs_cdf()
