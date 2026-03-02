# Linear Congruential Generator (LCG) - Summary

## Key Definitions

- **Linear Congruential Generator (LCG)**: A deterministic algorithm for generating a sequence of pseudorandom numbers using the recurrence relation Xₙ₊₁ = (a × Xₙ + c) mod m
- **Seed**: The initial value X₀ that starts the random number sequence
- **Period**: The length of the sequence before it repeats (maximum is m)
- **Full Period**: Achieving the maximum possible period of m
- **Mixed LCG**: When c ≠ 0 in the formula
- **Multiplicative LCG**: When c = 0 (also called Lehmer generator)

## Important Formulas

- **Core Recurrence**: Xₙ₊₁ = (a × Xₙ + c) mod m
- **Hull-Dobell Conditions for Full Period**:
  1. gcd(c, m) = 1
  2. For every prime p dividing m: p | (a - 1)
  3. If 4 | m: then 4 | (a - 1)

## Key Points

1. The LCG, introduced by Lehmer in 1949, is the oldest and simplest PRNG algorithm

2. Parameters must be carefully chosen - poor choices lead to predictable sequences or bad statistical properties

3. The RANDU algorithm (a = 65539, m = 2³¹) is a famous failure case where generated points fell onto only 15 planes in 3D space

4. LCGs are computationally efficient and achieve full period easily with proper parameter selection

5. LCGs are NOT cryptographically secure - they are vulnerable to prediction attacks given few output values

6. For cryptographic purposes, cryptographically secure PRNGs like Blum Blum Shub must be used instead

7. The MINSTD generator (a = 48271, m = 2³¹-1) represents a reasonably good non-cryptographic LCG

## Common Mistakes

1. **Assuming LCGs are random**: They are entirely deterministic and reproducible given the seed

2. **Using LCGs for cryptography**: This is a serious security vulnerability - LCGs are predictable

3. **Ignoring parameter selection**: Parameters a, c, and m critically affect the quality of output

4. **Overlooking the period**: The sequence will eventually repeat, which can be problematic for long-running applications