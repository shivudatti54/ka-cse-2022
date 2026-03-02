# **Basic Connectives and Truth Tables**

## **Introduction**

In discrete mathematical structures, logic plays a crucial role in understanding and analyzing the behavior of complex systems. One fundamental concept in logic is the use of connectives to combine propositions (statements that can be either true or false). In this study material, we will explore the basic connectives and their truth tables.

## **Definition of Connectives**

A connective is a logical operator that combines two or more propositions to form a new proposition. Connectives are used to express relationships between propositions, such as conjunction (AND), disjunction (OR), negation (NOT), and implication (IF-THEN).

## **Basic Connectives**

### 1. Conjunction (AND)

Conjunction is a connective that combines two propositions to form a new proposition that is true only if both propositions are true.

- Definition: P ∧ Q (P and Q) is true if and only if both P and Q are true.
- Truth Table:

| P   | Q   | P ∧ Q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | F     |
| F   | F   | F     |

### 2. Disjunction (OR)

Disjunction is a connective that combines two propositions to form a new proposition that is true if at least one of the propositions is true.

- Definition: P ∨ Q (P or Q) is true if and only if at least one of P or Q is true.
- Truth Table:

| P   | Q   | P ∨ Q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | T     |
| F   | T   | T     |
| F   | F   | F     |

### 3. Negation (NOT)

Negation is a connective that combines a proposition to form a new proposition that is true if the original proposition is false.

- Definition: ¬P (not P) is true if and only if P is false.
- Truth Table:

| P   | ¬P  |
| --- | --- |
| T   | F   |
| F   | T   |

### 4. Implication (IF-THEN)

Implication is a connective that combines two propositions to form a new proposition that is true if the antecedent (the proposition before the arrow) is false or if the consequent (the proposition after the arrow) is true.

- Definition: P → Q (if P then Q) is true if and only if:
  - P is false or
  - Q is true.
- Truth Table:

| P   | Q   | P → Q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | T     |
| F   | F   | T     |

## **Key Concepts**

- Connectives are used to combine propositions to form new propositions.
- Each connective has a specific definition and truth table.
- Understanding the truth tables of connectives is essential for analyzing complex logical expressions.

## **Example**

Use the truth tables of conjunction and disjunction to evaluate the following expression:

(P ∧ Q) ∨ ¬P

Using the truth tables, we can evaluate the expression as follows:

| P   | Q   | P ∧ Q | ¬P  | P ∧ Q ∨ ¬P |
| --- | --- | ----- | --- | ---------- |
| T   | T   | T     | F   | T          |
| T   | F   | F     | F   | F          |
| F   | T   | F     | T   | T          |
| F   | F   | F     | T   | F          |

As we can see, the expression (P ∧ Q) ∨ ¬P is true if P is false or if Q is true, which is consistent with the definition of disjunction.

## **Conclusion**

In this study material, we have explored the basic connectives and their truth tables. Understanding the definitions and truth tables of connectives is essential for analyzing complex logical expressions. By mastering the basic connectives, you will be able to build more complex logical expressions and make informed decisions in a variety of fields, including computer science, mathematics, and philosophy.
