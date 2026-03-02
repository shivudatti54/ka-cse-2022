# Reasoning Patterns in Propositional Logic

## Introduction

Reasoning patterns in propositional logic form the foundation of mathematical reasoning and automated theorem proving. In computer science, these patterns are essential for program verification, artificial intelligence, database systems, and circuit design. Propositional logic deals with propositions—statements that are either true or false—and provides systematic methods for determining whether a conclusion follows logically from a set of premises.

The study of reasoning patterns equips us with tools to construct valid arguments and proofs. A valid argument is one where if all premises are true, the conclusion must necessarily be true. This concept is crucial in 's Computer Science curriculum, as it develops logical thinking skills necessary for algorithm design, software engineering, and technical problem-solving. Understanding these patterns enables programmers to write correct code, verify program properties, and reason about complex systems systematically.

This module explores various rules of inference, proof techniques, and strategies for constructing logical derivations. These skills are not merely theoretical but have practical applications in formal methods, hardware verification, and logical programming languages like Prolog.

## Key Concepts

### 1. Argument and Validity

An argument in propositional logic consists of a set of premises (propositions P₁, P₂, ..., Pₙ) and a conclusion (Q). The argument is **valid** if and only if whenever all premises are true, the conclusion is also true. The validity of an argument depends purely on its logical form, not on the specific truth values of its components. An argument is **sound** if it is valid AND all its premises are actually true.

### 2. Rules of Inference

Rules of inference are basic valid argument forms that serve as building blocks for constructing formal proofs. The fundamental rules include:

**Modus Ponens (Affirming the Antecedent):**

- Form: P → Q, P ⊢ Q
- If P implies Q, and P is true, then Q must be true.

**Modus Tollens (Denying the Consequent):**

- Form: P → Q, ¬Q ⊢ ¬P
- If P implies Q, and Q is false, then P must be false.

**Hypothetical Syllogism (Chain Rule):**

- Form: P → Q, Q → R ⊢ P → R
- If P implies Q and Q implies R, then P implies R.

**Disjunctive Syllogism:**

- Form: P ∨ Q, ¬P ⊢ Q
- If either P or Q is true, and P is false, then Q must be true.

**Addition (Disjunction Introduction):**

- Form: P ⊢ P ∨ Q
- From P, we can infer P ∨ Q (for any Q).

**Simplification (Conjunction Elimination):**

- Form: P ∧ Q ⊢ P
- From P ∧ Q, we can infer P.

**Conjunction (Conjunction Introduction):**

- Form: P, Q ⊢ P ∧ Q
- From P and Q, we can infer P ∧ Q.

**Resolution:**

- Form: P ∨ Q, ¬P ∨ R ⊢ Q ∨ R
- This is a fundamental rule used in automated theorem proving.

### 3. Formal Proofs / Derivations

A formal proof (or derivation) is a sequence of statements where each statement is either a premise or follows from previous statements by applying a rule of inference. The final statement in the proof is the conclusion we wish to derive. Formal proofs provide a rigorous way to demonstrate that a conclusion follows from given premises.

### 4. Proof Strategies

**Direct Proof:** Start from premises and use rules of inference to derive the conclusion directly.

**Indirect Proof (Proof by Contradiction):** Assume the negation of what we want to prove, derive a contradiction, and then conclude the original statement is true.

**Proof by Contraposition:** To prove P → Q, instead prove ¬Q → ¬P, which is logically equivalent.

## Examples

### Example 1: Using Modus Ponens and Modus Tollens

**Premises:**

1. If it rains (R), then the ground gets wet (W).
2. It is raining (R).
3. If the ground gets wet (W), then the grass becomes slippery (S).

**Prove:** The grass becomes slippery (S).

**Solution:**

| Step | Statement | Reason              |
| ---- | --------- | ------------------- |
| 1    | R → W     | Premise             |
| 2    | R         | Premise             |
| 3    | W → S     | Premise             |
| 4    | W         | Modus Ponens (1, 2) |
| 5    | S         | Modus Ponens (3, 4) |

Thus, the grass becomes slippery.

### Example 2: Constructing a Formal Proof

**Premises:**

1. P → (Q ∨ R)
2. P ∧ ¬Q

**Prove:** R

**Solution:**

| Step | Statement   | Reason                       |
| ---- | ----------- | ---------------------------- |
| 1    | P → (Q ∨ R) | Premise                      |
| 2    | P ∧ ¬Q      | Premise                      |
| 3    | P           | Simplification (2)           |
| 4    | ¬Q          | Simplification (2)           |
| 5    | Q ∨ R       | Modus Ponens (1, 3)          |
| 6    | R           | Disjunctive Syllogism (5, 4) |

### Example 3: Proof by Contradiction

**Statement:** Prove that √2 is irrational.

**Proof:**
Assume for contradiction that √2 is rational. Then √2 = a/b where a and b are integers with no common factors, and b ≠ 0.

From √2 = a/b, we get 2 = a²/b², so a² = 2b².
This means a² is even, so a is even (since square of odd is odd).
Let a = 2k for some integer k.
Then (2k)² = 2b² ⇒ 4k² = 2b² ⇒ b² = 2k².
This means b² is even, so b is even.

But if both a and b are even, they have a common factor of 2, contradicting our assumption that they have no common factors.

Therefore, √2 cannot be rational; it must be irrational.

## Exam Tips

1. **Identify the Rule:** In exam questions, carefully identify which rule of inference is being applied. Modus Ponens and Modus Tollens are the most commonly tested.

2. **Truth vs. Validity:** Remember that validity concerns logical form, not actual truth. An argument can be valid even with false premises.

3. **Proof Structure:** Always structure your formal proofs clearly with each step numbered and the reason (rule of inference) cited.

4. **Logical Equivalences:** Know the logical equivalences (De Morgan's laws, contrapositive, etc.) as they help in transforming formulas during proofs.

5. **Common Patterns:** Memorize the eight fundamental rules of inference—they form the toolkit for all propositional proofs.

6. **Strategy Selection:** For complex proofs, first determine whether direct proof, proof by contraposition, or proof by contradiction is most appropriate.

7. **Contradiction Indicators:** Look for keywords like "assume the opposite," "cannot be both," or "suppose not" which often indicate proof by contradiction.

8. **Practice Translation:** Practice converting English statements into logical formulas, as this is often the first step in solving reasoning problems.
