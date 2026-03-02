# Module 1: Software Process Models - Concurrent Models

## Introduction

Traditional software process models like the Waterfall model operate in a linear, sequential manner, where a new phase begins only after the previous one is complete. This approach is often unrealistic for modern, complex projects where requirements evolve and tasks can overlap. The **Concurrent Model**, also known as Concurrent Engineering, addresses this by allowing multiple activities to progress simultaneously. It provides a more accurate representation of the state of a project and is particularly suited for client-server and web application development where different components are developed at different times and rates.

## Core Concepts of the Concurrent Model

The fundamental idea behind the concurrent model is that any software engineering activity can be in one of several **states** at any given time. The model is often represented as a series of fundamental software engineering activities (e.g., modelling, code generation, testing) surrounded by a set of **triggering events**.

### 1. The State-Transition Representation

The model defines a **network** of activities. Instead of a simple sequence, each activity (e.g., Requirements Modeling) can be in one of the following states:
*   **Inactive:** The activity has not yet commenced.
*   **Under Review:** The activity is currently being performed but is not yet complete.
*   **Awaiting Changes:** The activity is complete but is pending modifications based on changes in another activity.
*   **Under Revision:** The activity is currently being modified.
*   **Done:** The activity is completed and requires no further work.

A state transition occurs when an event (e.g., a requirement change is requested) triggers a shift. For instance, a completed design (Done state) might move back to the **Under Revision** state if a coding activity uncovers a flaw.

### 2. The Concurrency Dimension in Development

The model recognizes that while development activities can happen concurrently, they all stem from a common core. The process begins with the **Business Modeling** activity. As requirements are outlined, the subsequent activities branch into their own concurrent threads.

*   **Example:** Early in a project, the team might be finalizing requirements (Requirements Modeling - *Under Review*) while a separate team begins preliminary architectural design for the known requirements (Design - *Under Review*). Meanwhile, the user interface prototyping activity might be *Inactive*.

### 3. Event-Driven Transitions

The entire network of activities is driven by **events**. The completion of part of an activity, or a change request, becomes an event that triggers a transition in another activity. This creates a dynamic system where progress and change are continuously integrated.

*   **Example:** The completion of a software component's coding (an event) will trigger the testing activity to move from *Inactive* or *Awaiting Changes* to *Under Review*. If testing uncovers a defect, it generates an event that sends the corresponding design and coding activities back to the *Under Revision* state.

## A Practical Example: E-commerce Website Development

Consider building an e-commerce website with features like a product catalog, user login, and a shopping cart.

1.  **Initial Phase:** The team starts with **Requirements Modeling** for the entire system. As the high-level features are agreed upon, this activity is *Under Review*.
2.  **Concurrent Activities:**
    *   The team responsible for the product catalog begins **Design** and then **Construction** (coding) for that module.
    *   Simultaneously, another team starts **Design** for the user authentication module. Their progress is independent but aligned to the overall requirements.
3.  **Triggering an Event:** During the construction of the shopping cart, a developer realizes a performance issue with the initial design. This is an event.
4.  **State Transition:** This event triggers:
    *   The shopping cart's **Design** activity to re-enter the *Under Revision* state.
    *   Its **Construction** activity is put *On Hold* or moved to *Awaiting Changes* until the design is revised.
    *   The **Testing** activity for this module remains *Inactive*.
5.  **Resumption:** Once the design is revised and approved (moves back to *Done*), it triggers the Construction activity to resume (*Under Revision*).

This entire process happens while other teams continue work on their stable modules without interruption.

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Core Idea** | Moves away from a linear flow to a network of activities that can occur simultaneously and be in different states. |
| **Representation** | Uses a **state-transition** model (e.g., Inactive, Under Review, Done, Under Revision) to represent the status of each activity. |
| **Driver** | Progress is **event-driven**. The completion or change in one activity triggers a state change in another. |
| **Advantages** | <ul><li>**Accurate Project View:** Provides a realistic snapshot of the project's true status.</li><li>**Manages Change Well:** Handles evolving requirements and iterative development effectively.</li><li>**Efficiency:** Allows multiple teams to work concurrently on different system components.</li></ul> |
| **Disadvantages** | <ul><li>**Complexity:** Can be difficult to manage due to the need to track numerous concurrent activities and their dependencies.</li><li>**Communication Overhead:** Requires excellent communication between teams to avoid integration issues.</li></ul> |
| **Best For** | **Large-scale projects** with clearly defined components, **reactive systems**, and **projects where requirements are expected to change** frequently. |