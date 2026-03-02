# Jointly Distributed Random Variables - Summary

## Key Definitions and Concepts
- **Joint CDF:** $F_{X,Y}(x,y) = P(X \leq x, Y \leq y)$
- **Joint PMF (discrete):** $p_{X,Y}(x,y) = P(X = x, Y = y)$; must sum to 1
- **Joint PDF (continuous):** $f_{X,Y}(x,y) \geq 0$; must integrate to 1 over entire plane
- **Marginal PMF:** $p_X(x) = \sum_y p_{X,Y}(x,y)$; similarly for $p_Y$
- **Marginal PDF:** $f_X(x) = \int f_{X,Y}(x,y) \, dy$
- **Conditional PMF:** $p_{Y|X}(y|x) = p_{X,Y}(x,y) / p_X(x)$
- **Conditional PDF:** $f_{Y|X}(y|x) = f_{X,Y}(x,y) / f_X(x)$
- **Independence:** $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$ for all $(x,y)$

## Important Formulas
- **Covariance:** $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$
- **Correlation:** $\rho = \text{Cov}(X,Y) / (\sigma_X \sigma_Y)$, with $-1 \leq \rho \leq 1$
- **Variance of sum:** $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$
- **Linearity:** $E[aX + bY] = aE[X] + bE[Y]$ (always)
- **Product rule for independence:** If X, Y independent, $E[XY] = E[X]E[Y]$
- **Rectangle probability:** $P(a < X \leq b, c < Y \leq d) = F(b,d) - F(a,d) - F(b,c) + F(a,c)$

## Key Points
- Marginals are obtained by "summing/integrating out" the other variable
- Independence requires the factorization to hold for **all** (x, y), not just some
- Non-rectangular support automatically means the variables are dependent
- Conditional expectation $E[Y|X=x]$ is a function of x
- $\text{Cov}(X,Y) = 0$ does NOT imply independence (only converse is true for jointly normal)
- Correlation measures only **linear** association; nonlinear dependencies may give $\rho$ close to 0
- For $n$ uncorrelated variables: $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$
- Joint distributions are essential in Bayesian inference, ML, and algorithm analysis

## Common Mistakes to Avoid
- **Incorrect integration limits:** Always sketch the support region before integrating. Most errors come from swapping or misidentifying limits in triangular/non-standard regions.
- **Assuming independence without verification:** Just because two events seem unrelated intuitively doesn't make the random variables independent. Always check the factorization condition.
- **Confusing uncorrelated with independent:** Zero covariance is necessary but NOT sufficient for independence (except for jointly Gaussian random variables).
- **Forgetting the covariance term in variance of sums:** $\text{Var}(X+Y) \neq \text{Var}(X) + \text{Var}(Y)$ unless X and Y are uncorrelated.

## Revision Tips
- **Practice setting up integrals:** The most exam-critical skill is correctly identifying the region and translating it to integration limits. Do at least 5 problems with triangular and circular regions.
- **Build a table for discrete problems:** Always organize joint PMFs in a table and add row/column totals for marginals — this prevents arithmetic errors.
- **Memorize the covariance shortcut** and the properties of correlation. These appear in almost every exam.
- **Use the independence-support trick:** Before any computation, check if the support is rectangular. If not, immediately conclude dependence and move on.