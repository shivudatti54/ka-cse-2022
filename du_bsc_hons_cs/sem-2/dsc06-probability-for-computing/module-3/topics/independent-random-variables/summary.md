# Independent Random Variables - Summary

## Key Definitions and Concepts

- **Independent Random Variables**: Two random variables X and Y are independent if and only if P(X = x, Y = y) = P(X = x) × P(Y = y) for all x, y (discrete case), or f(x, y) = f_X(x) × f_Y(y) (continuous case)

- **Joint Distribution**: The complete probability distribution of two or more random variables together

- **Marginal Distribution**: The probability distribution of a single variable obtained by summing/integrating over all possible values of other variables

- **Convolution**: The operation to find the distribution of the sum of two independent random variables

## Important Formulas and Theorems

- **Independence Condition**: P(X = x, Y = y) = P(X = x) · P(Y = y)
- **Product Expectation**: E[XY] = E[X] · E[Y] (only for independent variables)
- **Variance of Sum**: Var(X + Y) = Var(X) + Var(Y) (only when independent)
- **Covariance**: Cov(X, Y) = E[XY] - E[X]E[Y] = 0 when independent
- **Discrete Convolution**: P(Z = z) = Σₓ P(X = x) · P(Y = z - x)
- **Continuous Convolution**: f_Z(z) = ∫ f_X(x) · f_Y(z - x) dx

## Key Points

1. Independence requires the condition to hold for ALL value pairs, not just some
2. Zero covariance implies NO linear correlation, but does NOT guarantee independence
3. Independent random variables are always uncorrelated, but uncorrelated variables may be dependent
4. The sum of independent random variables has a distribution given by convolution
5. Many algorithms assume independence for tractable expected value calculations
6. Independence is symmetric: if X is independent of Y, then Y is independent of X
7. Independence of more than two variables requires the joint factorizes to product of marginals

## Common Mistakes to Avoid

1. **Assuming zero covariance means independence**: X and X² are dependent but have zero covariance when X is symmetric
2. **Checking only some pairs**: You must verify the independence condition for ALL possible pairs
3. **Applying E[XY] = E[X]E[Y] without verifying independence**: This property only holds for independent variables
4. **Confusing independence with identical distribution**: Independent variables need not have the same distribution

## Revision Tips

1. Practice verifying independence with both discrete and continuous examples
2. Memorize the key properties and understand when each applies
3. Be comfortable computing convolutions for sums of independent variables
4. Review counterexamples to understand the difference between covariance and independence
5. Solve previous year DU exam questions on this topic to understand the question patterns