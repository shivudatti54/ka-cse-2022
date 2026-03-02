# Protection And Security - Summary

## Key Definitions

- **Protection**: Internal OS mechanisms controlling resource access by users and processes
- **Security**: Measures defending the system against external threats and unauthorized access
- **Subject**: Active entity (process or user) that requests access to resources
- **Object**: Passive resource (file, memory, device) being accessed
- **Access Control List (ACL)**: List associated with each object specifying permitted subjects and operations
- **Capability List**: List associated with each subject specifying permitted objects and operations
- **Authentication**: Process of verifying user identity
- **Authorization**: Process of determining permitted actions for authenticated users
- **Privilege Escalation**: Attack gaining elevated access beyond authorized privileges

## Important Formulas

- **Unix Permission Model**: Permissions represented as 9-bit string (owner/group/others × read/write/execute)
- **Octal Permission Notation**: Read=4, Write=2, Execute=1; permissions summed for each category
- **Bell-LaPadula**: Simple Security Property (no read up), Star Property (no write down)

## Key Points

1. Protection mechanisms enforce internal access control; security mechanisms defend against external threats
2. The CIA triad (Confidentiality, Integrity, Availability) defines fundamental security goals
3. Authentication must precede authorization in the access control process
4. ACLs are object-centric while capability lists are subject-centric
5. The principle of least privilege minimizes potential damage from compromised accounts
6. Buffer overflows represent a primary vector for privilege escalation attacks
7. Multi-factor authentication significantly improves security over single-factor methods
8. Security models like Bell-LaPadula provide theoretical foundations for secure system design

## Common Mistakes

1. Confusing protection (internal access control) with security (external defense mechanisms)
2. Treating authentication and authorization as interchangeable concepts
3. Ignoring the importance of least privilege in system configuration
4. Believing password-based authentication alone provides adequate security
5. Overlooking the need for defense in depth—relying on single security mechanisms
6. Failing to consider social engineering attacks, which exploit human psychology rather than technical vulnerabilities