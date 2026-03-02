# Strassen's Matrix Multiplication - Summary

## Key Definitions and Concepts

- **Matrix Multiplication**: Given A (n×n) and B (n×n), compute C = A × B where C[i][j] = Σ(k=1 to n) A[i][k] × B[k][j]

- **Strassen's Algorithm**: A divide-and-conquer algorithm that multiplies two 2×2 matrices using 7 multiplications instead of 8

- **Divide-and-Conquer Paradigm**: Split matrices into quadrants, recursively compute products, combine results

## Important Formulas and Theorems

**The Seven Strassen Products (for 2×2 matrices):**
- M1 = (a11 + a22) × (b11 + b22)
- M2 = (a21 + a22) × b11
- M3 = a11 × (b12 - b22)
- M4 = a22 × (b21 - b11)
- M5 = (a11 + a12) × b22
- M6 = (a21 - a11) × (b11 + b12)
- M7 = (a12 - a22) × (b21 + b22)

**Result Matrix:**
- C11 = M1 + M4 - M5 + M7
- C12 = M3 + M5
- C21 = M2 + M4
- C22 = M1 - M2 + M3 + M6

**Recurrence Relation:** T(n) = 7T(n/2) + O(n²)

**Time Complexity:** Θ(n^log₂7) ≈ Θ(n^2.807)

## Key Points

- Strassen reduces the multiplication count from 8 to 7 for 2×2 matrices
- This translates to O(n^2.807) vs O(n³) asymptotically
- Uses divide-and-conquer: divide into quadrants, recurse, combine
- Trade-off: fewer multiplications but more additions/subtractions
- Works efficiently only for large matrices (n > threshold, typically ~100-1000)
- Requires matrices of size power of 2; padding needed otherwise
- Space complexity: O(n²) auxiliary space
- Slightly less numerically stable than standard multiplication

## Common Mistakes to Avoid

1. Forgetting that Strassen increases additions—it's only beneficial when matrix size is large
2. Confusing the formulas for M1-M7 or C11-C22
3. Not padding matrices to power-of-2 size when required
4. Using the wrong base case (n=1, not n=2)
5. Applying Master Theorem incorrectly—remember a=7, b=2

## Revision Tips

1. Practice deriving the 7 formulas by hand multiple times until memorized
2. Work through at least one complete 2×2 example step-by-step
3. Memorize the recurrence relation T(n) = 7T(n/2) + O(n²)
4. Remember the asymptotic improvement: n^2.807 vs n³
5. Know the practical threshold where Strassen becomes faster than naive
6. Review divide-and-conquer fundamentals to understand the recursive structure