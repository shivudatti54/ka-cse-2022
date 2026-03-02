# Binomial Coefficients

## Introduction

Binomial coefficients are fundamental mathematical quantities that appear extensively in combinatorics, probability theory, and algebra. Represented as $\binom{n}{k}$ (read as "n choose k"), these coefficients count the number of ways to select k elements from a set of n distinct elements without regard to order. This seemingly simple concept forms the backbone of the Binomial Theorem, which provides a powerful tool for expanding expressions of the form $(a+b)^n$.

The study of binomial coefficients has a rich historical background, with early contributions from Indian mathematicians like Pingala (3rd century BCE) and later systematic development by mathematicians such as al-Karaji and Pascal. The geometric representation of binomial coefficients in what is now known as Pascal's Triangle (though discovered independently by several cultures) provides an elegant visual pattern that reveals many deep properties of these coefficients.

In the context of Computer Science, binomial coefficients find applications in algorithm analysis (complexity of combinatorial algorithms), cryptography, coding theory, and probability distributions. Understanding binomial coefficients is essential for any computer science student, as they frequently appear in the analysis of recursive algorithms and in various computational problems.

## Key Concepts

### Definition and Fundamental Formula

The binomial coefficient $\binom{n}{k}$ is defined as the number of k-element subsets of an n-element set. Mathematically:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

where $n!$ (n factorial) is the product of all positive integers from 1 to n, with $0! = 1$ by convention.

**Key properties:**
- $\binom{n}{k} = 0$ when $k > n$ or $k < 0$
- $\binom{n}{0} = \binom{n}{n} = 1$
- $\binom{n}{k} = \binom{n}{n-k}$ (symmetry property)

### The Binomial Theorem

For any non-negative integer n:

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \cdots + \binom{n}{n}b^n$$

This theorem provides a systematic way to expand binomials raised to any positive integer power.

### Pascal's Identity and Triangle

**Pascal's Identity:** For integers n and k with $1 \leq k \leq n$:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

This identity leads to Pascal's Triangle, where each entry is the sum of two entries above it:

```
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
```

The nth row of Pascal's Triangle contains the coefficients $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$.

### Combinatorial Interpretations

1. **Selection:** $\binom{n}{k}$ = number of ways to choose k objects from n distinct objects
2. **Paths:** Number of paths from (0,0) to (n-k,k) using only right and up moves
3. **Coefficients:** Coefficient of $x^k$ in the expansion of $(1+x)^n$

### Generalizations and Identities

**Vandermonde's Identity:** For non-negative integers m, n, and r:

$$\sum_{k=0}^{r} \binom{m}{k} \binom{n}{r-k} = \binom{m+n}{r}$$

**Binomial Sum Identities:**
- $\sum_{k=0}^{n} \binom{n}{k} = 2^n$
- $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$ for $n \geq 1$
- $\sum_{k=0}^{n} k \binom{n}{k} = n \cdot 2^{n-1}$
- $\sum_{k=0}^{n} k^2 \binom{n}{k} = n(n+1) \cdot 2^{n-2}$

### Extension to Non-Integer Arguments

Using the Gamma function, binomial coefficients can be generalized:

$$\binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$$

This extension is useful in binomial series expansions.

## Examples

### Example 1: Computing Binomial Coefficients

**Problem:** Compute $\binom{6}{2}$ and $\binom{8}{3}$.

**Solution:**

For $\binom{6}{2}$:
$$\binom{6}{2} = \frac{6!}{2! \cdot 4!} = \frac{6 \times 5 \times 4!}{2 \times 1 \times 4!} = \frac{30}{2} = 15$$

For $\binom{8}{3}$:
$$\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \times 7 \times 6 \times 5!}{6 \times 5!} = 56$$

**Verification using Pascal's Triangle:** The 6th row is 1, 6, 15, 20, 15, 6, 1, confirming $\binom{6}{2} = 15$.

### Example 2: Binomial Expansion

**Problem:** Expand $(2x - 3)^4$ using the Binomial Theorem.

**Solution:**

Using $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k}b^k$ with $a = 2x$, $b = -3$, $n = 4$:

$(2x - 3)^4 = \sum_{k=0}^{4} \binom{4}{k} (2x)^{4-k}(-3)^k$

- k = 0: $\binom{4}{0}(2x)^4(-3)^0 = 1 \cdot 16x^4 \cdot 1 = 16x^4$
- k = 1: $\binom{4}{1}(2x)^3(-3)^1 = 4 \cdot 8x^3 \cdot (-3) = -96x^3$
- k = 2: $\binom{4}{2}(2x)^2(-3)^2 = 6 \cdot 4x^2 \cdot 9 = 216x^2$
- k = 3: $\binom{4}{3}(2x)^1(-3)^3 = 4 \cdot 2x \cdot (-27) = -216x$
- k = 4: $\binom{4}{4}(2x)^0(-3)^4 = 1 \cdot 1 \cdot 81 = 81$

**Answer:** $(2x - 3)^4 = 16x^4 - 96x^3 + 216x^2 - 216x + 81$

### Example 3: Proving Combinatorial Identity

**Problem:** Prove that $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ using combinatorial reasoning.

**Solution:**

Consider a set S with n elements. We want to count all subsets of S.

**Method 1 (Direct):** Each element can either be in a subset or not, giving $2^n$ total subsets.

**Method 2 (Case Analysis):** Count subsets by their size:
- Subsets of size 0: $\binom{n}{0}$ ways
- Subsets of size 1: $\binom{n}{1}$ ways
- ...
- Subsets of size n: $\binom{n}{n}$ ways

Total: $\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n}$

Since both methods count the same thing, they must be equal:
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

This is called a combinatorial proof.

## Exam Tips

1. **Memorize the fundamental formula** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ and know when to apply it for direct computation.

2. **Use symmetry property** $\binom{n}{k} = \binom{n}{n-k}$ to simplify calculations when $k > n/2$.

3. **Pascal's Identity** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ is frequently used in induction proofs and computing coefficients.

4. **For expansion problems**, always identify a, b, and n clearly in the binomial expression before applying the Binomial Theorem.

5. **Know the standard sums**: $\sum \binom{n}{k} = 2^n$ and $\sum (-1)^k \binom{n}{k} = 0$ are the most frequently tested.

6. **Practice Vandermonde's Identity** problems as they appear regularly in DU exams.

7. **Combinatorial proofs** require clear logical reasoning—explain both sides of the identity clearly.

8. **Check your answers**: For $\binom{n}{k}$, ensure $k \leq n$ and the result is always a non-negative integer.