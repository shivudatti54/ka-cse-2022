# Joint Probability Distribution - Summary

## Key Definitions

- **Joint Probability Distribution**: The function P(X=x, Y=y) (discrete) or f(x,y) (continuous) that gives the probability of two random variables taking specific values simultaneously.

- **Marginal Probability Distribution**: The probability distribution of a single variable obtained by summing or integrating over all values of other variables: P(X=x) = Σ_y P(X=x,Y=y) or f_X(x) = ∫ f(x,y)dy.

- **Conditional Probability Distribution**: The probability distribution of one variable given knowledge of another: P(Y=y|X=x) = P(X=x,Y=y)/P(X=x).

- **Independent Random Variables**: Two variables X and Y are independent if P(X=x,Y=y) = P(X=x) × P(Y=y) for all (x,y).

## Important Formulas

- **Joint to Marginal (Discrete)**: P(X=x) = Σ_y P(X=x, Y=y)
- **Joint to Marginal (Continuous)**: f_X(x) = ∫_{-∞}^{∞} f(x,y)dy
- **Conditional Probability**: P(Y=y|X=x) = P(X=x,Y=y)/P(X=x)
- **Chain Rule**: P(X,Y) = P(X) × P(Y|X)
- **Independence Test**: P(X=x,Y=y) = P(X=x) × P(Y=y)
- **Total Probability (two variables)**: P(X=x) = Σ_y P(X=x|Y=y)P(Y=y)

## Key Points

1. Joint probability distributions must satisfy non-negativity and sum/integrate to 1.

2. The joint distribution contains all information about the relationship between variables.

3. Marginal distributions can be derived from joint distributions but lose dependency information.

4. Conditional distributions describe how knowledge about one variable affects another.

5. Independence is a symmetric relationship between random variables.

6. The joint distribution of independent factors as product of marginals is crucial for many algorithms.

7. For dependent variables, the joint distribution carries more information than marginals alone.

8. The concept extends to n variables using multi-dimensional arrays or integrals.

## Common Mistakes

1. **Forgetting to normalize**: Not verifying that probabilities sum to 1 or that density integrates to 1.

2. **Incorrect integration bounds**: In continuous cases, failing to properly determine the limits of integration.

3. **Assuming independence**: Using P(X,Y) = P(X)P(Y) when variables are actually dependent.

4. **Division by zero**: Computing conditional probabilities when the conditioning event has zero probability.