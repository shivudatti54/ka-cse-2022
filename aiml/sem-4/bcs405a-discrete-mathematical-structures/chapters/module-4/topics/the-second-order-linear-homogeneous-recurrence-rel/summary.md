# Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients

=====================================================

### Key Concepts

- **Definition**: A recurrence relation of the form:
  $$a_n + b_1a_{n-1} + b_2a_{n-2} = 0$$
  where $a_n$ is the value at $n$ and $b_1$, $b_2$ are constants.
- **Homogeneous**: The equation does not contain any non-homogeneous terms.
- **Linear**: The equation can be expressed in the form of a linear combination of previous terms.

### Important Formulas

- **Characteristic Equation**: $x^2 + b_1x + b_2 = 0$
- **Roots of the Characteristic Equation**: $r_1$ and $r_2$ (repeated or distinct)
- **General Solution**: $a_n = c_1(r_1)^n + c_2n(r_1)^n$ (for distinct roots) or $a_n = c_1(r_1)^n + c_2n(r_1)^{n-1}$ (for repeated roots)

### Theorems

- **Fundamental Theorem of Recurrence Relations**: If the characteristic equation has distinct roots $r_1$ and $r_2$, then the solution is unique and given by the general solution.
- **Theorem for Repeated Roots**: If the characteristic equation has a repeated root $r$, then the solution is given by $a_n = c_1r^n + c_2nr^n$.

### Other Key Points

- **Initial Conditions**: Initial conditions are used to determine the constants $c_1$ and $c_2$.
- **Solving Methods**: Methods for solving these recurrence relations include:
  - Characteristic equation method
  - Using matrices
  - Using generating functions
