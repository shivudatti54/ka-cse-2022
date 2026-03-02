# **Significance & p-values, t-tests, multiple testing, degrees of freedom**

## **1. Significance & p-values**

### Definition:

Significance refers to the probability that a result occurred by chance. In statistical testing, significance is often measured by the p-value, which is the probability of observing results as extreme or more extreme than the ones observed, assuming that the null hypothesis is true.

### p-value:

- The p-value is a measure of the probability of obtaining a result as extreme or more extreme than the one observed, assuming that the null hypothesis is true.
- A small p-value (typically < 0.05) indicates strong evidence against the null hypothesis.
- A p-value close to 1 (typically > 0.05) indicates weak evidence against the null hypothesis.

### Example:

Suppose we conduct an A/B test to determine if a new advertising campaign is effective in increasing sales. We collect data and find that the average sales for the control group is $100,000, while the average sales for the treatment group is $120,000. We calculate the p-value for the difference between the two groups.

- Null Hypothesis: The new advertising campaign has no effect on sales.
- Alternative Hypothesis: The new advertising campaign has an effect on sales.
- p-value = 0.01
- Since the p-value is less than 0.05, we reject the null hypothesis and conclude that the new advertising campaign is effective in increasing sales.

### Code Example (Python):

```python
import scipy.stats as stats

# Define the data
control_group = [100, 110, 120, 130, 140]
treatment_group = [120, 130, 140, 150, 160]

# Calculate the mean and standard deviation for each group
control_mean, control_std = stats.tmean(control_group), stats.tstd(control_group)
treatment_mean, treatment_std = stats.tmean(treatment_group), stats.tstd(treatment_group)

# Calculate the t-statistic and p-value
t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)

print("T-statistic:", t_statistic)
print("p-value:", p_value)
```

## **2. t-tests**

### Definition:

A t-test is a statistical test used to compare the means of two groups to determine if there is a significant difference between them.

### Types of t-tests:

- **Independent samples t-test**: Used to compare the means of two independent groups.
- **Paired samples t-test**: Used to compare the means of two related groups (e.g., before-and-after measurements).

### Example:

Suppose we conduct an independent samples t-test to compare the average heights of two groups of people. We collect data and find that the average height for the control group is 175 cm, while the average height for the treatment group is 180 cm.

- Null Hypothesis: The average height for the treatment group is equal to the average height for the control group.
- Alternative Hypothesis: The average height for the treatment group is greater than the average height for the control group.
- p-value = 0.01
- Since the p-value is less than 0.05, we reject the null hypothesis and conclude that the average height for the treatment group is greater than the average height for the control group.

### Code Example (Python):

```python
import scipy.stats as stats

# Define the data
control_group = [175, 180, 175, 180, 175]
treatment_group = [180, 185, 180, 185, 180]

# Calculate the mean and standard deviation for each group
control_mean, control_std = stats.tmean(control_group), stats.tstd(control_group)
treatment_mean, treatment_std = stats.tmean(treatment_group), stats.tstd(treatment_group)

# Calculate the t-statistic and p-value
t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)

print("T-statistic:", t_statistic)
print("p-value:", p_value)
```

## **3. Multiple Testing**

### Definition:

Multiple testing refers to the process of performing multiple statistical tests on the same data. This can lead to a problem known as the multiple testing problem, where the probability of obtaining a result by chance increases.

### Types of multiple testing:

- **Family-wise error rate (FWER)**: The probability of obtaining at least one false positive result across all tests.
- **Type I error rate**: The probability of obtaining a false positive result for a single test.

### Example:

Suppose we conduct 10 independent samples t-tests to compare the means of 10 different groups. We want to ensure that the probability of obtaining at least one false positive result is less than 0.05.

- Null Hypothesis: The null hypotheses for all 10 tests are true.
- Alternative Hypothesis: At least one of the null hypotheses for the 10 tests is false.
- p-value = 0.01
- Since the p-value is less than 0.05, we reject the null hypothesis and conclude that at least one of the null hypotheses is false.

### Code Example (Python):

```python
import numpy as np
from scipy.stats import ttest_ind

# Define the data
n_groups = 10
groups = np.random.normal(0, 1, size=(n_groups, 10))

# Perform multiple t-tests
for i in range(n_groups):
    control_group = groups[i, :]
    treatment_group = groups[1-i, :]
    t_statistic, p_value = ttest_ind(control_group, treatment_group)
    print("Group", i+1, "p-value:", p_value)

# Calculate the family-wise error rate
fwer = 1 - np.power(1-p_value, n_groups)
print("Family-wise error rate:", fwer)
```

## **4. Degrees of Freedom**

### Definition:

Degrees of freedom (DF) is a measure of the number of values in the sample that are free to vary during the estimation of a parameter.

### Formula:

DF = N - k

- N: The sample size
- k: The number of parameters being estimated

### Example:

Suppose we want to estimate the mean of a population with a sample size of 100. We estimate the mean with a single parameter, so k = 1.

- N = 100
- k = 1
- DF = N - k = 100 - 1 = 99

### Code Example (Python):

```python
import numpy as np

# Define the data
n = 100

# Calculate the degrees of freedom
k = 1
df = n - k
print("Degrees of freedom:", df)
```

### Conclusion:

Significance & p-values, t-tests, multiple testing, and degrees of freedom are all important concepts in statistical machine learning. By understanding these concepts, you can make informed decisions about your data and choose the right statistical tests to use.
