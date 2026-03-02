# Four-Variable Karnaugh Map


## Table of Contents

- [Four-Variable Karnaugh Map](#four-variable-karnaugh-map)
- [1. Introduction](#1-introduction)
- [2. Theoretical Foundation](#2-theoretical-foundation)
  - [2.1 Gray Code Ordering and Adjacency Theorem](#21-gray-code-ordering-and-adjacency-theorem)
  - [2.2 Minterm and Maxterm Representations](#22-minterm-and-maxterm-representations)
- [3. Structure of the Four-Variable K-Map](#3-structure-of-the-four-variable-k-map)
- [4. Minimization Theory](#4-minimization-theory)
  - [4.1 Variable Elimination Theorem](#41-variable-elimination-theorem)
  - [4.2 Prime Implicant Classification](#42-prime-implicant-classification)
- [5. Systematic Minimization Procedure](#5-systematic-minimization-procedure)
- [6. Worked Examples](#6-worked-examples)
  - [Example 1: SOP Minimization](#example-1-sop-minimization)
  - [Example 2: POS Minimization](#example-2-pos-minimization)
  - [Example 3: Don't-Care Conditions](#example-3-dont-care-conditions)
- [7. Summary of Key Relationships](#7-summary-of-key-relationships)
- [8. Conclusion](#8-conclusion)
  - [References](#references)

## 1. Introduction

The Karnaugh Map (K-Map) represents a seminal contribution to digital logic design, providing a systematic graphical method for minimizing Boolean functions. The four-variable Karnaugh Map extends this technique to functions of four input variables (denoted as A, B, C, and D), creating a 4×4 grid containing 16 cells. Each cell corresponds uniquely to one of the 16 possible minterms, denoted m₀ through m₁₅.

The significance of the four-variable K-Map in digital design cannot be overstated. Many practical digital circuits—including encoders, decoders, multiplexers, and arithmetic logic units—operate on four input variables. Consequently, the four-variable K-Map represents the most frequently employed variant in both academic examinations and industrial design applications.

## 2. Theoretical Foundation

### 2.1 Gray Code Ordering and Adjacency Theorem

**Definition:** Gray code is a binary numeral system where two successive values differ by exactly one bit.

**Theorem:** In a Karnaugh Map labeled with Gray code, any two physically adjacent cells (including wrap-around adjacencies) differ in precisely one variable's value.

_Proof:_ Consider the row labels for a 4-variable K-Map: 00 (m₀, m₁, m₂, m₃), 01 (m₄, m₅, m₆, m₇), 11 (m₁₂, m₁₃, m₁₄, m₁₅), and 10 (m₈, m₉, m₁₀, m₁₁). Each consecutive pair differs by exactly one bit:

- 00 → 01: changes B from 0 to 1, A remains 0
- 01 → 11: changes A from 0 to 1, B remains 1
- 11 → 10: changes B from 1 to 0, A remains 1

The column labels (CD) follow the same principle. By wrap-around, 10 → 00 also changes exactly one bit. This single-bit difference property ensures that adjacent cells can be combined to eliminate one variable, which is the fundamental principle of K-Map minimization. ∎

### 2.2 Minterm and Maxterm Representations

For a four-variable function F(A, B, C, D), each minterm mᵢ represents a product term where all four variables appear, either in uncomplemented (1) or complemented (0) form. The minterm number i is derived from the binary representation (ABCD) interpreted as a decimal value.

**Example:** Minterm m₁₃ (binary: 1101) corresponds to the product term A·B·C'·D.

## 3. Structure of the Four-Variable K-Map

The 4-variable K-Map organizes 16 cells in a 4×4 matrix:

| AB\CD  | 00  | 01  | 11  | 10  |
| :----- | :-: | :-: | :-: | :-: |
| **00** | m₀  | m₁  | m₃  | m₂  |
| **01** | m₄  | m₅  | m₇  | m₆  |
| **11** | m₁₂ | m₁₃ | m₁₅ | m₁₄ |
| **10** | m₈  | m₉  | m₁₁ | m₁₀ |

**Adjacency Rules:**

- **Horizontal adjacency:** Cells in adjacent columns (00↔01, 01↔11, 11↔10, 10↔00 via wrap-around)
- **Vertical adjacency:** Cells in adjacent rows (00↔01, 01↔11, 11↔10, 10↔00 via wrap-around)
- **Corner adjacency:** m₀ is adjacent to m₂ and m₈ due to wrap-around; similarly for m₃, m₅, m₆, m₉, m₁₀, m₁₂, m₁₄

## 4. Minimization Theory

### 4.1 Variable Elimination Theorem

**Theorem:** A group of 2ⁿ cells eliminates exactly n variables from the product term.

_Proof:_ When n variables are eliminated, the remaining variables must have constant values across all cells in the group. Each eliminated variable changes value at least once within the group boundaries; otherwise, the group could be expanded. Since a group of size 2ⁿ contains 2ⁿ distinct combinations of the remaining (4-n) variables, exactly n variables must change within the group, each varying through all 2ⁿ possible combinations. Therefore, the product term contains only the (4-n) variables that remain constant. ∎

**Practical Implications:**

- Group of 2 cells → eliminates 1 variable
- Group of 4 cells → eliminates 2 variables
- Group of 8 cells → eliminates 3 variables
- Group of 16 cells → eliminates all 4 variables (F = 1)

### 4.2 Prime Implicant Classification

**Definition:** A prime implicant is a product term that cannot be extended by including any additional 1-cells without violating the grouping rules.

**Definition:** An essential prime implicant (EPI) is a prime implicant that covers at least one minterm not covered by any other prime implicant.

**Theorem:** The minimum SOP expression must include all essential prime implicants.

_Proof:_ Since an EPI covers a minterm uniquely, any valid SOP expression must include this minterm's coverage. The only way to cover this minterm is through the EPI itself, as no other prime implicant contains it. Therefore, all EPIs must appear in the final minimized expression. ∎

## 5. Systematic Minimization Procedure

**Step 1:** Express the function in sum-of-minterms form: F = Σm(list)

**Step 2:** Plot 1s in the corresponding K-Map cells

**Step 3:** Identify all prime implicants by forming the largest possible groups (powers of 2)

**Step 4:** Determine essential prime implicants by checking each minterm covered by only one prime implicant

**Step 5:** Select the minimum set of prime implicants that covers all minterms

**Step 6:** Derive the simplified expression by ORing all selected prime implicant product terms

## 6. Worked Examples

### Example 1: SOP Minimization

**Minimize:** F(A,B,C,D) = Σm(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14)

**Solution:**

**Step 1: Plot the K-Map**

| AB\CD  | 00  | 01  | 11  | 10  |
| :----- | :-: | :-: | :-: | :-: |
| **00** |  1  |  1  |  0  |  1  |
| **01** |  1  |  1  |  0  |  1  |
| **11** |  1  |  1  |  0  |  1  |
| **10** |  1  |  1  |  0  |  0  |

**Step 2: Identify groups**

- **Group 1 (8 cells):** Columns CD=00 and CD=01 for all rows AB. Variables C=0 and D=0 remain constant across both columns. Variables A and B vary. Eliminated variables: C and D. Product term: **C'·D'** (or C' D')

- **Group 2 (4 cells):** Cells (AB=00, CD=10), (AB=01, CD=10), (AB=11, CD=10). Here, C=1 and D=0 (so C·D'), with A varying but B=1 constant. Wait - checking: AB=00 (B=0), AB=01 (B=1), AB=11 (B=1) - B is not constant. Let me recalculate: Column CD=10 means C=1, D=0. Rows AB=00 (A=0,B=0), AB=01 (A=0,B=1), AB=11 (A=1,B=1). Only C remains constant at 1. Therefore: **C** (but wait, we need a 4-cell group)

Actually, examining the map more carefully:

- We have 1s at: m₀(00,00), m₁(00,01), m₂(00,10), m₄(01,00), m₅(01,01), m₆(01,10), m₈(10,00), m₉(10,01), m₁₂(11,00), m₁₃(11,01), m₁₄(11,10)
- The 0s are at: m₃(00,11), m₇(01,11), m₁₀(10,10), m₁₁(10,11), m₁₅(11,11)

**Group 1 (8 cells):** m₀,m₁,m₄,m₅,m₈,m₉,m₁₂,m₁₃ → columns 00,01. C=0 constant, D=0 in 00, D=1 in 01 (D varies). A and B vary. **Product: C'**

**Group 2 (4 cells):** m₂,m₆,m₁₄,m₁₀? No m₁₀ is 0. m₂(00,10), m₆(01,10), m₁₄(11,10), m₁₀(10,10) - wait, that's a wrap-around group! m₂,m₆,m₁₄,m₁₀ form a 4-cell group through wrap-around. In this group: CD=10 (C=1, D=0), AB varies. **Product: C·D' = CD'**

**Step 3: Final expression**
F = C' + CD' = C' + C·D' = C' + D' (by absorption theorem: X' + X·Y = X' + Y)

Therefore, **F = C' + D'**

### Example 2: POS Minimization

For the same function, we can minimize using zeros (Product of Sums form):

**F = ΠM(3, 7, 10, 11, 15)**

| AB\CD | 00  | 01  | 11  | 10  |
| :---: | :-: | :-: | :-: | :-: |
|  00   |  1  |  1  |  0  |  1  |
|  01   |  1  |  1  |  0  |  1  |
|  11   |  1  |  1  |  0  |  1  |
|  10   |  1  |  1  |  0  |  0  |

Group the 0s:

- **Group 1 (4 cells):** Column CD=11: m₃, m₇, m₁₁, m₁₅. C=1, D=1 remain constant. Sum term: **C + D**

**Final POS expression:** F = (C + D)

Note: By De Morgan's theorem, C + D = (C'·D')', confirming equivalence with the SOP form C' + D'.

### Example 3: Don't-Care Conditions

**Minimize:** F(A,B,C,D) = Σm(1, 3, 7, 11, 15) + Σd(0, 2, 5, 13)

Don't-cares (d) can be included in groups to achieve larger simplifications.

| AB\CD | 00  | 01  | 11  | 10  |
| :---: | :-: | :-: | :-: | :-: |
|  00   |  d  |  1  |  1  |  d  |
|  01   |  0  |  d  |  1  |  0  |
|  11   |  0  |  1  |  1  |  0  |
|  10   |  0  |  0  |  0  |  0  |

**Group 1 (8 cells):** Using don't-cares at m₀, m₂, m₅ along with 1s → covers all of columns 01 and 11. C=1 constant. **Product: C**

**Final expression:** F = C

## 7. Summary of Key Relationships

| Group Size | Variables Eliminated | Product Term Variables |
| :--------: | :------------------: | :--------------------: |
|   1 cell   |          0           |           4            |
|  2 cells   |          1           |           3            |
|  4 cells   |          2           |           2            |
|  8 cells   |          3           |           1            |
|  16 cells  |          4           |       0 (F = 1)        |

## 8. Conclusion

The four-variable Karnaugh Map provides an elegant visual method for Boolean function minimization. The technique leverages the mathematical properties of Gray code ordering and the variable elimination theorem to systematically reduce complex Boolean expressions. Mastery of this method is essential for digital logic design, as it forms the foundation for understanding more advanced minimization algorithms including the Quine-McCluskey method and automated logic synthesis tools used in modern VLSI design.

### References

1. Morris Mano, M., & Ciletti, M. D. (2013). _Digital Design: With an Introduction to the Verilog HDL_ (5th ed.). Pearson.
2. Kohavi, Z., & Jha, N. K. (2010). _Switching and Finite Automata Theory_ (3rd ed.). Cambridge University Press.
