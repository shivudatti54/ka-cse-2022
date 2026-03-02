# The Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients

===========================================================

## Key Points

---

- A second-order linear homogeneous recurrence relation with constant coefficients is an equation of the form:
  - $a_n + b_n \cdot a_{n-1} + c_n \cdot a_{n-2} = 0$
- where $a_n$ is a sequence and $a_{n-1}, a_{n-2}$ are the previous terms.
- The coefficients $a_n, b_n, c_n$ are constants.
- The recurrence relation can be solved using characteristic equations, which are polynomial equations of the form:
  - $r^2 + b \cdot r + c = 0$
- The roots of the characteristic equation determine the general solution of the recurrence relation.

## Important Formulas

---

- Characteristic equation: $r^2 + b \cdot r + c = 0$
- General solution: $a_n = A \cdot r_1^n + B \cdot r_2^n$ (where $r_1, r_2$ are the roots of the characteristic equation)
- Initial conditions:
  - $a_0 = A$
  - $a_1 = A \cdot r_1 + B \cdot r_2$

## Definitions and Theorems

---

- **Roots of the characteristic equation**: the values of $r$ that satisfy the characteristic equation.
- **General solution**: the solution that expresses the nth term of the sequence in terms of the roots of the characteristic equation.
- **Particular solution**: a solution that satisfies a specific initial condition.

## Important Theorems

---

- **Fundamental Theorem of Recurrence Relations**: if the characteristic equation has distinct roots, then the general solution is unique and depends only on the initial conditions.
- **Homogeneity**: if the characteristic equation has repeated roots, then the general solution is a polynomial of degree one less than the order of the recurrence relation.

## Quick Revision Tips

---

- Focus on solving characteristic equations using the quadratic formula.
- Understand the relationship between the roots of the characteristic equation and the general solution.
- Review the initial conditions and how they affect the particular solution.

## References

---

- [Textbook], [Chapter]
