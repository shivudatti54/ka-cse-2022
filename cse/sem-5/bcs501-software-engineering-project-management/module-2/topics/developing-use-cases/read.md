# Developing Use Cases

## Introduction

Use cases represent a formalized technique for capturing and specifying functional requirements from a user-centered perspective. Developed by Ivar Jacobson in 1986 and subsequently incorporated into the Unified Modeling Language (UML), use cases provide a structured approach to understanding system behavior as viewed by external entities. This methodology bridges the conceptual gap between technical system implementation and genuine user needs, establishing itself as an indispensable competency for software engineers engaged in requirements engineering.

Within the Software Engineering curriculum, use case development constitutes a critical component of the requirements gathering and analysis phase. A use case articulates the manner in which users interact with a system to accomplish specific objectives. Unlike conventional functional specifications that emphasize internal system operations, use cases prioritize the value delivered to end-users. This user-centric paradigm ensures that developed software systems address authentic business requirements and provide meaningful functionality aligned with stakeholder expectations.

The significance of use cases extends substantially beyond basic requirement documentation. They serve multiple critical functions: acting as communication vehicles between diverse stakeholders (users, developers, project managers, and quality assurance teams); providing a foundation for test case generation through scenario coverage; facilitating identification of system boundaries and scope; and supporting iterative and agile development methodologies. Furthermore, use cases establish traceability links to subsequent design artifacts and implementation components, enabling impact analysis during system evolution. Mastery of use case development therefore remains essential for software engineers operating in contemporary development environments characterized by complex stakeholder interactions and evolving requirements.

## Theoretical Foundation

### Formal Definition

A use case constitutes a specification of behavior that a system can perform in collaboration with external actors. Formally, a use case represents a collection of related scenarios connecting preconditions to postconditions through a sequence of system interactions. Each use case must represent a complete, meaningful unit of functionality that delivers measurable value to at least one actor.

**Definition**: A use case U is defined as a tuple U = (A, P, Q, S, E) where A denotes the set of actors, P represents preconditions, Q represents postconditions, S denotes the basic flow (success scenario), and E represents the set of alternative flows including error conditions.

This formal characterization enables rigorous analysis of use case completeness and consistency. The preconditions P must be satisfiable (there exists a valid system state where P holds), and the postconditions Q must be achievable from states satisfying P through the execution of S or E.

### System Boundary and Actor Classification

The system boundary defines the scope of functionality exposed to external entities. This boundary is explicitly represented in UML use case diagrams and serves to clarify what remains inside versus outside the system under development. Establishing correct system boundaries is critical as it determines which functionalities require use case specifications and which represent external system interactions.

Actors are classified into two categories based on their interaction patterns:

- **Primary Actors**: Users who initiate use cases to achieve specific goals and receive tangible value from the system. For instance, in a library management system, the "Library Member" constitutes a primary actor for use cases such as "Borrow Book" and "Return Book."

- **Secondary Actors**: Entities that provide services to the system but do not initiate use cases. These actors respond to system requests and include external systems, support personnel, and automated services. In an ATM system, the "Bank Database" functions as a secondary actor that validates account information upon system request.

## Components of Use Cases

A comprehensive use case specification encompasses multiple essential components that collectively define system behavior from the user perspective:

### 1. Use Case Name

The use case name must be descriptive, action-oriented, and verb-inflected, clearly indicating the specific goal being accomplished. Effective names follow the pattern "Verb + Object" (e.g., "Withdraw Cash," "Register Student," "Place Order") and should be sufficiently specific to distinguish this use case from related ones while remaining concise enough for diagram representation.

### 2. Actors

Actors represent external entities that interact with the system but constitute no part of the system itself. An actor may be a human user, an external system, or a hardware device. Crucially, actors are defined by their role rather than as specific individuals—a single physical person may play multiple actor roles (e.g., both "Customer" and "Administrator" in an e-commerce system).

### 3. Preconditions and Postconditions

**Preconditions** establish the conditions that must be true before the use case execution commences. These conditions define the system state or context required for the use case to proceed validly. Preconditions represent guarantees that the system assumes, not guarantees it establishes—they are obligations that must be satisfied by preceding use cases or external initialization.

**Postconditions** define the conditions that must hold true after the use case completes successfully. Postconditions represent the definitive outcomes or state changes guaranteed by the system regardless of which flow (basic or alternative) was followed. Strong postconditions enhance use case utility for testing and validation by providing clear success criteria.

**Theorem (Use Case Completeness)**: A use case is complete if and only if for every valid initial state satisfying its preconditions, execution of either the basic flow or an alternative flow terminates in a state satisfying the postconditions.

### 4. Basic Flow (Main Success Scenario)

The basic flow describes the primary sequence of steps leading to successful use case completion. This scenario represents the most common and expected interaction path, executed when no exceptional conditions arise. Each step in the basic flow should specify a single atomic interaction between an actor and the system, using active voice and present tense. Steps must be numbered sequentially and should include both actor actions and system responses.

### 5. Alternative Flows (Alternate Scenarios)

Alternative flows capture variations from the basic flow that handle different conditions, errors, or exceptional situations. These flows document optional functionality, branching decision points, and error handling mechanisms. Each alternative flow must specify its triggering condition and the point in the basic flow where it branches.

### 6. Extensions and Extension Points

Extensions represent the precise locations within the basic flow where alternative behaviors may occur. Extension points are explicitly designated steps in the basic flow where extension use cases can be triggered based on specific conditions. This explicit specification enables modular composition of complex behaviors from simpler use cases.

## Use Case Relationships

Use case relationships define how use cases interact with and depend upon each other, enabling reuse and behavioral extension through composition.

### Include Relationship

The include relationship specifies that one use case (the including use case) explicitly incorporates the behavior of another use case (the included use case). This relationship is mandatory—the including use case cannot complete without executing the included behavior. Include relationships eliminate redundant specifications when identical behavior appears in multiple use cases.

**Notation**: A dashed arrow with stereotype "<<include>>" pointing from the including use case to the included use case.

**Example**: The use case "Process Order" <<includes>> "Validate Payment" because payment validation constitutes mandatory behavior required by "Process Order" regardless of other order processing variations.

### Extend Relationship

The extend relationship specifies that one use case (the extending use case) adds behavior to another use case (the base use case) under specific conditions. Unlike include relationships, extend relationships are conditional—the extended behavior executes only when particular conditions are satisfied. This relationship enables modeling of optional or exceptional functionality without modifying the base use case specification.

**Notation**: A dashed arrow with stereotype "<<extend>>" pointing from the extending use case to the base use case, with extension points in the base use case indicating where extensions may be inserted.

**Example**: "Process International Order" extends "Process Order" at extension point "Shipping Method Selection" when the customer specifies an international shipping address.

### Generalization

Generalization relationships model inheritance between use cases, where a child use case specializes a parent use case by adding or modifying behavior. The child use case inherits all characteristics of the parent while providing more specific behavior tailored to particular actor types or scenarios.

**Notation**: A solid triangular arrow pointing from the specialized (child) use case toward the generalized (parent) use case.

**Example**: "Withdraw Cash from Savings" and "Withdraw Cash from Checking" both generalize "Withdraw Cash," each specifying the particular account type from which funds are drawn.

## Use Case Diagram (UML Notation)

The use case diagram provides a graphical representation of system boundaries, actors, use cases, and their relationships. UML specifies precise notation for each diagram element:

| Element | UML Notation | Description |
|---------|--------------|-------------|
| System Boundary | Rectangle with title | Defines scope of modeled functionality |
| Use Case | Ellipse with name inside | Represents system functionality |
| Actor | Stick figure (also rectangle with actor name) | External entity interacting with system |
| Association | Solid line connecting actor to use case | Shows actor participates in use case |
| Include | Dashed arrow with <<include>> | Mandatory behavior incorporation |
| Extend | Dashed arrow with <<extend>> | Conditional behavior addition |
| Generalization | Solid triangular arrow | Inheritance relationship |

## Guidelines for Writing Effective Use Cases

Effective use case development requires adherence to established principles that ensure clarity, completeness, and utility throughout the development lifecycle:

**1. User Goal Orientation**: Each use case should address a single, complete user goal. Avoid decomposing functionality at too fine a granularity—atomic actions (e.g., "Enter Password") constitute steps within use cases rather than independent use cases themselves.

**2. Essential Description**: Write use cases at the essential level, describing what the system must accomplish without prescribing implementation details. Focus on user intentions and system responsibilities rather than user interface mechanics.

**3. Completeness**: Ensure use cases cover all possible scenarios including normal execution, alternative paths, and error conditions. Verify that preconditions and postconditions fully characterize the use case scope.

**4. Consistency**: Maintain consistent terminology, formatting, and detail level across all use cases in a system. Use a standard template to ensure uniform structure.

**5. Testability**: Formulate postconditions precisely enough to enable objective verification. Each postcondition should be checkable through system inspection or testing.

## Example: ATM Withdrawal System

**Use Case Name**: Withdraw Cash

**Actor**: Bank Customer (Primary), Bank Database (Secondary)

**Preconditions**:
1. Customer possesses a valid ATM card
2. Customer knows the correct PIN
3. ATM terminal is operational and contains sufficient cash

**Basic Flow**:
1. Customer inserts ATM card into card reader
2. System reads and validates card format
3. System prompts for PIN entry
4. Customer enters PIN
5. System validates PIN against database
6. System displays main menu
7. Customer selects "Withdraw Cash" option
8. System prompts for withdrawal amount
9. Customer enters desired amount
10. System verifies sufficient account balance
11. System dispenses specified cash amount
12. System updates account balance in database
13. Customer retrieves cash from dispenser
14. System returns ATM card to customer
15. Customer retrieves card
16. System displays transaction completion message

**Alternative Flows**:
- Step 2: Invalid card format → System displays error message, ejects card, use case terminates
- Step 5: Invalid PIN (first attempt) → System displays error, returns to step 3 for retry
- Step 5: Invalid PIN (three consecutive attempts) → System retains card for security, displays error message, notifies bank, use case terminates
- Step 10: Insufficient balance → System displays available balance, returns to step 8 for amount reconsideration
- Step 11: Cash dispenser malfunction → System cancels transaction, reverses balance deduction, displays error, returns card

**Postconditions**:
1. Customer has received the requested cash amount (if basic flow succeeded)
2. Customer's account balance has been reduced by the withdrawn amount
3. Transaction record has been created in the system database
4. Customer has retrieved their ATM card

**Extension Points**:
- "Authentication" (after step 4): Where account verification occurs
- "Amount Entry" (after step 8): Where withdrawal amount is specified
- "Dispensation" (after step 10): Where cash delivery occurs