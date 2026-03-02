# Protection and Security in Operating Systems - Summary

## Key Definitions and Concepts

- PROTECTION: Mechanisms that control access to system resources among processes and users within the operating system, ensuring proper usage and preventing interference.

- SECURITY: Safeguards that protect the operating system from external threats, unauthorized access, malicious attacks, and data breaches.

- ACCESS CONTROL LIST (ACL): A protection mechanism that associates each resource with a list specifying which subjects can access it and what operations are permitted.

- CAPABILITY LIST: A protection mechanism that associates each subject with a list of resources they can access and the permitted operations on each resource.

- AUTHENTICATION: The process of verifying the identity of a user or process before granting system access.

- AUTHORIZATION: The process of determining what operations an authenticated user or process is permitted to perform.

- PRINCIPLE OF LEAST PRIVILEGE: A security principle stating that processes and users should have only the minimum permissions necessary to accomplish their tasks.

- DOMAIN: A set of objects and the operations that can be performed on them; processes operate within domains.

## Important Formulas and Techniques

- Unix permission representation: THREE sets of permissions (owner, group, others) with THREE bits each (read, write, execute) = 9 bits total.

- Octal permission mapping: r=4, w=2, x=1. Permissions combine by adding values (rwx = 7, rw- = 6, r-- = 4).

- File permission display format: First character indicates file type (- for regular file, d for directory), followed by nine permission characters in three groups.

## Key Points

- Protection and security serve complementary but distinct purposes in operating systems; protection is internal while security addresses external threats.

- Access control lists associate permissions with objects (resources), while capability lists associate permissions with subjects (users/processes).

- Unix/Linux uses a 9-bit permission system with owner, group, and other categories, each having read, write, and execute permissions.

- Authentication verifies identity through passwords, tokens, or biometrics; authorization determines access rights after authentication.

- Multi-factor authentication combines multiple verification methods for enhanced security.

- The Bell-LaPadula model ensures confidentiality through simple security property and star property, preventing information flow from higher to lower security levels.

- The Biba model ensures integrity by preventing modification of data by unauthorized subjects.

- The principle of least privilege minimizes potential damage from compromised accounts or processes.

- Capability revocation presents challenges in capability-based protection systems.

## Common Mistakes to Avoid

- Confusing protection with security: Remember protection controls internal access, security defends against external threats.

- Mixing up ACLs and capability lists: ACLs are attached to objects, capabilities are attached to subjects.

- Forgetting that root/superuser typically bypasses permission checks in Unix systems, which is both powerful and dangerous.

- Overlooking the difference between authentication (who you are) and authorization (what you can do).

- Assuming that implementing security mechanisms alone is sufficient without proper configuration and user awareness.

## Revision Tips

- Practice interpreting Unix file permissions until you can quickly convert between symbolic (rwxr-x---) and octal (750) representations.

- Create comparison tables for ACLs vs capabilities, authentication methods, and security models.

- Understand the step-by-step flow from user login through authentication to authorization for resource access.

- Review the fundamental security principles: least privilege, separation of duties, defense in depth.

- Be prepared to explain why certain design choices were made in protection and security mechanisms.