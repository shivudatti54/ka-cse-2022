# Requirement Analysis and Software Requirement Specification (SRS)

## 1. Introduction

Requirement Analysis constitutes a fundamental phase in the Software Development Life Cycle (SDLC) that serves as the critical bridge between problem definition and solution design. This phase encompasses the systematic identification, documentation, validation, and management of stakeholder needs and constraints to produce a comprehensive specification document. The quality of requirements gathered during this phase demonstrably determines the success or failure of the final software product, as poorly defined requirements propagate errors throughout subsequent development phases with exponentially increasing remediation costs.

The significance of requirement analysis cannot be overstated in modern software engineering practice. Industry studies consistently indicate that approximately 40-60% of software project failures can be traced directly to inadequate requirements engineering practices. Common manifestations include project delays, cost overruns, customer dissatisfaction, and in extreme cases, complete project failure. The economic impact is substantial: the cost of fixing a requirement error discovered during implementation is approximately 5-10 times higher than fixing it during the analysis phase, while errors discovered post-deployment can cost 20-100 times more to rectify.

This module equips students with the knowledge to elicit, analyze, specify, and validate requirements systematically using industry-standard techniques and documentation practices conforming to IEEE 830 and IEEE 829 standards.

## 2. Requirements Engineering: Formal Framework

### 2.1 Definition and Scope

Requirements Engineering (RE) is defined as the systematic process of developing requirements through an iterative negotiation, documentation, and validation cycle. The International Requirements Engineering Board (IREB) defines RE as the branch of software engineering concerned with the real-world goals of, functions of, and constraints on software systems. It also involves the relationship of these factors to precise specifications of software behavior, and to their evolution over time and across software product families.

The requirements engineering process comprises four interconnected activities that form an iterative cycle:

**Requirements Elicitation**: This activity involves gathering requirements from stakeholders through various techniques including interviews, surveys, observations, workshops, and prototyping. Elicitation is challenging because stakeholders often cannot articulate their needs clearly, and implicit requirements may remain unspoken. The process requires skilled facilitation and multiple interaction cycles to ensure comprehensive coverage.

**Requirements Analysis**: This critical activity involves studying and refining requirements to identify conflicts, ambiguities, inconsistencies, and incomplete specifications. Analysis techniques include constraint analysis, feasibility studies, and mathematical modeling of requirements relationships. Analysts must resolve conflicts between stakeholder needs and identify implied requirements not explicitly stated.

**Requirements Specification**: This activity involves documenting requirements in a formal, structured format that serves as the contractual basis between stakeholders and developers. The Software Requirements Specification (SRS) must be complete, unambiguous, verifiable, and traceable.

**Requirements Validation**: This activity ensures that the documented requirements accurately represent stakeholder needs and are internally consistent. Validation techniques include requirements reviews, prototyping, and test case derivation from requirements specifications.

### 2.2 The Requirements Engineering Hierarchy

Requirements are organized in a hierarchical structure that facilitates systematic analysis:

- **Business Requirements**: High-level organizational goals and objectives that the software system must support
- **User Requirements**: Descriptions of what users need to accomplish, expressed from the user's perspective
- **Functional Requirements**: Specific system behaviors that describe what the system must do
- **System Requirements**: Comprehensive requirements for the entire system including hardware, software, and manual procedures

## 3. Classification of Requirements

### 3.1 Functional Requirements

Functional requirements specify the behaviors, functions, and features of the system from the user's perspective. They define what the system should do and describe the inputs, processing logic, and outputs for each system function. A well-formed functional requirement is complete, consistent, unambiguous, and verifiable.

**Formal Definition**: A functional requirement R is a triple R = (I, P, O) where I represents the set of valid inputs, P represents the processing logic or transformation function, and O represents the set of expected outputs. The requirement is verifiable if there exists a finite test procedure that can determine whether the system produces O when presented with I.

**Examples**:

- User authentication and authorization mechanisms
- Data processing, computation, and storage operations
- Report generation and formatting capabilities
- Communication interfaces and data exchange protocols
- Business rule enforcement and validation logic

### 3.2 Non-Functional Requirements (Quality Attributes)

Non-functional requirements define system properties and constraints that determine the quality of the system. They specify how the system should perform rather than what it should do. Non-functional requirements are often called "quality attributes" because they directly impact the user's perception of system quality.

The ISO/IEC 25010 standard classifies quality characteristics as follows:

**Performance Requirements**:

- Response time: The maximum time elapsed between user input and system response
- Throughput: The number of transactions or operations the system can process per unit time
- Resource utilization: CPU, memory, and storage consumption thresholds
- Capacity: Maximum load the system can handle (concurrent users, data volume)

**Security Requirements**:

- Authentication: Verification of user identity through passwords, biometrics, or multi-factor mechanisms
- Authorization: Determination of user privileges and access rights to system resources
- Data encryption: Protection of sensitive data in transit and at rest using cryptographic algorithms
- Audit logging: Recording of security-relevant events for forensic analysis

**Reliability Requirements**:

- Mean Time Between Failures (MTBF): Expected operational time between system failures
- Mean Time To Repair (MTTR): Average time required to restore system functionality
- Availability: Percentage of time the system is operational (typically expressed as "nines": 99.9% = three nines)
- Fault tolerance: System's ability to continue operation despite component failures

**Usability Requirements**:

- User interface design standards and consistency
- Accessibility compliance (WCAG 2.1 guidelines)
- Learning time: Maximum time required for users to become proficient
- Error handling: User-friendly error messages and recovery mechanisms

**Maintainability Requirements**:

- Modular design: System should be decomposed into independent, replaceable modules
- Extensibility: Ease of adding new features without modifying existing code
- Testability: Ease of verifying system correctness through testing

**Portability Requirements**:

- Platform compatibility: Operating systems, browsers, hardware configurations
- Installation requirements: Ease of deployment and configuration

## 4. Requirements Elicitation Techniques

### 4.1 Interview Techniques

**Structured Interviews**: These use predetermined question sets to ensure consistency across multiple stakeholders. Structured interviews facilitate quantitative analysis but may limit discovery of unexpected requirements.

**Unstructured Interviews**: These open-ended conversations allow exploratory investigation of stakeholder needs. They are effective for initial requirements discovery but may lack consistency.

**Focus Group Interviews**: These bring together multiple stakeholders to discuss complex requirements. Facilitated discussions can reveal conflicting needs and generate innovative solutions.

### 4.2 Systematic Elicitation Methods

**Questionnaires**: Structured surveys distributed to large stakeholder groups for quantitative feedback. Effective for gathering statistical data and prioritizing requirements across many stakeholders.

**Observation**: Direct study of users in their natural work environment to understand actual workflows, workarounds, and implicit requirements that users may not articulate.

**Document Analysis**: Systematic review of existing system documentation, procedures, policies, and regulatory requirements to identify explicit and implicit requirements.

**Prototyping**: Creation of preliminary versions (paper or functional prototypes) to validate understanding and elicit feedback on proposed solutions before full implementation.

**Joint Application Development (JAD)**: Collaborative workshops bringing together stakeholders and developers for intensive, time-boxed requirements definition sessions.

**Brainstorming**: Structured group creativity sessions designed to generate a wide range of requirements without immediate criticism or evaluation.

## 5. Requirements Analysis Techniques

### 5.1 Use Case Modeling

Use cases represent system functionality from the user's perspective, describing interactions between actors and the system to achieve specific goals. Use case modeling is formalized in the Unified Modeling Language (UML 2.5).

**Components**:

- **Actors**: External entities (users, other systems, hardware devices) that interact with the system
- **Use Cases**: Distinct system functions initiated by actors to accomplish specific goals
- **Relationships**: Include (mandatory behavior), Extend (optional behavior), and Generalization (inheritance)
- **System Boundary**: Defines the scope by delineating what lies inside and outside the system

**Use Case Description Template**:

```
Use Case Name: [Descriptive name]
Actor: [Primary actor(s)]
Preconditions: [Conditions that must be true before use case begins]
Postconditions: [Conditions that must be true after use case completes]
Main Flow:
 1. [First step]
 2. [Second step]
 ...
Alternative Flows:
 [Alternative scenarios and error conditions]
```

### 5.2 Requirements Prioritization

Prioritization is essential when resource constraints prevent implementing all requirements. Common techniques include:

**MoSCoW Method**:

- **M**ust Have: Critical requirements without which the system fails
- **S**hould Have: Important requirements that significantly impact success
- **C**ould Have: Desirable requirements that enhance the product
- **W**ould Like: Future considerations if time and resources permit

**Analytic Hierarchy Process (AHP)**: A mathematical prioritization method using pairwise comparisons. For requirements r₁ and r₂, the relative priority is determined by answering: "How much more important is r₁ than r₂ for achieving the project goal?" The resulting comparison matrix is analyzed to compute priority weights.

**Hundred-Dollar Method**: Each stakeholder is given "100 votes" to distribute among requirements proportionally. The aggregated scores provide a ranked list reflecting collective stakeholder priorities.

### 5.3 Traceability Matrix

Requirements traceability establishes and maintains links between requirements and other SDLC artifacts. The traceability matrix documents relationships between:

- Source requirements and derived requirements
- Requirements and design elements
- Requirements and test cases
- Requirements and implementation components

**Forward Traceability**: Maps requirements to downstream artifacts ensuring each requirement is addressed
**Backward Traceability**: Maps downstream artifacts to source requirements ensuring no unauthorized functionality is added

### 5.4 Conflict Resolution

When stakeholder requirements conflict, systematic resolution approaches include:

**Negotiation**: Facilitated discussions to identify mutually acceptable compromises
**Prioritization Based Resolution**: Higher-priority requirements take precedence
**Stakeholder Analysis**: Identifying which stakeholders have authority to resolve specific conflicts
**Trade-off Analysis**: Documenting the implications of different resolution options

## 6. Software Requirements Specification (SRS)

### 6.1 IEEE 830 Standard

The IEEE 830-1998 standard provides guidelines for writing a well-structured SRS. A quality SRS possesses the following properties:

**Completeness**: Every requirement is present with no missing information
**Consistency**: No requirement contradicts another requirement
**Unambiguity**: Each requirement has only one interpretation
**Verifiability**: Each requirement can be tested to determine if it is met
**Traceability**: Each requirement can be linked to its source and design elements
**Modifiability**: The document is structured to facilitate changes

### 6.2 SRS Structure

**1. Introduction**

- Purpose: Why the SRS is written and its intended audience
- Scope: What system is being described, benefits, and objectives
- Definitions, Acronyms, and Abbreviations
- References: External documents, standards, and specifications
- Overview: Summary of the remaining document structure

**2. Overall Description**

- Product Perspective: Relationship to other systems and hardware/software constraints
- User Characteristics: Demographics, technical expertise, and responsibilities
- Design Constraints: Standards, hardware limitations, software interfaces
- Assumptions and Dependencies: External factors affecting requirements

**3. Functional Requirements**

- All functional requirements with unique identifiers
- Description of inputs, processing logic, outputs, and error conditions
- Include only external behavior visible to users

**4. Non-Functional Requirements**

- Performance Specifications: Response times, throughput, capacity
- Security Requirements: Authentication, authorization, encryption standards
- Reliability Requirements: MTBF, availability targets
- Usability Requirements: Accessibility, learning time
- Environmental Requirements: Operating conditions, physical environment

**5. Appendices**

- Glossary: Definitions of technical terms
- Analysis Models: UML diagrams, data flow diagrams, entity-relationship diagrams
- Issues List: Known problems requiring resolution

## 7. Worked Examples

### Example 1: Requirements Classification

**Scenario**: For an Online Banking System, classify the following requirements:

a) The system must support at least 1000 concurrent users during peak hours
b) Customers should be able to transfer funds between accounts
c) All transactions must be completed within 3 seconds
d) The system must generate monthly account statements in PDF format
e) Customer data must be encrypted using AES-256 encryption
f) The system should allow account holders to view transaction history for 24 months
g) The system must comply with PCI-DSS security standards

**Solution**:

**Functional Requirements**: Requirements describing specific system behaviors:

- b) Fund transfer capability (core banking function)
- d) Statement generation (report production)
- f) Transaction history viewing (data retrieval function)

**Non-Functional Requirements**: Requirements describing quality attributes:

- a) Performance - Capacity requirement (1000 concurrent users)
- c) Performance - Response time requirement (< 3 seconds)
- e) Security - Data encryption (AES-256)
- g) Security - Regulatory compliance (PCI-DSS)

### Example 2: Use Case Development

**Scenario**: Develop a complete use case description for the "Withdraw Cash" functionality in an ATM System.

**Solution**:

```
Use Case Name: Withdraw Cash
Actor: Bank Customer
Primary Actor: Bank Customer
Stakeholders and Interests:
 - Bank Customer: Desires quick, secure cash withdrawal
 - Bank: Requires accurate transaction logging and fraud prevention

Preconditions:
 1. Customer has successfully authenticated at the ATM
 2. Customer's account is active and has sufficient balance
 3. ATM has sufficient cash available

Postconditions (Success):
 1. Cash has been dispensed to the customer
 2. Customer's account has been debited correctly
 3. Transaction has been logged in the system

Postconditions (Failure):
 1. No cash has been dispensed
 2. Account balance remains unchanged
 3. Error message has been displayed to customer

Main Flow:
 1. Customer selects "Withdraw Cash" option
 2. System displays withdrawal amount options ($20, $40, $60, $80, $100, Other)
 3. Customer selects or enters desired amount
 4. System validates sufficient account balance
 5. System validates ATM cash availability
 6. System processes withdrawal transaction
 7. System dispenses cash
 8. System dispenses receipt
 9. Customer takes cash and receipt
 10. Use case terminates

Alternative Flows:
 - A1: Insufficient Balance - Display error, return to main menu
 - A2: ATM Cash Insufficient - Display error, suggest alternative amount
 - A3: Network Timeout - Cancel transaction, retain cash in account
 - A4: Customer Cancellation - Return card, terminate use case
```

### Example 3: Requirements Prioritization using MoSCoW

**Scenario**: An e-commerce website development project has the following requirements. Apply MoSCoW prioritization:

1. User registration and login
2. Product catalog with search
3. Shopping cart functionality
4. Payment gateway integration
5. Advanced recommendation engine
6. Social media integration
7. Order tracking
8. Customer review system

**Solution**:

**Must Have (Critical for launch)**:

- 1. User registration and login
- 3. Shopping cart functionality
- 4. Payment gateway integration
- 7. Order tracking

**Should Have (Important, not critical)**:

- 2. Product catalog with search
- 8. Customer review system

**Could Have (Enhancements)**:

- 5. Advanced recommendation engine
- 7. Social media integration

**Would Like (Future releases)**:

- All social features can be enhanced in subsequent releases

## 8. Assessment Questions

### Multiple Choice Questions

**Question 1**: In the IEEE 830 standard for SRS, which section contains the "User Characteristics" and "Product Perspective" information?

A) Introduction
B) Overall Description
C) Functional Requirements
D) Appendices

**Answer**: B) Overall Description. The Overall Description section provides context about the system's environment, including user characteristics, product perspective, design constraints, and assumptions.

---

**Question 2**: Consider two functional requirements R1 and R2 that specify conflicting behaviors for the same input condition. What is the appropriate first step in requirements analysis to resolve this conflict?

A) Implement both requirements and allow runtime resolution
B) Elicit additional information from stakeholders to clarify the true requirement
C) Remove both requirements from the SRS
D) Prioritize based on development cost alone

**Answer**: B) Elicit additional information from stakeholders. Conflicts between functional requirements must be resolved through further elicitation to determine the correct system behavior. Premature implementation decisions or elimination of requirements without stakeholder input can lead to system failure.

---

**Question 3**: A system requires that "all database queries must complete within 2 seconds for 95% of requests under normal operating conditions." This is an example of:

A) A functional requirement
B) A non-functional requirement specifying performance
C) A user requirement
D) A business requirement

**Answer**: B) A non-functional requirement specifying performance. This requirement describes how the system should perform (response time, percentile-based threshold) rather than what the system should do. Performance is a quality attribute classified under non-functional requirements.

---

**Question 4**: In use case modeling, what is the purpose of an "include" relationship between use cases?

A) To model optional behavior that may or may not execute
B) To model mandatory behavior that is extracted into a separate use case for reuse
C) To show inheritance between actors
D) To define system boundaries

**Answer**: B) To model mandatory behavior that is extracted into a separate use case for reuse. The include relationship indicates that one use case incorporates the behavior of another use case. This is used when common functionality is shared across multiple use cases and needs to be defined once for reusability.

---

**Question 5**: Which requirements prioritization method uses pairwise comparisons to compute relative weights?

A) MoSCoW Method
B) Hundred-Dollar Method
C) Analytic Hierarchy Process (AHP)
D) Kano Model

**Answer**: C) Analytic Hierarchy Process (AHP). AHP uses a pairwise comparison matrix where stakeholders compare requirements relative to each other. The matrix is analyzed mathematically (eigenvalue analysis) to compute priority weights for each requirement.

---

### Short Answer Questions

**Question 1**: Explain the difference between forward and backward requirements traceability.

**Answer**: Forward traceability maps requirements to downstream artifacts (design, implementation, test cases), ensuring each requirement is addressed in the system. Backward traceability maps artifacts back to source requirements, ensuring no unauthorized functionality is added. Forward traceability answers "what design elements implement this requirement?" while backward traceability answers "why was this component implemented?"

---

**Question 2**: List three techniques for requirements elicitation and explain one advantage and one disadvantage of each.

**Answer**:

- **Interviews**: Advantage - allows in-depth exploration of stakeholder needs. Disadvantage - time-consuming and requires skilled interviewers.
- **Questionnaires**: Advantage - can reach many stakeholders quickly. Disadvantage - limited ability to explore unexpected issues.
- **Observation**: Advantage - reveals implicit requirements users cannot articulate. Disadvantage - obtrusive and may alter user behavior.

---

**Question 3**: What are the six quality characteristics defined in the ISO/IEC 25010 standard relevant to software requirements?

**Answer**: The ISO/IEC 25010 standard defines: Functional Suitability (including functional completeness and correctness), Performance Efficiency (including time behavior, resource utilization, and capacity), Compatibility (including co-existence and interoperability), Usability (including appropriateness, recognizability, learnability, and user error protection), Reliability (including maturity, availability, and fault tolerance), Security (including confidentiality, integrity, and non-repudiation), Maintainability (including modularity, reusability, and analysability), and Portability (including adaptability, installability, and replaceability).

---

### Long Answer Questions

**Question 1**: A hospital management system has conflicting requirements: Doctors require detailed patient records access for treatment, while Privacy Officers require strict access controls to comply with HIPAA regulations. Doctors want quick access without multiple authentication steps, while Privacy Officers want multi-factor authentication for all record access.

Using requirements analysis techniques, propose a resolution approach that addresses both stakeholder concerns while maintaining system usability and security compliance.

**Answer**: This scenario presents a classic conflict between usability (doctors require quick access) and security (privacy officers require strict controls). The resolution approach should include:

1. **Stakeholder Analysis**: Identify that doctors (treatment providers) and privacy officers represent different stakeholder categories with legitimate but conflicting interests.

2. **Context-Based Security**: Implement role-based access control where authentication requirements scale with data sensitivity. Emergency access (break-the-glass) can be provided for critical situations with full audit logging.

3. **Conflict Resolution through Negotiation**: Facilitate a session where stakeholders agree on acceptable trade-offs, possibly accepting slightly longer authentication for regular access in exchange for emergency access privileges.

4. **Compromise Solution**: Implement single sign-on for routine access within a session, combined with multi-factor authentication at session initiation. Sensitive record categories (e.g., psychiatric, HIV records) require additional authentication.

5. **Prioritization using AHP**: Weight security slightly higher than convenience, but not so high that it impedes patient care.

6. **Validation**: Prototype the solution with representative doctors and privacy officers to verify acceptance.

---

**Question 2**: Explain the requirements engineering process and describe how each activity contributes to producing a high-quality SRS document. Include a discussion of why iteration is necessary in requirements engineering.

**Answer**: The requirements engineering process consists of four interconnected activities that form an iterative cycle:

**Elicitation** gathers stakeholder needs through interviews, workshops, observation, and prototyping. This activity produces a raw collection of stakeholder desires, constraints, and expectations. Without thorough elicitation, critical requirements may be missed.

**Analysis** examines elicited requirements for conflicts, ambiguities, and inconsistencies. Mathematical techniques can model requirement relationships. Analysis transforms raw stakeholder input into refined, unambiguous specifications. This activity prevents requirement defects from propagating to later phases.

**Specification** documents analyzed requirements in a formal structure (SRS) following IEEE 830 guidelines. Specification produces the contractual basis between stakeholders and developers. The SRS must be complete, consistent, unambiguous, and modifiable.

**Validation** verifies the SRS accurately represents stakeholder needs through reviews, prototyping, and test case derivation. Validation catches specification errors before implementation begins.

**Iteration** is necessary because:

- Stakeholders cannot articulate all needs initially
- Requirements evolve as understanding deepens
- Conflicts emerge during analysis requiring re-elicitation
- External changes (regulations, technology) necessitate updates

The iterative cycle continues until requirements stabilize and stakeholders approve the SRS as accurately representing their needs.

---

## 9. Summary

Requirement Analysis is a foundational phase in software engineering that directly determines project success or failure. This module covered:

1. **Requirements Engineering Framework**: The systematic process of elicitation, analysis, specification, and validation that transforms stakeholder needs into formal requirements documentation.

2. **Requirements Classification**: The distinction between functional requirements (what the system does) and non-functional requirements (how the system performs), including quality attributes defined in ISO/IEC 25010.

3. **Elicitation Techniques**: Methods including interviews, questionnaires, observation, prototyping, and JAD workshops for gathering stakeholder requirements.

4. **Analysis Techniques**: Use case modeling, requirements prioritization (MoSCoW, AHP), traceability matrices, and conflict resolution strategies.

5. **SRS Documentation**: The IEEE 830 standard for producing well-structured, complete, consistent, and unambiguous requirements specifications.

The principles and techniques learned in this module form the foundation for successful software development and are essential for any software engineering professional.
