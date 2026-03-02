# Divide and Conquer - Advanced - Summary

## Key Definitions and Concepts

- **Divide and Conquer**: Algorithmic paradigm with three steps—Divide (break into subproblems), Conquer (solve recursively), Combine (merge solutions)
- **Fast Fourier Transform (FFT)**: Computes DFT in O(n log n) using divide and conquer on complex roots of unity
- **Strassen's Matrix Multiplication**: Achieves O(n^log₂7) ≈ O(n^2.81) using 7 recursive multiplications instead of 8
- **Closest Pair Problem**: Finds minimum distance between points in O(n log n) using geometric strip processing
- **QuickSelect**: Randomized algorithm for order statistics with expected O(n) time
- **Median of Medians**: Deterministic O(n) selection algorithm using groups of 5
- **Master Theorem**: Provides asymptotic analysis for T(n) = aT(n/b) + f(n) recurrences

## Important Formulas and Theorems

- **FFT Recurrence**: T(n) = 2T(n/2) + Θ(n) → Θ(n log n)
- **Strassen Complexity**: T(n) = 7T(n/2) + Θ(n²) → Θ(n^log₂7) ≈ Θ(n^2.81)
- **QuickSelect Expected Time**: T(n) = T(n/2) + Θ(n) → O(n)
- **Master Theorem Cases**:
  - Case 1: f(n) = O(n^(log_b a - ε)) → T(n) = Θ(n^(log_b a))
  - Case 2: f(n) = Θ(n^(log_b a) × log^k n) → T(n) = Θ(n^(log_b a) × log^(k+1) n)
  - Case 3: f(n) = Ω(n^(log_b a + ε)) → T(n) = Θ(f(n))

## Key Points

- Divide and Conquer transforms exponential problems to polynomial through recursive decomposition
- FFT revolutionized signal processing by reducing DFT computation from O(n²) to O(n log n)
- Strassen's algorithm was the first to beat the naive n³ matrix multiplication bound
- The closest pair algorithm exploits geometric packing—only 7 points can fit in a d×2d rectangle
- QuickSelect achieves linear expected time through random pivot selection
- Master Theorem requires comparing f(n) with n^(log_b a) to determine the asymptotic behavior
- The choice between divide and conquer and dynamic programming depends on subproblem independence
- Current research in fast matrix multiplication has achieved O(n^2.3728) but with impractical constants

## Common Mistakes to Avoid

1. **Confusing divide and conquer with dynamic programming**: Divide and conquer produces independent subproblems, while DP has overlapping subproblems requiring memoization

2. **Incorrect Master Theorem application**: Case 2 requires the polylogarithmic factor; don't apply it when f(n) is polynomially different from n^(log_b a)

3. **Forgetting the combining step**: A divide and conquer algorithm is only efficient if the combine step is efficient (often O(n))

4. **Misapplying Strassen**: Strassen's overhead makes it slower than naive multiplication for small matrices (typically n < 32 or so)

5. **Confusing expected vs worst-case**: QuickSelect is O(n) expected but O(n²) worst-case; Median of Medians guarantees O(n) worst-case

## Revision Tips

1. Practice deriving recurrence relations from algorithm descriptions and applying Master Theorem

2. Work through the FFT with small examples to understand the even-odd decomposition

3. Review the geometric arguments in closest pair, particularly the packing proof

4. Compare QuickSelect and Median of Medians side-by-side to understand when each is preferred

5. Remember that Strassen and FFT are theoretical breakthroughs—implementations often use optimized versions