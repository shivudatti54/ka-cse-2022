# Module 5: Knowledge Representation (K. Knight & S. B. Nair) - Introduction to Artificial Intelligence

## Introduction

Knowledge Representation (KR) is a fundamental pillar of Artificial Intelligence. It is the field of study concerned with how an AI system's knowledge about the world can be represented in a formal, symbolic language that the computer can utilize to reason, solve problems, and make decisions. The work of researchers like **Kevin Knight** and **S. B. Nair** has significantly contributed to this area, particularly in formal logic-based representation and structured representation using frames and semantic networks. This module explores these core KR schemes, which are essential for building intelligent systems that can effectively model and interact with their environment.

## Core Concepts of Knowledge Representation

The primary goal of KR is to create a surrogate inside an AI agent—a symbolic model of the world that it can manipulate. A good knowledge representation scheme must possess four essential properties:

1.  **Representational Adequacy:** The ability to represent all necessary knowledge about the domain.
2.  **Inferential Adequacy:** The ability to manipulate the represented knowledge to derive new conclusions.
3.  **Inferential Efficiency:** The ability to direct the inferential mechanisms to use the most appropriate knowledge efficiently.
4.  **Acquisitional Efficiency:** The ability to acquire new knowledge easily, either automatically or from human experts.

Two prominent and complementary schemes for KR are **Logical Representation** and **Structured Representation**.

### 1. Logical Representation (Propositional & First-Order Logic)

Logic provides a formal language with precise syntax (how sentences are formed) and semantics (what they mean). It is a declarative approach, where we state what is true, and the inference engine figures out what else must be true.

*   **Propositional Logic (PL):** The simplest form. It deals with propositions (statements) that are either `True` or `False`. These propositions can be combined using logical connectives like AND (`∧`), OR (`∨`), NOT (`¬`), IMPLIES (`→`), and IF AND ONLY IF (`↔`).
    *   **Example:** `It_Is_Raining → The_Grass_Is_Wet`. This is a simple rule. If "It_Is_Raining" is true, we can infer that "The_Grass_Is_Wet" is also true.

*   **First-Order Logic (FOL) / Predicate Logic:** A much more powerful and expressive language. FOL extends propositional logic by introducing:
    *   **Objects:** Constants (e.g., `John`, `Book1`).
    *   **Relations/Predicates:** Properties of objects or relationships between them (e.g., `Student(John)`, `On(Book1, Table)`).
    *   **Functions:** Mappings from objects to objects (e.g., `FatherOf(John)`).
    *   **Quantifiers:** `∀` (for all) and `∃` (there exists).
    *   **Example:** `∀x [Student(x) ∧ Has(x, Assignment) → ShouldSubmit(x, Assignment)]`. This rule states: "For all x, if x is a student and x has an assignment, then x should submit the assignment." This single, general rule can apply to all students, unlike in propositional logic where we would need a separate rule for each student.

### 2. Structured Representation (Frames & Semantic Networks)

While logic is powerful, it can be verbose for representing complex, hierarchical real-world knowledge. Structured representations offer a more intuitive, organized way to model knowledge.

*   **Semantic Networks:** A graphical form of representation consisting of **nodes** (representing objects, concepts, or events) and **arcs** (representing relationships between them). They are excellent for representing inheritance (e.g., "an apple *is a* fruit") and other semantic relationships.
    *   **Example:** A node for "Bird" is connected to "Has-Wings" and "Can-Fly." A node for "Penguin" is connected to "Bird" with an *is-a* link, but also has a property "Can-Fly = False," which overrides the inherited property.

*   **Frames:** A frame is a data structure that holds a collection of **attributes** (called slots) about a stereotypical object, situation, or concept. Frames are organized in a hierarchy, allowing lower-level frames to **inherit** properties from higher-level frames. This is closely related to object-oriented programming.
    *   **Example:** A frame for the class `Vehicle` might have slots for `Number-of-Wheels` and `Engine-Type`. A frame for `Car` *inherits* from `Vehicle` and fills the `Number-of-Wheels` slot with the value `4`. Another frame for `Bicycle` (inheriting from `Vehicle`) might fill the `Engine-Type` slot with `None`.

## Key Points & Summary

| Concept | Description | Key Feature |
| :--- | :--- | :--- |
| **Knowledge Representation (KR)** | The symbolic model of the world inside an AI agent. | Foundation for reasoning and intelligent behavior. |
| **Logical Representation** | Uses formal logic (PL, FOL) to declare facts and rules. | **Precise and declarative.** Excellent for automated reasoning and theorem proving. |
| **Structured Representation** | Uses networks (Semantic Nets) or structures (Frames) to organize knowledge. | **Intuitive and hierarchical.** Excellent for representing inheritance and default knowledge. |
| **Inheritance** | A mechanism where a concept can acquire properties from a more general concept. | Central to frames and semantic nets; promotes efficiency and avoids redundancy. |

In practice, modern AI systems often use a hybrid approach, combining the rigorous inferential capabilities of logic with the efficient, human-like organization of structured representations. Understanding these foundational schemes, as explored by experts like Knight and Nair, is crucial for designing the "brain" of any sophisticated AI application.