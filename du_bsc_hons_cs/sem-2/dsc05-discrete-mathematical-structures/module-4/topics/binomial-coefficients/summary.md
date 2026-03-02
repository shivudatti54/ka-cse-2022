# Binomial Coefficients - Summary

## Key Definitions and Concepts

- **Binomial Coefficient** $\binom{n}{k}$: The number of ways to choose k elements from an n-element set, given by $\frac{n!}{k!(n-k)!}$
- **Binomial Theorem**: $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k}b^k$
- **Pascal's Triangle**: Triangular array where each entry is $\binom{n}{k}$, satisfying $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$

## Important Formulas and Theorems

| Formula | Description |
|---------|-------------|
| $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Fundamental definition |
| $\binom{n}{k} = \binom{n}{n-k}$ | Symmetry property |
| $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ | Sum of all coefficients |
| $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$ | Alternating sum |
| $\sum_{k=0}^{n} k \binom{n}{k} = n \cdot 2^{n-1}$ | Weighted sum |
| $\sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$ | Vandermonde's Identity |

## Key Points

- $\binom{n}{0} = \binom{n}{n} = 1$ for all non-negative integers n
- Pascal's Identity is the foundation of Pascal's Triangle construction
- Binomial coefficients are always integers (combinatorial significance)
- The middle coefficients are largest; coefficients are symmetric around the middle
- $\binom{n}{k} = 0$ when k > n or k < 0
- For $(1+x)^n$, the coefficient of $x^k$ is exactly $\binom{n}{k}$

## Common Mistakes to Avoid

1. **Forgetting factorials**: Always compute factorials correctly; remember $0! = 1$
2. **Ignoring domain**: $\binom{n}{k}$ is defined as 0 when $k > n$
3. **Sign errors**: In expansions with negative terms, carefully track $(-1)^k$ factors
4. **Misapplying identities**: Ensure conditions (like $1 \leq k \leq n$) are satisfied before using Pascal's Identity

## Revision Tips

1. **Practice computation**: Work through 5-10 binomial coefficient calculations daily until comfortable
2. **Memorize Pascal's Triangle** rows for n = 0 to 10 for quick reference during exams
3. **Prove identities yourself**: Writing out combinatorial proofs reinforces understanding
4. **Solve previous year questions**: DU exam papers frequently test specific identities and expansion problems