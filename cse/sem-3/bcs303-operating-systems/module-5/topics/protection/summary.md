# Protection in Operating Systems - Summary

## Key Definitions

- **Protection**: Mechanisms that control access to system resources by users and processes
- **Protection Domain**: A set of objects and the rights that a process can exercise within the system
- **Access Matrix**: A two-dimensional model with domains as rows, objects as columns, and rights as cell contents
- **ACL (Access Control List)**: Object-centric protection mechanism listing domains and their rights for each object
- **Capability List**: Subject-centric mechanism where each domain holds capabilities specifying object access rights
- **Authentication**: Process of verifying the identity of a user or process
- **Authorization**: Process of determining what an authenticated user is permitted to do

## Important Formulas

- **UNIX Permission Octal Notation**: Each permission set (rwx) converts to octal where r=4, w=2, x=1
  - Example: rwxr-xr-- = 754 (7=4+2+1, 5=4+0+1, 4=4+0+0)

- **Access Matrix Check**: Access granted if (domain, object, right) ∈ Access Matrix

## Key Points

1. Protection ensures resource isolation and prevents unauthorized access in multi-user systems

2. The Access Matrix provides a global, abstract view of all protection relationships in the system

3. ACLs offer intuitive, object-centered control while capabilities offer efficient, subject-centered control

4. UNIX permissions use a 9-bit system (3 categories × 3 permissions) plus three special bits

5. Setuid allows programs to execute with owner privileges; setgid with group privileges

6. The sticky bit on directories prevents users from deleting files they don't own

7. Bell-LaPadula model emphasizes confidentiality with "no read up, no write down" rules

8. Biba model emphasizes integrity with "no read down, no write up" rules

9. Authentication should use salted password hashes rather than plaintext storage

10. The principle of least privilege minimizes security risks by granting minimal necessary permissions

## Common Mistakes

1. Confusing authentication with authorization—they serve different purposes in security

2. Believing file permissions alone are sufficient without proper authentication

3. Overlooking the difference between directory and file permission meanings (execute on directories means traversal)

4. Forgetting that root/superuser can bypass most permission checks, making system administration critical

5. Not understanding that ACLs in Windows and capability lists work differently—ACLs are object-specific while capabilities must be presented with each access request

6. Setting overly permissive permissions (777) thinking it solves access issues, which creates security vulnerabilities