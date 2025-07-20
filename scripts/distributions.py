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


def pdf_vs_cdf_normal():
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


def compare_to_distributions(data, discrete=False, max_bins=30):
    data = np.array(data)
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    x_cont = np.linspace(np.min(data), np.max(data), 1000)
    x_disc = np.arange(np.min(data), np.max(data) + 1)

    #Normal Distribtuion
    mu = np.mean(data)
    std = np.std(data)
    axs[0, 0].set_title("Normal Distribution")
    sns.histplot(data=data, bins=max_bins, stat="density", kde=True, ax=axs[0,0], color='lightgray', label='Empirical')
    axs[0, 0].plot(x_cont, norm.pdf(x_cont, mu, std), label="Normal PDF", color='red')
    axs[0, 0].legend()
    ks_stat, ks_p = kstest(data, "norm", args=(mu, std))
    axs[0, 0].text(0.95, 0.95, f"KS p={ks_p:.3f}", ha='right', va='top', transform=axs[0, 0].transAxes)

    #Exponential Distribution
    scale = np.mean(data)
    axs[0, 1].set_title("Exponential Distribution")
    sns.histplot(data, bins=max_bins, stat="density", kde=True, ax=axs[0, 1], color='lightgray', label='Empirical')
    axs[0, 1].plot(x_cont, expon.pdf(x_cont, scale=scale), label="Exponential PDF", color='green')
    axs[0, 1].legend()
    ks_stat, ks_p = kstest(data, 'expon', args=(0, scale))
    axs[0, 1].text(0.95, 0.95, f"KS p={ks_p:.3f}", ha='right', va='top', transform=axs[0, 1].transAxes)

    #Poisson Distribution
    lam = np.mean(data)
    axs[1, 0].set_title("Poisson Distribution")
    if discrete:
        counts, bins = np.histogram(data, bins=np.arange(x_disc.min(), x_disc.max() + 2), density=True)
        sns.histplot(data, bins=max_bins, stat="probability", discrete=True, ax=axs[1, 0], color='lightgray', label='Empirical')
        axs[1, 0].plot(x_disc, poisson.pmf(x_disc, lam), marker='o', linestyle='', label="Poisson PMF", color='blue')
        axs[1, 0].legend()
        expected = poisson.pmf(x_disc, lam) * len(data)
        observed = np.array([(data == x).sum() for x in x_disc])
        expected *= observed.sum() / expected.sum()  # Normalize
        chisq_stat, chisq_p = chisquare(f_obs=observed, f_exp=expected)
        axs[1, 0].text(0.95, 0.95, f"Chi² p={chisq_p:.3f}", ha='right', va='top', transform=axs[1, 0].transAxes)
    
    #Binomial Distribution
    n = 20
    p = np.mean(data) / n
    axs[1, 1].set_title("Binomial Distribution (n=20)")
    if discrete:
        sns.histplot(data, bins=max_bins, stat="probability", discrete=True, ax=axs[1, 1], color='lightgray', label='Empirical')
        axs[1, 1].plot(x_disc, binom.pmf(x_disc, n, p), marker='o', linestyle='', label="Binomial PMF", color='purple')
        axs[1, 1].legend()
        expected = binom.pmf(x_disc, n, p) * len(data)
        observed = np.array([(data == x).sum() for x in x_disc])
        expected *= observed.sum() / expected.sum()  # Normalize
        chisq_stat, chisq_p = chisquare(f_obs=observed, f_exp=expected)
        axs[1, 1].text(0.95, 0.95, f"Chi² p={chisq_p:.3f}", ha='right', va='top', transform=axs[1, 1].transAxes)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Distributions as main file.")

    #Uncomment to show some basic distributions.
    #show_distributions()

    #Uncomment to show the differences between PDF and CDF.
    #pdf_vs_cdf_normal()

    #Uncomment to show the normal_data vs 4 distributions (Note that the poisson or binomial will not show unles discrete is true.)
    #normal_test_data = np.random.normal(0, 1, 1000)
    #compare_to_distributions(normal_test_data)

    #Uncomment to show test_poisson vs 4 distributions. (discrete=True, will show all distributions.)
    poisson_test_data = np.random.poisson(5, 1000)
    compare_to_distributions(poisson_test_data, discrete=True)
