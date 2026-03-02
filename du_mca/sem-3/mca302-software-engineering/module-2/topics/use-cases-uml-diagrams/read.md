# Use Cases UML Diagrams

## Introduction
Use Case diagrams form the foundation of requirement analysis in software engineering, providing visual representation of system functionality from end-user perspective. As a core component of Unified Modeling Language (UML), they bridge communication between stakeholders and developers by modeling interactions between actors (users/systems) and key system functionalities.

In DU's MCA curriculum, mastery of Use Case diagrams is critical for Software Requirements Specification (SRS) documentation and agile development processes. Industry reports show 78% of successful projects employ UML diagrams in initial phases (Standish Group, 2023). These diagrams help identify system boundaries, validate requirements, and prevent scope creep - essential skills for Delhi University graduates targeting product management or analyst roles.

Modern applications range from banking transaction systems to AI-powered chatbots. For instance, PhonePe's payment failure handling and IRCTC's ticket booking system both rely on complex Use Case models. Understanding extension points, inclusion relationships, and actor generalization becomes crucial when scaling systems for India's digital infrastructure needs.

## Key Concepts
1. **Actors**: External entities interacting with system (Human/System roles)
   - Primary vs Secondary Actors
   - Generalization (e.g., User → Customer/Admin)

2. **Use Cases**: Ellipses representing system functionalities
   - Atomic business goals ("Withdraw Cash")
   - Level: Abstract (User Management) vs Concrete (Reset Password)

3. **Relationships**:
   - **Include**: Mandatory dependency (<<include>>)
     ```plaintext
     "Withdraw Cash" includes "Authenticate User"
     ```
   - **Extend**: Optional/conditional flow (<<extend>>)
     ```plaintext
     "Order Book" extends "Search Book" with "Out-of-Stock Handling"
     ```
   - **Generalization**: Inheritance between use cases/actors

4. **System Boundary**: Rectangle enclosing all use cases

5. **Stereotypes**: <<extend>>, <<include>>, <<system>>

6. **Scenario Modeling**:
   - Basic Flow (Happy Path)
   - Alternate Flows (Exceptions)
   - Postconditions

## Examples

**Example 1: Online Exam System**
```
Actors: Student, Examiner, Admin

Use Cases:
- Take Exam (Student)
- Evaluate Answer (Examiner)
- Generate Report (Admin)

Relationships:
- "Take Exam" includes "Login"
- "Generate Report" extends "View Results" if results are published
```

**Step-by-Step Solution:**
1. Identify primary actors: Student, Examiner
2. Define system boundary as "Online Examination Platform"
3. Connect Student to "Take Exam" with association line
4. Add <<include>> relationship from "Take Exam" to "Login"
5. Create extension point "Results Published" for "Generate Report"

**Example 2: E-Commerce Return Process**
Model a 30-day return policy with conditions:
- Basic Flow: Initiate Return → Approve → Refund
- Alternate Flow: Return window expired
- Exception: Damaged product deduction

Use <<extend>> for "Validate Return Window" and "Assess Product Condition"

## Exam Tips
1. Always start by identifying ALL actors - missing secondary actors (e.g., Payment Gateway) is common error
2. Use proper stereotype notation: <<include>> vs <<extend>> arrows
3. For 8-mark questions: Follow DU's 3-step approach - 1) List actors, 2) Define use cases, 3) Establish relationships
4. In case studies (like banking apps), highlight security-related use cases ("Two-Factor Authentication")
5. Remember: Actors are OUTSIDE system boundary, use cases INSIDE
6. When describing generalization, use inheritance tree notation
7. For "virtual" actors like Cron Jobs, use <<system>> stereotype