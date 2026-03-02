# Rook Polynomials - Summary

## Key Definitions and Concepts

- **Board (B):** A subset of squares on a chessboard where rooks can be placed; can be represented using coordinates or Ferrers diagrams.

- **Rook Number r_k(B):** The number of ways to place k non-attacking rooks on board B, where non-attacking means no two rooks share the same row or column.

- **Rook Polynomial:** R(B, x) = Σ\_{k=0}^{n} r_k(B) x^k, where n is the maximum number of rooks that can be placed.

- **Non-attacking rooks:** Rooks that do not share any row or column; this is the fundamental constraint in all rook polynomial problems.

## Important Formulas and Theorems

- **Basic definition:** R(B, x) = r_0 + r_1x + r_2x² + ... + r_nx^n

- **Board splitting theorem:** If B = B1 ∪ B2 where B1 and B2 are disjoint (no shared rows or columns), then R(B, x) = R(B1, x) × R(B2, x)

- **Restricted permutations:** Number of valid permutations = Σ\_{k=0}^{n} (-1)^k r_k(B) (n-k)!

- **Maximum rooks:** n = min(number of rows, number of columns) for the board

## Key Points

1. r_0(B) = 1 for any board (always one way to place zero rooks)

2. The coefficient of x^k in R(B, x) equals r_k(B), the number of ways to place k non-attacking rooks

3. Rook polynomials provide an elegant generating function approach to counting problems

4. The board splitting theorem converts polynomial multiplication into simpler sub-problems

5. Rook polynomials connect directly to inclusion-exclusion principle for solving derangement-type problems

6. The degree of the rook polynomial equals the size of the largest matching (maximum rooks) on the board

7. For complete m×n board, r_k = C(m,k) × C(n,k) × k! representing row selections, column selections, and arrangements

## Common Mistakes to Avoid

1. Forgetting that r_0 = 1 and assuming r_0 = 0 for empty placements

2. Counting attacking rooks as valid placements (violates non-attacking condition)

3. Not recognizing when boards can be split into disjoint components

4. Incorrectly calculating the maximum number of rooks (should be min of rows and columns)

5. Confusing the signs in the inclusion-exclusion formula for permutation problems (should alternate: +, -, +, ...)

## Revision Tips

1. Practice drawing various board configurations and listing all possible non-attacking rook placements for small values of k

2. Memorize the formula for complete rectangular boards: r_k = C(m,k) × C(n,k) × k!

3. Use the board splitting theorem proactively to simplify complex boards before calculating rook numbers

4. Solve at least 3-4 problems involving different board shapes to gain confidence

5. Remember the connection to derangements: when solving permutation problems with forbidden positions, use the inclusion-exclusion formula with rook numbers
