# EXPECTATION - SUMMARY

## Key Definitions and Concepts

- EXPECTED VALUE: The weighted average of all possible values a random variable can take. For discrete X: E(X) = Σ xᵢpᵢ; for continuous X: E(X) = ∫ xf(x)dx.

- LINEARITY OF EXPECTATION: E(aX + bY) = aE(X) + bE(Y) holds for any random variables X, Y and constants a, b, regardless of dependence.

- LAW OF THE UNCONSCIOUS STATISTICIAN (LOTUS): E[g(X)] = Σ g(xᵢ)pᵢ for discrete; E[g(X)] = ∫ g(x)f(x)dx for continuous—compute expectation of functions without finding distribution of g(X).

- VARIANCE: Var(X) = E[(X - E(X))²] = E(X²) - [E(X)]²; measures dispersion. Standard deviation is √Var(X).

- COVARIANCE: Cov(X, Y) = E(XY) - E(X)E(Y); indicates direction of linear relationship between X and Y.

- CORRELATION: ρ = Cov(X,Y) / [√Var(X)√Var(Y)]; normalized measure between -1 and 1.

- CONDITIONAL EXPECTATION: E(X|Y = y) is the expected value of X given Y takes value y.

- LAW OF TOTAL EXPECTATION: E[E(X|Y)] = E(X); unconditional expectation equals expectation of conditional expectations.

## Important Formulas and Theorems

- E(c) = c for constant c
- E(X + c) = E(X) + c
- E(aX) = aE(X)
- Var(aX + b) = a²Var(X)
- Cov(X, Y) = 0 if X and Y are independent
- Cov(X, X) = Var(X)

## Key Points

1. EXPECTATION IS NOT NECESSARILY AN OBSERVABLE VALUE—it represents the theoretical long-run average.

2. EXPECTATION MAY NOT EXIST for distributions with heavy tails where the defining sum or integral diverges.

3. INDEPENDENCE IS NOT REQUIRED for linearity of expectation, making it exceptionally powerful.

4. VARIANCE OF A CONSTANT IS ZERO—constant random variables have no dispersion.

5. POSITIVE COVARIANCE DOES NOT IMPLY CAUSATION—both variables might be influenced by a third factor.

6. CORRELATION OF ±1 INDICATES PERFECT LINEAR RELATIONSHIP.

7. COVARIANCE IS AFFECTED BY SCALE—changing units of X or Y changes Cov(X,Y) but correlation remains invariant.

8. EXPECTED VALUE MINIMIZES MEAN SQUARED ERROR—among all constants, E(X) is the best predictor of X in the least squares sense.

## Common Mistakes to Avoid

1. CONFUSING E(X²) WITH [E(X)]²—these are different; E(X²) is the second raw moment while [E(X)]² is the square of the mean.

2. FORGETTING TO SQUARE THE COEFFICIENT when computing Var(aX)—remember Var(aX) = a²Var(X), not aVar(X).

3. ASSUMING ZERO COVARIANCE IMPLIES INDEPENDENCE—this is only true for jointly normal distributions; in general, uncorrelated variables can be dependent.

4. NOT CHECKING CONVERGENCE when computing expectation of continuous distributions—the integral must converge absolutely.

5. INCORRECT APPLICATION OF LOTUS—remember to use g(xᵢ) or g(x) in the formula, not just xᵢ or x.

## Revision Tips

1. PRACTICE COMPUTATION: Solve at least 5 problems each for discrete and continuous expectation calculations before the exam.

2. MEMORIZE KEY PROPERTIES: Write down all linearity and variance properties on a single sheet for quick review.

3. UNDERSTAND INTERPRETATION: Be able to explain what "expected value = 3.5" means in the context of rolling dice.

4. WORK WITH JOINT DISTRIBUTIONS: Practice computing E(X), E(Y), E(XY), Var(X), Var(Y), and Cov(X,Y) from given joint probability tables.

5. RELATE TO MARKOV CHAINS: Understand how expectation connects to stationary distributions and long-run behavior of stochastic processes you will study next.