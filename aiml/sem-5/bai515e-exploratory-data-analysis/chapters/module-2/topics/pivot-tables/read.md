# Truth Tables

## What is a Truth Table?

A truth table is a systematic tabular representation that shows **all possible combinations** of inputs and their corresponding outputs for a Boolean function. It completely describes the behavior of a logic circuit or Boolean expression.

## Structure of a Truth Table

For a function with **n input variables**, the truth table has:

- **2^n rows** (all possible input combinations)
- **n+1 columns** (n inputs + 1 output, or more for intermediate values)

### Example: 2-Variable Truth Table

| A   | B   | F   |
| --- | --- | --- |
| 0   | 0   | ?   |
| 0   | 1   | ?   |
| 1   | 0   | ?   |
| 1   | 1   | ?   |

## Constructing Truth Tables

### Step 1: Determine Number of Inputs

Count the variables in your expression.

- F = A.B has 2 inputs (4 rows)
- F = A.B + C has 3 inputs (8 rows)
- F = A.B.C.D has 4 inputs (16 rows)

### Step 2: List All Input Combinations

Use **binary counting** from 0 to 2^n - 1:

For 3 variables (A, B, C):
| Decimal | A | B | C |
|---------|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 2 | 0 | 1 | 0 |
| 3 | 0 | 1 | 1 |
| 4 | 1 | 0 | 0 |
| 5 | 1 | 0 | 1 |
| 6 | 1 | 1 | 0 |
| 7 | 1 | 1 | 1 |

### Step 3: Evaluate Expression for Each Row

Calculate the output for each input combination.

**Example:** F = A.B + C

| A   | B   | C   | A.B | F = A.B + C |
| --- | --- | --- | --- | ----------- |
| 0   | 0   | 0   | 0   | 0           |
| 0   | 0   | 1   | 0   | 1           |
| 0   | 1   | 0   | 0   | 0           |
| 0   | 1   | 1   | 0   | 1           |
| 1   | 0   | 0   | 0   | 0           |
| 1   | 0   | 1   | 0   | 1           |
| 1   | 1   | 0   | 1   | 1           |
| 1   | 1   | 1   | 1   | 1           |

## Canonical Forms from Truth Tables

### Sum of Products (SOP) - Minterms

A **minterm** is a product term where each variable appears exactly once (either complemented or uncomplemented).

**To get SOP:**

1. Find all rows where output = 1
2. Write the AND term for each such row
3. OR all the terms together

**Example:** From the table above, F = 1 for rows 1, 3, 5, 6, 7

F = A'B'C + A'BC + AB'C + ABC' + ABC

Using minterm notation: F = m1 + m3 + m5 + m6 + m7 = Σm(1,3,5,6,7)

### Product of Sums (POS) - Maxterms

A **maxterm** is a sum term where each variable appears exactly once.

**To get POS:**

1. Find all rows where output = 0
2. Write the OR term for each such row (complement of the row values)
3. AND all the terms together

**Example:** F = 0 for rows 0, 2, 4

F = (A+B+C)(A+B'+C)(A'+B+C)

Using maxterm notation: F = M0 . M2 . M4 = ΠM(0,2,4)

## Minterm and Maxterm Table

| Decimal | A   | B   | C   | Minterm     | Maxterm       |
| ------- | --- | --- | --- | ----------- | ------------- |
| 0       | 0   | 0   | 0   | A'B'C' (m0) | A+B+C (M0)    |
| 1       | 0   | 0   | 1   | A'B'C (m1)  | A+B+C' (M1)   |
| 2       | 0   | 1   | 0   | A'BC' (m2)  | A+B'+C (M2)   |
| 3       | 0   | 1   | 1   | A'BC (m3)   | A+B'+C' (M3)  |
| 4       | 1   | 0   | 0   | AB'C' (m4)  | A'+B+C (M4)   |
| 5       | 1   | 0   | 1   | AB'C (m5)   | A'+B+C' (M5)  |
| 6       | 1   | 1   | 0   | ABC' (m6)   | A'+B'+C (M6)  |
| 7       | 1   | 1   | 1   | ABC (m7)    | A'+B'+C' (M7) |

## Applications of Truth Tables

1. **Verifying Boolean identities**
2. **Deriving Boolean expressions from requirements**
3. **Testing circuit correctness**
4. **Converting between SOP and POS forms**
5. **Input for Karnaugh map minimization**

## Summary

- Truth tables show ALL input-output combinations
- 2^n rows for n input variables
- Use binary counting for input combinations
- SOP: OR of minterms where output = 1
- POS: AND of maxterms where output = 0
- Foundation for logic design and minimization
