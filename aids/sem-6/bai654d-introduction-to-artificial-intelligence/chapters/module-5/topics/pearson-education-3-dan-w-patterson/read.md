# Module 5: Introduction to Expert Systems & Knowledge Representation

## Introduction

This module focuses on a pivotal application of classical Artificial Intelligence: **Expert Systems**. Based on the reference from Dan W. Patterson's work in Pearson Education's materials, we will explore how human expertise is captured and replicated in a machine. An Expert System (ES) is a computer system that emulates the decision-making ability of a human expert in a specific, narrow domain. Its core purpose is to make scarce, expensive expertise widely available and to preserve knowledge.

---

## Core Concepts Explained

### 1. What is an Expert System?

An Expert System is a knowledge-based system that uses a **knowledge base** (KB) and an **inference engine** to solve complex problems that typically require human expertise. Unlike conventional procedural programs, ESs deal with symbolic reasoning and heuristics rather than just numerical calculations.

*   **Key Components:**
    *   **Knowledge Base:** This is the heart of the ES. It is a repository of facts, rules, procedures, and data representing the expert's knowledge. The knowledge is typically represented as **IF-THEN rules** (e.g., IF the engine does not start AND the lights are dim, THEN the battery is likely dead).
    *   **Inference Engine:** This is the brain of the ES. It is a software program that uses the knowledge base to draw conclusions. It applies logical rules to the known facts to infer new facts. Common inference strategies include **forward chaining** (data-driven) and **backward chaining** (goal-driven).
    *   **User Interface:** The medium through which the user communicates with the system, answering questions and receiving advice.
    *   **Explanation Facility:** A crucial feature that allows the ES to explain *how* it reached a conclusion and *why* it is asking a specific question, building user trust.

### 2. Knowledge Representation

This refers to the method used to encode knowledge into the knowledge base. Effective representation is critical for the inference engine to reason efficiently.

*   **Common Methods:**
    *   **Production Rules:** The most common method in ES. Knowledge is represented as a set of condition-action pairs: `IF <condition> THEN <action>`.
    *   **Semantic Nets:** A graphical representation where nodes represent objects or concepts, and arcs represent the relationships between them (e.g., an "is-a" relationship).
    *   **Frames:** A data structure that holds all information about a particular object or concept. Think of it as a form with slots to be filled (e.g., a "car" frame has slots for `make`, `model`, `engine-type`).

### 3. Inference Strategies

The inference engine uses these strategies to navigate the web of knowledge.

*   **Forward Chaining:** Starts with known facts and fires rules whose conditions are satisfied until a goal is reached. It is **data-driven**.
    *   *Example:* A medical diagnostic system starts with patient symptoms (data) and applies rules to eventually suggest a disease.
*   **Backward Chaining:** Starts with a hypothesis (a goal) and works backward to find evidence that supports it. It is **goal-driven**.
    *   *Example:* The same medical system starts with a possible disease (goal) and checks if the patient's symptoms match the known symptoms of that disease.

---

## Example: A Simple Car Diagnosis Expert System

Imagine a system designed to diagnose why a car won't start.

**Knowledge Base (Simplified Rules):**
1.  IF engine does NOT crank THEN problem is battery OR starter.
2.  IF lights are dim THEN problem is battery.
3.  IF engine cranks BUT does NOT start THEN problem is fuel OR spark.
4.  IF you smell fuel THEN problem is NOT fuel (it's spark).

**Scenario:** A user says, "My car won't start. The engine cranks normally, and I smell fuel."
1.  The inference engine (using backward chaining for the goal "find problem") starts with Rule 3 because the engine cranks.
2.  It investigates the "fuel" sub-goal. Rule 4 fires because the user smells fuel, concluding the problem is NOT fuel.
3.  It then investigates the "spark" sub-goal. No rules contradict this.
4.  The system concludes: "Problem is likely a spark issue (e.g., faulty spark plugs)." The explanation facility can show the user the rules (2 and 4) it used to reach this conclusion.

---

## Key Points / Summary

*   **Purpose:** Expert Systems are designed to replicate human expertise in a specific domain to make it consistent, permanent, and widely accessible.
*   **Core Components:** They are built on a **Knowledge Base** (facts & rules) and an **Inference Engine** (reasoning mechanism).
*   **Knowledge Representation:** Expertise is formally encoded using methods like production rules, semantic nets, and frames to enable machine reasoning.
*   **Inference:** The system uses **forward chaining** (from data to conclusion) or **backward chaining** (from goal to supporting data) to solve problems.
*   **Transparency:** The **Explanation Facility** is a defining feature, allowing users to understand the system's reasoning process, which is crucial for trust and debugging.
*   **Applications:** Historically and still today, ES are used in medical diagnosis, equipment repair, financial planning, and chemical analysis. They form the foundation for modern "chatbots" and decision support systems.