# Basic Connectives and Truth Tables

## Table of Contents

- [Basic Connectives and Truth Tables](#basic-connectives-and-truth-tables)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Propositions and Truth Values](#propositions-and-truth-values)
  - [Basic Logical Connectives](#basic-logical-connectives)
  - [Order of Operations (Precedence)](#order-of-operations-precedence)
  - [Tautology, Contradiction, and Contingency](#tautology-contradiction-and-contingency)
  - [Logical Equivalence](#logical-equivalence)
- [Examples](#examples)
  - [Example 1: Constructing a Truth Table for (p ∨ q) → ¬r](#example-1-constructing-a-truth-table-for-p--q--r)
  - [Example 2: Showing Logical Equivalence using Truth Tables](#example-2-showing-logical-equivalence-using-truth-tables)
  - [Example 3: Determining the Type of Proposition](#example-3-determining-the-type-of-proposition)
- [Exam Tips](#exam-tips)

## Introduction

Propositional logic forms the foundation of discrete mathematics and computer science. It provides a formal framework for representing and manipulating logical statements that are either true or false. In digital computing, circuit design, and algorithm development, understanding propositional logic is essential for creating reliable and efficient systems. The study of basic connectives and truth tables enables us to evaluate complex logical expressions, prove mathematical theorems, and design decision-making algorithms.

A proposition is a declarative statement that is either definitively true or definitively false, but not both. For example, "university is located in Belgaum" is a true proposition, "2 + 2 = 5" is a false proposition, and "Close the door" is not a proposition at all since it's neither true nor false. Once we understand propositions, we can combine them using logical connectives to form compound propositions whose truth values depend on the truth values of their constituent simple propositions.

Truth tables serve as powerful tools for systematically enumerating all possible truth value combinations of simple propositions and determining the resulting truth value of the compound proposition. This methodical approach allows us to analyze complex logical expressions, identify logical equivalences, and verify the validity of logical arguments. In university examinations, truth tables and logical connectives frequently appear as fundamental questions testing students' understanding of propositional logic.

## Key Concepts

### Propositions and Truth Values

A **proposition** (or statement) is a declarative sentence that is either true (T) or false (F), but not both. The truth value of a proposition is denoted as T for true and F for false. Simple propositions are represented using lowercase letters such as p, q, r, s, and are called **atomic propositions**. When atomic propositions are combined using logical connectives, they form **compound propositions** (or molecular propositions).

**Examples of propositions:**

- "Bangalore is the capital of Karnataka" (True)
- "5 > 7" (False)
- "x + 3 = 7" (Not a proposition unless x is specified)

**Non-propositions:**

- "What is your name?" (Question)
- "Close the door!" (Command)
- "This sentence is false" (Paradox)

### Basic Logical Connectives

#### 1. Negation (¬ or ~)

The negation operator reverses the truth value of a proposition. If p is true, then ¬p is false, and vice versa.

| p   | ¬p  |
| --- | --- |
| T   | F   |
| F   | T   |

#### 2. Conjunction (∧)

The conjunction of two propositions p and q is true only when both p and q are true. It represents the logical "AND" operation.

| p   | q   | p ∧ q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | F     |
| F   | F   | F     |

#### 3. Disjunction (∨)

The disjunction of two propositions p and q is true when at least one of p or q is true. It represents the logical "OR" operation. Note that this is "inclusive or," meaning it includes the case where both are true.

| p   | q   | p ∨ q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | T     |
| F   | T   | T     |
| F   | F   | F     |

#### 4. Implication (p → q)

The implication p → q represents "if p then q." It is false only when p is true and q is false. In all other cases, it is true. Here, p is called the **antecedent** (or hypothesis) and q is called the **consequent** (or conclusion).

| p   | q   | p → q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | T     |
| F   | F   | T     |

#### 5. Biconditional (p ↔ q)

The biconditional p ↔ q represents "p if and only if q" or "p is equivalent to q." It is true when both p and q have the same truth value.

| p   | q   | p ↔ q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | F     |
| F   | F   | T     |

### Order of Operations (Precedence)

When evaluating compound propositions without parentheses, the following precedence order applies (from highest to lowest):

1. Negation (¬)
2. Conjunction (∧)
3. Disjunction (∨)
4. Implication (→)
5. Biconditional (↔)

For example, the expression p → q ∧ r is interpreted as p → (q ∧ r).

### Tautology, Contradiction, and Contingency

- **Tautology**: A compound proposition that is always true, regardless of the truth values of its component propositions. Example: p ∨ ¬p (Law of Excluded Middle)
- **Contradiction**: A compound proposition that is always false. Example: p ∧ ¬p (Law of Non-Contradiction)
- **Contingency**: A compound proposition that is neither always true nor always false. Its truth value depends on the truth values of its components.

### Logical Equivalence

Two propositions p and q are logically equivalent (denoted p ≡ q or p ⇔ q) if they have identical truth values in all possible cases. This can be verified using truth tables. Common logical equivalences include:

- **De Morgan's Laws**:
- ¬(p ∧ q) ≡ ¬p ∨ ¬q
- ¬(p ∨ q) ≡ ¬p ∧ ¬q
- **Implication Equivalence**: p → q ≡ ¬p ∨ q
- **Biconditional Equivalence**: p ↔ q ≡ (p → q) ∧ (q → p)

## Examples

### Example 1: Constructing a Truth Table for (p ∨ q) → ¬r

**Step-by-step solution:**

We need to create a truth table for the compound proposition: (p ∨ q) → ¬r

**Step 1:** Identify the number of atomic propositions: p, q, r (3 propositions)
**Step 2:** Calculate number of rows: 2³ = 8 rows

| p   | q   | r   | p ∨ q | ¬r  | (p ∨ q) → ¬r |
| --- | --- | --- | ----- | --- | ------------ |
| T   | T   | T   | T     | F   | F            |
| T   | T   | F   | T     | T   | T            |
| T   | F   | T   | T     | F   | F            |
| T   | F   | F   | T     | T   | T            |
| F   | T   | T   | T     | F   | F            |
| F   | T   | F   | T     | T   | T            |
| F   | F   | T   | F     | F   | T            |
| F   | F   | F   | F     | T   | T            |

**Explanation:** The implication is false only when the antecedent (p ∨ q) is true AND the consequent (¬r) is false. This happens when r is true and at least one of p or q is true.

### Example 2: Showing Logical Equivalence using Truth Tables

**Problem:** Prove that p → q is logically equivalent to ¬p ∨ q

**Solution:** Construct truth tables for both expressions:

| p   | q   | ¬p  | p → q | ¬p ∨ q |
| --- | --- | --- | ----- | ------ |
| T   | T   | F   | T     | T      |
| T   | F   | F   | F     | F      |
| F   | T   | T   | T     | T      |
| F   | F   | T   | T     | T      |

Since the columns for p → q and ¬p ∨ q are identical, they are logically equivalent: **p → q ≡ ¬p ∨ q**

### Example 3: Determining the Type of Proposition

**Problem:** Classify the proposition (p ∧ q) → (p ∨ q) as tautology, contradiction, or contingency.

**Solution:**

| p   | q   | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| --- | --- | ----- | ----- | ----------------- |
| T   | T   | T     | T     | T                 |
| T   | F   | F     | T     | T                 |
| F   | T   | F     | T     | T                 |
| F   | F   | F     | F     | T                 |

All truth values are T, so this is a **tautology**. This makes intuitive sense: if both p and q are true, then certainly at least one of them is true.

## Exam Tips

1. **Memorize truth tables**: All five connectives (¬, ∧, ∨, →, ↔) must be memorized. Pay special attention to the implication truth table, which is often confusing.

2. **Count rows correctly**: For n propositions, the truth table requires 2^n rows. A common mistake is missing combinations.

3. **Understand implication deeply**: Remember that p → q is only false when p is TRUE and q is FALSE. Many students incorrectly assume it requires some causal relationship.

4. **Practice De Morgan's Laws**: These are frequently tested and essential for simplifying logical expressions.

5. **Use precedence rules**: When drawing truth tables, evaluate sub-expressions in the correct order based on operator precedence.

6. **Check for tautology/contradiction efficiently**: If any row shows F in the final column, it's a contingency. If all rows show T, it's a tautology; all F indicates a contradiction.

7. **Write clear steps**: In exams, show intermediate columns in truth tables to earn partial marks even if the final answer has errors.

8. **Remember key equivalences**: The implication equivalence (p → q ≡ ¬p ∨ q) and De Morgan's laws appear frequently in proof questions.
