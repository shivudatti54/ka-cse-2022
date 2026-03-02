# Protection - Summary

## Key Definitions and Concepts

- PROTECTION: Mechanisms that control access to system resources, ensuring authorized use of files and directories

- PROTECTION DOMAIN: A set of objects and the operations permitted on those objects, associated with a process or user

- ACCESS CONTROL LIST (ACL): A protection mechanism that associates each object with a list of users and their permitted operations

- CAPABILITY LIST: A protection mechanism that associates each domain with a list of objects and permitted operations

- DISCRETIONARY ACCESS CONTROL (DAC): Protection policy where resource owners determine access rights

- MANDATORY ACCESS CONTROL (MAC): System-enforced protection policy that users cannot override

## Important Formulas and Theorems

- Unix permission bits: Three sets of three bits each (owner, group, others) representing read (4), write (2), and execute (1) permissions. Numeric notation adds these values: chmod 755 sets rwxr-xr-x

- Protection matrix: Theoretical model showing domains (rows) and objects (columns) with rights in each cell

## Key Points

- Protection mechanisms prevent unauthorized access to files and maintain data integrity in multi-user systems

- ACLs provide fine-grained, object-centric control while capability lists offer process-centric protection

- Unix systems use permission bits (rwxr-xr-x) for basic protection with additional special bits for setuid, setgid, and sticky bit

- User authentication verifies identity before granting access, ranging from passwords to biometrics

- The principle of least privilege states that processes should have minimum necessary permissions

- Protection in distributed systems requires additional mechanisms like Kerberos and PKI due to network security concerns

- Protection differs from security: protection handles internal access control while security encompasses broader threats

## Common Mistakes to Avoid

- Confusing ACLs with capability lists: Remember ACLs are attached to objects while capabilities are attached to domains

- Believing passwords alone provide adequate security: Modern systems require multi-factor authentication

- Ignoring the order of permission checking in Unix: Owner permissions are checked first, then group, then others

- Overlooking directory permissions: Directories require execute permission to access contained files and read permission to list contents

## Revision Tips

- Practice interpreting and setting Unix permissions using both symbolic (u+rwx) and numeric (755) notation

- Draw protection matrices for simple scenarios to visualize domain-object relationships

- Compare DAC and MAC with concrete examples from different operating systems

- Review how modern file systems (NTFS, ext4) implement extended ACLs beyond traditional Unix permissions

- Understand the relationship between authentication (who you are) and authorization (what you can do)