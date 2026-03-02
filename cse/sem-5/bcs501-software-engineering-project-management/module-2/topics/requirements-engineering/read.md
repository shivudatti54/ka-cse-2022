# Requirements Engineering

## 1. Introduction

Requirements Engineering (RE) constitutes a foundational discipline within software engineering that establishes the critical groundwork for successful software development initiatives. It encompasses the systematic processes of identifying, documenting, validating, and managing the requirements of a software system throughout its lifecycle. The paramount importance of requirements engineering cannot be overstated, as empirical studies consistently indicate that inadequately defined requirements account for approximately 40% of software project failures, positioning this discipline as critically important for engineering students and practitioners alike.

The discipline of Requirements Engineering serves as a crucial bridge between stakeholder needs and the technical teams responsible for implementing solutions. It transcends mere feature listing to encompass comprehensive understanding of the problem domain, business context, user expectations, organizational constraints, and regulatory requirements. The significance of effective requirements engineering manifests in multiple dimensions: it substantially reduces development time by minimizing rework iterations, decreases overall project costs, enhances customer satisfaction through accurate delivery of needed functionality, and facilitates maintainability by establishing clear specifications. Within academic curricula, this topic equips students with essential analytical skills to dissect user needs, reconcile conflicting stakeholder demands, and translate them into precise, testable, achievable, and traceable requirements that guide the entire development lifecycle from conception through retirement.

## 2. Classification of Requirements

Requirements are systematically categorized into distinct types based on their nature and purpose, each requiring different elicitation, analysis, and specification approaches.

### 2.1 Functional Requirements

Functional requirements specify the behavior and functionality of the system from the user's perspective. They define **what the system shall do** by describing inputs, outputs, processing logic, and exceptional conditions for each system function. These requirements are typically captured through use cases, user stories, or functional specifications and form the core value proposition of the software system.

**Examples:**

- "The system shall allow customers to transfer funds between accounts with real-time balance updates."
- "The system shall generate monthly statements for all account holders by the fifth business day of each month."
- "The system shall authenticate users using multi-factor authentication before granting access to sensitive data."

Functional requirements must satisfy the criteria of completeness, correctness, consistency, and verifiability. They should be unambiguous, feasible, and necessary for meeting stakeholder objectives.

### 2.2 Non-Functional Requirements

Non-functional requirements (NFRs), also termed quality requirements, specify the constraints under which the system must operate and the quality attributes it must exhibit. Unlike functional requirements that define **what** the system does, NFRs define **how well** the system performs its functions. These requirements are often critical differentiators that determine user satisfaction and system success.

**Categories of Non-Functional Requirements:**

| Category        | Description                                               | Examples                                                         |
| --------------- | --------------------------------------------------------- | ---------------------------------------------------------------- |
| Performance     | Response time, throughput, resource utilization           | "Transaction processing shall complete within 3 seconds"         |
| Security        | Confidentiality, integrity, authentication, authorization | "All sensitive data shall be encrypted using AES-256"            |
| Reliability     | Mean time between failures, availability, fault tolerance | "System shall maintain 99.9% availability"                       |
| Usability       | Learnability, efficiency, satisfaction, accessibility     | "New users shall accomplish primary tasks within 30 minutes"     |
| Maintainability | Modifiability, analyzability, testability                 | "Module changes shall not exceed 4 hours of integration testing" |
| Scalability     | Ability to handle increased load                          | "System shall support 10,000 concurrent users"                   |

The challenge with NFRs lies in their subjective nature and the difficulty of verification. They require quantifiable metrics and acceptance criteria to ensure proper validation.

### 2.3 Domain Requirements

Domain requirements emerge from the problem domain and specific industry regulations. They derive from the application area of the software system and may not be explicitly stated by stakeholders but are essential for system correctness.

**Examples:**

- Banking systems: "Interest calculations shall comply with Basel III regulations"
- Healthcare systems: "Patient data handling shall conform to HIPAA compliance requirements"
- E-commerce systems: "Tax calculations shall follow the tax jurisdiction of the customer's shipping address"

## 3. Requirements Engineering Process

The Requirements Engineering process comprises five interconnected phases that iteratively refine understanding and specifications.

### 3.1 Requirements Elicitation

Requirements Elicitation (also called requirements discovery) is the process of gathering requirements from various stakeholders through various techniques. This phase addresses the fundamental challenge of discovering what stakeholders actually need versus what they express.

**Elicitation Techniques:**

**Interviews** represent one-on-one or group sessions where analysts directly question stakeholders. Structured interviews employ predetermined questions for consistency, while unstructured interviews use open-ended discussions to explore topics flexibly. The effectiveness of interviews depends critically on interviewer skills and the establishment of rapport with stakeholders.

**Questionnaires and Surveys** serve for gathering quantitative data from large stakeholder populations. They efficiently identify patterns across user groups and establish statistical baselines. However, they lack the flexibility to explore unexpected issues or probe deeper into responses.

**Observation Techniques** involve analysts watching users perform tasks in natural work environments. Methods include participant observation, shadowing, and job shadowing. This technique reveals implicit knowledge and actual work practices that users cannot articulate or forget to mention.

**Prototyping** creates early approximations of the system to gather stakeholder feedback. Low-fidelity prototypes (paper-based, wireframes) are quick to create and modify, while high-fidelity prototypes (interactive mockups) provide realistic user experience. Prototyping effectively validates requirements and reduces interpretation ambiguity.

**Joint Application Development (JAD)** sessions convene multiple stakeholders in intensive collaborative workshops. These structured sessions accelerate requirements gathering through group dynamics, consensus building, and cross-functional communication.

**Brainstorming and Workshop Sessions** encourage creative idea generation and requirements exploration in group settings, particularly effective for identifying innovative solutions and uncovering hidden requirements.

### 3.2 Requirements Analysis

Requirements Analysis examines elicited requirements to identify inconsistencies, ambiguities, conflicts, and gaps. This critical phase transforms raw stakeholder input into refined, consistent, and feasible requirements.

**Key Activities:**

**Requirements Decomposition** breaks complex requirements into manageable components, establishing hierarchical relationships and dependencies. This decomposition facilitates understanding, allocation, and verification of requirements.

**Requirements Prioritization** ranks requirements based on business value, technical feasibility, dependencies, and stakeholder preferences. Common prioritization frameworks include MoSCoW (Must have, Should have, Could have, Won't have), Kano model, and pairwise comparison.

**Feasibility Analysis** evaluates technical, financial, and schedule feasibility of requirements. It identifies requirements that cannot be implemented with available technology, budget, or timeline constraints.

**Conflict Resolution** addresses conflicting requirements from different stakeholders through negotiation, compromise, and consensus-building techniques. Analysts must mediate competing interests while maintaining project objectives.

**Modeling Techniques:**

- **Object-Oriented Analysis**: Uses UML class diagrams, use case models, and sequence diagrams
- **Structured Analysis**: Employs data flow diagrams (DFDs), entity-relationship diagrams (ERDs)
- **Domain Modeling**: Creates conceptual models of the problem domain

### 3.3 Requirements Specification

Requirements Specification produces detailed, structured, and unambiguous descriptions of requirements in a formal document. The primary output is the Software Requirements Specification (SRS), which serves as a contractual agreement between developers and stakeholders.

**IEEE 830 Standard:**

The IEEE 830-1998 standard provides guidelines for SRS quality characteristics:

| Characteristic | Description                                                 |
| -------------- | ----------------------------------------------------------- |
| Complete       | All requirements are included; no placeholder statements    |
| Consistent     | No contradictory or conflicting requirements                |
| Verifiable     | Each requirement can be verified through test/inspection    |
| Traceable      | Each requirement has unique identification linked to source |
| Modifiable     | Document structure supports easy change management          |
| Unambiguous    | Each requirement has single, clear interpretation           |

**SRS Structure:**

1. Introduction (purpose, scope, definitions, references)
2. Overall Description (user characteristics, product perspective, constraints)
3. Functional Requirements (detailed behavior specifications)
4. Non-Functional Requirements (performance, reliability, security, etc.)
5. Appendices (glossary, analysis models, issues list)

**Formal Specification Techniques:**

Z notation, VDM, and Petri Nets provide mathematically rigorous specification languages for unambiguous requirements definition in safety-critical or complex systems.

### 3.4 Requirements Validation

Requirements Validation ensures that documented requirements accurately represent stakeholder needs and are testable. This phase catches errors early when correction costs are minimal, preventing expensive downstream rework.

**Validation Techniques:**

**Requirements Reviews** systematically examine requirements documentation through structured inspections and walkthroughs. Peer review teams identify defects, inconsistencies, and missing information.

**Prototyping** validates requirements through tangible system approximations, allowing stakeholders to experience and confirm their needs before full implementation.

**Test Case Generation** derives test cases from requirements to verify that requirements are testable and correctly specified. If requirements cannot be tested, they must be refined.

**Acceptance Criteria Definition** establishes clear, measurable conditions for requirement satisfaction, enabling objective validation.

**Validation Checklist:**

- Are requirements complete?
- Are requirements consistent?
- Are requirements feasible?
- Are requirements clear and unambiguous?
- Are requirements traceable to stakeholders?
- Are NFRs quantified with metrics?
- Are functional requirements testable?

### 3.5 Requirements Management

Requirements Management provides ongoing processes for controlling changes to requirements throughout the project lifecycle. Requirements inevitably evolve due to changing stakeholder needs, market conditions, technical constraints, and project learnings.

**Key Activities:**

**Change Control** establishes procedures for submitting, evaluating, approving, and implementing requirement changes. It prevents uncontrolled changes while accommodating necessary evolution.

**Version Control** maintains historical records of requirement changes, enabling rollback and audit trails.

**Requirements Traceability** establishes and maintains links between requirements and other project artifacts (design elements, code modules, test cases). Two types of traceability exist:

- **Forward Traceability**: Maps requirements to design elements and code
- **Backward Traceability**: Maps design/code back to source requirements

Traceability facilitates impact analysis when requirements change and ensures complete implementation coverage.

**Requirements Attributes** track metadata for each requirement, including:

- Unique identifier
- Source (stakeholder, document)
- Status (proposed, approved, implemented, verified)
- Priority
- Version
- Stability metric

## 4. Requirements Engineering Challenges

### 4.1 Common Problems

**Requirements Volatility**: Stakeholder needs change; requirements must accommodate evolution without derailing projects.

**Stakeholder Diversity**: Multiple stakeholders with conflicting interests require sophisticated negotiation and prioritization.

**Implicit Requirements**: Stakeholders fail to articulate requirements they consider obvious, leading to missing functionality.

**Ambiguity**: Natural language requirements permit multiple interpretations; formal methods mitigate this risk.

**Scope Creep**: Uncontrolled expansion of requirements beyond project boundaries causes budget and schedule overruns.

### 4.2 Best Practices

1. Engage stakeholders continuously throughout the project
2. Document all requirements with clear, measurable criteria
3. Establish explicit prioritization frameworks
4. Maintain bidirectional traceability
5. Conduct regular requirements reviews
6. Use prototyping for early validation
7. Implement formal change control processes

## 5. Summary

Requirements Engineering forms the cornerstone of successful software development, encompassing five critical phases: elicitation, analysis, specification, validation, and management. The discipline requires practitioners to master diverse techniques for gathering stakeholder needs, analyzing complex requirements, producing unambiguous specifications, verifying correctness, and managing evolution. The distinction between functional requirements (system behavior) and non-functional requirements (quality attributes) guides appropriate elicitation and validation approaches. Effective requirements engineering significantly reduces project failure risk, with studies indicating that inadequate requirements practices contribute to approximately 40% of project failures. for engineering students, mastering these concepts prepares them for professional practice where requirements quality directly determines system success and stakeholder satisfaction.
