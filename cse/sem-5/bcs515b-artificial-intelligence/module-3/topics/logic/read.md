# Propositional Logic and Predicate Logic

## Introduction

Logic forms the foundation of computer science and digital computing. It provides the systematic framework for reasoning, proof construction, and algorithmic thinking. In the context of 's Computer Science and Engineering curriculum, logic serves as the backbone for various applications including circuit design, database queries, artificial intelligence, and software verification.

Propositional Logic, also known as propositional calculus, deals with propositions—statements that are either true or false—and the logical connectives that combine them. This branch of logic enables us to represent real-world statements symbolically and determine their truth values through systematic rules. Predicate Logic extends propositional logic by introducing quantifiers and predicates, allowing us to express more complex statements about objects and their properties. Together, these logical systems provide the mathematical foundation for formal reasoning in computer science, essential for tasks such as program verification, query processing, and automated theorem proving.

Understanding logic is crucial for CSE students because it develops analytical thinking skills necessary for algorithm design and problem-solving. Whether you're writing a complex program or designing a digital circuit, logical reasoning helps ensure correctness and efficiency.

## Key Concepts

### Propositional Logic

**Proposition**: A declarative statement that is either true (T) or false (F), but not both. Examples: "2 + 2 = 4" (true), "5 is even" (false), "It is raining" (can be true or false depending on context).

**Logical Connectives**:

- **Negation (¬)**: Reverses the truth value of a proposition. If P is true, ¬P is false.
- **Conjunction (∧)**: Returns true only when both operands are true.
- **Disjunction (∨)**: Returns true when at least one operand is true.
- **Implication (P → Q)**: "If P then Q" — false only when P is true and Q is false.
- **Biconditional (P ↔ Q)**: "P if and only if Q" — true when both have the same truth value.

**Truth Tables**: Systematic tables showing all possible combinations of truth values for propositions and the resulting truth values for compound propositions.

**Tautology**: A compound proposition that is always true regardless of truth values of its components.
**Contradiction**: A compound proposition that is always false.
**Contingency**: A proposition that is neither a tautology nor a contradiction.

### Predicate Logic

**Predicate**: A statement containing variables that becomes a proposition when specific values are assigned. For example, P(x) : "x is a prime number" is a predicate where P is the predicate and x is the variable.

**Quantifiers**:

- **Universal Quantifier (∀)**: "For all" — ∀x P(x) means P(x) is true for every x in the domain.
- **Existential Quantifier (∃)**: "There exists" — ∃x P(x) means there is at least one x in the domain for which P(x) is true.

**Domain (Universe)**: The set of all values that variables can take.

**Atomic Formula**: A predicate applied to terms, e.g., P(x), Q(x,y).
**Well-Formed Formula (WFF):** A correctly formed logical expression using quantifiers, connectives, and predicates.

### Logical Equivalences

Important equivalences include:

- De Morgan's Laws: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q and ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
- Implication Equivalence: P → Q ≡ ¬P ∨ Q
- Commutative, Associative, and Distributive laws for ∧ and ∨

### Rules of Inference

- Modus Ponens: P → Q, P ⊢ Q
- Modus Tollens: P → Q, ¬Q ⊢ ¬P
- Hypothetical Syllogism: P → Q, Q → R ⊢ P → R
- Disjunctive Syllogism: P ∨ Q, ¬P ⊢ Q
- Addition: P ⊢ P ∨ Q
- Simplification: P ∧ Q ⊢ P

## Examples

**Example 1: Construct Truth Table for (P ∧ Q) → R**

| P   | Q   | R   | P ∧ Q | (P ∧ Q) → R |
| --- | --- | --- | ----- | ----------- |
| T   | T   | T   | T     | T           |
| T   | T   | F   | T     | F           |
| T   | F   | T   | F     | T           |
| T   | F   | F   | F     | T           |
| F   | T   | T   | F     | T           |
| F   | T   | F   | F     | T           |
| F   | F   | T   | F     | T           |
| F   | F   | F   | F     | T           |

Since the last column is not all T, this is a contingency (neither tautology nor contradiction).

**Example 2: Translate to Predicate Logic**

Statement: "Every student in the class passed the exam."

Let S(x): x is a student in the class
Let P(x): x passed the exam

Translation: ∀x (S(x) → P(x))

Note: We use implication (→) rather than conjunction (∧) because not everyone in the domain is necessarily a student.

**Example 3: Prove using Rules of Inference**

Given:

1. If it rains (R), then the ground gets wet (W).
2. It rains (R).
   Conclusion: The ground gets wet (W).

Proof:

- Premise 1: R → W
- Premise 2: R
- By Modus Ponens: W (from 1 and 2)

Therefore, the ground gets wet.

## Exam Tips

1. **Remember implication truth condition**: P → Q is false only when P is true and Q is false—this is the most common trap in truth tables.

2. **Use De Morgan's Laws correctly**: Always distribute the negation to both components and change ∨ to ∧ (and vice versa).

3. **Quantifier order matters**: ∀x∀y P(x,y) is not always equivalent to ∀y∀x P(x,y); similarly for ∃.

4. **Domain specification**: Always consider the domain when working with quantifiers—it defines what values variables can take.

5. **Distinguish between ∀ and ∃ in translations**: "All" → ∀ with implication (→), "Some/At least one" → ∃ with conjunction (∧).

6. **Practice constructing truth tables**: For n propositions, you need 2^n rows—start with simpler 2-3 variable problems before attempting complex ones.

7. **Know the difference between tautology and contradiction**: A tautology is always true; a contradiction is always false.

8. **Apply modus ponens and modus tollens correctly**: These are the most frequently used rules of inference in proofs.
