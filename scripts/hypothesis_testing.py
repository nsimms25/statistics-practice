from math import sqrt

import numpy as np
import pandas as pd
from scipy.stats import t, ttest_1samp

def one_sample_t_test_byhand(pop_mean: float, samples: np.ndarray, alpha: float = 0.05):
    n = len(samples)
    sample_mean = samples.mean()
    sample_std = samples.std(ddof=1)
    standard_error = sample_std / sqrt(n)

    t_score = (sample_mean - pop_mean) / standard_error

    degrees_of_freedom = n - 1

    t_critical = float(t.ppf(1 - alpha/2, degrees_of_freedom))

    p_value = 2 * (1 - float(t.cdf(abs(t_score), degrees_of_freedom)))

    return {
        "sample_mean": round(sample_mean, 3),
        "t_score": round(t_score, 3),
        "degrees_of_freedom": degrees_of_freedom,
        "t_critical (±)": f"±{round(t_critical, 3)}",
        "p_value": round(p_value, 3),
        "reject_null": p_value < alpha
    }


def one_sample_t_test_scipy(samples: np.ndarray, pop_mean: float, alpha: float = 0.05) -> dict:
    result = ttest_1samp(samples, pop_mean)
    t_stat = float(result.statistic)
    p_value = float(result.pvalue)

    reject_null = p_value < alpha

    print(type(t_stat))

    return {
        "t_score": round(t_stat, 3),
        "p_value": round(p_value, 3),
        "reject_null": reject_null
    }


if __name__ == "__main__":
    samples = np.array([5.1, 5.3, 4.9, 5.0, 5.2, 5.4, 4.8])
    pop_mean = 5.0

    result_byhand = one_sample_t_test_byhand(pop_mean, samples)
    result_scipy = one_sample_t_test_scipy(samples, pop_mean=pop_mean)
    #Uncomment to show that by hand and scipy functions are the same. 
    #print(result_byhand)
    #print(result_byhand["p_value"])
    #print(result_scipy)
    #print(result_scipy["p_value"])
