# Conditional Expectation - Summary

## Key Definitions and Concepts

- **Conditional Expectation E[X | Y = y]**: The expected value of X computed with respect to the conditional distribution of X given Y = y. For discrete case: E[X | Y = y] = Σₓ x · P(X = x | Y = y)

- **E[X | Y] as Random Variable**: Conditional expectation is a function g(Y) of the random variable Y, making it itself a random variable

- **Law of Total Expectation**: E[E[X | Y]] = E[X] - the average of conditional expectations equals the unconditional expectation

- **Law of Total Variance**: Var(X) = E[Var(X | Y)] + Var(E[X | Y])

## Important Properties

- **Linearity**: E[aX + bY | Z] = aE[X | Z] + bE[Y | Z]
- **Taking out what is known**: E[g(Z)X | Z] = g(Z) · E[X | Z]
- **Independence**: If X ⟂ Y, then E[X | Y] = E[X]

## Key Points

1. Conditional expectation refines predictions when partial information is available

2. The Law of Total Expectation is essential for computing expectations by conditioning on simpler sub-problems

3. In algorithm analysis, we often condition on random choices (like pivot selection in QuickSort)

4. For independent random variables, conditioning provides no additional information

5. E[X | Y = y] can take different values for different y, but its expectation equals E[X]

6. The variance decomposition separates within-group variation from between-group variation

7. Conditional expectation is fundamental to Markov chains and stochastic processes

## Common Mistakes to Avoid

1. Treating conditional expectation as a fixed number instead of a random variable
2. Forgetting to use the Law of Total Expectation when it simplifies calculations
3. Confusing conditional expectation with conditional probability
4. Ignoring the independence property when X and Y are independent

## Revision Tips

1. Practice computing conditional expectations from joint distributions for both discrete and continuous cases

2. Memorize and practice applying the Law of Total Expectation and Total Variance

3. Work through algorithm analysis examples (like QuickSort) to understand practical applications

4. Always verify results using E[E[X | Y]] = E[X] as a check