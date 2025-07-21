from math import sqrt

import numpy as np
import pandas as pd
from scipy.stats import t

def one_sample_t_test_byhand(pop_mean: float, samples: np.ndarray, alpha: float = 0.05):
    n = len(samples)
    sample_mean = samples.mean()
    sample_std = samples.std(ddof=1)
    standard_error = sample_std * sqrt(n)

    t_score = (sample_mean - pop_mean) / standard_error

    degrees_of_freedom = n - 1

    t_critical = t.ppf(1 - alpha/2, degrees_of_freedom)

    p_value = (1 - t.cdf(abs(t_score), degrees_of_freedom)) * 2

    return {
        "sample_mean": sample_mean,
        "t_score": t_score,
        "degrees_of_freedom": degrees_of_freedom,
        "t_critical (±)": +-t_critical,
        "p_value": p_value,
        "reject_null": p_value < alpha
    }





if __name__ == "__main__":
    samples = np.array([5.1, 5.3, 4.9, 5.0, 5.2, 5.4, 4.8])
    pop_mean = 5.0

    result = one_sample_t_test_byhand(pop_mean, samples)
    print(result)
    