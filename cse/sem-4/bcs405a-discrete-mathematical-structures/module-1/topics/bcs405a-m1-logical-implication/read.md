# Logical Implication and Rules of Inference

## Table of Contents

- [Logical Implication and Rules of Inference](#logical-implication-and-rules-of-inference)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Logical Implication (p → q)](#logical-implication-p--q)
  - [Key Terminology](#key-terminology)
  - [Valid Arguments and Rules of Inference](#valid-arguments-and-rules-of-inference)
  - [Common Fallacies](#common-fallacies)
- [Examples](#examples)
  - [Example 1: Using Modus Ponens](#example-1-using-modus-ponens)
  - [Example 2: Using Multiple Rules of Inference](#example-2-using-multiple-rules-of-inference)
  - [Example 3: Formal Proof Construction](#example-3-formal-proof-construction)
- [Exam Tips](#exam-tips)

## Introduction

Logical implication and rules of inference form the foundational framework for mathematical reasoning and proof construction in computer science and engineering. These concepts enable us to derive conclusions from given premises systematically, ensuring that our arguments are valid and logically sound. In the context of discrete mathematics, understanding these principles is essential for algorithm design, database query languages, circuit design, and software verification.

The study of logical implication deals with the relationship between propositions where one proposition leads to another, while rules of inference provide the mechanical procedures for constructing valid arguments. Together, they form the backbone of propositional logic and serve as prerequisites for more advanced topics including predicate logic, mathematical proofs, and automated reasoning systems. For university students, mastering these concepts is crucial as they appear consistently in competitive examinations and technical interviews.

## Key Concepts

### Logical Implication (p → q)

Logical implication is a compound proposition that is false only when the antecedent (p) is true and the consequent (q) is false. The implication p → q can be read as "if p then q" or "p implies q." The truth table for implication is:

| p   | q   | p → q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | T     |
| F   | F   | T     |

The implication p → q is equivalent to ¬p ∨ q (negation of p or q).

### Key Terminology

**Converse**: The converse of p → q is q → p
**Inverse**: The inverse of p → q is ¬p → ¬q
**Contrapositive**: The contrapositive of p → q is ¬q → ¬p (logically equivalent to original)

**Tautology**: A proposition that is always true
**Contradiction**: A proposition that is always false
**Contingency**: A proposition that is neither always true nor always false

### Valid Arguments and Rules of Inference

An argument is a sequence of propositions where the last proposition is the conclusion, and all preceding propositions are premises. An argument is valid if whenever all premises are true, the conclusion must also be true.

#### Fundamental Rules of Inference

1. **Modus Ponens (Law of Detachment)**

- Premises: p → q, p
- Conclusion: q
- Example: If it rains (p), the ground gets wet (q). It rains. Therefore, the ground gets wet.

2. **Modus Tollens (Law of Contraposition)**

- Premises: p → q, ¬q
- Conclusion: ¬p
- Example: If it rains (p), the ground gets wet (q). The ground is not wet (¬q). Therefore, it does not rain (¬p).

3. **Hypothetical Syllogism**

- Premises: p → q, q → r
- Conclusion: p → r
- Example: If I study hard, I will pass. If I pass, I will get a job. Therefore, if I study hard, I will get a job.

4. **Disjunctive Syllogism**

- Premises: p ∨ q, ¬p
- Conclusion: q
- Example: Either the light is on or the switch is broken. The light is not on. Therefore, the switch is broken.

5. **Addition (Disjunction Introduction)**

- Premises: p
- Conclusion: p ∨ q
- Example: It is raining. Therefore, it is raining or it is snowing.

6. **Simplification (Conjunction Elimination)**

- Premises: p ∧ q
- Conclusion: p (or q)
- Example: It is raining and cold. Therefore, it is raining.

7. **Conjunction (Conjunction Introduction)**

- Premises: p, q
- Conclusion: p ∧ q
- Example: It is raining. It is cold. Therefore, it is raining and cold.

8. **Resolution**

- Premises: p ∨ q, ¬p ∨ r
- Conclusion: q ∨ r
- This is the fundamental rule used in automated theorem proving.

### Common Fallacies

- **Affirming the Consequent**: Invalidly concluding p from p → q and q
- **Denying the Antecedent**: Invalidly concluding ¬q from p → q and ¬p

## Examples

### Example 1: Using Modus Ponens

**Problem**: Given premises:

1. If the program compiles successfully (c), then there are no syntax errors (s).
2. The program compiles successfully (c).

Prove: There are no syntax errors (s).

**Solution**:

- Premise 1: c → s
- Premise 2: c
- By Modus Ponens: From c → s and c, we infer s
- Conclusion: There are no syntax errors

### Example 2: Using Multiple Rules of Inference

**Problem**: Given premises:

1. If the server is down (d), then users cannot login (l).
2. If users cannot login (l), then productivity decreases (p).
3. The server is down (d) or maintenance is scheduled (m).
4. Not maintenance is scheduled (¬m).

Prove: Productivity decreases (p).

**Solution**:

- From (1) d → l and (2) l → p, by Hypothetical Syllogism: d → p
- From (3) d ∨ m and (4) ¬m, by Disjunctive Syllogism: d
- From d and d → p, by Modus Ponens: p
- Conclusion: Productivity decreases

### Example 3: Formal Proof Construction

**Problem**: Construct a formal proof for the argument:
Premises: (p ∧ q) → r, p, q
Conclusion: r

**Solution**:

1. p Premise
2. q Premise
3. p ∧ q Conjunction (from 1, 2)
4. (p ∧ q) → r Premise
5. r Modus Ponens (from 3, 4)

## Exam Tips

1. **Understand truth tables**: Memorize the truth table for implication p → q - it is false only when p is true and q is false.

2. **Contrapositive is equivalent**: Remember that p → q and ¬q → ¬p are logically equivalent; this is frequently used in proofs.

3. **Identify the rule quickly**: In exam questions, carefully identify which rule of inference is being applied. Look for patterns like "if-then" statements with additional statements.

4. **Common fallacy trap**: Be careful not to confuse modus ponens with affirming the consequent. Modus ponens requires the antecedent to be true, not the consequent.

5. **Construct step-by-step proofs**: For formal proof questions, list each step clearly with the rule name and premise numbers.

6. **Use abbreviations**: Assign simple letters to complex statements (p = "it rains", q = "ground wet") to simplify the problem.

7. **Practice conversion**: Convert implications to disjunctions (p → q ≡ ¬p ∨ q) when working with resolution or when other rules don't apply directly.

8. **Check validity**: To verify an argument is valid, construct a truth table showing that whenever all premises are true, the conclusion is also true.
