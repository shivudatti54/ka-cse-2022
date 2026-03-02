# Representation Revisited

## Introduction

In the previous modules, we have discussed propositional logic and its applications in artificial intelligence. However, propositional logic has its limitations, and it is not sufficient to represent complex knowledge and relationships. In this module, we will revisit the concept of representation and introduce first-order logic, which is a more powerful and expressive language for representing knowledge.

## Limitations of Propositional Logic

Propositional logic is limited in its ability to represent complex relationships and knowledge. It is not possible to express relationships between objects or to represent knowledge that involves variables and quantifiers. For example, in propositional logic, we can represent the statement "It is raining" as a single proposition, but we cannot represent the statement "For all x, if x is a bird, then x can fly."

## First-Order Logic

First-order logic is a more powerful and expressive language than propositional logic. It allows us to represent relationships between objects and to express knowledge that involves variables and quantifiers. In first-order logic, we can represent the statement "For all x, if x is a bird, then x can fly" using the following formula:

∀x (Bird(x) → CanFly(x))

This formula states that for all x, if x is a bird, then x can fly.

## Syntax and Semantics of First-Order Logic

The syntax of first-order logic consists of the following elements:

- Variables: x, y, z, etc.
- Constants: a, b, c, etc.
- Predicates: P(x), Q(x), R(x), etc.
- Functions: f(x), g(x), h(x), etc.
- Quantifiers: ∀, ∃
- Logical operators: ∧, ∨, ¬, →, ←

The semantics of first-order logic is based on the concept of interpretation. An interpretation is a mapping from the variables, constants, predicates, and functions to a non-empty set of objects, called the domain.

## Using First-Order Logic

First-order logic can be used to represent a wide range of knowledge and relationships. For example, we can use first-order logic to represent the following statements:

- "All humans are mortal."
  ∀x (Human(x) → Mortal(x))
- "There exists a person who is a doctor."
  ∃x (Person(x) ∧ Doctor(x))
- "For all x, if x is a student, then x is enrolled in a course."
  ∀x (Student(x) → Enrolled(x))

## Knowledge Engineering in First-Order Logic

Knowledge engineering is the process of representing knowledge in a formal language, such as first-order logic. The goal of knowledge engineering is to create a knowledge base that can be used to reason about a particular domain.

The process of knowledge engineering involves the following steps:

1. Identify the domain and the knowledge that needs to be represented.
2. Define the vocabulary and the syntax of the knowledge base.
3. Represent the knowledge using first-order logic formulas.
4. Test and validate the knowledge base.

## Propositional Versus First-Order Inference

Inference is the process of drawing conclusions from a set of premises. In propositional logic, inference is based on the rules of propositional logic, such as modus ponens and modus tollens.

In first-order logic, inference is based on the rules of first-order logic, such as universal instantiation and existential generalization.

## Unification

Unification is the process of finding a substitution that makes two formulas equal. Unification is used in first-order logic to solve equations and to find the values of variables.

## Forward Chaining

Forward chaining is a method of reasoning that involves applying the rules of a knowledge base to a set of facts to derive new conclusions.

## Exam Tips

- Make sure to understand the syntax and semantics of first-order logic.
- Practice representing knowledge using first-order logic formulas.
- Understand the difference between propositional and first-order inference.
- Be able to apply the rules of first-order logic to solve problems.

### Comparison of Propositional and First-Order Logic

|                | Propositional Logic          | First-Order Logic             |
| -------------- | ---------------------------- | ----------------------------- |
| Expressiveness | Limited                      | More expressive               |
| Variables      | No variables                 | Variables and quantifiers     |
| Relationships  | No relationships             | Relationships between objects |
| Inference      | Based on propositional rules | Based on first-order rules    |

### Example ASCII Diagram

```
+---------------+
|  Domain  |
+---------------+
|  +-------+  |
|  |  x  |  |
|  +-------+  |
|  |  P(x)  |
|  +-------+  |
|  |  Q(x)  |
|  +-------+  |
+---------------+
```

This diagram represents a domain with a variable x and two predicates P(x) and Q(x).
