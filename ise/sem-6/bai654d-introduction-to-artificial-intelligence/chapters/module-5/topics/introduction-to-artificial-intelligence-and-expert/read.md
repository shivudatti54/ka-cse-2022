# Module 5: Introduction to Artificial Intelligence and Expert Systems

## 1. Introduction

Welcome to Module 5 of our Introduction to Artificial Intelligence series. This module bridges the foundational concepts of AI with one of its most successful and historically significant applications: **Expert Systems**. These systems were the hallmark of the AI boom in the 1980s and represent a practical approach to encapsulating human expertise in a software program. For engineering students, understanding expert systems provides a concrete example of how logical reasoning and knowledge representation are implemented in real-world AI solutions.

## 2. Core Concepts

### What is an Expert System (ES)?

An Expert System is a computer system that emulates the decision-making ability of a human expert. It is designed to solve complex problems in a specific domain (e.g., medical diagnosis, chemical analysis, mechanical fault detection) by reasoning about knowledge, represented primarily as **IF-THEN rules**, rather than by following conventional procedural code.

The power of an ES does not come from complex algorithmic procedures but from the **knowledge** it contains.

### Key Components of an Expert System

An expert system's architecture typically consists of three core components:

1.  **Knowledge Base:** This is the heart of the system. It is a repository of domain-specific facts, rules, procedures, and heuristics (rules of thumb) gathered from human experts. In a rule-based system, knowledge is stored as a set of production rules:
    `IF <condition> THEN <action/conclusion>`
    *   *Example:* `IF the engine does not crank AND the headlights are dim THEN the battery is likely dead (Probability: 85%)`

2.  **Inference Engine:** This is the brain of the system. It is a generic control mechanism that uses the knowledge from the Knowledge Base to draw conclusions and solve problems. It works by selecting applicable rules and executing them, a process known as **reasoning**. The two primary reasoning strategies are:
    *   **Forward Chaining (Data-Driven):** Starts with known facts and uses inference rules to extract more data until a desired goal is reached. It is like a breadth-first search. *Ideal for problems like planning, monitoring, and control.*
    *   **Backward Chaining (Goal-Driven):** Starts with a hypothesis (a goal) and works backward to find evidence that supports it. It is like a depth-first search. *Ideal for diagnostic and recommendation systems.*

3.  **User Interface:** This is the communication channel through which the user interacts with the expert system. The user inputs data, answers questions posed by the system, and receives advice, explanations, or recommendations.

Two other important, but optional, components are:
*   **Explanation Facility:** Justifies its reasoning by explaining *how* it reached a conclusion (by tracing the chain of rules used) and *why* it is asking a specific question. This transparency builds user trust.
*   **Knowledge Acquisition Facility:** A tool that helps knowledge engineers extract knowledge from human experts and feed it into the knowledge base. This is often the bottleneck in developing ES.

### The Development Process

The creation of an expert system is carried out by a team typically involving:
*   **Domain Expert:** The human whose expertise is being captured (e.g., a senior engineer).
*   **Knowledge Engineer:** The AI specialist who designs and builds the expert system by "interviewing" the domain expert and encoding their knowledge.
*   **End User:** The person who will ultimately use the finished system.

## 3. Example: A Simple Diagnostic System

Imagine a system designed to diagnose why a car won't start.

**Knowledge Base (Simplified Rules):**
1.  IF engine does not crank THEN problem is with starting system.
2.  IF engine does not crank AND headlights are dim THEN battery is dead.
3.  IF engine does not crank AND headlights are normal THEN starter motor is faulty.
4.  IF engine cranks but does not start THEN problem is with fuel or spark.
5.  IF engine cranks but does not start AND fuel gauge is empty THEN out of fuel.

**Scenario:** A user interacts with the system.
1.  The **Inference Engine** (using backward chaining) starts with the goal: `find fault`.
2.  It uses Rule 1 and asks the user: "Does the engine crank?"
3.  User inputs: `No`.
4.  The engine now knows the problem is with the starting system. It activates Rules 2 and 3.
5.  It asks the user: "Are the headlights dim?"
6.  User inputs: `Yes`.
7.  The engine executes Rule 2 and concludes: "The battery is likely dead."
8.  The **Explanation Facility** can tell the user: "I concluded the battery is dead because you stated the engine does not crank and the headlights are dim."

## 4. Key Points & Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Definition** | A computer system that mimics the decision-making of a human expert in a narrow domain. |
| **Core Idea** | The power is in the knowledge, not just the algorithms. **Knowledge + Inference = Expertise** |
| **Key Components** | Knowledge Base (rules/facts), Inference Engine (reasoning), User Interface. |
| **Reasoning Methods** | **Forward Chaining:** Data-driven, from facts to conclusion. <br> **Backward Chaining:** Goal-driven, from hypothesis to facts. |
| **Advantages** | • Permanence & reproducibility of expertise.<br>• Documentation and explanation of reasoning.<br>• Enhanced decision consistency. |
| **Disadvantages** | • Limited to narrow domains.<br>• Knowledge acquisition is difficult and expensive (the "bottleneck").<br>• Lacks common sense and cannot learn automatically (traditional ES). |
| **Legacy** | Expert Systems paved the way for modern knowledge-based systems and demonstrated the value of explicit knowledge representation. Their principles are foundational to today's decision-support systems and diagnostic tools used across engineering disciplines. |

Expert systems represent a crucial step in applied AI, demonstrating how to effectively capture and utilize human expertise to solve well-defined, complex problems.