# Logic Equivalence and the Laws of Logic

## Table of Contents

- [Logic Equivalence and the Laws of Logic](#logic-equivalence-and-the-laws-of-logic)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Basic Logical Connectives](#1-basic-logical-connectives)
  - [2. Definition of Logical Equivalence](#2-definition-of-logical-equivalence)
  - [3. Fundamental Laws of Logic](#3-fundamental-laws-of-logic)
  - [4. Implications and Their Equivalences](#4-implications-and-their-equivalences)
  - [5. Tautology, Contradiction, and Contingency](#5-tautology-contradiction-and-contingency)
- [Examples](#examples)
  - [Example 1: Proving Equivalence Using Truth Table](#example-1-proving-equivalence-using-truth-table)
  - [Example 2: Simplifying a Logical Expression](#example-2-simplifying-a-logical-expression)
  - [Example 3: Verifying Logical Implication](#example-3-verifying-logical-implication)
- [Exam Tips](#exam-tips)

## Introduction

Logic equivalence is a fundamental concept in discrete mathematics that deals with determining when two propositions have the same truth value under all possible interpretations. This topic forms the bedrock of mathematical reasoning, computer science algorithms, and digital circuit design. Understanding logical equivalence allows us to simplify complex logical expressions, prove mathematical theorems, and construct efficient computational systems.

In propositional logic, we work with propositions—statements that are either true or false. The laws of logic, also known as logical equivalences or tautologies, provide systematic methods for transforming and simplifying logical expressions without changing their fundamental meaning. These laws are essential tools for circuit minimization in digital electronics, query optimization in databases, and program verification in software engineering.

This module explores the major logical equivalences, demonstrates their applications through worked examples, and provides exam-focused strategies for solving logic problems effectively.

## Key Concepts

### 1. Basic Logical Connectives

Before studying equivalence, we must understand the fundamental connectives:

- **Negation (¬p)**: True when p is false, and vice versa
- **Conjunction (p ∧ q)**: True only when both p and q are true
- **Disjunction (p ∨ q)**: True when at least one is true
- **Implication (p → q)**: False only when p is true and q is false
- **Biconditional (p ↔ q)**: True when p and q have the same truth value

### 2. Definition of Logical Equivalence

Two propositions p and q are **logically equivalent** (denoted p ≡ q or p ⇔ q) if they have identical truth values in all possible truth assignments. For example, p → q is logically equivalent to ¬p ∨ q.

To prove equivalence, we can use:

- Truth tables (showing identical columns)
- Algebraic manipulation using established laws

### 3. Fundamental Laws of Logic

#### Identity Laws

- p ∧ T ≡ p
- p ∨ F ≡ p

#### Domination Laws

- p ∨ T ≡ T (Tautology)
- p ∧ F ≡ F (Contradiction)

#### Idempotent Laws

- p ∧ p ≡ p
- p ∨ p ≡ p

#### Commutative Laws

- p ∧ q ≡ q ∧ p
- p ∨ q ≡ q ∨ p

#### Associative Laws

- (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
- (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)

#### Distributive Laws

- p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
- p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)

#### De Morgan's Laws (Crucial)

- ¬(p ∧ q) ≡ ¬p ∨ ¬q
- ¬(p ∨ q) ≡ ¬p ∧ ¬q

#### Absorption Laws

- p ∧ (p ∨ q) ≡ p
- p ∨ (p ∧ q) ≡ p

#### Negation Laws

- p ∧ ¬p ≡ F (Contradiction)
- p ∨ ¬p ≡ T (Tautology)

### 4. Implications and Their Equivalences

The implication p → q is logically equivalent to:

- ¬p ∨ q
- ¬q → ¬p (Contrapositive)
- ¬(p ∧ ¬q)

Key equivalences involving implications:

- p → q ≡ ¬q → ¬p (Contrapositive)
- p → q ≡ ¬p ∨ q
- p ↔ q ≡ (p → q) ∧ (q → p)
- p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)

### 5. Tautology, Contradiction, and Contingency

- **Tautology**: Always true (T), e.g., p ∨ ¬p
- **Contradiction**: Always false (F), e.g., p ∧ ¬p
- **Contingency**: Neither always true nor always false

## Examples

### Example 1: Proving Equivalence Using Truth Table

**Problem**: Show that p → q is logically equivalent to ¬p ∨ q using a truth table.

**Solution**:

| p   | q   | p → q | ¬p  | ¬p ∨ q |
| --- | --- | ----- | --- | ------ |
| T   | T   | T     | F   | T      |
| T   | F   | F     | F   | F      |
| F   | T   | T     | T   | T      |
| F   | F   | T     | T   | T      |

Since columns for (p → q) and (¬p ∨ q) are identical, they are logically equivalent.

### Example 2: Simplifying a Logical Expression

**Problem**: Simplify the expression: ¬(p ∨ q) ∨ (p ∧ q)

**Solution**:

Using De Morgan's Law and distributive properties:

```
¬(p ∨ q) ∨ (p ∧ q)
≡ (¬p ∧ ¬q) ∨ (p ∧ q) [De Morgan's Law]
≡ (¬p ∧ ¬q) ∨ (p ∧ q)
≡ (¬p ∧ ¬q) ∨ (p ∧ q) ∨ F [Domination Law: x ∨ F ≡ x]
≡ (¬p ∧ ¬q) ∨ (p ∧ q) ∨ (p ∧ ¬p) [Negation Law: p ∧ ¬p ≡ F]
≡ (¬p ∧ ¬q) ∨ (p ∧ (q ∨ ¬q)) [Distributive: a ∨ (b ∧ c) ≡ (a ∨ b) ∧ (a ∨ c)]
≡ (¬p ∧ ¬q) ∨ (p ∧ T) [Negation: q ∨ ¬q ≡ T]
≡ (¬p ∧ ¬q) ∨ p [Identity: p ∧ T ≡ p]
≡ p ∨ (¬p ∧ ¬q) [Commutative]
≡ (p ∨ ¬p) ∧ (p ∨ ¬q) [Distributive]
≡ T ∧ (p ∨ ¬q) [Negation: p ∨ ¬p ≡ T]
≡ p ∨ ¬q [Identity: T ∧ p ≡ p]
```

The simplified form is **p ∨ ¬q**, which is equivalent to **q → p**.

### Example 3: Verifying Logical Implication

**Problem**: Show that (p ∧ q) → p is a tautology.

**Solution**:

```
(p ∧ q) → p
≡ ¬(p ∧ q) ∨ p [Implication equivalence]
≡ (¬p ∨ ¬q) ∨ p [De Morgan's Law]
≡ ¬p ∨ p ∨ ¬q [Associative/Commutative]
≡ T ∨ ¬q [Negation: p ∨ ¬p ≡ T]
≡ T [Domination: T ∨ x ≡ T]
```

Since the result is always true (T), (p ∧ q) → p is a **tautology**.

## Exam Tips

1. **Memorize all the logical equivalence laws** - These are essential for solving problems quickly in exams.

2. **Use truth tables for verification** - When in doubt about equivalence, construct a truth table; this is a foolproof method.

3. **Remember De Morgan's Laws** - These are frequently tested and often misapplied. Note that negation "distributes" but changes AND to OR and vice versa.

4. **Convert implications early** - Replace p → q with ¬p ∨ q immediately; this simplifies most expressions.

5. **Check for common patterns**:

- p ∧ (p ∨ q) ≡ p (Absorption)
- p → q ≡ ¬q → ¬p (Contrapositive)
- ¬(p ∧ q) ≡ ¬p ∨ ¬q (De Morgan)

6. **Practice simplification** - Work through at least 10-15 simplification problems to recognize common patterns in exams.

7. **Verify your simplified form** - Always cross-check by constructing a truth table if time permits.

8. **State the law being applied** - In exam solutions, explicitly mention which law you're using (e.g., "By De Morgan's Law...").
