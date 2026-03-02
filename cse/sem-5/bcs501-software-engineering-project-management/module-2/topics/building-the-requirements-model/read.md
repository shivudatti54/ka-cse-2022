# Building the Requirements Model

## Introduction

Building the requirements model constitutes a fundamental phase in software engineering that systematically transforms stakeholder needs, expectations, and organizational constraints into a structured, unambiguous representation of the system to be developed. This phase, alternatively termed requirements modeling or analysis modeling, serves as the critical bridge between the problem domain and the solution space. The requirements model captures **what the system must accomplish** rather than **how it will be implemented**, providing a comprehensive blueprint that guides all subsequent development activities including design, implementation, testing, and maintenance.

The significance of constructing a robust requirements model cannot be overstated in modern software development lifecycle management. Empirical studies consistently demonstrate that defects discovered during requirements gathering and modeling phases are approximately 10-100 times less expensive to rectify than those identified during implementation or post-deployment phases. A well-constructed requirements model facilitates stakeholder visualization of system functionality, substantially reduces ambiguity in inter-team communication, and establishes a definitive baseline for subsequent validation and verification activities. For students pursuing professional qualifications in software engineering, comprehensive understanding of various modeling techniques and their appropriate contextual application is essential for developing industry-grade software systems.

This topic explores the fundamental approaches to requirements modeling, encompassing structured analysis methodologies, object-oriented analysis frameworks, and various diagrammatic techniques prescribed by international standards. The discussion examines how different models capture distinct aspects of requirements and how these models synergistically integrate to provide a comprehensive understanding of the target system.

## Theoretical Foundations of Analysis Modeling

### Definition and Scope

Analysis modeling represents the complete requirements specification of a system utilizing various graphical, textual, and mathematical notations. The primary objective is to capture both **functional requirements** (specifying what the system does) and **non-functional requirements** (defining qualities such as performance, reliability, security, usability, and maintainability) in a form suitable for comprehensive stakeholder review and precise technical implementation. Analysis models are deliberately designed to be comprehensible by non-technical stakeholders while maintaining sufficient precision for technical teams.

The theoretical basis of analysis modeling draws from set theory, graph theory, and formal specification languages. A formal definition can be expressed as follows:

**Definition**: An analysis model M is a quadruple (V, D, F, C) where:

- V represents the set of views or perspectives (functional, data, behavioral, object)
- D represents the domain or problem space being modeled
- F represents the set of formal constraints and rules governing the model
- C represents the completeness criteria ensuring all stakeholder needs are captured

### Types of Analysis Models

The analysis model typically comprises multiple complementary views of the system, each emphasizing distinct aspects:

1. **Functional Model**: Depicts system functionality through use cases, activity diagrams, and data flow diagrams, representing the transformation of inputs to outputs.

2. **Data Model**: Illustrates information structure through entity-relationship diagrams, showing data elements and their intrinsic relationships.

3. **Behavioral Model**: Captures system states, state transitions, and dynamic interactions through state diagrams and sequence diagrams.

4. **Object Model**: Represents the static structure in terms of classes, objects, attributes, operations, and various inter-class relationships.

Each model provides unique analytical insights, and collectively they create a holistic representation of system requirements. The principle of **model completeness** mandates that all four perspectives must be developed to ensure comprehensive requirements specification.

## Data Modeling

### Entity-Relationship (ER) Diagrams

Data modeling focuses on representing data elements and their structural relationships within the system domain. Entity-Relationship (ER) diagrams, originally proposed by Peter Chen in 1976, remain the primary tool for this purpose. An ER diagram comprises three fundamental components:

**Entities**: Objects in the problem domain about which data is stored. Entities possess identity distinct from their attributes and can be classified as:

- **Strong Entities**: Have independent existence and a primary key
- **Weak Entities**: Depend on strong entities for identification and require a foreign key

**Attributes**: Properties or characteristics of entities. Attributes are classified as:

- **Simple Attributes**: Atomic, indivisible values (e.g., age, salary)
- **Composite Attributes**: Composed of multiple simple components (e.g., address = street + city + state + zip)
- **Single-valued Attributes**: Contain one value per entity instance
- **Multi-valued Attributes**: Contain multiple values (e.g., phone_numbers)
- **Derived Attributes**: Computed from other attributes (e.g., age computed from date_of_birth)

**Relationships**: Associations between entities representing business rules. Relationships are characterized by:

- **Cardinality**: Specifies the number of entity instances that can participate in the relationship
- One-to-One (1:1)
- One-to-Many (1:N)
- Many-to-Many (M:N)
- **Participation**: Determines whether entity participation is mandatory or optional
- Total (mandatory) participation
- Partial (optional) participation

### Example: University Management System

Consider a university management system with the following specification:

**Entities**: Student, Course, Instructor, Department

**Attributes**:

- Student: student_id (PK), name, date_of_birth, address, major
- Course: course_id (PK), title, credits, department_id (FK)
- Instructor: instructor_id (PK), name, specialization, department_id (FK)
- Department: dept_id (PK), name, budget

**Relationships**:

- Student enrolls in Course (M:N) - with attributes enrollment_date, grade
- Instructor teaches Course (1:N) - one instructor teaches multiple courses
- Department offers Course (1:N) - one department offers many courses
- Instructor belongs to Department (N:1) - each instructor belongs to one department

The ER diagram representation follows Chen's notation where entities are rectangles, attributes are ovals, and relationships are diamonds connected by lines bearing cardinality indicators.

### Extended ER (EER) Concepts

For complex domain modeling, Extended ER concepts provide additional modeling power:

- **Specialization/Generalization**: Top-down and bottom-up refinement of entity types
- **Aggregation**: Treating relationships as higher-level entities
- **Composition**: Strong whole-part relationships with dependent parts

## Functional Modeling and Data Flow Diagrams

### Theoretical Foundation

Data Flow Diagrams (DFDs) originated from structured analysis methodology and provide a network representation of data movement through the system. DFDs are grounded in the principles of data transformation, where the system is viewed as a collection of processes that transform input data streams into output data streams.

**Formal Definition**: A DFD is a directed graph G = (N, E) where:

- N represents nodes (processes, data stores, external entities)
- E represents directed edges (data flows)
- The graph is acyclic (no cycles representing infinite loops)

### Components of DFD

The four primary components of DFDs are:

1. **External Entities (Sources/Sinks)**: Represented as squares, these are sources or destinations of data existing outside the system boundary. They define the system's operational boundary and interface points.

2. **Processes (Transformations)**: Represented as circles or rounded rectangles, processes transform input data into output data through computation, transformation, or manipulation operations.

3. **Data Flows**: Represented as directed arrows, data flows show the movement of data elements between components. Data flows must be named with meaningful nouns describing the data being transmitted.

4. **Data Stores**: Represented as open-ended rectangles, data stores represent repositories where data is persistently stored for subsequent retrieval. Data stores do not perform transformations but serve as data repositories.

### DFD Leveling and Decomposition

DFDs are systematically created at multiple levels of abstraction following the **balance** principle - data flowing into a process must equal data flowing out when decomposed to lower levels.

**Level 0 DFD (Context Diagram)**: The highest abstraction level showing the entire system as a single process bubble with all external entities and major data flows connecting to system boundaries.

**Level 1 DFD**: Decomposes the single process into major functional areas (typically 7±2 processes), showing the primary workflow and data store interactions.

**Level 2 DFD and beyond**: Provides progressively detailed decomposition of individual Level 1 processes, revealing sub-processes and detailed data movements.

### Example: Library Management System

**Context Diagram (Level 0)**:

- System: Library Management System
- External Entities: Member, Librarian, Publisher, External Library
- Major Data Flows: Book requests, Membership applications, Book information, Transaction records

**Level 1 DFD Decomposition**:

- Process 1: Member Management (registration, membership renewal)
- Process 2: Book Catalog Management (cataloging, inventory)
- Process 3: Circulation Management (borrowing, returning, reservations)
- Process 4: Fine Management (calculation, payment processing)

### Rules and Constraints

DFD construction follows essential rules to ensure syntactic correctness:

- Processes must have at least one input and one output flow
- Data cannot flow directly between external entities
- Data cannot flow directly between data stores without process intervention
- Each data flow must connect to at least one process
- Processes and data stores must have unique names

## Use Case Modeling

### Theoretical Framework

Use case modeling, introduced by Ivar Jacobson in 1987 and subsequently integrated into the Unified Modeling Language (UML), has become the predominant approach for capturing functional requirements, particularly in object-oriented development methodologies. Use cases represent **complete sequences of actions** that the system performs to produce observable results of value to particular actors.

**Formal Definition**: A use case U is defined as U = (A, S, I, O, P, Q) where:

- A represents the set of actors initiating or participating in the use case
- S represents the initiating actor's trigger event
- I represents the sequence of interactions (dialogue between actor and system)
- O represents the observable result produced by the system
- P represents preconditions that must be satisfied before execution
- Q represents postconditions that hold after successful completion

### Components of Use Case Specification

Each comprehensive use case description includes:

1. **Use Case Name**: A verb-noun phrase uniquely identifying the use case

2. **Actors**: External entities (users, other systems) that interact with the system

3. **Preconditions**: Conditions that must be true before the use case begins execution

4. **Postconditions**: Conditions guaranteed to be true upon successful completion

5. **Basic Flow (Primary Scenario)**: The normal, successful sequence of interactions

6. **Alternative Flows (Secondary Scenarios)**: Variations and error conditions including:

- Alternate paths achieving the same goal
- Error conditions and exception handling
- Alternate termination scenarios

7. **Business Rules**: Organizational policies and constraints governing the behavior

8. **Extension Points**: Specific locations where extensions may be attached

### Example: Online Shopping System

**Use Case: Place Order**

- **Actors**: Customer (primary), Payment System (external), Inventory System (external)
- **Preconditions**: Customer is authenticated; shopping cart contains at least one item
- **Postconditions**: Order is created; inventory is reserved; payment is processed; confirmation is sent

**Basic Flow**:

1. Customer initiates "Place Order" request
2. System displays order summary with item details and total amount
3. Customer selects payment method
4. Customer provides payment information
5. System validates payment information
6. System processes payment through Payment System
7. System reserves inventory through Inventory System
8. System generates order confirmation with unique order ID
9. System sends confirmation email to customer

**Alternative Flows**:

- **Payment Failure**: If payment is declined, system displays error message; customer may modify payment method or cancel order
- **Out-of-Stock Item**: If item is unavailable, system notifies customer; customer may remove item or place backorder
- **Address Verification Failure**: System prompts customer to verify/enter corrected address

### Use Case Relationships

Use cases exhibit various relationships that promote reuse and reduce redundancy:

- **Include Relationship**: One use case incorporates the behavior of another (compulsory inclusion)
- **Extend Relationship**: One use case extends the behavior of another under specific conditions
- **Generalization Relationship**: Specialized use cases inherit behavior from a general use case

## Class Diagrams and Object Modeling

### Object-Oriented Analysis Fundamentals

Class diagrams represent the static structural view of the system in terms of classes, their attributes, operations (methods), and relationships. In object-oriented analysis, classes are derived through systematic domain analysis, identifying meaningful categories of entities that share common characteristics and behaviors. Each class encapsulates **data** (state in attributes) and **behavior** (functionality in operations).

**Definition**: A class C is defined as C = (A, O, I, R) where:

- A represents the set of attributes (properties holding values)
- O represents the set of operations (methods/functions)
- I represents the set of invariants (conditions that must always hold)
- R represents the set of relationships with other classes

### Class Relationships

Class relationships define how classes interact and collaborate:

1. **Association**: A structural relationship representing a connection between classes. Associations can be:

- **Bidirectional**: Both classes know about the relationship
- **Unidirectional**: Only one class knows about the relationship
- **Multiplicity**: Specifies how many instances participate (0..1, 0.._, 1.._, 1, 2..5, etc.)

2. **Aggregation**: A special form of association representing "has-a" relationship where the part can exist independently of the whole. Represented by a hollow diamond.

3. **Composition**: A stronger form of aggregation where the part's lifecycle is completely controlled by the whole. Represented by a filled diamond. If the composite is destroyed, all its parts are destroyed.

4. **Generalization/Inheritance**: A "is-a" relationship where a subclass inherits attributes, operations, and relationships from a superclass. Enables polymorphism and code reuse.

5. **Dependency**: A weakest relationship where one class depends on another class for its specification or implementation. Typically occurs when a class uses another class as a parameter or local variable.

### Example: E-Commerce Class Diagram

```
Class: Customer
Attributes: customerId, name, email, password, address
Operations: login(), logout(), updateProfile(), placeOrder()
Relationships:
- Customer places Order (1..*)
- Customer has Address (1)

Class: Order
Attributes: orderId, orderDate, status, totalAmount
Operations: calculateTotal(), addItem(), removeItem(), processPayment()
Relationships:
- Order contains OrderItem (1..*)
- Order associated with Customer (1)
- Order processed by Payment (1)

Class: Product
Attributes: productId, name, description, price, stockQuantity
Operations: getDetails(), updateStock(), applyDiscount()
Relationships:
- Product appears in OrderItem (0..*)
- Product categorized by Category (N:1)

Class: OrderItem
Attributes: quantity, unitPrice, discount
Operations: calculateSubtotal()
Relationships:
- OrderItem links Product (1)
- OrderItem belongs to Order (1)
```

### Association Classes

When an association needs its own attributes and operations, an **association class** is used. For example, in the relationship between Student and Course (enrollment), the association class "Enrollment" would include attributes like enrollmentDate, grade, and status.

## Behavioral Modeling

### State Diagrams

Behavioral modeling captures the dynamic behavior of system components through state machines. State diagrams (or statechart diagrams in UML) represent the sequence of states an object or system traverses during its lifetime in response to events.

**Definition**: A state machine is defined as M = (S, E, T, s0, F) where:

- S represents the finite set of states
- E represents the set of events triggering transitions
- T represents the set of transitions (S × E → S)
- s0 represents the initial state
- F represents the set of final (accepting) states

### State Diagram Components

1. **States**: Conditions or situations during object lifetime

- **Initial State**: Denoted by a filled circle
- **Final State**: Denoted by a circle inside another circle (bullseye)
- **Simple States**: Basic states with entry/exit actions
- **Composite States**: Contain nested substates

2. **Transitions**: Directed connections between states

- Format: Event [Guard Condition] / Action
- Guard conditions must be true for transition to occur
- Actions are executed during transition

3. **Events**: Occurrences that trigger state changes

### Example: Order Processing State Machine

```
States: New, Confirmed, Processing, Shipped, Delivered, Cancelled

Transitions:
- New → Confirmed: orderSubmitted [paymentValid] / sendConfirmation()
- Confirmed → Processing: paymentProcessed / reserveInventory()
- Processing → Shipped: itemsPacked / updateTracking()
- Shipped → Delivered: deliveryConfirmed / notifyCustomer()
- New → Cancelled: orderCancelled / refundPayment()
- Confirmed → Cancelled: customerRequested / initiateRefund()
```

### Sequence Diagrams

Sequence diagrams illustrate object interactions arranged in time sequence, emphasizing the temporal order of message passing between objects.

**Components**:

- **Lifelines**: Vertical dashed lines representing object existence
- **Activations**: Thin vertical rectangles showing when an object is active
- **Messages**: Horizontal arrows showing communication (synchronous, asynchronous, return)
- **Combined Fragments**: Decision logic (alt, loop, par, opt)

## Model Integration and Traceability

### Inter-Model Relationships

A comprehensive requirements model integrates multiple modeling techniques, with each model providing complementary perspectives:

| Model Type       | Captures                    | Key Techniques                    |
| ---------------- | --------------------------- | --------------------------------- |
| Data Model       | Information structure       | ER Diagrams, Class attributes     |
| Functional Model | Data transformation         | DFDs, Use Cases                   |
| Behavioral Model | Dynamic behavior            | State Diagrams, Sequence Diagrams |
| Object Model     | Structure and relationships | Class Diagrams, Object Diagrams   |

### Requirements Traceability

**Traceability Matrix**: A tool linking requirements to design elements, test cases, and other artifacts. The matrix ensures each requirement is addressed and can be verified.

**Forward Traceability**: Mapping requirements to design components and test cases
**Backward Traceability**: Ensuring design elements and tests trace back to specific requirements

A sample requirements traceability matrix format:

| Requirement ID | Requirement Description         | Related Use Case | Design Component            | Test Case ID   |
| -------------- | ------------------------------- | ---------------- | --------------------------- | -------------- |
| REQ-001        | System shall authenticate users | UC-01 Login      | AuthService, User class     | TC-001, TC-002 |
| REQ-002        | System shall process payments   | UC-05 Payment    | PaymentGateway, Order class | TC-015         |

## Summary

Building the requirements model is a critical software engineering activity that transforms stakeholder needs into structured, unambiguous specifications. Key modeling approaches include:

1. **Analysis Modeling**: Multi-perspective requirements capture through functional, data, behavioral, and object views

2. **Data Modeling**: ER diagrams capturing entities, attributes, and relationships with cardinality specifications

3. **Functional Modeling**: DFDs showing data movement, transformation processes, data stores, and external entities at multiple abstraction levels

4. **Use Case Modeling**: Scenario-based capture of functional requirements from user perspective, including basic flows, alternative flows, and business rules

5. **Class Diagrams**: Object-oriented structural representation showing classes, attributes, operations, and relationships (association, aggregation, composition, inheritance)

6. **Behavioral Modeling**: State diagrams and sequence diagrams capturing dynamic system behavior and object interactions

These modeling techniques collectively provide comprehensive requirements specification, enabling successful system development while minimizing requirements-related defects and associated costs.

---

## Assessment Questions

### Multiple Choice Questions

**Question 1**: In an Entity-Relationship diagram for a hospital management system, which relationship type represents the association between "Doctor" and "Patient" where a doctor can treat multiple patients and a patient can be treated by multiple doctors?

(A) One-to-One (1:1)
(B) One-to-Many (1:N)
(C) Many-to-Many (M:N)
(D) Zero-to-Many (0:N)

**Answer**: (C) Many-to-Many (M:N)
**Explanation**: The relationship between Doctor and Patient is inherently many-to-many because multiple doctors can treat the same patient (e.g., for different medical conditions), and a single doctor can treat multiple patients. In ER modeling, this requires an associative entity (like "Treatment" or "Appointment") to resolve the M:N relationship into two 1:N relationships, as relational databases do not directly support many-to-many relationships.

---

**Question 2**: Consider a DFD level 1 decomposition where the process "Process Order" receives input data flows "Customer Order" and "Inventory Status", and produces output data flows "Order Confirmation" and "Updated Inventory". If "Customer Order" contains 5 data elements and "Inventory Status" contains 3 data elements, and the output flows contain 4 and 2 data elements respectively, which DFD balancing principle is being violated?

(A) Process naming convention
(B) Data flow completeness
(C) Input-output data element conservation
(D) External entity consistency

**Answer**: (C) Input-output data element conservation
**Explanation**: DFD balancing requires that data flowing into a process must equal data flowing out at the same level of decomposition. Here, total input elements = 5 + 3 = 8, while total output elements = 4 + 2 = 6. This violates the conservation principle, indicating either missing output data or redundant input data that needs to be identified and corrected before proceeding to Level 2 decomposition.

---

**Question 3**: In a class diagram for an inventory management system, "Warehouse" contains multiple "Shelf" objects, and when a Warehouse is deleted, all its Shelf objects must also be deleted. Which relationship type correctly models this constraint?

(A) Aggregation
(B) Composition
(C) Association
(D) Dependency

**Answer**: (B) Composition
**Explanation**: Composition represents a strong whole-part relationship where the part's lifecycle is completely controlled by the whole. The constraint that "when a Warehouse is deleted, all Shelf objects must also be deleted" explicitly defines composition semantics. Aggregation, in contrast, allows parts to exist independently of the whole (a Shelf could be moved to another Warehouse).

---

**Question 4**: A use case "Calculate Loan EMI" has a precondition that "Customer account is validated" and a postcondition that "EMI amount is displayed to customer". If during execution, the external "Credit Rating Service" returns an error, which use case component handles this scenario?

(A) Basic Flow
(B) Alternative Flow
(C) Business Rule
(D) Extension Point

**Answer**: (B) Alternative Flow
**Explanation**: Alternative flows handle variations and error conditions during use case execution. The scenario where the Credit Rating Service returns an error is an exception condition that deviates from the normal successful path (Basic Flow). An alternative flow would specify actions like displaying an error message, offering retry options, or suggesting alternative loan assessment methods. Extension points could be used if the error handling was designed as a separate extension that triggers under specific conditions.

---

**Question 5**: In the context of requirements traceability, forward traceability primarily ensures:

(A) Test cases are written before implementation
(B) Each design element can be traced back to a specific requirement
(C) Requirements are not added after design completion
(D) Implementation satisfies the documented requirements

**Answer**: (D) Implementation satisfies the documented requirements
**Explanation**: Forward traceability maps requirements to downstream artifacts (design components, implementation code, test cases). Its primary purpose is to ensure that all implemented functionality can be traced back to documented requirements, thereby verifying that the implementation satisfies what was originally specified. While option (B) describes backward traceability, forward traceability specifically ensures that requirements drive implementation rather than the reverse.
