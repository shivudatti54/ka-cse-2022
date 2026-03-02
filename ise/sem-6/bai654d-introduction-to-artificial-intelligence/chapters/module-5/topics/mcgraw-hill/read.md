**Subject: Introduction to Artificial Intelligence**
**Module 5: Knowledge Representation and Reasoning**

# Module 5: Knowledge Representation and Reasoning (McGraw Hill Reference)

### Introduction

Knowledge Representation (KR) is a fundamental pillar of Artificial Intelligence. It is the field of study focused on how to represent information about the world in a form that an AI system can utilize to solve complex problems, reason, and make decisions. Without a robust method to store and manipulate knowledge, an AI agent cannot exhibit true intelligence. This module, often detailed in textbooks like those from **McGraw Hill**, covers the critical frameworks and languages used to formally encode knowledge for machine use. The ultimate goal of KR is to facilitate **knowledge engineering**—the process of building a knowledge base that an inference engine can use to derive new facts.

---

### Core Concepts of Knowledge Representation

A knowledge representation system must fulfill several key roles:
1.  **A Surrogate:** It must act as a substitute for the real world, allowing the AI to reason about the world by manipulating the representation.
2.  **A Set of Ontological Commitments:** It defines the vocabulary of concepts (objects, relations, properties) used to describe a domain.
3.  **A Fragmentary Theory of Intelligent Reasoning:** It provides the basis for the computational reasoning processes.
4.  **A Medium for Efficient Computation:** The structure should enable efficient storage and retrieval of information.
5.  **A Medium of Human Expression:** It should be understandable for humans to create and maintain the knowledge base.

#### 1. Types of Knowledge

*   **Declarative Knowledge:** Knowledge about facts and objects. It is static and describes "what is true" (e.g., "The sky is blue").
*   **Procedural Knowledge:** Knowledge about how to do things. It is dynamic and describes "how to perform a task" (e.g., the algorithm for solving a Rubik's cube).
*   **Meta Knowledge:** Knowledge about knowledge. It involves information about what the system knows and how it uses that knowledge.
*   **Heuristic Knowledge:** Rule-of-thumb knowledge based on practical experience rather than pure theory, often used to guide search and reasoning efficiently.

#### 2. Approaches to Knowledge Representation

##### A. Logical Representation
This approach uses formal logic to represent knowledge and draw conclusions. The most common type is **First-Order Logic (FOL)**, also known as Predicate Logic.
*   **Syntax:** Uses predicates, constants, variables, functions, and quantifiers (∀ for all, ∃ for exists).
*   **Example:**
    *   Fact: `Is_a(cat, mammal)` (A cat is a mammal).
    *   Rule: `∀x: Is_a(x, mammal) → Has(x, spine)` (All mammals have a spine).
    *   Inference: Therefore, we can conclude `Has(cat, spine)`.

##### B. Semantic Networks
A graphical representation where knowledge is represented as a network of nodes and arcs.
*   **Nodes** represent objects, concepts, or events.
*   **Arcs** represent the relationships between them (e.g., `is-a`, `has-part`, `located-in`).
*   **Example:** A network where the node "Robin" is connected to "Bird" with an `is-a` link, and "Bird" is connected to "Animal" with another `is-a` link. This allows for **inheritance**; the system can infer that a Robin has wings because it inherits properties from the Bird class.

##### C. Frames
A frame is a data structure that represents a stereotypical situation, object, or event. It is like a "form" to be filled out with specific information.
*   **Slots:** Attributes describing the frame. Slots can have default values.
*   **Example:** A `Car` frame would have slots like `Number-of-doors`, `Manufacturer`, `Engine-type`. A specific instance, `My-Car`, would fill these slots with values `4`, `Toyota`, `Hybrid`.

##### D. Rule-Based Systems
Knowledge is represented as a set of **IF-THEN** rules (production rules) and a **working memory** of facts.
*   **Inference Engine:** The brain of the system. It uses **forward chaining** (data-driven) to start from known facts and apply rules to deduce new facts until a goal is reached, or **backward chaining** (goal-driven) to start with a hypothesis and work backwards to see if it is supported by known facts.
*   **Example (Medical Diagnosis):**
    *   Rule: `IF patient has high fever AND patient has a rash THEN suggest diagnosis = measles`
    *   Working Memory: `patient has high fever`, `patient has a rash`
    *   Inference: The rule is triggered, and `diagnosis = measles` is added to memory.

##### E. Ontologies
An ontology is a formal, explicit specification of a shared conceptualization. It defines a common vocabulary for researchers and a taxonomy of concepts and their interrelationships within a domain. They are crucial for the **Semantic Web**.

---

### Key Points and Summary

*   **Purpose:** Knowledge Representation is essential for enabling intelligent behavior through reasoning.
*   **Core Trade-off:** A key challenge is the trade-off between **expressiveness** (the breadth of what can be represented) and **computational efficiency**.
*   **Major Approaches:** The primary methods include **Logical representations** (precise and mathematical), **Semantic Networks & Frames** (intuitive and hierarchical), and **Rule-Based Systems** (good for expert systems).
*   **The Role of Reasoning:** Representation is useless without **reasoning**—the process of using the knowledge base to answer questions and derive new information. This is done via logical deduction, inheritance, or rule inference.
*   **Foundation for AI:** Mastering KR is a prerequisite for advanced AI topics like Natural Language Processing, Expert Systems, and Robotics, as it provides the foundational "knowledge" these systems operate on. Textbooks like those from **McGraw Hill** provide structured learning paths through these complex topics.