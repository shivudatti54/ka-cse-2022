# Quantifiers: Definitions and Proofs of Theorems

## Table of Contents

- [Quantifiers: Definitions and Proofs of Theorems](#quantifiers-definitions-and-proofs-of-theorems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Predicates and Propositional Functions](#predicates-and-propositional-functions)
  - [Universal Quantifier (∀)](#universal-quantifier-)
  - [Existential Quantifier (∃)](#existential-quantifier-)
  - [Negation of Quantified Statements](#negation-of-quantified-statements)
  - [Multiple Quantifiers](#multiple-quantifiers)
  - [Bound and Free Variables](#bound-and-free-variables)
- [Examples](#examples)
  - [Example 1: Negating a Universally Quantified Statement](#example-1-negating-a-universally-quantified-statement)
  - [Example 2: Translating Mathematical Statements](#example-2-translating-mathematical-statements)
  - [Example 3: Proof with Multiple Quantifiers](#example-3-proof-with-multiple-quantifiers)
- [Exam Tips](#exam-tips)

## Introduction

Quantifiers are fundamental constructs in mathematical logic that allow us to express statements about collections of objects rather than individual elements. In discrete mathematics and computer science, quantifiers serve as the backbone for formal specification, program verification, and mathematical reasoning. The two primary quantifiers—the universal quantifier (∀) and the existential quantifier (∃)—enable us to make precise statements about all elements or the existence of specific elements within a domain.

Understanding quantifiers is essential for any computer science student because they appear prominently in database query languages (like SQL), formal methods, algorithm analysis, and the foundations of mathematical proofs. This topic forms the bridge between simple propositional logic and the more powerful predicate logic, which is indispensable for rigorous reasoning in computer science.

## Key Concepts

### Predicates and Propositional Functions

A predicate (or propositional function) is a statement containing variables that becomes a proposition (true or false) when specific values are substituted for those variables. We typically denote a predicate by P(x), Q(x,y), or similar notation, where x, y are variables.

For example:

- P(x): "x is an even number"
- Q(x, y): "x + y = 10"
- R(x): "x > 0"

The domain (or universe) of a predicate is the set of all possible values that variables can take.

### Universal Quantifier (∀)

The universal quantifier ∀x P(x) states that "for all x, P(x) is true" or "for every x, P(x) holds." This means P(x) must be true for every element x in the domain.

**Formal Definition:**
∀x P(x) is true if and only if P(a) is true for every element a in the domain.

**Examples:**

- ∀x (x + 0 = x) — for all integers x, adding zero gives x
- ∀x (x² ≥ 0) — for all real numbers x, x squared is nonnegative

### Existential Quantifier (∃)

The existential quantifier ∃x P(x) states that "there exists an x such that P(x) is true" or "there is at least one x for which P(x) holds."

**Formal Definition:**
∃x P(x) is true if and only if there exists at least one element a in the domain such that P(a) is true.

**Examples:**

- ∃x (x² = 4) — there exists a number whose square is 4
- ∃x (x is a prime number) — there exists at least one prime number

### Negation of Quantified Statements

One of the most important theorems in predicate logic concerns the negation of quantified statements:

**Theorem 1: Negation of Universal Quantifier**
¬∀x P(x) ≡ ∃x ¬P(x)

The negation of "for all x, P(x)" is equivalent to "there exists an x such that not P(x)."

**Theorem 2: Negation of Existential Quantifier**
¬∃x P(x) ≡ ∀x ¬P(x)

The negation of "there exists an x such that P(x)" is equivalent to "for all x, not P(x)."

**Proof of Theorem 1:**
We prove that ¬∀x P(x) and ∃x ¬P(x) have the same truth value.

- (→) Assume ¬∀x P(x) is true. This means it is not the case that P(x) is true for every x in the domain. Therefore, there must exist at least one element a in the domain for which P(a) is false, i.e., ¬P(a) is true. Hence, ∃x ¬P(x) is true.

- (←) Assume ∃x ¬P(x) is true. Then there exists some a in the domain such that ¬P(a) is true, meaning P(a) is false. Since P(x) is not true for all elements (specifically, it's false for a), ¬∀x P(x) is true.

Thus, ¬∀x P(x) ≡ ∃x ¬P(x).

### Multiple Quantifiers

When predicates contain multiple variables, we use multiple quantifiers. The order of quantifiers critically affects the meaning of the statement.

**Common patterns:**

1. **∀x ∀y P(x, y)** — "for all x and for all y, P(x, y)"
2. **∃x ∃y P(x, y)** — "there exist x and y such that P(x, y)"
3. **∀x ∃y P(x, y)** — "for every x, there exists a y such that P(x, y)"
4. **∃x ∀y P(x, y)** — "there exists an x such that for every y, P(x, y)"

**Important Distinction:**

- ∀x ∃y P(x, y) ≠ ∃y ∀x P(x, y) in general

Example: Let P(x, y) be "x + y = 0" over integers.

- ∀x ∃y (x + y = 0) is true: for any integer x, we can choose y = -x
- ∃y ∀x (x + y = 0) is false: no single y works for all x

### Bound and Free Variables

In expressions involving quantifiers, a variable is **bound** if it falls within the scope of a quantifier; otherwise, it is **free**.

In ∀x P(x, y), x is bound and y is free.
In ∃x (x > 0 ∧ x < 10), x is bound.

Only statements with no free variables (closed formulas) have definite truth values.

## Examples

### Example 1: Negating a Universally Quantified Statement

**Problem:** Express the negation of "All students in this class passed the exam" using quantifiers.

**Solution:**
Let D = {students in this class}
Let P(x): "x passed the exam"

Original statement: ∀x P(x)

Negation: ¬∀x P(x) ≡ ∃x ¬P(x)

Therefore, the negated statement is: "There exists a student in this class who did not pass the exam" or "At least one student failed."

### Example 2: Translating Mathematical Statements

**Problem:** Translate "There is a real number whose square is negative" into symbolic form and determine its truth value.

**Solution:**
Domain: ℝ (real numbers)
P(x): "x² < 0"

Symbolic form: ∃x P(x) = ∃x (x² < 0)

This statement is **false** because for all real numbers x, x² ≥ 0. No real number has a negative square.

### Example 3: Proof with Multiple Quantifiers

**Problem:** Prove or disprove: ∀x ∈ ℤ ∃y ∈ ℤ (x + y = 0)

**Solution:**
We need to show that for every integer x, there exists an integer y such that x + y = 0.

**Proof:**
Let x be an arbitrary integer. Choose y = -x. Since x is an integer, -x is also an integer (closure of integers under negation).

Then x + (-x) = 0, so P(x, y) holds.

Since x was arbitrary, this works for all integers. Therefore, ∀x ∈ ℤ ∃y ∈ ℤ (x + y = 0) is **true**.

## Exam Tips

1. **Remember the negation rules:** When negating ∀, change to ∃ with negated predicate; when negating ∃, change to ∀ with negated predicate.

2. **Quantifier order matters:** Always pay attention to whether ∀ comes before ∃ or vice versa—they are not interchangeable.

3. **Identify the domain clearly:** Many mistakes occur when students forget to specify or consider the domain of discourse.

4. **Free variables have no truth value:** A predicate with free variables cannot be true or false until values are assigned.

5. **Constructive vs. non-constructive existence:** In proofs, distinguish between showing something exists and actually finding/constructing it.

6. **Counterexamples:** To disprove ∀x P(x), find one counterexample where ¬P(x) holds. To disprove ∃x P(x), show P(x) is false for all x.

7. **Common translations:** "None" = ¬∃, "no" = ¬∃, "every" = ∀, "some" = ∃, "at least one" = ∃.

8. **Practice with English to symbolic form:** This is a common exam question type that requires careful reading.
