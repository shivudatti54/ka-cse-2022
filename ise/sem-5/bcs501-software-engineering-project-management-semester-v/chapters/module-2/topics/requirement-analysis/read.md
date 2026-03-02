# Requirements Analysis in Software Engineering

## Introduction to Requirements Analysis

Requirements Analysis is a critical phase in the Requirements Engineering process that follows Requirements Elicitation. It involves the thorough examination, organization, and specification of the gathered requirements to ensure they are complete, consistent, unambiguous, and verifiable. This phase acts as a bridge between the initial collection of stakeholder needs and the creation of formal documentation that will guide the entire software development lifecycle.

The primary goal of requirements analysis is to transform often vague, incomplete, and sometimes contradictory stakeholder wishes into a clear, precise, and agreed-upon set of requirements that developers can implement and testers can validate.

## Key Concepts in Requirements Analysis

### 1. Types of Requirements

Requirements are typically categorized into two main types:

**Functional Requirements:**

- Describe what the system should do
- Specify the behavior and functions of the system
- Example: "The system shall allow users to reset their password"

**Non-Functional Requirements:**

- Describe how the system should perform its functions
- Specify quality attributes and constraints
- Example: "The system shall respond to user requests within 2 seconds"

### 2. Characteristics of Good Requirements

Effective requirements should possess the following qualities (often remembered by the acronym SMART):

- **Specific**: Clearly defined and unambiguous
- **Measurable**: Quantifiable and testable
- **Achievable**: Realistic within constraints
- **Relevant**: Aligned with business objectives
- **Traceable**: Can be tracked through development

### 3. Requirements Analysis Techniques

Several structured techniques are employed during requirements analysis:

#### Data Flow Diagrams (DFDs)

DFDs illustrate how data moves through a system, showing processes, data stores, data flows, and external entities.

```
Example DFD for a Library System:

+-------------+      +-----------+      +---------------+
|   Member    |----->|  Borrow   |----->|  Book Database |
| (External   |<-----| (Process) |<-----|   (Data Store) |
|   Entity)   |      +-----------+      +---------------+
+-------------+
```

#### Entity-Relationship Diagrams (ERDs)

ERDs model the data aspects of a system, showing entities, their attributes, and relationships.

```
Example ERD snippet:

+-------------+        has        +-------------+
|   Member    |==================>|   Loan      |
+-------------+        1..N       +-------------+
| - memberID  |                    | - loanID    |
| - name      |                    | - date      |
| - email     |        belongs     +-------------+
+-------------+        to
                         |
                         | 1..1
                         |
                         V
                 +-------------+
                 |    Book     |
                 +-------------+
                 | - bookID    |
                 | - title     |
                 | - author    |
                 +-------------+
```

#### Use Case Diagrams

Use cases describe interactions between actors (users or external systems) and the system to achieve specific goals.

```
Example Use Case Diagram:

+----------------+       +-------------------------+
|    Librarian   |-------|  Manage Book Inventory  |
+----------------+       +-------------------------+
       |                           |
       |                           |
       |       +----------------+  |
       |-------|  Process Loan  |  |
       |       +----------------+  |
       |                           |
+----------------+       +-------------------------+
|     Member     |-------|    Search Catalog       |
+----------------+       +-------------------------+
```

#### State Transition Diagrams

These diagrams show how the system responds to various events by changing its state.

```
Example State Transition for a Book:

+--------+   reserve   +----------+   cancel    +--------+
|        | ----------> |          | ----------> |        |
| Available |          | Reserved |             | Available |
|        | <---------- |          | <---------- |        |
+--------+   return    +----------+   timeout  +--------+
```

### 4. Requirements Prioritization

Not all requirements are equally important. Common prioritization techniques include:

**MoSCoW Method:**

- **M**ust have: Critical for current delivery
- **S**hould have: Important but not vital
- **C**ould have: Desirable but not necessary
- **W**on't have: Least critical, postponed

**Kano Model:**
Categorizes requirements based on customer satisfaction:

- Basic needs (expected features)
- Performance needs (more is better)
- Excitement needs (unexpected delights)

### 5. Requirements Validation

Validation ensures that the requirements accurately reflect stakeholder needs and are of sufficient quality. Techniques include:

- **Reviews**: Formal inspections of requirements documents
- **Prototyping**: Creating mockups to validate understanding
- **Model Validation**: Checking consistency of analysis models
- **Checklists**: Systematic verification of requirement qualities

## Common Challenges in Requirements Analysis

1. **Ambiguity**: Vague requirements that can be interpreted differently
2. **Inconsistency**: Conflicting requirements from different stakeholders
3. **Incompleteness**: Missing requirements or details
4. **Gold Plating**: Adding unnecessary features that increase complexity
5. **Scope Creep**: Uncontrolled expansion of requirements during analysis

## Tools for Requirements Analysis

Various tools support the requirements analysis process:

| Tool Type               | Examples                              | Purpose                              |
| ----------------------- | ------------------------------------- | ------------------------------------ |
| Modeling Tools          | Enterprise Architect, Visual Paradigm | Create and manage analysis models    |
| Requirements Management | IBM DOORS, Jama Connect               | Track and trace requirements         |
| Collaboration Tools     | Confluence, SharePoint                | Facilitate stakeholder communication |
| Prototyping Tools       | Figma, Axure                          | Create interactive mockups           |

## The Requirements Analysis Process

A typical requirements analysis process follows these steps:

1. **Categorization**: Group requirements into functional, non-functional, business, etc.
2. **Prioritization**: Determine which requirements are most critical
3. **Conflict Resolution**: Identify and resolve contradictory requirements
4. **Detailed Analysis**: Elaborate each requirement with precise details
5. **Modeling**: Create visual representations of requirements
6. **Validation**: Verify requirements with stakeholders
7. **Documentation**: Record analyzed requirements in appropriate formats

## Relationship with Other RE Activities

Requirements analysis doesn't occur in isolation. It connects to:

- **Elicitation**: Analysis begins as requirements are gathered
- **Specification**: Analysis results feed into formal documentation
- **Validation**: Analysis helps identify requirements that need validation
- **Management**: Analyzed requirements become baselined for management

## Exam Tips

1. **Understand the Difference**: Be clear on the distinction between requirements elicitation (gathering) and analysis (structuring and refining).

2. **Know the Techniques**: Be prepared to explain different analysis techniques (DFD, ERD, use cases) and when each is appropriate.

3. **Practice Modeling**: Expect questions where you need to create or interpret simple analysis diagrams.

4. **Remember Characteristics**: Memorize the qualities of good requirements (unambiguous, consistent, complete, etc.) and be able to identify poor requirements.

5. **Prioritization Methods**: Understand different prioritization techniques and their applications.

6. **Real-world Examples**: Be ready to provide examples of functional vs. non-functional requirements from everyday systems.

7. **Traceability**: Understand how requirements analysis supports traceability through the development process.
