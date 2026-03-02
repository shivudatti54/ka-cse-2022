# Summary of Covariance and Correlation

## Definitions and Formulas

### Covariance

- **Definition**: Measures how much two random variables vary together. Positive covariance indicates a positive relationship, while negative covariance suggests an inverse relationship.
  - Formula: \(\text{Cov}(X,Y) = E[(X-E[X])(Y-E[Y])]\)

### Correlation Coefficient

- **Definition**: Standardized measure of linear dependence between two variables. Range from -1 to +1.
  - Formula: \(\rho\_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}\), where \(\sigma_X\) and \(\sigma_Y\) are the standard deviations of X and Y respectively.

### Key Points

- **Correlation vs Covariance**: Correlation is covariance normalized by the product of their standard deviations. They both measure linear association but correlation removes scale dependency, giving a standardized output from -1 to +1.

## Theorems

### Cauchy-Schwarz Inequality for Covariance and Correlation

- **Inequality**: \(|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y\)
- **Interpretation**: This inequality provides an upper bound on the possible value of covariance, reinforcing that correlation is bounded between -1 and +1.

## Applications

### Joint Probability Distribution

- **Context**: In joint probability distribution, covariance helps understand how changes in one variable relate to another. Positive covariance suggests a joint increase or decrease in values.

### Markov Chains

- **Application**: While not directly related to covariance/correlation formulas, understanding their applications can provide context for interpreting these measures within dynamic systems.

---

This summary provides essential points and formulas on covariance and correlation, suitable for quick revision before exams.
