# Least Squares Problem and Least Square Error - Summary

## Key Definitions and Concepts

- **Least Squares Problem:** Given A ∈ ℝᵐˣⁿ (m ≥ n) and b ∈ ℝᵐ, find x ∈ ℝⁿ that minimizes ‖b - Ax‖₂²

- **Normal Equations:** AᵀAx̂ = Aᵀb — the fundamental system that the least squares solution must satisfy

- **Residual:** r = b - Ax̂; the residual is orthogonal to Col(A)

- **Projection Matrix:** P = A(AᵀA)⁻¹Aᵀ projects any vector onto Col(A)

- **Moore-Penrose Pseudoinverse:** A⁺ = (AᵀA)⁻¹Aᵀ for full column rank matrices; solution is x̂ = A⁺b

## Important Formulas and Theorems

- **Minimization Condition:** ∇‖b - Ax‖² = -2Aᵀ(b - Ax) = 0 ⇒ AᵀAx = Aᵀb

- **QR Solution:** If A = QR with QᵀQ = I, then x̂ = R⁻¹Qᵀb

- **SVD Solution:** If A = UΣVᵀ, then x̂ = VΣ⁺Uᵀb where Σ⁺ contains reciprocal non-zero singular values

- **Minimum Error:** ‖r‖² = ‖b‖² - ‖Ax̂‖² = bᵀb - x̂ᵀAᵀAx̂

- **Uniqueness Condition:** Solution is unique if and only if rank(A) = n (full column rank)

## Key Points

- The least squares problem finds approximate solutions to overdetermined systems where no exact solution exists

- The solution represents the orthogonal projection of b onto the column space of A

- Three main solution methods: Normal equations (simplest), QR decomposition (numerically stable), SVD (most general)

- Full column rank ensures uniqueness; rank deficiency leads to infinitely many solutions

- The least square error quantifies goodness of fit; smaller error indicates better approximation

- Linear regression is a special case of least squares for fitting straight lines

- QR decomposition is preferred in practice due to better numerical stability than normal equations

- The pseudoinverse provides a unified framework for all least squares solutions

## Common Mistakes to Avoid

- Forgetting to check rank(A) before claiming unique solution existence

- Computing AᵀA incorrectly—always verify matrix dimensions and multiplication

- Using normal equations when matrix is ill-conditioned; QR or SVD preferred numerically

- Confusing the pseudoinverse with the regular inverse (only works for full rank square matrices)

- Not understanding that residual is orthogonal to column space—key exam concept

## Revision Tips

- Practice deriving normal equations from first principles using calculus

- Memorize the three solution methods and know when to apply each

- Solve at least 5-6 problems from each method to build fluency

- Remember the geometric interpretation: projection onto column space

- Review pseudoinverse properties for rank-deficient cases

- Understand the connection between least squares and linear regression
