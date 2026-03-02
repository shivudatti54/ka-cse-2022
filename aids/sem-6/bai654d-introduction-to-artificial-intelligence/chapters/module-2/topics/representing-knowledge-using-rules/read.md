# Module 2: Representing Knowledge Using Rules

## Introduction

In Artificial Intelligence, knowledge representation is the fundamental pillar that enables an intelligent agent to store and utilize information for reasoning and problem-solving. Among the various paradigms for representing knowledge, **rule-based systems** are one of the most intuitive and widely used methods. This approach captures knowledge in the form of simple **IF-THEN** statements, closely mimicking human expertise and decision-making processes. This module explores how rules are used to encode knowledge effectively.

## Core Concepts

### 1. What is a Rule?

A rule is a conditional statement that represents a piece of knowledge or a heuristic. It has two main parts:

*   **Antecedent (IF part):** This is the condition or the premise. It is a conjunction of one or more facts or patterns.
*   **Consequent (THEN part):** This is the action or the conclusion that is drawn if the antecedent is satisfied.

**Syntax:** `IF <condition(s)> THEN <action/conclusion>`

### 2. Rule-Based Systems (RBS)

A collection of such rules forms a **Rule-Based System**, often referred to as a **Production System**. The core components of a Production System are:

*   **Rule Base (Knowledge Base):** This is the heart of the system—a set of rules that encapsulate the domain knowledge.
*   **Working Memory:** A global database that contains the known facts, assertions, and data (the current state of the world) against which the rules are matched.
*   **Inference Engine:** This is the "brain" of the system. It is an algorithm that matches the rules against the facts in the working memory to determine which rules are applicable. It then selects and executes (fires) a rule, which may add new facts or modify the working memory.

### 3. The Inference Process

The inference engine primarily uses one of two strategies to control the reasoning process:

*   **Forward Chaining (Data-Driven Reasoning):** The engine starts with the known facts in the working memory. It checks the IF part of all rules to see which ones are triggered by these facts. When a rule fires, its THEN part is executed, potentially adding a new fact to the working memory. This process repeats until a desired goal state is reached or no more rules can fire.
    *   *Analogy:* You have some ingredients (data) and you use recipes (rules) to see what you can make (conclusion).

*   **Backward Chaining (Goal-Driven Reasoning):** The engine starts with a hypothesis or a goal it wants to prove. It then looks for rules whose THEN part (consequent) can conclude that goal. It checks the IF part (antecedent) of those rules, which themselves become new sub-goals to be proven. This process continues recursively until all sub-goals are satisfied by existing facts or until it fails.
    *   *Analogy:* You decide what dish you want to make (goal) and check the recipe (rule) to see what ingredients (facts) you need.

## Example: A Simple Diagnostic System

Let's encode knowledge for a system that diagnoses why a car won't start.

**Rule Base:**
1.  `IF fuel_gauge_is_empty THEN problem_is(out_of_fuel)`
2.  `IF engine_does_not_crank AND lights_are_dim THEN problem_is(dead_battery)`
3.  `IF engine_does_not_crank AND lights_are_bright THEN problem_is(starter_motor_fault)`
4.  `IF engine_cranks_but_does_not_start THEN problem_is(no_spark)`

**Scenario 1 (Forward Chaining):**
*   **Working Memory Facts:** `[engine_does_not_crank, lights_are_dim]`
*   **Process:** The inference engine scans the rules. Rule 2 has an IF part that perfectly matches the facts (`engine_does_not_crank` AND `lights_are_dim`). It fires Rule 2.
*   **Result:** The new fact `problem_is(dead_battery)` is added to working memory. The diagnosis is complete.

**Scenario 2 (Backward Chaining):**
*   **Goal:** To prove `problem_is(dead_battery)`.
*   **Process:** The engine finds Rule 2, whose THEN part matches the goal. To prove Rule 2, it must now prove the antecedents `engine_does_not_crank` and `lights_are_dim`. It checks the working memory for these facts. If they are present, the original goal is proven.

## Advantages and Disadvantages

| Advantages                                                                 | Disadvantages                                                               |
| :------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Modularity:** Rules are independent, making knowledge easy to add/remove. | **Inefficiency:** Can be slow for large rule bases due to pattern matching.  |
| **Natural Representation:** Easy to understand and articulate.             | **Lack of structure:** Poor at representing complex hierarchical knowledge. |
| **Explanation:** The chain of fired rules provides a clear trace of reasoning. | **Conflict Resolution:** Choosing which rule to fire next can be complex.   |

## Key Points / Summary

*   **Intuitive Format:** Knowledge is represented as **IF-THEN** rules, which is a natural way to express human expertise and heuristics.
*   **Core Components:** A Rule-Based System consists of a **Rule Base** (set of rules), **Working Memory** (set of facts), and an **Inference Engine** (processing unit).
*   **Two Reasoning Styles:**
    *   **Forward Chaining** is data-driven, starting from facts to find a conclusion.
    *   **Backward Chaining** is goal-driven, starting from a hypothesis and proving it with facts.
*   **Well-Suited For:** Diagnostic systems, expert systems, classification problems, and procedural knowledge encoding.
*   **Key Trade-off:** Offers excellent modularity and explainability but can become inefficient and unstructured as the scope of knowledge grows very large.