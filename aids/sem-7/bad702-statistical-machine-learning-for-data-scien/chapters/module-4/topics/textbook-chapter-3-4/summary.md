# Statistical Machine Learning for Data Science: Chapter 3 & 4 Revision Notes

### Chapter 3: Multi-Arm Bandit Algorithm

- **Definition:** A multi-armed bandit is a decision-making problem where an agent must choose between multiple actions to maximize a reward.
- **Optimal Strategy:** The optimal strategy is to explore as much as possible in the early stages to gain knowledge about the rewards, and then exploit the best-known action.
- **Upper Confidence Bound (UCB) Algorithm:**
  - Formula: $\theta_i + \sqrt{2\log(T)/n_i}$
  - Definition: Upper confidence bound, where $\theta_i$ is the expected reward, $T$ is the total time, $n_i$ is the number of pulls for action $i$.
- **Gittins-Hart Theorem:** The UCB algorithm is the optimal strategy for a one-armed bandit problem.
- **Key Concepts:**
  - Exploration-Exploitation Trade-off
  - Confidence Intervals
  - Regret Minimization

### Chapter 4: Power and Sample Size

- **Definition:** Power is the probability of rejecting the null hypothesis when it is false.
- **Sample Size Calculation:**
  - Formula: $n = \frac{(Z_{\alpha} + Z_{\beta})^2 \sigma^2}{\mu_1 - \mu_0}^2$
  - Definition: Sample size required to detect a certain effect size with a specified power.
- **Factors Affecting Power:**
  - Effect Size
  - Precision
  - Variance
  - Sample Size
- **Key Concepts:**
  - Confidence Intervals
  - Hypothesis Testing
  - Effect Size

### Factor Variables in Regression

- **Definition:** Factor variables are variables that explain the variation in another variable.
- **Types of Factor Variables:**
  - Continuous Factor Variables
  - Categorical Factor Variables
- **Regression Analysis with Factor Variables:**
  - Formula: $\hat{\beta}_{(x)} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}$
  - Definition: Coefficient of a factor variable in a multiple regression model.
- **Factor Analysis:**
  - Formula: $X = PA$
  - Definition: Factor analysis is a technique to reduce the dimensionality of a dataset by extracting underlying factors.

### Interpreting the Regression

- **Coefficient Interpretation:**
  - Definition: The change in the response variable for a one-unit change in the predictor variable, while holding all other variables constant.
- **Standardized Coefficients:**
  - Definition: Coefficients that are scaled to have a mean of 0 and a standard deviation of 1.
- **Partial Coefficient:**
  - Definition: Coefficient of a single predictor variable while holding all other variables constant.

### Important Formulas and Theorems

- **T-Test:** $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$
- **ANOVA:** $F = \frac{MSR}{MSE}$
- **Correlation Coefficient:** $\rho = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$
- **Confidence Interval:** $CI = \bar{y} \pm Z_{\alpha/2} \sigma/\sqrt{n}$
