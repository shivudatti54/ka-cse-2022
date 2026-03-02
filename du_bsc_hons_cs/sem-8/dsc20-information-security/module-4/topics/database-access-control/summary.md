# Database Access Control - Summary

## Key Definitions and Concepts

- **Authentication:** The process of verifying the identity of a user attempting to access the database (e.g., username/password, certificates, biometrics).

- **Authorization:** Determines what permissions an authenticated user has—what data they can access and what operations they can perform.

- **Discretionary Access Control (DAC):** Access control model where object owners discretionarily grant permissions to other users using GRANT/REVOKE statements.

- **Mandatory Access Control (MAC):** System-enforced access control based on security labels (clearance levels for users, classification levels for data).

- **Role-Based Access Control (RBAC):** Access rights are assigned to roles, not directly to users. Users are assigned to roles, simplifying administration.

- **Principle of Least Privilege:** Users should receive only the minimum privileges necessary to perform their job functions.

## Important SQL Commands

| Command | Purpose |
|---------|---------|
| GRANT | Assigns privileges to users/roles |
| REVOKE | Removes previously granted privileges |
| WITH GRANT OPTION | Allows recipient to propagate privileges |
| CREATE ROLE | Creates a new role for RBAC implementation |

## Key Points

1. Database access control operates through authentication (identity verification) followed by authorization (permission assignment).

2. DAC allows object owners to control access and propagate permissions; MAC enforces strict system-wide policies based on data classification.

3. RBAC is the most widely used model in modern enterprises due to simplified administration and support for separation of duties.

4. SQL's GRANT/REVOKE statements implement access control in relational databases. The WITH GRANT OPTION creates permission propagation chains.

5. Views provide an additional security layer by exposing only specific data columns or rows to authorized users.

6. Row-Level Security (RLS) restricts access to individual rows within a table based on user context—essential for multi-tenant applications.

7. Audit trails recording access attempts, queries, and modifications are critical for security monitoring and forensic analysis.

8. Database access control must align with organizational security policies and regulatory compliance requirements (GDPR, HIPAA, PCI-DSS).

## Common Mistakes to Avoid

1. **Confusing Authentication with Authorization:** Authentication answers "who are you?" while authorization answers "what can you do?"—these are distinct concepts.

2. **Granting Excessive Privileges:** Giving users more permissions than necessary violates the principle of least privilege and increases security risk.

3. **Forgetting to Revoke Privileges:** When employees leave or change roles, their access rights must be promptly revoked to prevent unauthorized access.

4. **Ignoring the WITH GRANT OPTION Implications:** When granting with this option, recipients can propagate permissions, potentially creating unintended wide access.

5. **Overlooking Audit Trails:** Without logging, security breaches may go undetected and forensic investigation becomes impossible.

## Revision Tips

1. Practice writing GRANT and REVOKE statements for different scenarios until syntax becomes automatic.

2. Create comparison tables for DAC, MAC, and RBAC—understand when each is appropriate.

3. Work through the university database example in the text to understand end-to-end RBAC implementation.

4. Remember that views can restrict both columns (projection) and rows (selection), providing granular access control.

5. Review your institution's attendance/grade system from an access control perspective—who can see what, and why?