# Multiplication of Large Integers and Strassen's Matrix Multiplication - Summary

## Key Definitions

- **School Method**: The traditional algorithm for multiplication taught in primary education, operating in O(n²) time for n-digit integers or n×n matrices.

- **Karatsuba Algorithm**: A divide-and-conquer integer multiplication algorithm that reduces four recursive multiplications to three, achieving Θ(n^log₂3) complexity.

- **Strassen's Algorithm**: A divide-and-conquer matrix multiplication algorithm that reduces eight recursive block multiplications to seven, achieving Θ(n^log₂7) complexity.

- **Master Theorem**: A mathematical tool for solving recurrence relations of the form T(n) = aT(n/b) + f(n), where a ≥ 1, b > 1.

## Important Formulas

**Karatsuba Integer Multiplication:**

- Split: A = A₁ × 10^(n/2) + A₀, B = B₁ × 10^(n/2) + B₀
- AB = A₁B₁ × 10^n + [(A₁ + A₀)(B₁ + B₀) - A₁B₁ - A₀B₀] × 10^(n/2) + A₀B₀
- Recurrence: T(n) = 3T(n/2) + Θ(n)
- Solution: T(n) = Θ(n^log₂3) ≈ Θ(n^1.585)

**Strassen Matrix Multiplication:**

- 7 intermediate values: M₁ through M₇ (as defined in theory)
- Recurrence: T(n) = 7T(n/2) + Θ(n²)
- Solution: T(n) = Θ(n^log₂7) ≈ Θ(n^2.807)

## Key Points

1. Both Karatsuba and Strassen algorithms employ the divide-and-conquer paradigm, breaking problems into smaller subproblems and combining solutions.

2. Karatsuba reduces integer multiplication from 4 to 3 recursive multiplications by computing the middle term algebraically.

3. The key Strassen identity uses 7 multiplications to compute the 2×2 block matrix product that traditionally requires 8.

4. Despite theoretical improvements, Strassen has practical limitations: larger constant factors, numerical instability, and increased memory overhead from storing intermediate matrices.

5. The Master Theorem confirms that both algorithms provide asymptotic improvements over their naive counterparts.

6. For practical implementations, threshold values determine when to switch from naive to advanced algorithms (typically n > 16-64 for Karatsuba, n > 512-1024 for Strassen).

7. FFT-based multiplication can achieve O(n log n) complexity for extremely large integers, surpassing even Karatsuba.

## Common Mistakes

1. **Confusing the Paradigm**: Treating Karatsuba and Strassen as brute-force algorithms when they are fundamentally divide-and-conquer approaches that optimize through algebraic insight.

2. **Recurrence Errors**: Forgetting the additive term in the recurrence—Karatsuba has O(n) for additions/shifts, Strassen has O(n²) for matrix additions/subtractions.

3. **Missing Base Case**: Failing to specify when recursion terminates (typically for small n where naive method is faster).

4. **Strassen Assembly Errors**: Incorrectly combining the seven intermediate values to form the four output blocks; each formula must be applied precisely.

5. **Ignoring Practical Constants**: Theoretically superior algorithms may be slower for moderate input sizes due to overhead from recursion and additional arithmetic operations.
