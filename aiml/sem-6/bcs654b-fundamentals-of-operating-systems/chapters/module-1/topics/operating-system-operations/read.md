# Boolean Operations

## What is Boolean Algebra?

Boolean algebra is a branch of mathematics that deals with variables that have two possible values: **true (1)** and **false (0)**. It was developed by George Boole in 1854 and forms the mathematical foundation for digital circuit design and computer science.

## Fundamental Boolean Operations

There are three fundamental operations in Boolean algebra:

### 1. AND Operation (Conjunction)

The AND operation outputs **1** only when **all inputs are 1**.

**Notation:** A AND B = A.B = A \* B = AB

| A   | B   | A AND B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |

**Analogy:** Two switches in series - both must be ON for current to flow.

### 2. OR Operation (Disjunction)

The OR operation outputs **1** when **at least one input is 1**.

**Notation:** A OR B = A + B

| A   | B   | A OR B |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |

**Analogy:** Two switches in parallel - either one ON allows current to flow.

### 3. NOT Operation (Negation/Complement)

The NOT operation **inverts** the input.

**Notation:** NOT A = A' = A-bar = ~A

| A   | NOT A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

**Analogy:** A normally-closed switch - when pressed (1), it opens and blocks current.

## Derived Operations

### XOR (Exclusive OR)

Outputs **1** when inputs are **different**.

**Notation:** A XOR B = A ^ B

| A   | B   | A XOR B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

**Expression:** A XOR B = A'B + AB'

### XNOR (Exclusive NOR)

Outputs **1** when inputs are **same**.

**Notation:** A XNOR B = (A XOR B)'

| A   | B   | A XNOR B |
| --- | --- | -------- |
| 0   | 0   | 1        |
| 0   | 1   | 0        |
| 1   | 0   | 0        |
| 1   | 1   | 1        |

**Expression:** A XNOR B = AB + A'B'

### NAND (NOT AND)

**Notation:** A NAND B = (A.B)'

### NOR (NOT OR)

**Notation:** A NOR B = (A + B)'

## Operator Precedence

The order of operations in Boolean algebra (highest to lowest):

1. **Parentheses** ()
2. **NOT** (complement)
3. **AND** (conjunction)
4. **OR** (disjunction)

**Example:** A + B.C' = A + (B.(C'))

## Properties of Boolean Operations

| Property    | AND               | OR                |
| ----------- | ----------------- | ----------------- |
| Commutative | A.B = B.A         | A+B = B+A         |
| Associative | (A.B).C = A.(B.C) | (A+B)+C = A+(B+C) |
| Identity    | A.1 = A           | A+0 = A           |
| Null        | A.0 = 0           | A+1 = 1           |
| Idempotent  | A.A = A           | A+A = A           |
| Complement  | A.A' = 0          | A+A' = 1          |

## Summary

- Boolean algebra uses only two values: 0 and 1
- Three fundamental operations: AND, OR, NOT
- AND = multiplication-like behavior (all inputs must be 1)
- OR = addition-like behavior (any input can be 1)
- NOT = inversion (flips the value)
- Derived operations: XOR, XNOR, NAND, NOR
- Operator precedence: Parentheses > NOT > AND > OR
