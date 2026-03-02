# Discretionary Role-Based Access Control (DRBAC) - Summary

## Key Definitions and Concepts

- **Access Control:** The process of regulating who can access what resources in a computing environment, involving identification, authentication, and authorization.
- **Subject:** An active entity (user, process, program) that requests access to resources.
- **Object:** A passive entity (file, database, printer) containing or receiving information.
- **Permission:** The specific type of access (read, write, execute, delete) granted to a subject for an object.
- **Discretionary Access Control (DAC):** Access model where resource owners have complete discretion over access policies.
- **Role-Based Access Control (RBAC):** Access model where permissions are assigned to organizational roles, and users are assigned to roles based on job functions.
- **Discretionary RBAC (DRBAC):** Hybrid model combining RBAC structure with discretionary privileges allowing role holders limited flexibility in access delegation.
- **Role Hierarchy:** Organizational structure where child roles inherit permissions from parent roles.
- **Separation of Duties (SoD):** Security principle preventing single individuals from completing critical transactions alone—implemented as Static SoD (mutually exclusive roles) and Dynamic SoD (session-based restrictions).

## Important Formulas and Theorems

- **RBAC Formal Definition:** A DRBAC system can be formally defined as (U, R, P, S, UA, PA, RH) where U=users, R=roles, P=permissions, S=sessions, UA=user-role assignments, PA=permission-role assignments, and RH=role hierarchy relations.
- **Least Privilege Principle:** Users should be granted only the minimum permissions necessary to perform their job functions—core to DRBAC role design.
- **Permission Assignment:** `Perm(r) = {p | (p, r) ∈ PA} ∪ {p | (∃r' ∈ R) [(r' ∈ RH*(r)) ∧ (p, r') ∈ PA]}`

## Key Points

- DRBAC combines the administrative efficiency of RBAC with discretionary flexibility for task-specific access delegation.
- Role hierarchies in DRBAC support permission inheritance but can be constrained to prevent excessive privilege accumulation.
- Separation of duties (both static and dynamic) prevents fraud and error in critical business processes.
- DRBAC maintains comprehensive audit logs for all discretionary access grants, supporting compliance and forensic analysis.
- The model is particularly suitable for large organizations with dynamic job responsibilities and regulatory compliance requirements.
- Real-world applications include healthcare systems (PHI access), financial systems (transaction approval), and enterprise resource planning.

## Common Mistakes to Avoid

- Confusing DAC with DRBAC—DRBAC is NOT simply "DAC with roles" but a structured hybrid with controlled discretionary elements.
- Overlooking separation of duties—many exam answers fail to mention SoD constraints when designing access control.
- Ignoring audit requirements—every discretionary access must be logged, including the reason and duration.
- Creating too many roles—role explosion defeats the administrative benefits of RBAC; consolidate where possible.

## Revision Tips

1. Practice drawing DRBAC models for common scenarios—university systems, hospitals, banks are typical exam examples.
2. Memorize the RBAC96 model components (core, hierarchy, SSoD, DSSoD).
3. Always relate answers to the principle of least privilege and audit accountability.
4. Review the differences between DAC, MAC, RBAC, and DRBAC in a comparative table.
5. Solve previous year DU questions on access control models to understand the exam pattern and depth expected.