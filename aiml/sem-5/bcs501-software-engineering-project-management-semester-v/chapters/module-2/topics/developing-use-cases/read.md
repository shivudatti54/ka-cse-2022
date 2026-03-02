# Module 2: Developing Use Cases (Software Engineering & Project Management)

## Introduction

In the world of software engineering, building a system that perfectly meets user needs is the ultimate goal. But how do you ensure you've captured all those needs accurately? This is where **Use Cases** come in. A use case is a powerful technique used primarily during the requirements elicitation and analysis phase. It describes a set of interactions between a system and its users (called "actors") to achieve a specific goal. Think of them as stories or scenarios that explain how the system will be used in the real world.

Developing use cases is crucial because they bridge the communication gap between stakeholders (clients, users) and the development team. They provide a clear, narrative-driven understanding of system functionality, which forms a solid foundation for design, development, and testing.

## Core Concepts

### 1. Actor
An **Actor** is a role played by a person, another system, or an external hardware device that interacts with the system under discussion. Actors are always external to the system.
*   **Primary Actor:** Initiates the use case to achieve a goal (e.g., a `Student` logging in).
*   **Secondary Actor:** Supports the system to complete the use case (e.g., the `Database` or an `Email Server`).

### 2. Use Case
A **Use Case** is a single unit of meaningful work. It defines a goal-oriented set of interactions between actors and the system. Each use case should represent a distinct functionality, such as `Login`, `Withdraw Cash`, or `Register for Course`.

### 3. System Boundary
A box that represents the scope of the system being developed. All use cases are placed inside this box, and actors are placed outside, visually clarifying what is part of the system and what is external to it.

### 4. Relationships
Actors and use cases are connected by associations (lines). Relationships between use cases themselves include:
*   **`<<include>>`**: Represents mandatory inclusion. One use case explicitly incorporates the behavior of another. (e.g., the `Withdraw Cash` use case *includes* the `Authenticate User` use case).
*   **`<<extend>>`**: Represents optional behavior. One use case (the extension) can add behavior to another under specific conditions (e.g., the `Request Overdraft` use case *extends* the `Withdraw Cash` use case only if the account is overdrawn).

## Components of a Use Case Description

A textual description provides the detailed story behind the diagram. A common template includes:

*   **Use Case Name:** e.g., `Register for Course`
*   **Actor(s):** `Student`, `Academic System` (secondary)
*   **Brief Description:** Describes the goal of the use case.
*   **Preconditions:** What must be true before the use case begins (e.g., "Student is logged in and has no registration holds").
*   **Basic Flow (Main Success Scenario):** The primary, happy path sequence of steps that leads to the goal.
*   **Alternative Flows:** Variations from the basic flow, including error conditions and exceptional behavior.
*   **Postconditions:** The state of the system after the use case completes successfully.

### Example: "Withdraw Cash" Use Case

**Use Case Name:** Withdraw Cash
**Primary Actor:** Bank Customer
**Secondary Actor:** Database
**Precondition:** Customer is authenticated, and ATM has sufficient cash.
**Basic Flow:**
1.  Customer inserts card and enters PIN.
2.  System validates PIN (`<<includes>>` Authenticate User).
3.  Customer selects "Withdraw Cash" and enters amount.
4.  System verifies account has sufficient funds.
5.  System dispenses cash, updates the database, and ejects the card.
6.  Customer takes the cash and card.
**Alternative Flow:**
*   **A1: Invalid PIN:** System prompts for re-entry (max 3 attempts).
*   **A2: Insufficient Funds:** System displays error message and cancels transaction.
**Postcondition:** Customer account balance is decreased by the withdrawal amount.

## Key Points & Summary

*   **Purpose:** Use cases are a technique for **capturing functional requirements** from a user's perspective. They describe *what* the system does, not *how* it does it.
*   **Focus on Goal:** Each use case is centered around a specific, user-valued goal.
*   **Foundation for Testing:** The scenarios (basic and alternative flows) directly form the basis for creating system test cases.
*   **Improves Communication:** They provide a common language that both technical and non-technical stakeholders can understand.
*   **Drives Design:** The structure and interactions identified in use cases often influence the initial architectural and detailed design of the system.
*   **Visual and Textual:** Effective use case modeling involves both **Use Case Diagrams** (for a high-level overview) and **Detailed Textual Descriptions** (for the complete specification of behavior).

In summary, mastering use cases is an essential skill for a software engineer. They are a practical tool to ensure the software you build aligns perfectly with user expectations and business goals, significantly reducing the risk of project failure.