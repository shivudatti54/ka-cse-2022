# Propositional Logic Equivalences

## Introduction

Propositional logic equivalences form the backbone of logical reasoning in computer science and mathematics. In our previous studies, we learned that propositions are statements that are either true or false. Now, we explore when two propositions share the same truth value under all possible circumstances—this fundamental concept is known as logical equivalence.

Logical equivalence is not merely an academic exercise; it has profound practical applications. In digital circuit design, engineers use logical equivalences to simplify boolean expressions, reducing the number of gates required and minimizing power consumption. In programming, understanding equivalences helps in writing cleaner conditional statements and optimizing code. In database systems, query optimization relies on applying logical equivalences to transform queries into more efficient forms. For competitive examinations like those at DU, this topic frequently appears as both direct questions and as essential background for more complex logical reasoning problems.

This module explores the three categories of propositions—tautologies, contradictions, and contingencies—before diving into the fundamental equivalence laws and their applications in proof techniques.

## Key Concepts

### Tautology, Contradiction, and Contingency

Every proposition falls into one of three categories based on its truth value:

A **tautology** is a proposition that is always true, regardless of the truth values of its component propositions. For example, "It will rain tomorrow or it will not rain tomorrow" is a tautology because one of the two statements must always be true. We denote a tautology by the symbol **T** or simply write the proposition is a tautology.

A **contradiction** (or absurdity) is the opposite of a tautology—it is always false. "It is raining and it is not raining" is a contradiction because both statements cannot simultaneously hold true. We denote a contradiction by **F** or say the proposition is a contradiction.

A **contingency** (or satisfiable proposition) is a proposition whose truth value depends on the truth values of its components. Most compound propositions we encounter are contingencies. For instance, "It is raining" is a contingency because its truth varies.

### Logical Equivalence

Two propositions P and Q are **logically equivalent**, written P ≡ Q (or P ↔ Q is a tautology), if they have identical truth values under all possible interpretations. This means that in every row of their combined truth table, P and Q have the same truth value.

The biconditional connective (P ↔ Q) expresses logical equivalence. When P ≡ Q, the biconditional P ↔ Q becomes a tautology. This is the formal definition we use throughout our study.

### Fundamental Logical Equivalences

The following table presents the essential logical equivalences organized by their logical purpose. These laws are provable through truth tables and form the foundation for algebraic proof techniques.

**Identity Laws:**
- P ∧ T ≡ P
- P ∨ F ≡ P

**Domination Laws:**
- P ∨ T ≡ T
- P ∧ F ≡ F

**Idempotent Laws:**
- P ∧ P ≡ P
- P ∨ P ≡ P

**Complement Laws:**
- P ∧ ¬P ≡ F
- P ∨ ¬P ≡ T
- ¬T ≡ F
- ¬F ≡ T

**Double Negation Law:**
- ¬(¬P) ≡ P

**Commutative Laws:**
- P ∧ Q ≡ Q ∧ P
- P ∨ Q ≡ Q ∨ P

**Associative Laws:**
- (P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R)
- (P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R)

**Distributive Laws:**
- P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)
- P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)

**De Morgan's Laws:**
- ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
- ¬(P ∨ Q) ≡ ¬P ∧ ¬Q

**Absorption Laws:**
- P ∧ (P ∨ Q) ≡ P
- P ∨ (P ∧ Q) ≡ P

### Proving Logical Equivalences

We can establish logical equivalences using two primary methods:

**Truth Table Method:** Construct a truth table for both propositions and compare their truth values in each row. If they match in every row, they are logically equivalent.

**Algebraic Proof Method:** Start with one proposition and systematically transform it using known equivalences until we arrive at the other proposition. This method is particularly valuable when truth tables become unwieldy (as with many variables).

## Examples

### Example 1: Proving Distributive Law Using Truth Table

**Problem:** Prove that P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)

**Solution:** We construct a truth table with columns for P, Q, R, Q ∨ R, P ∧ (Q ∨ R), P ∧ Q, P ∧ R, and (P ∧ Q) ∨ (P ∧ R):

| P | Q | R | Q ∨ R | P ∧ (Q ∨ R) | P ∧ Q | P ∧ R | (P ∧ Q) ∨ (P ∧ R) |
|---|---|---|-------|-------------|-------|-------|-------------------|
| T | T | T | T     | T           | T     | T     | T                 |
| T | T | F | T     | T           | T     | F     | T                 |
| T | F | T | T     | T           | F     | T     | T                 |
| T | F | F | F     | F           | F     | F     | F                 |
| F | T | T | T     | F           | F     | F     | F                 |
| F | T | F | T     | F           | F     | F     | F                 |
| F | F | T | T     | F           | F     | F     | F                 |
| F | F | F | F     | F           | F     | F     | F                 |

Since columns 5 and 8 are identical in all rows, the equivalence holds.

### Example 2: Simplifying a Complex Proposition

**Problem:** Show that (P ∨ Q) ∧ ¬P simplifies to P ∧ Q

**Solution using algebraic method:**

```
(P ∨ Q) ∧ ¬P
≡ (¬P ∧ P) ∨ (¬P ∧ Q)     [Distributive Law]
≡ F ∨ (¬P ∧ Q)            [Complement Law: ¬P ∧ P ≡ F]
≡ ¬P ∧ Q                  [Identity Law: F ∨ X ≡ X]
```

Wait, let me recalculate—this gives us ¬P ∧ Q, not P ∧ Q. Let me verify the original claim by truth table:

Looking at the truth table, (P ∨ Q) ∧ ¬P is true only when P is false and Q is true, which is exactly ¬P ∧ Q. The original claim that it equals P ∧ Q was incorrect—it actually equals ¬P ∧ Q.

### Example 3: Application in Digital Circuits

**Problem:** Simplify the boolean expression for an OR gate fed by the outputs of two AND gates: (A ∧ B) ∨ (A ∧ C)

**Solution:** Using the distributive law in reverse (factoring):

```
(A ∧ B) ∨ (A ∧ C)
≡ A ∧ (B ∨ C)          [Distributive Law reversed]
```

This simplification reduces two AND gates and one OR gate to just one AND gate and one OR gate, significantly reducing circuit complexity.

## Exam Tips

1. **Identify the question type first:** Determine whether you need to use truth tables, algebraic manipulation, or both. Truth tables work well for 2-3 variables; algebraic method is better for complex expressions.

2. **Memorize the fundamental equivalences:** The 10-12 core laws (identity, domination, idempotent, complement, double negation, commutative, associative, distributive, De Morgan's, absorption) form your toolkit for algebraic proofs.

3. **Apply De Morgan's Laws carefully:** Remember that negation distributes over conjunction and disjunction but flips the connective. The negation of "P and Q" becomes "not P or not Q."

4. **Distinguish between ↔ and ≡:** The biconditional (↔) is a connective that creates a compound proposition. Logical equivalence (≡) is a relationship between two propositions. Write P ≡ Q (not P ↔ Q) to indicate equivalence.

5. **Check boundary cases:** When using truth tables, ensure you include all combinations—2^n rows for n variables. Missing rows lead to incorrect conclusions.

6. **Use the contrapositive strategically:** Remember that P → Q ≡ ¬Q → ¬P. This equivalence is frequently useful in logical proofs.

7. **Simplify step-by-step in algebraic proofs:** Write each transformation on a new line, citing the law used. This demonstrates understanding and makes error identification easier for examiners.

8. **Remember the order of operations:** In the absence of parentheses, ¬ has highest priority, then ∧, then ∨, then →, then ↔.