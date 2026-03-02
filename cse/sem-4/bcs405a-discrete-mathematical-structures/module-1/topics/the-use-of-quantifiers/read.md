# The Use of Quantifiers

## Introduction

Quantifiers are fundamental components of mathematical logic that allow us to make statements about collections of objects rather than individual elements. In discrete mathematics and formal logic, quantifiers provide a way to express propositions that involve "all" or "some" elements within a domain. The two primary quantifiers are the **universal quantifier (∀)**, meaning "for all," and the **existential quantifier (∃)**, meaning "there exists."

Understanding quantifiers is essential for computer science students because they form the backbone of formal specification, database query languages, algorithm correctness proofs, and formal verification. When we write programs or design algorithms, we often need to make statements about all possible inputs or assert the existence of certain conditions—precisely what quantifiers allow us to express formally. This topic connects directly to predicate logic, which extends propositional logic by incorporating variables and quantifiers to create more expressive mathematical statements.

## Key Concepts

### Universal Quantifier (∀)

The universal quantifier symbol ∀ is used to express that a predicate is true for every element in the domain of discourse. The statement ∀x P(x) is read as "for all x, P(x) is true" or "for every x, P(x) holds."

**Syntax**: ∀x P(x)

- Domain: The set of all possible values that x can take
- P(x): A predicate or property that depends on x

**Example**: ∀x ∈ ℕ, x² ≥ 0
This reads as "for all natural numbers x, x squared is greater than or equal to zero."

### Existential Quantifier (∃)

The existential quantifier symbol ∃ is used to express that there exists at least one element in the domain for which the predicate is true. The statement ∃x P(x) is read as "there exists an x such that P(x) is true" or "for some x, P(x) holds."

**Syntax**: ∃x P(x)

- Domain: The set of all possible values that x can take
- P(x): A predicate or property that depends on x

**Example**: ∃x ∈ ℤ, x² = 4
This reads as "there exists an integer x such that x squared equals four" (x = 2 or x = -2).

### Domain of Discourse

The domain of discourse (or universe of discourse) defines the set of all possible values that variables can take. It is crucial to specify the domain clearly because the truth value of quantified statements depends on it.

**Example**:

- ∀x ∈ ℝ, x² > 0 is FALSE (since 0² = 0, not > 0)
- ∀x ∈ ℝ⁺, x² > 0 is TRUE (all positive real numbers squared are positive)

### Negation of Quantified Statements

One of the most important rules in quantifier logic is how to negate statements involving quantifiers:

**Negation of Universal Quantifier**:
¬∀x P(x) ≡ ∃x ¬P(x)
"The statement 'not all x satisfy P(x)' is equivalent to 'there exists an x that does not satisfy P(x).'"

**Negation of Existential Quantifier**:
¬∃x P(x) ≡ ∀x ¬P(x)
"The statement 'there does not exist an x satisfying P(x)' is equivalent to 'for all x, P(x) is false.'"

This relationship is known as **De Morgan's Laws for Quantifiers**.

### Multiple Quantifiers

When we use more than one quantifier, the order becomes critically important. Different orders can create statements with completely different meanings.

**Example with different orders**:

- ∀x ∈ ℤ ∃y ∈ ℤ, x + y = 0: "For every integer x, there exists an integer y such that x + y = 0" — TRUE (y = -x works)
- ∃y ∈ ℤ ∀x ∈ ℤ, x + y = 0: "There exists an integer y such that for every integer x, x + y = 0" — FALSE (no single y works for all x)

**Common patterns**:

- ∀x ∀y P(x,y) ≡ ∀y ∀x P(x,y) — Universal quantifiers commute
- ∃x ∃y P(x,y) ≡ ∃y ∃x P(x,y) — Existential quantifiers commute
- ∀x ∃y P(x,y) ≠ ∃y ∀x P(x,y) — Order matters when mixing quantifiers

### Bound and Free Variables

A variable is **bound** if it falls within the scope of a quantifier. A variable is **free** if it is not bound by any quantifier.

**Example**: In ∀x (P(x) → Q(y)), x is bound and y is free.

- Bound variables can be renamed (α-conversion) without changing the meaning
- Free variables make the statement depend on external assignment

## Examples

### Example 1: Translating English to Symbolic Form

**Problem**: Translate the following statements into logical notation using quantifiers.

(a) "Every student in the class passed the exam."

**Solution**:

- Let D = {students in the class}
- Let P(x) = "x passed the exam"
- Symbolic form: ∀x ∈ D, P(x)

(b) "There is a student in the class who scored 100 marks."

**Solution**:

- Let D = {students in the class}
- Let Q(x) = "x scored 100 marks"
- Symbolic form: ∃x ∈ D, Q(x)

(c) "At least two students in the class scored 100 marks."

**Solution**:

- Symbolic form: ∃x ∈ D ∃y ∈ D, (x ≠ y ∧ Q(x) ∧ Q(y))

### Example 2: Negating Quantified Statements

**Problem**: Negate the following statements and express in English.

(a) ∀x ∈ ℤ, (x > 0 → x² > 0)

**Solution**:

- Original: "For all integers, if x is positive then x squared is positive"
- Negation: ∃x ∈ ℤ, ¬(x > 0 → x² > 0)
- Simplify: ∃x ∈ ℤ, (x > 0 ∧ x² ≤ 0)
- English: "There exists an integer x such that x is positive but x squared is not positive"

(b) ∃x ∈ ℝ, (x² = 2 ∧ x > 0)

**Solution**:

- Original: "There exists a real number x such that x squared equals 2 and x is positive"
- Negation: ∀x ∈ ℝ, ¬(x² = 2 ∧ x > 0)
- Simplify: ∀x ∈ ℝ, (x² ≠ 2 ∨ x ≤ 0)
- English: "For every real number x, either x squared does not equal 2, or x is not positive"

### Example 3: Multiple Quantifiers and Order

**Problem**: Determine whether the following statements are true or false, where the domain is ℤ (integers).

(a) ∀x ∀y (x < y → x + 1 < y + 1)

**Solution**: TRUE

- For any integers x and y, if x < y, then adding 1 to both sides preserves the inequality
- This is a fundamental property of integers

(b) ∀x ∃y (x + y = 0)

**Solution**: TRUE

- For every integer x, we can find y = -x such that x + y = 0
- The y depends on x (it's not a single fixed y for all x)

(c) ∃y ∀x (x + y = 0)

**Solution**: FALSE

- This claims a single y works for ALL x
- If y = 0, then x + 0 = x, not 0 for x ≠ 0
- No single integer y can satisfy x + y = 0 for every integer x

## Exam Tips

1. **Remember the negation rules**: ¬∀x P(x) ≡ ∃x ¬P(x) and ¬∃x P(x) ≡ ∀x ¬P(x). These are frequently tested in exams.

2. **Always specify the domain**: When answering questions about quantifiers, explicitly mention the domain of discourse—it affects truth values.

3. **Pay attention to quantifier order**: When both universal and existential quantifiers appear, the order matters. A common exam mistake is assuming ∀x ∃y means the same as ∃y ∀x.

4. **Use counterexamples wisely**: To show ∀x P(x) is false, find one counterexample where P(x) is false. To show ∃x P(x) is false, show P(x) is false for ALL x.

5. **Translate carefully between English and symbols**: Practice converting statements like "no," "none," "not all," and "at least one" into proper quantifier notation.

6. **Understand bound vs. free variables**: Know that changing bound variable names doesn't change the meaning of a statement.

7. **Apply De Morgan's Laws**: When negating complex statements with multiple quantifiers, apply De Morgan's laws step by step from the outside quantifier inward.
