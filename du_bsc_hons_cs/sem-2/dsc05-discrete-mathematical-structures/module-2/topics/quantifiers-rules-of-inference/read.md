# Quantifiers and Rules of Inference

## Introduction

Quantifiers and rules of inference form the backbone of logical reasoning in computer science and mathematics. While propositional logic deals with simple true or false statements, real-world reasoning often requires expressing statements about "all" or "some" elements in a domain. This is where quantifiers come into play—they allow us to express generalizations and particularities with precision.

In the context of the University of Delhi's Computer Science program, this topic is fundamental because it directly relates to formal verification, database query languages (like SQL's SELECT and WHERE clauses), algorithm correctness proofs, and programming language semantics. Understanding how to manipulate quantified statements and construct valid logical arguments is essential for any computer scientist. The rules of inference provide the mechanical framework for determining whether a logical argument is valid, regardless of the truth values of individual propositions.

This module will explore universal and existential quantifiers in depth, examine their negation, and establish the connection between quantifiers and the rules of inference that govern logical reasoning. These concepts are tested extensively in DU semester examinations and form the foundation for advanced topics like predicate calculus and formal methods.

## Key Concepts

### 1. Predicates and Propositional Functions

A predicate (or propositional function) is a statement containing variables that becomes a proposition when specific values are substituted for those variables. For example, "P(x): x is a prime number" is a predicate where P(x) is true when x is a prime number and false otherwise. The domain (or universe of discourse) specifies the set of all possible values that the variables can take. In computer science, predicates are extensively used in loops, conditions, and database queries.

When we write P(x), we mean "the property P holds for element x." The truth value of P(x) depends on both the predicate definition and the value of x. A predicate can have multiple variables, such as Q(x, y): "x is greater than y," which becomes a proposition only when both x and y are assigned specific values.

### 2. Universal Quantifier (∀)

The universal quantifier ∀ expresses that a property holds for all elements in the domain. The notation ∀x P(x) means "for all x, P(x) is true" or "for every x, P(x) holds." The symbol ∀ is read as "for all" or "for every." For instance, ∀x (x² ≥ 0) means "for all x, x squared is greater than or equal to zero," which is true when the domain is real numbers.

The domain specification is crucial for universal quantifiers. The statement ∀x P(x) is true if and only if P(x) is true for every element x in the domain. If the domain is empty, ∀x P(x) is vacuously true—this is an important convention in logic. When working with universal quantifiers in programming contexts, we often specify domains explicitly: ∀x ∈ ℕ, P(x).

### 3. Existential Quantifier (∃)

The existential quantifier ∃ expresses that there exists at least one element in the domain with a certain property. The notation ∃x P(x) means "there exists an x such that P(x) is true" or "there is at least one x for which P(x) holds." The symbol ∃ is read as "there exists" or "there is."

For example, ∃x (x + 5 = 10) means "there exists an x such that x plus five equals ten," which is true (x = 5). The existential quantifier requires at least one element in the domain to satisfy the predicate. Unlike the universal quantifier, an existential statement is false only if no element in the domain satisfies the predicate.

### 4. Negation of Quantified Statements

The negation of quantified statements follows a crucial pattern: the negation of a universal quantifier becomes an existential quantifier, and vice versa. This is known as De Morgan's laws for quantifiers:

- ¬∀x P(x) ≡ ∃x ¬P(x): "Not all x satisfy P" is equivalent to "There exists an x that does not satisfy P."
- ¬∃x P(x) ≡ ∀x ¬P(x): "There does not exist an x satisfying P" is equivalent to "For all x, P is false."

For example, the negation of "All students in the class passed" is "There exists at least one student in the class who did not pass." In programming, this principle is essential when writing loop invariants and conditions—understanding how to negate quantified statements helps in writing correct loop conditions and assertions.

### 5. Rules of Inference for Propositional Logic

Rules of inference are logical rules that allow us to derive conclusions from premises. An argument is valid if the conclusion necessarily follows from the premises—that is, if the premises are true, the conclusion must also be true. The validity of an argument depends on its form, not the truth of its specific premises.

**Modus Ponens (Affirming the Antecedent):**
```
P → Q
P
∴ Q
```
If P implies Q, and P is true, then Q must be true. Example: "If it rains (P), the ground gets wet (Q). It rains. Therefore, the ground is wet."

**Modus Tollens (Denying the Consequent):**
```
P → Q
¬Q
∴ ¬P
```
If P implies Q, and Q is false, then P must be false. Example: "If it rains, the ground gets wet. The ground is not wet. Therefore, it did not rain."

**Hypothetical Syllogism (Chain Rule):**
```
P → Q
Q → R
∴ P → R
```

**Disjunctive Syllogism:**
```
P ∨ Q
¬P
∴ Q
```

**Addition:**
```
P
∴ P ∨ Q
```

**Simplification:**
```
P ∧ Q
∴ P
```

### 6. Rules of Inference for Quantified Statements

When quantifiers are involved, we need additional rules to manipulate statements:

**Universal Instantiation:** From ∀x P(x), we can infer P(c) for any specific element c in the domain. If a property holds for all elements, it holds for any particular element.

**Universal Generalization:** From P(c) for an arbitrary element c in the domain, we can infer ∀x P(x). This requires that c is arbitrary, not a specific constant.

**Existential Instantiation:** From ∃x P(x), we can infer P(c) for some specific element c, where c is a new constant representing some element satisfying P.

**Existential Generalization:** From P(c) for some specific element c, we can infer ∃x P(x).

These rules are essential when constructing formal proofs involving quantified statements. They allow us to move between general statements about all elements and specific instances.

## Examples

### Example 1: Negating Quantified Statements

**Problem:** Write the negation of the statement: "Every computer science student in this class knows Python."

**Solution:**
Let the domain be the set of students in the class. Let P(x) = "x knows Python."

Original statement: ∀x P(x)

Negation: ¬∀x P(x) ≡ ∃x ¬P(x)

Therefore, the negation is: "There exists at least one computer science student in this class who does not know Python."

**Step-by-step:**
1. Original: ∀x (Student(x) → KnowsPython(x))
2. Apply negation: ¬∀x (Student(x) → KnowsPython(x))
3. Using ¬∀x ≡ ∃x¬: ∃x ¬(Student(x) → KnowsPython(x))
4. Using implication equivalence: ∃x (Student(x) ∧ ¬KnowsPython(x))
5. Final English: "There is a student in this class who is a computer science student and does not know Python."

### Example 2: Valid Argument with Quantifiers

**Problem:** Determine whether the following argument is valid:

Premise 1: All programming languages are formal languages.
Premise 2: Python is a programming language.
Conclusion: Python is a formal language.

**Solution:**
Let the domain be all languages.

- P(x): x is a programming language
- F(x): x is a formal language
- a: Python

**Formal representation:**
1. ∀x (P(x) → F(x)) — All programming languages are formal languages
2. P(a) — Python is a programming language
3. ∴ F(a) — Python is a formal language

**Proof using rules of inference:**
1. ∀x (P(x) → F(x)) [Premise]
2. P(a) → F(a) [Universal Instantiation from 1]
3. P(a) [Premise]
4. F(a) [Modus Ponens from 2 and 3]

**Conclusion:** The argument is valid. This is essentially modus ponens applied to a universally quantified premise after instantiation.

### Example 3: Constructing a Formal Proof

**Problem:** Given the premises:
1. Everyone who studies hard passes the exam.
2. Someone studied hard.
Prove: Someone passed the exam.

**Solution:**
Let the domain be all people.

- S(x): x studies hard
- P(x): x passes the exam

**Formal representation:**
1. ∀x (S(x) → P(x)) — Everyone who studies hard passes
2. ∃x S(x) — Someone studied hard
3. ∃x P(x) — Someone passed the exam (to be proven)

**Proof:**
1. ∀x (S(x) → P(x)) [Premise]
2. ∃x S(x) [Premise]
3. S(c) [Existential Instantiation from 2, where c is some person]
4. S(c) → P(c) [Universal Instantiation from 1]
5. P(c) [Modus Ponens from 3 and 4]
6. ∃x P(x) [Existential Generalization from 5]

**Conclusion:** The argument is valid. We instantiated the existential premise to get a specific person c who studied hard, then used universal instantiation and modus ponens to show this person passed, finally generalizing to conclude someone passed.

## Exam Tips

1. **Master quantifier negation:** This is the most frequently tested concept. Remember: ¬∀ ≡ ∃¬ and ¬∃ ≡ ∀¬. Practice converting English statements to logical form and back.

2. **Know all rules of inference by name:** In DU exams, you must be able to identify which rule is being applied and use them correctly in proof problems. Memorize the Latin names: Modus Ponens, Modus Tollens, etc.

3. **Understand the difference between validity and truth:** An argument can be valid but have a false conclusion if the premises are false. The validity concerns the form, not the content.

4. **Practice formalization:** Convert English statements to logical expressions using predicates and quantifiers. This is essential for both theory questions and proof problems.

5. **Be careful with universal vs. existential:** Using universal instantiation incorrectly is a common error. Remember that from ∀x P(x), you can derive P(c) for any c, but from ∃x P(x), you can only derive P(c) for some unspecified c.

6. **Domain matters:** Always consider the domain of discourse when evaluating quantified statements. The truth value changes with the domain.

7. **Know when to use existential vs. universal instantiation:** Universal instantiation works for any element in the domain. Existential instantiation introduces a new constant that represents "some" element satisfying the predicate.

8. **Check your work with counterexamples:** If asked to determine whether an argument is valid, try to find a counterexample where premises are true but conclusion is false.