# Quadratic Forms and Its Classifications - Summary

## Key Definitions and Concepts

- **Quadratic Form:** A homogeneous polynomial of degree 2 in n variables: Q(x₁, x₂, ..., xₙ) = Σᵢ Σⱼ aᵢⱼ xᵢ xⱼ

- **Matrix Representation:** Q(x) = xᵀAx where A is symmetric and x is a column vector.

- **Definiteness Classification:**
  - Positive Definite: Q(x) > 0 for all x ≠ 0
  - Negative Definite: Q(x) < 0 for all x ≠ 0
  - Positive Semi-Definite: Q(x) ≥ 0 for all x
  - Negative Semi-Definite: Q(x) ≤ 0 for all x
  - Indefinite: Takes both positive and negative values

## Important Formulas and Theorems

- **Eigenvalue Criterion:** A quadratic form is positive definite iff all eigenvalues of A are positive; negative definite iff all eigenvalues are negative; indefinite if eigenvalues have mixed signs.

- **Principal Minors Test (Positive Definite):** All leading principal minors must be positive: Δ₁ > 0, Δ₂ > 0, ..., Δₙ > 0.

- **Principal Minors Test (Negative Definite):** Leading principal minors alternate in sign: Δ₁ < 0, Δ₂ > 0, Δ₃ < 0, ...

- **Sylvester's Law of Inertia:** The number of positive, negative, and zero eigenvalues (signature) remains invariant under congruence.

- **Canonical Form:** Q(y) = λ₁y₁² + λ₂y₂² + ... + λₙyₙ² where λᵢ are eigenvalues of A.

## Key Points

- The symmetric matrix representation is crucial: coefficients of xᵢxⱼ (i ≠ j) go as half into off-diagonal positions.

- Eigenvalues fully determine the classification of quadratic forms.

- Positive definite matrices have all leading principal minors positive.

- Indefinite forms have both positive and negative eigenvalues.

- Orthogonal transformation x = Py preserves xᵀx but diagonalizes the quadratic form.

- Signature (p, n, z) counts positive, negative, and zero eigenvalues respectively.

## Common Mistakes to Avoid

- Forgetting the factor of 2 when forming the symmetric matrix: 2bxy becomes b in both (1,2) and (2,1) positions.

- Confusing leading principal minors with all principal minors for the definiteness test.

- Assuming the principal minors test works for semi-definite cases (it doesn't; use eigenvalues).

- Not recognizing that only symmetric matrices represent quadratic forms (any symmetric A can be used).

## Revision Tips

- Practice converting quadratic forms to matrix form with several examples.

- Memorize the principal minors conditions for 2×2 and 3×3 matrices.

- Remember: all eigenvalues positive → minimum; all negative → maximum; mixed → saddle point.

- Work through at least 3-4 problems from each category to build confidence for exams.
