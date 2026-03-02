# First-Order Predicate Logic

## Introduction

First-Order Predicate Logic (FOPL), also known as First-Order Logic (FOL), represents a significant advancement over propositional logic. While propositional logic deals with whole statements that are either true or false, predicate logic allows us to analyze the internal structure of statements by introducing predicates, variables, and quantifiers. This enables us to represent and reason about relationships between objects, making it an indispensable tool in computer science, artificial intelligence, formal verification, and mathematical reasoning.

In the context of the University of Delhi's BSc (H) Computer Science program, predicate logic forms the foundation for understanding database query languages (like SQL), formal specification languages, logic programming (Prolog), and automated theorem proving. The ability to translate natural language statements into precise logical formulas and vice-versa is a crucial skill that every computer science student must develop. This topic not only appears in discrete mathematics examinations but also serves as prerequisite knowledge for courses on compilers, artificial intelligence, and software engineering.

## Key Concepts

### Predicates and Propositional Functions

A **predicate** (or propositional function) is a statement containing variables that becomes a proposition (with definite truth value) when specific values are substituted for those variables. We typically denote predicates by uppercase letters followed by variables in parentheses, such as P(x), Q(x, y), or R(x, y, z).

For example:
- P(x): "x is a prime number"
- Q(x, y): "x is greater than y"
- Likes(x, y): "x likes y"

The domain (or universe of discourse) must be specified for predicates, defining the set of all possible values that variables can take.

### Variables and Constants

**Variables** are placeholders that can be replaced by elements from the domain. We distinguish between:
- **Free variables**: Variables not bound by any quantifier
- **Bound variables**: Variables that fall within the scope of a quantifier

**Constants** (or individual constants) are specific elements from the domain. For instance, if our domain is integers, constants might be 0, 1, 2, -5, etc.

### Quantifiers

Quantifiers specify the extent of validity for a predicate. There are two fundamental quantifiers:

**Universal Quantifier (∀)**: The statement ∀x P(x) means "for all x, P(x) is true" or "P(x) holds for every x in the domain." Its symbolic representation is ∀, derived from the word "all."

**Existential Quantifier (∃)**: The statement ∃x P(x) means "there exists an x such that P(x) is true" or "there is at least one x in the domain for which P(x) holds."

These quantifiers are duals of each other, connected by De Morgan's laws:
- ¬∀x P(x) ≡ ∃x ¬P(x)
- ¬∃x P(x) ≡ ∀x ¬P(x)

### Atomic and Well-Formed Formulas

An **atomic formula** (or atom) is the simplest predicate logic formula, consisting of a predicate symbol applied to term(s). Examples include P(x), Q(x, y), and R(a).

A **well-formed formula** (wff) in predicate logic is defined recursively:
1. Every atomic formula is a wff
2. If P is a wff, then ¬P is a wff
3. If P and Q are wffs, then (P ∧ Q), (P ∨ Q), (P → Q), and (P ↔ Q) are wffs
4. If P is a wff and x is a variable, then ∀x P and ∃x P are wffs
5. Nothing else is a wff

### Scope of Quantifiers and Binding

When a quantifier is applied to a variable, it **binds** that variable. The portion of the formula where the quantifier operates is called its **scope**. For instance, in ∀x (P(x) → ∃y Q(x, y)), the scope of ∀x is the entire implication, while the scope of ∃y is just Q(x, y).

A variable is **free** if it is not bound by any quantifier. A formula with no free variables is a **sentence** (or closed formula) and has a definite truth value.

### Interpretation and Truth

An interpretation (or structure) in predicate logic consists of:
1. A non-empty domain (universe of discourse)
2. An assignment of specific objects from the domain to each constant
3. An assignment of relations (extensions) to each predicate symbol

A sentence is true under an interpretation if it evaluates to true based on that interpretation. A sentence is **valid** (tautologically true) if it is true under every possible interpretation. A sentence is **satisfiable** if there exists at least one interpretation under which it is true.

## Examples

### Example 1: Translating Statements to Predicate Logic

**Problem**: Translate the following statements into predicate logic:
(a) "All students in this class have a laptop"
(b) "Some students in this class have a laptop"
(c) "Only students in this class have a laptop"

**Solution**:

Let our domain be all people. Define:
- S(x): "x is a student"
- C(x): "x is in this class"
- L(x): "x has a laptop"

(a) **All students in this class have a laptop**:
∀x ((S(x) ∧ C(x)) → L(x))

The universal quantifier with implication correctly captures that if someone is both a student and in this class, they must have a laptop.

(b) **Some students in this class have a laptop**:
∃x (S(x) ∧ C(x) ∧ L(x))

The existential quantifier with conjunction states there exists at least one person who is simultaneously a student, in this class, and has a laptop.

(c) **Only students in this class have a laptop**:
∀x (L(x) → (S(x) ∧ C(x)))

This states that anyone who has a laptop must be both a student and in this class.

### Example 2: Negating Quantified Statements

**Problem**: Find the negation of the statement "Every student passed the exam" and express it in natural language.

**Solution**:

Let P(x): "x is a student"
Let Q(x): "x passed the exam"

Original statement: ∀x (P(x) → Q(x))

Negation: ¬∀x (P(x) → Q(x))
≡ ∃x ¬(P(x) → Q(x))
≡ ∃x (P(x) ∧ ¬Q(x))

Natural language: "There exists a student who did not pass the exam" or "Some student failed the exam."

This illustrates the important transformation: the negation of a universal quantifier becomes an existential quantifier, and the inner statement is negated.

### Example 3: Determining Truth Values

**Problem**: Consider the interpretation with domain = {1, 2, 3}. Let P(x, y) mean "x is less than y." Evaluate the truth values of:
(a) ∀x ∃y P(x, y)
(b) ∃y ∀x P(x, y)

**Solution**:

Domain D = {1, 2, 3}
P(x, y): x < y

(a) ∀x ∃y P(x, y):
- For x = 1: ∃y such that 1 < y → y = 2 or 3 ✓
- For x = 2: ∃y such that 2 < y → y = 3 ✓
- For x = 3: ∃y such that 3 < y → No y in {1,2,3} makes 3 < y true ✗

Since x = 3 fails, ∀x ∃y P(x, y) is **FALSE**.

(b) ∃y ∀x P(x, y):
We need a single y that is greater than ALL x values in the domain.
- If y = 1: Is 1 < 1? No (reflexive relation doesn't hold)
- If y = 2: Is 1 < 2? Yes. Is 2 < 2? No.
- If y = 3: Is 1 < 3? Yes. Is 2 < 3? Yes. Is 3 < 3? No.

No single y works for all x, so ∃y ∀x P(x, y) is **FALSE**.

This example demonstrates that the order of quantifiers critically affects meaning: ∀x ∃y ≠ ∃y ∀x in general.

## Exam Tips

1. **Remember quantifier duality**: When negating statements with quantifiers, always swap ∀ to ∃ and vice versa while negating the predicate. The pattern is: ¬∀x P(x) ≡ ∃x ¬P(x) and ¬∃x P(x) ≡ ∀x ¬P(x).

2. **Order matters**: In predicate logic, the order of different quantifiers matters immensely. ∀x ∃y P(x, y) means "for every x, there exists a y" (which could vary with x), while ∃y ∀x P(x, y) means "there exists a y that works for all x." These are generally not equivalent.

3. **Use implication correctly with universal quantifiers**: For statements like "All A are B," use ∀x (A(x) → B(x)), not ∀x (A(x) ∧ B(x)). The latter would incorrectly require everything in the domain to be both A and B.

4. **Distinguish free from bound variables**: A formula with free variables cannot have a definite truth value until those variables are assigned values. In examinations, always check whether a formula is a sentence (closed formula).

5. **Be careful with empty domains**: In standard first-order logic, we typically assume non-empty domains. Some formulas that appear true with non-empty domains may behave differently with empty domains—though this is rarely tested at BSc level.

6. **Practice translation both ways**: Most examination questions require translating between English statements and predicate logic formulas. Master the translation of quantifiers: "every" and "all" → ∀, "some" and "there exists" → ∃.

7. **Understand valid inference rules**: Know modus ponens and universal instantiation in the context of predicate logic. Remember that from ∀x P(x), we can infer P(c) for any constant c in the domain.