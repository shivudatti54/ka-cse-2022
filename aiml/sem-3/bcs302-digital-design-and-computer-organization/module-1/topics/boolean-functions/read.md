# Boolean Functions


## Table of Contents

- [Boolean Functions](#boolean-functions)
- [1. Introduction and Fundamental Concepts](#1-introduction-and-fundamental-concepts)
- [2. Formal Definition](#2-formal-definition)
- [3. Representations of Boolean Functions](#3-representations-of-boolean-functions)
  - [3.1 Truth Table Representation](#31-truth-table-representation)
  - [3.2 Boolean Expression](#32-boolean-expression)
  - [3.3 Logic Circuit Diagram](#33-logic-circuit-diagram)
- [4. Canonical Forms](#4-canonical-forms)
  - [4.1 Minterms (Canonical SOP)](#41-minterms-canonical-sop)
  - [4.2 Maxterms (Canonical POS)](#42-maxterms-canonical-pos)
  - [4.3 Relationship Between Minterms and Maxterms](#43-relationship-between-minterms-and-maxterms)
- [5. Standard Forms vs. Canonical Forms](#5-standard-forms-vs-canonical-forms)
- [6. Boolean Function Simplification](#6-boolean-function-simplification)
  - [6.1 Algebraic Simplification Using Boolean Theorems](#61-algebraic-simplification-using-boolean-theorems)
  - [6.2 Karnaugh Map (K-Map) Method](#62-karnaugh-map-k-map-method)
  - [6.3 Quine-McCluskey Method](#63-quine-mccluskey-method)
- [7. Complement of a Boolean Function](#7-complement-of-a-boolean-function)
  - [7.1 Methods for Finding Complement](#71-methods-for-finding-complement)
- [8. Don't Care Conditions](#8-dont-care-conditions)
- [9. Functional Completeness](#9-functional-completeness)
  - [NAND/NOR Implementation](#nandnor-implementation)
- [10. Duality Principle](#10-duality-principle)
- [11. Applications](#11-applications)

## 1. Introduction and Fundamental Concepts

A Boolean function is a mathematical function that maps binary inputs to a binary output, defined using the operations of Boolean algebra: AND (·), OR (+), and NOT ('). The study of Boolean functions forms the cornerstone of digital logic design, providing the theoretical foundation for analyzing and synthesizing combinational circuits. Every digital system, from simple calculators to complex processors, ultimately implements Boolean functions through networks of logic gates. The theory of Boolean functions enables engineers to optimize hardware implementations, minimize circuit complexity, and ensure reliable operation of digital systems.

## 2. Formal Definition

A Boolean function of n variables is formally defined as a mapping:

**f: {0,1}ⁿ → {0,1}**

Where f takes n binary inputs (x₁, x₂, ..., xₙ) from the set {0,1}ⁿ and produces a single binary output. The total number of possible Boolean functions of n variables is 2^(2ⁿ), as there are 2ⁿ possible input combinations and 2 choices for the output for each combination.

**Example:**

- F(x, y, z) = xy + x'z represents a Boolean function of 3 variables that evaluates to 1 when either (x AND y) is true, or (x' AND z) is true.

## 3. Representations of Boolean Functions

Boolean functions admit multiple but equivalent representations, each suited to different analytical and design purposes.

### 3.1 Truth Table Representation

A truth table enumerates all 2ⁿ possible input combinations and their corresponding output values. This exhaustive listing provides complete specification of the function's behavior.

**Example: F(A, B, C) = A'BC + AB'C + ABC**

| A   | B   | C   | F   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |

### 3.2 Boolean Expression

An algebraic expression using Boolean operators. Two standard forms exist:

- **Sum of Products (SOP):** Disjunction (OR) of conjunction (AND) terms
- **Product of Sums (POS):** Conjunction (AND) of disjunction (OR) terms

**Example:**

- SOP: F = AB + A'C + BC
- POS: F = (A+B)(A'+C)(B+C)

### 3.3 Logic Circuit Diagram

A graphical representation using logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR) that physically implements the Boolean function.

## 4. Canonical Forms

Canonical forms are standardized representations that uniquely define a Boolean function, with each term containing all n variables either in complemented or uncomplemented form.

### 4.1 Minterms (Canonical SOP)

A minterm (denoted mᵢ) is a product term containing all n variables, where each variable appears exactly once either complemented (if corresponding bit is 0) or uncomplemented (if corresponding bit is 1). Each minterm evaluates to 1 for exactly one input combination.

**For 3 variables (A, B, C):**

| Index | Binary | Minterm |
| ----- | ------ | ------- |
| m₀    | 000    | A'B'C'  |
| m₁    | 001    | A'B'C   |
| m₂    | 010    | A'BC'   |
| m₃    | 011    | A'BC    |
| m₄    | 100    | AB'C'   |
| m₅    | 101    | AB'C    |
| m₆    | 110    | ABC'    |
| m₇    | 111    | ABC     |

**Theorem:** Any Boolean function can be uniquely expressed as the sum (OR) of minterms corresponding to rows where the output is 1.

**Proof:** Consider the truth table representation. For each input combination where F = 1, we construct a product term that is true ONLY for that specific combination. This is achieved by including each variable uncomplemented if it is 1 in that row, and complemented if it is 0. Taking the OR of all such terms ensures F = 1 whenever at least one minterm is true, and F = 0 otherwise. ∎

**Example:** If F(A,B,C) = 1 for indices 3, 5, and 7:

- F = m₃ + m₅ + m₇ = A'BC + AB'C + ABC = Σ(3, 5, 7)

### 4.2 Maxterms (Canonical POS)

A maxterm (denoted Mᵢ) is a sum term containing all n variables, where each variable appears exactly once. Each maxterm evaluates to 0 for exactly one input combination.

**For 3 variables (A, B, C):**

| Index | Binary | Maxterm  |
| ----- | ------ | -------- |
| M₀    | 000    | A+B+C    |
| M₁    | 001    | A+B+C'   |
| M₂    | 010    | A+B'+C   |
| M₃    | 011    | A+B'+C'  |
| M₄    | 100    | A'+B+C   |
| M₅    | 101    | A'+B+C'  |
| M₆    | 110    | A'+B'+C  |
| M₇    | 111    | A'+B'+C' |

**Theorem:** Any Boolean function can be uniquely expressed as the product (AND) of maxterms corresponding to rows where the output is 0.

**Proof:** Dual to the minterm proof. For each input combination where F = 0, construct a sum term that is false ONLY for that specific combination. Including each variable uncomplemented if it is 0, and complemented if it is 1, ensures the maxterm evaluates to 0 for exactly one input. Taking the AND of all such maxterms ensures F = 0 whenever at least one maxterm is false, and F = 1 otherwise. ∎

**Example:** If F(A,B,C) = 0 for indices 0, 2, 4, 6:

- F = M₀ · M₂ · M₄ · M₆ = (A+B+C)(A+B'+C)(A'+B+C)(A'+B'+C) = Π(0, 2, 4, 6)

### 4.3 Relationship Between Minterms and Maxterms

For n variables, the following relationship holds:

**mᵢ = Mᵢ'** (each minterm is the complement of the corresponding maxterm)

If F = Σ(minterm indices), then F' = Σ(other indices), and equivalently F = Π(complement of other indices).

**Conversion Formula:**
If F = Σ(m₁, m₂, ..., mₖ), then F = Π(Mⱼ for all j ∉ {m₁, m₂, ..., mₖ})

**Example:** Given F = Σ(1, 3, 5), find POS form:

- Total indices: {0,1,2,3,4,5,6,7}
- Missing indices: {0,2,4,6,7}
- F = Π(0, 2, 4, 6, 7)

## 5. Standard Forms vs. Canonical Forms

**Standard Forms** are simplified expressions that may not contain all variables in every term. They result from applying Boolean algebra simplification.

**Canonical Forms** are unique, un-simplified representations where every term contains all variables.

**Example:**

- Standard SOP: F = A + BC (simplified)
- Canonical SOP: F = A'B'C + A'BC + AB'C + ABC + AB'C' (not simplified)

## 6. Boolean Function Simplification

Minimizing Boolean functions reduces the number of gates and connections required for hardware implementation, decreasing cost, propagation delay, and power consumption.

### 6.1 Algebraic Simplification Using Boolean Theorems

Key theorems employed include:

| Theorem      | SOP Form                  | POS Form                  |
| ------------ | ------------------------- | ------------------------- |
| Identity     | A + 0 = A                 | A · 1 = A                 |
| Null         | A + 1 = 1                 | A · 0 = 0                 |
| Idempotent   | A + A = A                 | A · A = A                 |
| Complement   | A + A' = 1                | A · A' = 0                |
| Commutative  | A + B = B + A             | A · B = B · A             |
| Associative  | (A + B) + C = A + (B + C) | (A · B) · C = A · (B · C) |
| Distributive | A + BC = (A + B)(A + C)   | A · (B + C) = AB + AC     |
| Absorption   | A + AB = A                | A(A + B) = A              |
| De Morgan's  | (A + B)' = A' · B'        | (A · B)' = A' + B'        |

**Proof of Consensus Theorem: AB + A'C + BC = AB + A'C**

The consensus term BC is redundant. Proof:

```
AB + A'C + BC
= AB + A'C + BC(1)
= AB + A'C + BC(A + A')
= AB + A'C + ABC + A'BC
= AB(1 + C) + A'C(1 + B)
= AB + A'C
```

Thus, BC is the consensus term and can be eliminated. ∎

**Example 1: Simplify F = x'y'z + x'yz + xy'**

```
Step 1: F = x'z(y' + y) + xy'
Step 2: Apply Complement Law (y' + y = 1): F = x'z(1) + xy'
Step 3: Apply Identity Law: F = x'z + xy'
```

**Example 2: Simplify F = AB + A'C + BC**

```
Using consensus theorem:
F = AB + A'C + BC
Since BC is consensus of AB and A'C, BC is redundant
F = AB + A'C
```

### 6.2 Karnaugh Map (K-Map) Method

Karnaugh maps provide a systematic graphical method for minimizing Boolean functions by grouping adjacent 1s (for SOP) or 0s (for POS).

**Properties:**

- Adjacent cells differ in only one variable
- Groups must be powers of 2 (1, 2, 4, 8, ...)
- Groups can wrap around edges
- Larger groups yield simpler terms

**Example: Simplify F(A,B,C,D) = Σ(0,1,2,4,5,6,8,9,10,12,13,14)**

Using K-map with groups of 8 and 4:

- Group of 8 covers indices 0,1,2,4,5,6,8,9,10,12,13,14 → term = B' (B is 0 in all cells)
- Group of 4 covers indices 2,6,10,14 → term = D'
- Simplified: F = B' + D'

### 6.3 Quine-McCluskey Method

A tabular method suitable for functions with more than 4 variables, providing systematic minimization through iterative combination of minterms.

## 7. Complement of a Boolean Function

The complement F' of a Boolean function F is obtained by inverting all output values in the truth table.

### 7.1 Methods for Finding Complement

**Method 1: Using De Morgan's Theorems**

Apply De Morgan's laws iteratively to complement the entire expression.

**Example:** If F = AB + C', find F'

```
F' = (AB + C')'
 = (AB)' · (C')' [De Morgan's]
 = (A' + B') · C [De Morgan's on AB, Double complement]
 = (A' + B')C
```

**Method 2: From Truth Table**
List all input combinations where original F = 0, then express as sum of minterms.

**Method 3: Dual and Complement**
Take the dual of F, then complement each literal.

## 8. Don't Care Conditions

In practical digital systems, certain input combinations either never occur or have unspecified output requirements. These are represented as 'X' or 'd' (don't care).

Don't care conditions can be treated as either 0 or 1 during minimization to achieve maximum simplification.

**Example:** F(A,B,C,D) = Σ(1,3,7,11,15) + d(0,2,5)

By treating don't care terms appropriately:

- Include d(0) as 1 to form larger group → simplifies to F = AD + B'C

## 9. Functional Completeness

A set of gates is functionally complete if any Boolean function can be implemented using only gates from that set.

**Theorem:** {AND, OR, NOT} is functionally complete.

**Proof:** Any Boolean function can be expressed in SOP or POS form using AND, OR, and NOT operations. Since these can be directly implemented with AND, OR, and NOT gates, the set is functionally complete. ∎

**Other Complete Sets:**

- {NAND} - Universal gate
- {NOR} - Universal gate
- {AND, NOT}
- {OR, NOT}

### NAND/NOR Implementation

Any Boolean function can be implemented using only NAND gates (or only NOR gates).

**Example: Implement F = AB + C using only NAND gates**

```
F = AB + C
 = ((AB)')' + C
 = ((AB)' · C')' [Using De Morgan]
```

## 10. Duality Principle

The duality principle states that for every Boolean identity, its dual obtained by swapping AND (·) with OR (+) and 0 with 1 (without complementing variables) is also valid.

**Example:**

- Original: A + 0 = A
- Dual: A · 1 = A

**Proof:** Both SOP and POS forms of Boolean algebra satisfy identical postulates (commutative, associative, distributive). By substituting + with · and 0 with 1 (and vice versa), valid identities remain valid. ∎

## 11. Applications

Boolean functions are essential in:

- **Combinational Logic Design:** Adders, subtractors, multiplexers, decoders, encoders
- **Arithmetic Logic Units (ALUs):** Implementing arithmetic operations
- **Memory Systems:** Address decoders, read/write control logic
- **Error Detection:** Parity generators, checkers, Hamming code circuits
- **Control Systems:** State machine output functions

---

**End of Unit 1: Boolean Functions**
