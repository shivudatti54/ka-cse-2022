# Module 2: Representing Knowledge Using Rules

## Introduction

In Artificial Intelligence, an agent's ability to reason and solve problems is fundamentally dependent on how its knowledge is represented. Among the various paradigms for knowledge representation, **rule-based systems** are one of the most intuitive and widely used methods, especially in the development of expert systems. This module explores how we can encode human expertise and domain knowledge into a set of `IF-THEN` rules, creating a powerful mechanism for logical inference.

## Core Concepts

### 1. What is a Rule?

A rule is a conditional statement that represents a chunk of knowledge in the form:
**IF** `<antecedent>` **THEN** `<consequent>`.

*   **Antecedent (Left-Hand Side - LHS):** This is the condition or the premise. It is a combination of facts (using logical operators AND, OR) that must be true for the rule to be triggered.
*   **Consequent (Right-Hand Side - RHS):** This is the action, conclusion, or result that is deduced or executed when the antecedent is satisfied.

Rules are also known as **production rules**, and a collection of such rules forms a **knowledge base**.

### 2. Structure of a Rule-Based System

A typical rule-based system consists of three core components:

1.  **Knowledge Base (Rule Base):** This is the "brain" of the system. It is a collection of rules that encapsulate the domain-specific knowledge (e.g., medical diagnosis rules, fault detection rules for an engine).
2.  **Working Memory (Fact Base):** This is a database that contains the facts about the current situation or problem. These facts are initially provided by the user and new facts are added as rules fire and deduce new information.
3.  **Inference Engine:** This is the "processor" of the system. It is the algorithm that controls the reasoning process. It matches the facts in the working memory against the antecedents of rules in the knowledge base. When a match is found, the corresponding rule is triggered ("fired"), and its consequent is executed (adding a new fact, asking a user question, etc.).

### 3. The Inference Process

The inference engine primarily operates in one of two ways:

*   **Forward Chaining (Data-Driven Reasoning):** This strategy starts with the available data (facts in working memory) and uses the rules to derive new conclusions until a desired goal is reached. It's like working from evidence to a conclusion.
    *   *Example:* Diagnosing a car that won't start.
        *   Fact: `Fuel_Gauge is empty`
        *   Rule: `IF Fuel_Gauge is empty THEN Problem is out_of_fuel`
        *   Inference: The engine adds the new fact `Problem is out_of_fuel` to working memory.

*   **Backward Chaining (Goal-Driven Reasoning):** This strategy starts with a hypothesis (the goal) and works backward to see if the available data supports it. It checks what rules would lead to that goal and then tries to satisfy the conditions of those rules.
    *   *Example:* Proving the goal `Problem is out_of_fuel`.
        *   The engine finds the rule `IF Fuel_Gauge is empty THEN Problem is out_of_fuel`.
        *   It then sets a sub-goal to check if `Fuel_Gauge is empty` is true.
        *   It queries working memory or the user for this fact.

### 4. Example: A Simple Animal Classification System

Let's define a small knowledge base with rules:

**Rules:**
1.  IF `animal has fur` THEN `it is a mammal`
2.  IF `animal gives milk` THEN `it is a mammal`
3.  IF `animal eats meat` THEN `it is a carnivore`
4.  IF `it is a mammal` AND `it is a carnivore` AND `animal has tawny color` AND `animal has dark spots` THEN `it is a cheetah`
5.  IF `it is a mammal` AND `it is a carnivore` AND `animal has tawny color` AND `animal has black stripes` THEN `it is a tiger`

**Working Memory (User-provided facts):**
*   `animal gives milk`
*   `animal eats meat`
*   `animal has tawny color`
*   `animal has black stripes`

**Inference (Forward Chaining):**
1.  Fact `animal gives milk` triggers Rule 2: `it is a mammal` is added to memory.
2.  Fact `animal eats meat` triggers Rule 3: `it is a carnivore` is added to memory.
3.  The inference engine now has the facts: `it is a mammal`, `it is a carnivore`, `animal has tawny color`, `animal has black stripes`.
4.  These facts match the antecedent of Rule 5. The rule fires.
5.  Conclusion: `it is a tiger` is added to working memory.

## Advantages and Disadvantages

| Advantages | Disadvantages |
| :--- | :--- |
| **Modularity:** Rules are independent chunks of knowledge. Easy to add, remove, or modify. | **Inefficiency:** For large rule bases, the matching process can become computationally expensive. |
| **Naturalness:** `IF-THEN` structure is intuitive and easy for domain experts to understand. | **Conflict Resolution:** Multiple rules can be triggered simultaneously; choosing which one to fire next requires a strategy. |
| **Separation of Knowledge and Control:** The knowledge base (rules) is separate from the inference engine, providing clarity. | **Lack of Explanation:** While better than neural networks, explaining deep logical chains can sometimes be complex. |
| **Ability to Explain:** The system can trace its reasoning by listing the rules it fired to reach a conclusion. |  |

## Key Points / Summary

*   **Rule-based systems** represent knowledge using **IF-THEN production rules**.
*   The three key components are the **Knowledge Base** (rules), **Working Memory** (facts), and the **Inference Engine** (processor).
*   **Forward Chaining** is data-driven, moving from facts to a conclusion.
*   **Backward Chaining** is goal-driven, working backward from a hypothesis to supporting facts.
*   The main advantages include **modularity**, **natural representation**, and **explainable reasoning**.
*   They are the foundation for many **Expert Systems** used in medicine, diagnostics, and planning.
*   A key challenge is managing **rule conflicts** and ensuring efficiency in large systems.