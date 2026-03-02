# Linear Recurrence Relations with Constant Coefficients - Summary

## Key Definitions and Concepts

- **Recurrence Relation**: An equation that defines a sequence {a_n} where each term a_n depends on one or more preceding terms.

- **Linear Recurrence with Constant Coefficients**: A relation of the form a_n = c_1a_{n-1} + c_2a_{n-2} + ... + c_ka_{n-k} + f(n), where c_1, ..., c_k are constants.

- **Order**: The number of preceding terms needed, equal to k in the general form.

- **Homogeneous**: When f(n) = 0; otherwise **non-homogeneous**.

- **Characteristic Equation**: r^k - c_1r^{k-1} - ... - c_k = 0, derived by substituting a_n = r^n.

## Important Formulas and Theorems

- **Distinct Roots Solution**: If r_1, r_2, ..., r_k are distinct roots of characteristic equation: a_n = α_1r_1^n + α_2r_2^n + ... + α_kr_k^n

- **Repeated Roots Solution**: If root r has multiplicity m: include terms (α_0 + α_1n + ... + α_{m-1}n^{m-1})r^n

- **Complete Solution**: For non-homogeneous: a_n = a_n^(h) + a_n^(p), where a_n^(h) is homogeneous solution and a_n^(p) is particular solution

- **Particular Solution Trial Forms**:
  - f(n) = P(n) → try polynomial of same degree
  - f(n) = c^n → try A·c^n (if c not root), otherwise n^m·A·c^m

## Key Points

- Always solve the homogeneous part first for non-homogeneous recurrences.

- The number of arbitrary constants equals the order of the recurrence.

- Required initial conditions = order of the recurrence.

- Verify solutions by substituting back into original recurrence.

- For algorithm analysis, recurrence relations often have form T(n) = aT(n/b) + f(n).

- Characteristic equation roots determine solution behavior: roots inside unit circle → decaying sequence; roots outside → growing; roots on unit circle → oscillatory.

- When f(n) overlaps with homogeneous solution, multiply trial particular solution by n to the power of root multiplicity.

## Common Mistakes to Avoid

1. Forgetting to multiply by n^m when the trial particular solution form overlaps with homogeneous solution roots.

2. Not using enough initial conditions (need exactly k conditions for order k).

3. Incorrectly forming the characteristic equation (common sign errors).

4. Trying polynomial trial solutions for exponential non-homogeneous parts or vice versa.

5. Forgetting to add the homogeneous and particular solutions together.

## Revision Tips

1. Practice solving at least 5 homogeneous and 5 non-homogeneous problems to build proficiency.

2. Memorize the characteristic equation formation: replace a_n with r^n and simplify.

3. For each type of f(n) in non-homogeneous recurrences, remember the corresponding trial solution form.

4. Always verify your final answer by substituting n = 0, 1, 2 into the original recurrence.

5. Focus on understanding the "why" behind each solution method, not just memorizing procedures.