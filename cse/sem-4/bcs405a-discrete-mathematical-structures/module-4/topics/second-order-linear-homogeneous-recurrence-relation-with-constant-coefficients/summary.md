# Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients - Summary

## Key Definitions and Concepts

- **Second Order Linear Homogeneous Recurrence Relation**: A relation of the form aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ (with c₂ ≠ 0) where the right-hand side equals zero (homogeneous).

- **Characteristic Equation**: The quadratic equation r² - c₁r - c₂ = 0 obtained by substituting aₙ = rⁿ into the recurrence relation.

- **General Solution**: The complete solution expressed in terms of the characteristic roots and arbitrary constants.

## Important Formulas and Theorems

| Case                | Roots          | General Solution                                                      |
| ------------------- | -------------- | --------------------------------------------------------------------- |
| Distinct Real Roots | r₁ ≠ r₂ (real) | aₙ = A(r₁)ⁿ + B(r₂)ⁿ                                                  |
| Repeated Real Roots | r₁ = r₂ = r    | aₙ = (A + Bn)rⁿ                                                       |
| Complex Roots       | r = α ± iβ     | aₙ = rⁿ(A cos(nθ) + B sin(nθ)), where r = √(α² + β²), θ = arctan(β/α) |

## Key Points

- The characteristic equation is always quadratic for second order relations.

- Distinct real roots yield exponential solutions; repeated roots require the n-factor; complex roots yield sinusoidal solutions.

- Two initial conditions (a₀, a₁ or a₁, a₂) are required to uniquely determine the sequence.

- The solution form depends solely on the nature of the characteristic roots, not on initial conditions.

- Verification by substitution confirms the correctness of the solution.

## Common Mistakes to Avoid

- Forgetting to subtract c₁r from the left side when forming the characteristic equation (common sign error).

- Omitting the 'n' factor when dealing with repeated roots.

- Using the wrong trigonometric angle when converting complex roots to polar form.

- Incorrectly handling initial conditions, especially when n starts from 0 versus 1.

## Revision Tips

- Practice converting recurrence relations to characteristic equations until the process becomes automatic.

- Memorize the three solution forms for the three cases of roots.

- Always verify your final answer by checking both the recurrence relation and initial conditions.

- Work through at least 5-6 diverse problems covering all three cases before the exam.
