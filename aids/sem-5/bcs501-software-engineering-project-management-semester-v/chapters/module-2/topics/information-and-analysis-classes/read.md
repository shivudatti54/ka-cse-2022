# Module 2: Information and Analysis Classes in Software Engineering

**Subject:** Software Engineering & Project Management  
**Semester:** V

## Introduction

In the Unified Process and Unified Modeling Language (UML), the analysis phase is critical for transforming vague user requirements into a clear, structured model of the system-to-be. This module focuses on two pivotal types of analysis classes: **Entity**, **Boundary**, and **Control** classes. Together, these form the **Entity-Control-Boundary (ECB)** pattern (also known as the **Model-View-Controller (MVC)** analogy in analysis), which provides a robust and scalable structure for understanding a system's architecture during object-oriented analysis.

## Core Concepts: The ECB Pattern

The ECB pattern is a stereotype mechanism in UML that helps analysts categorize classes based on their specific responsibilities within the system. This separation of concerns makes the model easier to understand, maintain, and evolve.

### 1. Entity Classes (Model)

Entity classes represent persistent information tracked by the system. They are typically long-lived, often corresponding to real-world entities or major concepts within the problem domain. Their state must survive the execution of a single use case or even the entire application session.

*   **Responsibility:** To hold and manage data or business logic.
*   **Characteristics:** Often mapped to database tables; contain attributes and relationships that define their state.
*   **Example:** In a `Library Management System`, entity classes would include `Book`, `Member`, `LoanRecord`, and `Author`. The `Book` class would have attributes like `ISBN`, `title`, `author`, and `publicationYear`.

### 2. Boundary Classes (View)

Boundary classes model the interaction between the system and its external actors (users or other systems). They act as a protective interface, insulating the system's inner workings from changes in the external environment.

*   **Responsibility:** To handle all communication and translation between actors and the system.
*   **Characteristics:** Often associated with user interfaces (screens, reports, menus) or system interfaces (APIs, communication protocols).
*   **Example:** In the same library system, boundary classes would include `LoginScreen`, `SearchBookForm`, `CheckOutWindow`, and a `PrinterInterface` class for generating receipts. If the user interface changes from a window to a web page, only the boundary classes need modification.

### 3. Control Classes (Controller)

Control classes encapsulate application-specific business logic or workflow. They coordinate the processing of a use case, managing the sequencing of events, decision-making, and transactions. They act as the "glue" between boundary and entity objects.

*   **Responsibility:** To execute the business rules and coordinate the behavior of other objects for a specific task.
*   **Characteristics:** Often stateful for the duration of a use case but are not typically persistent; they represent the dynamic behavior of the system.
*   **Example:** For the "Borrow a Book" use case, a `LoanTransactionMgr` control class would be created. It would receive input from the `CheckOutWindow` (boundary), validate the `Member` status (entity), update the `Book` availability status (entity), and create a new `LoanRecord` (entity).

## Interaction in a Use Case

Let's see how these classes collaborate for the "Borrow a Book" use case:

1.  The actor (Librarian) interacts with the `CheckOutWindow` (**Boundary**).
2.  The `CheckOutWindow` captures the member ID and book ISBN and passes this information to the `LoanTransactionMgr` (**Control**).
3.  The `LoanTransactionMgr` coordinates the operation:
    *   It asks the `Member` (**Entity**) to validate the membership.
    *   It asks the `Book` (**Entity**) to check its availability.
    *   If all checks pass, it creates a new `LoanRecord` (**Entity**).
4.  The `LoanTransactionMgr` informs the `CheckOutWindow` of the success.
5.  The `CheckOutWindow` finally displays a confirmation message to the librarian.

This clear separation ensures that changes to the user interface (Boundary) or business rules (Control) do not directly impact the core data model (Entity).

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Purpose** | To decompose and structure the requirements captured from use cases into a robust object-oriented analysis model. |
| **Main Classes** | **Entity (Model):** Represents persistent data. <br> **Boundary (View):** Handles system-actor interaction. <br> **Control (Controller):** Manages business logic and workflow. |
| **Key Benefit** | **Separation of Concerns.** This makes the system more resilient to change. UI changes affect only Boundary classes, while business rule changes are localized to Control classes. |
| **Identification** | **Boundary:** From use case actors. <br> **Entity:** From nouns in the problem domain. <br> **Control:** From complex use case steps or workflows. |
| ** Relevance** | Understanding ECB is crucial for answering questions on object-oriented analysis, use case realization, and creating analysis class diagrams, which are common in  examinations. |
| **Next Step** | These analysis classes form the foundation for the subsequent design phase, where they are refined into detailed design classes with complete attributes, methods, and relationships. |

In conclusion, the ECB pattern provides a disciplined and systematic approach to analysis, ensuring a clean and maintainable structure for the software system from the very beginning of its development.