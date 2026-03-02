# Requirements Engineering Fundamentals

## What is Requirements Engineering?

Requirements Engineering (RE) is the process of establishing the services that a customer requires from a system and the constraints under which it operates and is developed.

### Definition

> "A requirement is a condition or capability needed by a user to solve a problem or achieve an objective." - IEEE

## Types of Requirements

### Functional Requirements

- What the system should **do**
- Specific functions and features
- Input/output behaviors
- Business rules

**Examples:**

- "The system shall allow users to login with email and password"
- "The system shall generate monthly reports"

### Non-Functional Requirements

| Category            | Description                   | Examples                        |
| ------------------- | ----------------------------- | ------------------------------- |
| **Performance**     | Speed, throughput             | Response time < 2 seconds       |
| **Security**        | Protection, privacy           | Data encryption, access control |
| **Reliability**     | Availability, fault tolerance | 99.9% uptime                    |
| **Usability**       | Ease of use                   | Intuitive interface             |
| **Scalability**     | Growth handling               | Support 10,000 concurrent users |
| **Maintainability** | Ease of modification          | Modular design                  |

### User Requirements

- Written in natural language
- For customer understanding
- High-level statements

### System Requirements

- Detailed technical specifications
- For developers
- Precise and unambiguous

## Requirements Engineering Process

```
Feasibility Study → Requirements Elicitation → Requirements Analysis →
Requirements Specification → Requirements Validation → Requirements Management
```

### 1. Feasibility Study

- Technical feasibility
- Economic feasibility
- Operational feasibility
- Schedule feasibility

### 2. Requirements Elicitation

- Interviews
- Questionnaires
- Observation
- Document analysis
- Prototyping
- Joint Application Development (JAD)

### 3. Requirements Analysis

- Conflict resolution
- Prioritization
- Dependency analysis
- Classification

### 4. Requirements Specification

- Software Requirements Specification (SRS)
- Use case documentation
- User stories

### 5. Requirements Validation

- Reviews and inspections
- Prototyping
- Test case generation
- Consistency checking

### 6. Requirements Management

- Change control
- Traceability
- Version control

## Establishing the Groundwork

### Identifying Stakeholders

**Stakeholder Categories:**

- End users
- Business sponsors
- Technical staff
- Regulatory bodies
- Support personnel

### Recognizing Multiple Viewpoints

- Different stakeholders have different needs
- Conflicting requirements must be resolved
- Prioritization needed

### Working Toward Collaboration

- Establish communication channels
- Regular meetings
- Shared documentation
- Iterative feedback

## Requirements Engineering Challenges

### Common Problems

| Problem                   | Impact                   |
| ------------------------- | ------------------------ |
| Incomplete requirements   | Missing functionality    |
| Ambiguous requirements    | Multiple interpretations |
| Inconsistent requirements | Conflicting features     |
| Volatile requirements     | Frequent changes         |
| Infeasible requirements   | Cannot be implemented    |

### Solutions

- Use structured techniques
- Involve stakeholders continuously
- Document assumptions
- Maintain traceability
- Use requirements management tools

## Software Requirements Specification (SRS)

### IEEE 830 Standard Structure

1. Introduction
   - Purpose
   - Scope
   - Definitions
   - References
   - Overview

2. Overall Description
   - Product perspective
   - Product functions
   - User characteristics
   - Constraints

3. Specific Requirements
   - Functional requirements
   - Non-functional requirements
   - Interface requirements

### Good Requirements Characteristics

**SMART Requirements:**

- **S**pecific
- **M**easurable
- **A**chievable
- **R**elevant
- **T**ime-bound

## Key Takeaways

1. Requirements Engineering is **foundational** to project success
2. Distinguish between **functional** and **non-functional** requirements
3. The RE process includes **elicitation, analysis, specification, and validation**
4. **Stakeholder involvement** is critical throughout
5. Use **SRS documents** following standards like IEEE 830
