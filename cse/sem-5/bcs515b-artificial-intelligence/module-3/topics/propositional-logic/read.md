# Propositional Logic

## Introduction

Propositional Logic, also known as Sentential Logic or Statement Logic, forms the foundational pillar of mathematical reasoning and computer science. It deals with propositions—statements that are either true or false—and the logical relationships between them. This branch of formal logic provides the mathematical framework for representing and manipulating knowledge, enabling computers to perform automated reasoning, validate arguments, and support decision-making processes.

In the context of computer science and engineering, propositional logic finds extensive applications in various domains including digital circuit design (where it forms the basis of Boolean algebra), database query languages, software verification, artificial intelligence algorithms, and programming language semantics. Understanding propositional logic is essential for any computer science student as it develops critical thinking skills and provides the logical foundation required for more advanced topics like predicate logic, algorithm analysis, and formal methods in software engineering.

## Key Concepts

### 1. Proposition (Statement)

A proposition is a declarative sentence that is either definitely true or definitely false, but not both. Statements like "Bangalore is the capital of Karnataka" (true) and "2 + 2 = 5" (false) are propositions. Questions like "What is your name?", commands like "Close the door!", and paradoxes like "This statement is false" are not propositions because they cannot be assigned a definite truth value.

**Atomic Propositions (Simple Propositions):** Propositions that do not contain any other propositions as components. Denoted by letters such as p, q, r, s.

**Compound Propositions (Molecular Propositions):** Formed by combining atomic propositions using logical connectives.

### 2. Logical Connectives

The five fundamental logical connectives in propositional logic are:

**Negation (¬ or ~):** If p is a proposition, ¬p (not p) is true when p is false, and false when p is true. It inverts the truth value.

**Conjunction (∧):** p ∧ q (p and q) is true only when both p and q are true; otherwise false.

**Disjunction (∨):** p ∨ q (p or q) is true when at least one of p or q is true; false only when both are false.

**Implication (→):** p → q (if p then q) is false only when p is true and q is false; true in all other cases. Here p is called the antecedent (hypothesis) and q is the consequent (conclusion).

**Biconditional (↔):** p ↔ q (p if and only if q) is true when both p and q have the same truth value; false otherwise.

### 3. Truth Tables

Truth tables systematically enumerate all possible truth value combinations for propositions and show the resulting truth value of compound propositions. For n propositions, there are 2ⁿ rows in the truth table.

### 4. Logical Equivalence (⟺)

Two propositions P and Q are logically equivalent (P ≡ Q or P ⟺ Q) if they have identical truth values for all possible truth assignments to their component propositions. The notation ∼P represents negation.

### 5. Tautology, Contradiction, and Contingency

**Tautology:** A proposition that is always true regardless of truth values of its components. Example: p ∨ ¬p

**Contradiction (Fallacy):** A proposition that is always false. Example: p ∧ ¬p

**Contingency:** A proposition that is neither always true nor always false; its truth depends on the truth values of components.

### 6. Normal Forms

**Disjunctive Normal Form (DNF):** A proposition is in DNF if it is a disjunction of conjunctions of literals (variables or their negations).

**Conjunctive Normal Form (CNF):** A proposition is in CNF if it is a conjunction of disjunctions of literals.

**Literal:** A propositional variable or its negation (p, ¬p, q, ¬q).

### 7. Key Logical Equivalences

- Identity Laws: p ∧ T ≡ p, p ∨ F ≡ p
- Domination Laws: p ∧ F ≡ F, p ∨ T ≡ T
- Idempotent Laws: p ∧ p ≡ p, p ∨ p ≡ p
- Double Negation: ¬(¬p) ≡ p
- Commutative Laws: p ∧ q ≡ q ∧ p, p ∨ q ≡ q ∨ p
- Associative Laws: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
- Distributive Laws: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r), p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
- De Morgan's Laws: ¬(p ∧ q) ≡ ¬p ∨ ¬q, ¬(p ∨ q) ≡ ¬p ∧ ¬q
- Implication Equivalence: p → q ≡ ¬p ∨ q

### 8. Argument Validity

An argument is a set of premises followed by a conclusion. An argument is valid if whenever all premises are true, the conclusion is also true. The validity of an argument can be checked using truth tables or logical equivalences.

## Examples

### Example 1: Constructing Truth Table

**Problem:** Construct the truth table for the compound proposition (p ∧ q) → (p ∨ q)

**Solution:**

| p   | q   | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| --- | --- | ----- | ----- | ----------------- |
| T   | T   | T     | T     | T                 |
| T   | F   | F     | T     | T                 |
| F   | T   | F     | T     | T                 |
| F   | F   | F     | F     | T                 |

Since the result is true for all combinations, (p ∧ q) → (p ∨ q) is a **tautology**.

### Example 2: Testing Logical Equivalence

**Problem:** Show that p → q is logically equivalent to ¬p ∨ q

**Solution using Truth Table:**

| p   | q   | p → q | ¬p  | ¬p ∨ q |
| --- | --- | ----- | --- | ------ |
| T   | T   | T     | F   | T      |
| T   | F   | F     | F   | F      |
| F   | T   | T     | T   | T      |
| F   | F   | T     | T   | T      |

Since columns for p → q and ¬p ∨ q are identical, they are logically equivalent: **p → q ≡ ¬p ∨ q**

### Example 3: Argument Validity

**Problem:** Determine if the following argument is valid:
Premise 1: If it rains (r), then the ground gets wet (w)
Premise 2: The ground is wet (w)
Conclusion: It rains (r)

**Solution:**

This argument has the form: (r → w), w ∴ r

| r   | w   | r → w |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | T     |
| F   | F   | T     |

Consider the case where r = F and w = T: premises (r → w) = T and w = T are both true, but conclusion r = F is false. Therefore, the argument is **invalid** (this is the fallacy of affirming the consequent).

### Example 4: Converting to CNF

**Problem:** Convert (p → q) ∧ (¬r ∨ s) to Conjunctive Normal Form

**Solution:**

Step 1: Replace implication
= (¬p ∨ q) ∧ (¬r ∨ s)

The expression is already in CNF since it's a conjunction of disjunctions of literals.

## Exam Tips

1. **Memorize Truth Tables:** The truth tables for all five connectives (¬, ∧, ∨, →, ↔) must be memorized perfectly—they are the foundation for solving most problems.

2. **Implication Trap:** Remember that p → q is FALSE only when p is TRUE and q is FALSE. Students often make mistakes here in exams.

3. **De Morgan's Laws Application:** These are frequently tested. Remember: Negation distributes over conjunction and disjunction with the operators switching.

4. **Identify Tautology/Contradiction Quickly:** For n variables, use 2ⁿ rows. If all entries are T → Tautology; all F → Contradiction.

5. **Argument Validity Method:** To check validity, assume all premises true and check if conclusion can be false. If yes → Invalid; if no → Valid.

6. **Know Implication Transformations:** Always convert implications to disjunctions (¬p ∨ q) when simplifying or converting to CNF/DNF.

7. **Use Substitution for Equivalence Proofs:** To show P ≡ Q, show that P ↔ Q is a tautology using truth tables or known equivalences.

8. **Word Problems:** In exam questions involving English statements, first identify atomic propositions, assign symbols, then form the logical expression.

9. **Normal Form Conversion:** Remember that CNF requires disjunctions inside conjunctions, while DNF requires conjunctions inside disjunctions.

10. **Time Management:** For truth table problems with many variables, focus on the relevant rows where premises are true when checking argument validity.
