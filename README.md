# Statistics Practice Repo
Repo to practice statistics using Python, outline and descriptions included. 

Descriptive Statistics Module

This section contains foundational statistical functions for comparing manual ("by hand") calculations to built-in Pandas methods. It reinforces core statistical concepts and shows how the math works under the hood.

Features

    Mean (by_hand_mean, pandas_mean)

    Median (by_hand_median, pandas_median)

    Mode (by_hand_mode, pandas_mode)

    Sample Variance (by_hand_sample_variance, pandas_variance)

    Standard Deviation (std_dev)

Example Output
By hand mean result:  18.068
Pandas mean result:  18.068
By hand median result:  17.2
Pandas median result:  17.2
By Hand mode result:  1
Pandas mode result:  1
By hand variance result:  43.98291666666666
Pandas variance result:  43.98291666666666
Std Deviation:  6.629720865776499
Pandas Std Dev:  6.629720865776499

Educational Purpose
    Reinforces understanding of statistical operations like:

        Bessel's correction in sample variance

        Sorting for medians

        Frequency counting for mode

    Highlights how close manual implementations are to Pandas built-ins.


Distribution Comparison Module (distributions.py)

This module provides tools to visualize and statistically compare your dataset against well-known theoretical distributions: Normal, Exponential, Poisson, and Binomial.

Features

    Visual comparison using histograms, KDE, and theoretical PDF/PMF curves.

    Goodness-of-fit tests:

        Kolmogorov–Smirnov (KS) for continuous distributions.

        Chi-squared for discrete distributions.

    Automatic parameter estimation (e.g., mean, standard deviation, rate, probability).

    Handles both continuous and discrete data.

Example Output
The function creates a 2×2 grid comparing the input dataset to:

    Normal Distribution

    Exponential Distribution

    Poisson Distribution (if data is discrete)

    Binomial Distribution (with fixed n=20)

Each subplot includes:

    Empirical histogram

    Fitted theoretical distribution

    Goodness-of-fit p-value

## Repo Outline
<pre>
python-statistics-practice/
│
├── README.md
├── data/                     # Datasets
├── scripts/                  # Python modules
│   ├── descriptive_stats.py
└── projects/                 # Projects
</pre>