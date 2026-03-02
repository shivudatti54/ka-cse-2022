# Formal Requirement Extraction

## Table of Contents

- [Formal Requirement Extraction](#formal-requirement-extraction)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Requirement Gathering Techniques](#1-requirement-gathering-techniques)
  - [2. Requirements Classification](#2-requirements-classification)
  - [3. User-Centered Design Requirements](#3-user-centered-design-requirements)
  - [4. Requirements Documentation](#4-requirements-documentation)
  - [5. Requirements Analysis Techniques](#5-requirements-analysis-techniques)
- [Examples](#examples)
  - [Example 1: E-Commerce Platform Requirements Extraction](#example-1-e-commerce-platform-requirements-extraction)
  - [Example 2: Hospital Management System User Scenarios](#example-2-hospital-management-system-user-scenarios)
  - [Example 3: Requirements Prioritization Using MoSCoW](#example-3-requirements-prioritization-using-moscow)
- [Exam Tips](#exam-tips)

## Introduction

Formal Requirement Extraction is a systematic approach to gathering, analyzing, and documenting software requirements from stakeholders using structured techniques and notations. In the context of UI/UX design, this process ensures that user needs, business objectives, and technical constraints are clearly understood before the design phase begins. The importance of formal requirement extraction cannot be overstated—it serves as the foundation for creating user-centered designs that meet actual user needs while aligning with organizational goals.

The requirements engineering process comprises several phases: requirements elicitation (gathering), requirements analysis (understanding), requirements specification (documenting), and requirements validation (verifying). Formal requirement extraction emphasizes the use of structured methods and sometimes mathematical or formal notations to minimize ambiguity in requirements. This approach is particularly crucial in complex systems where vague or incomplete requirements can lead to costly redesigns and user dissatisfaction.

For the university's UI/UX course, understanding formal requirement extraction equips students with the skills to bridge the gap between stakeholders (clients, users, business analysts) and designers. It provides a systematic framework to transform informal user desires into precise, testable, and implementable requirements that guide the entire design process.

## Key Concepts

### 1. Requirement Gathering Techniques

**Interviews:** Structured or semi-structured conversations with stakeholders, users, and domain experts. Types include:

- **Closed interviews:** Fixed questions with predefined responses
- **Open-ended interviews:** Exploratory discussions allowing free expression
- **Focus groups:** Group discussions with multiple stakeholders

**Questionnaires and Surveys:** Structured data collection tools for gathering information from large user populations. Effective questionnaires include scaled questions (Likert scale), multiple-choice questions, and open-ended questions.

**Observation:** Direct observation of users in their natural environment (field studies). Techniques include:

- **Shadowing:** Following users while they perform tasks
- **Think-aloud protocols:** Users verbalize their thoughts while performing tasks
- **Contextual inquiry:** Combining observation with interviewing

**Document Analysis:** Reviewing existing documentation such as:

- Current system documentation
- Business process documents
- Industry standards and regulations
- Competitor analysis reports

**Prototyping:** Creating preliminary versions of the interface to gather feedback. Includes:

- **Paper prototypes:** Low-fidelity mockups
- **Digital prototypes:** High-fidelity interactive models
- **Wizard of Oz:** Simulated functionality

### 2. Requirements Classification

**Functional Requirements:** Describe what the system should do

- User authentication and authorization
- Data input and processing capabilities
- Report generation and display
- Integration with external systems

**Non-Functional Requirements (Quality Attributes):** Describe how the system should perform

- **Performance:** Response time, throughput, resource utilization
- **Usability:** Learnability, efficiency, satisfaction, error prevention
- **Reliability:** Availability, mean time between failures
- **Security:** Authentication, authorization, data protection
- **Accessibility:** Compliance with WCAG guidelines

**Domain Requirements:** Specific to the business domain

- Industry-specific regulations
- Business rules and workflows
- Domain terminology and concepts

### 3. User-Centered Design Requirements

**User Personas:** Fictional representations of target users based on research data

- Demographics (age, education, occupation)
- Goals and motivations
- Pain points with current solutions
- Technical proficiency level

**User Scenarios:** Narrative descriptions of how users interact with the system

- Preconditions, trigger events
- Step-by-step interactions
- Expected outcomes
- Alternative paths

**Use Cases:** Structured descriptions of system interactions from user's perspective

- Actors, system, preconditions
- Main flow of events
- Alternative flows
- Postconditions

### 4. Requirements Documentation

**Software Requirements Specification (SRS):** Comprehensive document containing:

- Introduction and overview
- Functional requirements
- Non-functional requirements
- User interface requirements
- System constraints
- Appendices and glossary

**User Requirements Document:** Business-focused document in stakeholder language

- Business objectives
- User needs and expectations
- High-level features

**Agile User Stories:** Short, simple requirement descriptions

- Format: "As a [user], I want [feature], so that [benefit]"
- Acceptance criteria for validation

### 5. Requirements Analysis Techniques

**Gap Analysis:** Identifying differences between current state and desired state

- Current capabilities assessment
- Target state definition
- Gap identification and prioritization

**Root Cause Analysis:** Understanding underlying reasons for user needs

- 5 Whys technique
- Fishbone diagrams (Ishikawa)

**Moscow Prioritization:** Requirements classification

- Must have (critical)
- Should have (important)
- Could have (desirable)
- Won't have (out of scope)

## Examples

### Example 1: E-Commerce Platform Requirements Extraction

**Scenario:** A retail company wants to develop an e-commerce mobile application.

**Step 1: Stakeholder Interviews**
Conducted interviews with:

- Marketing team: "Need personalized product recommendations"
- IT department: "Must integrate with existing inventory system"
- Customer service: "Quick access to order history is crucial"

**Step 2: User Observation**
Observed users shopping on competitor apps:

- Users struggled with complex navigation
- Checkout process caused high abandonment
- Search functionality was inadequate

**Step 3: Requirements Specification**

_Functional Requirements:_

- FR1: User shall be able to search products by name, category, and attributes
- FR2: User shall be able to add products to cart with size/color variants
- FR3: User shall be able to complete payment via credit card, UPI, and wallet
- FR4: User shall receive push notifications for order status updates
- FR5: System shall integrate with inventory management API

_Non-Functional Requirements:_

- NFR1: App load time shall not exceed 3 seconds on 4G network
- NFR2: System shall handle 10,000 concurrent users during sale events
- NFR3: All payment data shall be encrypted using AES-256
- NFR4: Interface shall comply with WCAG 2.1 AA accessibility standards

### Example 2: Hospital Management System User Scenarios

**Scenario:** Developing a patient management system for a multi-specialty hospital.

**User Persona: Dr. Sharma (Senior Physician)**

- Age: 45 years
- Goals: Quick access to patient history, efficient appointment management
- Pain Points: Currently, multiple systems don't communicate with each other

**Use Case: View Patient History**

- **Actor:** Doctor
- **Precondition:** Doctor must be logged in with valid credentials
- **Main Flow:**

1.  Doctor selects "Patient Search" from dashboard
2.  System displays search form (by name, ID, phone)
3.  Doctor enters search criteria and submits
4.  System displays matching patient list
5.  Doctor selects desired patient
6.  System displays comprehensive patient record including:

- Demographics
- Medical history
- Previous prescriptions
- Lab reports
- Appointment history
- **Alternative Flow:** No matching patients found → System displays "No results found" message
- **Postcondition:** Doctor can view complete patient history

### Example 3: Requirements Prioritization Using MoSCoW

**Scenario:** Banking application development with fixed deadline

**Project:** Mobile banking app for a regional bank

**Requirements List with Prioritization:**

1. **Must Have:**

- Account balance display
- Fund transfer (internal)
- Bill payments
- Secure authentication (biometric + PIN)
- Transaction history

2. **Should Have:**

- Fund transfer (external/NEFT)
- Cheque book request
- Branch/ATM locator

3. **Could Have:**

- Investment portfolio view
- Personal finance management tools
- Video customer support

4. **Won't Have (this release):**

- Loan applications
- Credit card management
- International remittance

## Exam Tips

1. **Know the difference between elicitation and extraction:** Requirement elicitation is the process of gathering requirements from stakeholders, while extraction involves deriving requirements from various sources through analysis.

2. **Remember key techniques:** Be familiar with all major techniques—interviews, questionnaires, observation, prototyping, document analysis—and know when each is appropriate.

3. **Distinguish requirement types:** Clearly differentiate between functional, non-functional, and domain requirements with examples of each.

4. **User story format:** Remember the standard format: "As a [user type], I want [goal], so that [benefit]" with clear acceptance criteria.

5. **Prioritization methods:** Know MoSCoW (Must, Should, Could, Won't) and Kano model for requirements prioritization.

6. **Non-functional metrics:** Understand how to measure non-functional requirements—response time (in seconds), availability (percentage), accessibility (WCAG levels).

7. **Documentation standards:** Know the structure of SRS and understand its purpose in the development lifecycle.

8. **User-centered design importance:** Emphasize that formal requirements extraction ultimately serves to create better user experiences.

9. **Stakeholder identification:** Remember that stakeholders include end users, clients, developers, regulatory bodies, and domain experts.

10. **Validation vs. verification:** Requirements validation ensures we're building the right product (meeting user needs), while verification ensures we're building the product right (meeting specifications).
