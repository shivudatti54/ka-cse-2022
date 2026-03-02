# Module 5: Representing and Using Domain Knowledge

## Introduction

In Artificial Intelligence, an agent's ability to act intelligently is fundamentally tied to its knowledge of the world, or its **domain knowledge**. This module moves beyond simple problem-solving agents and delves into how to formally represent complex, real-world information so a machine can understand and reason with it. Effective knowledge representation is the bridge between raw data and intelligent action, forming the core of **knowledge-based systems**.

## Core Concepts

### 1. What is Domain Knowledge?

Domain knowledge is the specific, specialized knowledge about a particular application area. For example, in a medical diagnosis system, domain knowledge includes symptoms, diseases, treatments, and the causal relationships between them. Representing this knowledge involves choosing a formal structure (a **knowledge representation language**) that a computer can process.

### 2. The Role of a Knowledge Base (KB)

The Knowledge Base is a central component of a knowledge-based agent. It is a store of facts and rules about the world, represented in a formal language. The agent can:
*   **TELL** the KB new sentences (add knowledge).
*   **ASK** the KB questions (query knowledge).

The KB, with the help of an **inference engine**, derives new knowledge from the existing facts and rules.

### 3. Properties of a Good Knowledge Representation Scheme

A effective KR scheme should possess:
*   **Adequacy**: It must be able to represent all necessary knowledge about the domain.
*   **Inferential Adequacy**: It should allow new knowledge to be inferred from the existing knowledge.
*   **Efficiency**: The inference process should be computationally efficient.
*   **Naturalness**: It should be intuitive for humans to understand and encode the knowledge.

### 4. Key Knowledge Representation Techniques

#### a. Logical Representations (Propositional & First-Order Logic)
Logic uses formal syntax and semantics to represent knowledge as unambiguous logical sentences.
*   **Propositional Logic**: Facts are represented as symbols that can be either true or false. Useful for simple domains.
    *   Example: `IS_SUNNY ⇒ WEAR_SUNGLASSES`
*   **First-Order Logic (FOL)**: More powerful. It uses objects, relations, functions, and quantifiers (`∀` for all, `∃` there exists).
    *   Example: `∀x [ENGINEER(x) ⇒ STUDIED_LOGIC(x)]` (All engineers have studied logic).

#### b. Semantic Nets
A graphical representation where knowledge is stored as a network of nodes (objects/concepts) and arcs (relationships between them). It is intuitive and supports property inheritance.
*   **Example**: A semantic net for "" might have nodes for `University`, ``, `Engineering_Student`, and `Course`. Arcs would show ` is-a University`, `Engineering_Student attends `, and ` offers Course`. The `is-a` link allows `` to inherit properties from `University` (e.g., it has a chancellor, offers degrees).

#### c. Frames
A frame is a data structure that represents a stereotypical object, concept, or event. It contains **slots** (attributes) and their **fillers** (values). Frames are organized in a hierarchy, allowing for inheritance of slot values from more general frames (superclasses) to more specific ones (subclasses).
*   **Example**: A `Car` frame would have slots like `Number-of-Wheels: 4` and `Has-Engine: Yes`. A `Sports-Car` frame, which `is-a` `Car`, would inherit these slots but might have its own slot for `Top-Speed: 200 kmph`.

#### d. Scripts
A script is a structured representation of a stereotypical sequence of events in a specific context. It describes what happens in a standard situation, like going to a restaurant or a lecture.
*   **Example**: A `Restaurant` script would have slots for **Roles** (customer, waiter, chef), **Props** (menu, table, food), **Entry Conditions** (customer is hungry), **Scene 1: Entering**, **Scene 2: Ordering**, **Scene 3: Eating**, **Scene 4: Exiting**, and **Results** (customer is full, has less money). This helps an AI understand and answer questions about such events.

## Key Points & Summary

| Key Point | Description |
| :--- | :--- |
| **Purpose** | To encode real-world information in a formal, machine-readable format to enable reasoning and intelligent behavior. |
| **Knowledge Base (KB)** | The central repository of facts and rules about a domain. |
| **Inference Engine** | The component that derives new knowledge from the KB. |
| **Common Techniques** | **Logic** (precise, formal), **Semantic Nets** (intuitive, graphical), **Frames** (object-oriented, hierarchical), **Scripts** (for event sequences). |
| **Inheritance** | A powerful mechanism (in nets and frames) where subclasses inherit properties from superclasses, promoting efficiency and reducing redundancy. |
| **Choice of KR** | The best method depends on the specific domain and the type of reasoning required (e.g., logical deduction, pattern matching, inheritance). |

**In essence, representing domain knowledge is not just about storing data; it's about structuring it in a way that captures relationships, meaning, and context, empowering an AI agent to solve complex problems.**