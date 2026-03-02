# Univariate Data Analysis and Visualization

## 1. Introduction and Statistical Foundations

Univariate Data Analysis constitutes the foundational step in statistical inference and machine learning pipelines, focusing on the comprehensive examination of a single variable's distribution, central tendencies, and dispersion characteristics. Before deploying complex predictive models, understanding the marginal distribution of each feature is essential for identifying data quality issues, selecting appropriate preprocessing techniques, and validating model assumptions.

The theoretical framework of univariate analysis rests upon probability theory and statistical estimation. Given a random variable $X$ with observed values $x_1, x_2, ..., x_n$, we seek to characterize its underlying probability distribution or estimate population parameters from sample data.

## 2. Measures of Central Tendency

### 2.1 Mathematical Definitions

**Definition 2.1 (Arithmetic Mean):**
The population mean $\mu$ and sample mean $\bar{x}$ are defined as:

$$\mu = \frac{1}{N}\sum_{i=1}^{N} x_i \quad \text{(population)}$$
$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \quad \text{(sample)}$$

**Definition 2.2 (Median):**
The median $M$ is the value that divides the ordered dataset into two equal halves:

$$M = \begin{cases} x_{\frac{n+1}{2}} & \text{if } n \text{ is odd} \\ \frac{x_{n/2} + x_{n/2+1}}{2} & \text{if } n \text{ is even} \end{cases}$$

**Definition 2.3 (Mode):**
The mode is the value with maximum frequency: $M_o = \arg\max_x f(x)$

### 2.2 Proof: Why Sample Variance Uses (n-1)

**Theorem:** The sample variance with denominator $(n-1)$ is an unbiased estimator of population variance.

**Proof:**
Let $s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$ be the sample variance. We show $E[s^2] = \sigma^2$.

$$\sum_{i=1}^{n}(x_i - \bar{x})^2 = \sum_{i=1}^{n}(x_i - \mu)^2 - n(\bar{x} - \mu)^2$$

Taking expectations:
$$E\left[\sum_{i=1}^{n}(x_i - \bar{x})^2\right] = \sum_{i=1}^{n}E[(x_i - \mu)^2] - nE[(\bar{x} - \mu)^2]$$
$$= n\sigma^2 - n\left(\frac{\sigma^2}{n}\right) = (n-1)\sigma^2$$

Thus, $E[s^2] = \sigma^2$. ∎

This explains why we divide by $(n-1)$ rather than $n$—to obtain an unbiased estimator.

### 2.3 Comparative Analysis

| Measure | Formula               | Robustness             | Mathematical Property             |
| ------- | --------------------- | ---------------------- | --------------------------------- |
| Mean    | $\frac{1}{n}\sum x_i$ | Sensitive to outliers  | Minimizes sum of squared errors   |
| Median  | Middle value          | Robust to 50% outliers | Minimizes absolute deviation      |
| Mode    | Most frequent         | Robust to frequency    | Maximizes likelihood for discrete |

The mean minimizes the sum of squared deviations: $\frac{\partial}{\partial \mu}\sum(x_i - \mu)^2 = 0 \Rightarrow \mu = \bar{x}$

## 3. Measures of Dispersion

### 3.1 Theoretical Framework

**Definition 3.1 (Variance):**
$$\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2 \quad \text{Population variance}$$
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2 \quad \text{Sample variance}$$

**Definition 3.2 (Standard Deviation):**
$$\sigma = \sqrt{\sigma^2}, \quad s = \sqrt{s^2}$$

**Definition 3.3 (Interquartile Range - IQR):**
Given ordered data, $Q_1$ is the 25th percentile and $Q_3$ is the 75th percentile:
$$IQR = Q_3 - Q_1$$

### 3.2 Percentiles and Quantiles

**Definition 3.4 (p-th Percentile):**
The value $P_p$ such that $p\%$ of observations fall below it. For the $k$-th quantile:
$$Q_k = \begin{cases} x_{(np)} & \text{if } np \text{ is integer} \\ x_{(\lfloor np \rfloor + 1)} & \text{otherwise} \end{cases}$$

Common percentiles: $Q_1$ (25th), $Q_2$ (50th/median), $Q_3$ (75th), $Q_4$ (100th)

### 3.3 Relationship Between Measures

For any dataset, the following inequality holds (Cantelli's inequality variant):
$$Range \geq 4 \times Standard Deviation \geq 2 \times IQR$$

This relationship is useful for preliminary outlier detection.

## 4. Distribution Shape Analysis

### 4.1 Skewness

**Definition 4.1 (Coefficient of Skewness):**
$$\gamma_1 = \frac{E[(X - \mu)^3]}{\sigma^3} = \frac{\frac{1}{n}\sum(x_i - \bar{x})^3}{s^3}$$

- $\gamma_1 > 0$: Right-skewed (positive skew)—mean > median > mode
- $\gamma_1 < 0$: Left-skewed (negative skew)—mode > median > mean
- $\gamma_1 = 0$: Symmetric distribution

### 4.2 Kurtosis

**Definition 4.2 (Excess Kurtosis):**
$$\gamma_2 = \frac{E[(X - \mu)^4]}{\sigma^4} - 3$$

- $\gamma_2 > 0$: Leptokurtic (heavy tails,)
- $\gamma_2 = 0$: Mesokurtic (normal distribution baseline)
- $\gamma_2 < 0$: Platykurtic (light tails, flat peak)

## 5. Data Types and Appropriate Analysis

### 5.1 Numerical Data

**Continuous vs. Discrete:**

| Type       | Definition                         | Examples            | Analysis Methods            |
| ---------- | ---------------------------------- | ------------------- | --------------------------- |
| Continuous | $x \in \mathbb{R}$ within interval | Height, temperature | Mean, variance, histograms  |
| Discrete   | $x \in \mathbb{Z}$                 | Count data          | Poisson-appropriate methods |

### 5.2 Categorical Data

**Nominal vs. Ordinal:**

| Type    | Property           | Examples        | Analysis Methods         |
| ------- | ------------------ | --------------- | ------------------------ |
| Nominal | No inherent order  | Gender, color   | Mode, chi-square         |
| Ordinal | Ordered categories | Education level | Median, rank correlation |

## 6. Visualization Theory

### 6.1 Histograms

**Definition:** A histogram partitions the range of $X$ into $k$ bins of equal width $h$, with height representing frequency density $f_i = n_i/h$.

**Optimal Bin Width (Sturges' Rule):**
$$k = \lceil \log_2 n + 1 \rceil$$

**Interpretation Guidelines:**

- Unimodal: Single peak suggests single underlying population
- Bimodal: Multiple peaks may indicate subpopulations
- Uniform: No dominant value—uniform distribution

### 6.2 Box Plots (Box-and-Whisker)

**Five-Number Summary:** $\{\min, Q_1, M, Q_3, \max\}$

**Construction:**

```
 ┌─────────┐
 ───┤ ├──── Q3 + 1.5*IQR (upper whisker)
 │─────────| Maximum within fence
 │ │ |
 │─────────| Q3
 │─────────|
 │ M | Median
 │─────────|
 │─────────| Q1
 | | |
 └───|─────|───┘ Minimum within fence
 ───┤ ├──── Q1 - 1.5*IQR (lower whisker)
 └─────────┘
```

### 6.3 Q-Q Plots (Quantile-Quantile)

**Purpose:** Visually assess normality by plotting sample quantiles against theoretical normal quantiles.

**Interpretation:**

- Points along diagonal: Normal distribution
- S-curve: Heavy-tailed distribution
- Points above line at ends: Right-skewed

## 7. Outlier Detection Methods

### 7.1 IQR Method (Tukey's Fences)

**Definition:** An observation is an outlier if:
$$x_i < Q_1 - 1.5 \times IQR \quad \text{or} \quad x_i > Q_3 + 1.5 \times IQR$$

**Extreme outliers:** Using $3 \times IQR$ instead of $1.5 \times IQR$

### 7.2 Z-Score Method

**Definition:**
$$z_i = \frac{x_i - \bar{x}}{s}$$

Outlier threshold: $|z_i| > 3$ (for large $n$)

### 7.3 Worked Example

Given data: $[12, 14, 15, 16, 17, 18, 19, 100]$

Sorted: $[12, 14, 15, 16, 17, 18, 19, 100]$

- $Q_1 = 14.5$, $Q_3 = 18.5$, $IQR = 4$
- Lower fence: $14.5 - 1.5(4) = 8.5$
- Upper fence: $18.5 + 1.5(4) = 24.5$

**Conclusion:** $100$ is an outlier (above upper fence)

## 8. Practical Implementation

### 8.1 Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Sample dataset
data = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])

# Central Tendency
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True)

# Dispersion
variance = np.var(data, ddof=1) # Sample variance
std_dev = np.std(data, ddof=1)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Shape
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Outlier detection
def detect_outliers_iqr(data):
 q1, q3 = np.percentile(data, [25, 75])
 iqr = q3 - q1
 lower = q1 - 1.5 * iqr
 upper = q3 + 1.5 * iqr
 return data[(data < lower) | (data > upper)]

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(data, bins='sturges', edgecolor='black', alpha=0.7)
axes[0].set_title('Histogram')
axes[0].axvline(mean, color='r', linestyle='--', label=f'Mean={mean:.2f}')

axes[1].boxplot(data, vert=True)
axes[1].set_title('Box Plot')

plt.tight_layout
plt.savefig('univariate_analysis.png')
plt.show
```

### 8.2 Normality Testing

```python
# Shapiro-Wilk Test
stat, p_value = stats.shapiro(data)
# H0: Data is normally distributed
# Reject H0 if p_value < 0.05

# D'Agostino-Pearson Test
stat, p_value = stats.normaltest(data)

# Kolmogorov-Smirnov Test
stat, p_value = stats.kstest(data, 'norm', args=(mean, std_dev))
```

## 9. Relationship to Machine Learning

Univariate analysis directly informs:

1. **Feature Engineering:** Skewed features may require transformation ($\log$, Box-Cox)
2. **Model Selection:** Normality assumption for linear regression residuals
3. **Preprocessing Pipeline:** Outlier handling before model training
4. **Feature Scaling:** Understanding range aids in standardization decisions
5. **Data Imbalance:** Detecting skewed class distributions

## 10. Assessment Items

### Hard-Level Multiple Choice Questions

**Q1.** For a dataset with values $[2, 3, 5, 7, 100]$, which measure of central tendency is most appropriate and why?

- (a) Mean, because it uses all data points
- (b) Median, because it is robust to outliers
- (c) Mode, because it identifies the most frequent value
- (d) Geometric mean, because it handles large values better

**Answer:** (b) The median (value = 5) is robust to outliers, while the mean (23.4) is severely distorted by the outlier 100.

**Q2.** A sample of size $n=25$ has $\bar{x}=50$ and $s^2=16$. Using the IQR method for outlier detection, if $Q_1=42$ and $Q_3=58$, which of the following values would be flagged as an outlier?

- (a) 18
- (b) 35
- (c) 62
- (d) 75

**Answer:** (a) $IQR = 16$, lower fence = $42 - 1.5(16) = 18$. Any value below 18 is an outlier; 18 is at the boundary, and 18 < 18 is true if strictly less.

**Q3.** Given skewness $\gamma_1 = 2.5$ and kurtosis $\gamma_2 = 7.2$ for a dataset, which interpretation is correct?

- (a) Heavily right-skewed with light tails
- (b) Heavily right-skewed with heavy tails
- (c) Heavily left-skewed with heavy tails
- (d) Symmetric with heavy tails

**Answer:** (b) Positive skewness (>0) indicates right-skewed; positive excess kurtosis (>0) indicates heavy tails (leptokurtic).

---

**Exam Tips:**

1. Remember that sample variance uses $n-1$ (Bessel's correction) for unbiased estimation
2. For skewed distributions: median is more representative than mean
3. IQR method is preferred when data contains extreme outliers
4. Q-Q plots: departure from diagonal indicates non-normality
5. In machine learning, log-transform skewed features before modeling
