# Protection in Operating Systems - Summary

## Key Definitions

- **Protection**: Mechanisms controlling access to system resources based on defined policies.
- **Domain**: A set of objects and the operations that may be performed on those objects.
- **Access Matrix**: A formal model representing protection state with domains as rows and objects as columns.
- **Access Control List (ACL)**: A list associated with each object specifying which domains can perform which operations.
- **Capability**: An unforgeable token granting specific access rights to an object.
- **Privilege Ring**: Hierarchical protection levels supported by hardware, typically numbered 0 (most privileged) to n (least privileged).

## Important Formulas

- **Unix Permission Bits**: `rwxr-x---` represents owner(rwx), group(r-x), others(---)
- **Permission Octal**: r=4, w=2, x=1; combining permissions: rw = 4+2 = 6, rwx = 4+2+1 = 7

## Key Points

1. Protection ensures that processes access only authorized resources, enforcing the principle of least privilege.

2. The access matrix provides a complete, formal specification of system protection state but is rarely implemented directly due to size constraints.

3. ACLs associate permissions with objects and excel at answering "who can access this object," while capabilities associate objects with permissions and excel at answering "what can this holder access."

4. Modern processors support protection rings (e.g., x86 rings 0-3) that separate kernel privileges from user applications.

5. Authentication verifies identity before granting access; authorization determines permitted operations after authentication.

6. Unix file permissions use a simplified ACL with three categories: owner, group, and others, each with read, write, execute permissions.

7. Setuid and setgid mechanisms enable controlled domain transitions, allowing programs to acquire elevated privileges.

8. Complete mediation requires that every access be checked against protection policy; TOCTOU (Time-of-Check-Time-of-Use) vulnerabilities can bypass protection.

## Common Mistakes

1. **Confusing Authentication with Authorization**: Authentication verifies who you are; authorization determines what you can do. These are distinct concepts often confused in exams.

2. **Thinking ACLs and Capabilities are Mutually Exclusive**: Many practical systems combine both approaches, using capabilities within processes and ACLs at system boundaries.

3. **Assuming File Permissions Apply to All Operations**: Some operations (like changing ownership or permissions) require root privileges regardless of file permissions.

4. **Ignoring the Difference Between Effective and Real User IDs**: Unix processes maintain both, and understanding when each is used is essential for analyzing setuid programs.