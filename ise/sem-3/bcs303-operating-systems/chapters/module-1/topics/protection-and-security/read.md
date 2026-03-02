# Protection and Security

## Introduction

Protection and Security constitute fundamental pillars of modern operating systems, ensuring that computer resources are accessed only by authorized users and processes in defined ways. While often used interchangeably, these terms represent distinct but complementary concepts in operating system design. Protection refers to the internal mechanisms within the operating system that control access to resources by various users and processes, primarily concerned with ensuring proper resource utilization. Security, on the other hand, encompasses the external measures and policies that safeguard the system against unauthorized access, intrusion, and malicious attacks from external sources.

In the context of the University of Delhi's Computer Science curriculum, understanding protection and security mechanisms is essential for developing robust and reliable software systems. With the proliferation of networked computing and cloud services, operating system security has become paramount in protecting sensitive data and maintaining system integrity. Modern operating systems implement sophisticated protection mechanisms that balance security requirements with usability, performance, and flexibility. This topic explores the theoretical foundations, implementation strategies, and practical applications of protection and security in operating systems, providing students with the knowledge necessary to design and analyze secure computing environments.

## Key Concepts

### Distinction Between Protection and Security

Protection mechanisms operate within the boundaries of the operating system, governing how processes and users access resources such as files, memory, and devices. The primary goal of protection is to ensure that each component of the system uses resources only as intended, preventing accidental or intentional misuse. Security, conversely, deals with the defense mechanisms against external threats, including authentication, encryption, firewalls, and intrusion detection systems. While protection is concerned with internal access control, security focuses on external threats and boundary defenses.

### Access Matrix Model

The access matrix represents a fundamental abstraction for describing protection policies in operating systems. This model defines rights or permissions that subjects (users or processes) possess over objects (resources such as files, devices, or memory locations). In this two-dimensional matrix, rows represent subjects, columns represent objects, and each cell contains the access rights that the subject has over that particular object. The access matrix provides a flexible and intuitive framework for specifying complex protection policies, allowing system administrators to define fine-grained access control over system resources.

The access matrix model supports various access rights including read, write, execute, delete, and ownership. However, implementing the access matrix as a complete two-dimensional structure is impractical for large systems due to memory overhead. Two primary implementations address this limitation: Access Control Lists (ACLs) and Capability Lists (CapLists). ACLs store access rights with each object, listing which subjects can access the object and with what permissions. Capability lists associate each subject with a set of objects and their corresponding rights, effectively storing the column information for each subject.

### Access Control Lists (ACLs)

An Access Control List maintains a list of permissions attached to each object in the system. When a user attempts to access an object, the operating system consults the ACL to determine whether the requested access is permitted. UNIX and Linux file systems implement a form of ACL through permission bits (read, write, execute for owner, group, and others) and extended ACLs that provide more granular control. Windows operating systems use ACLs extensively for file security, registry keys, and other system objects.

ACLs offer several advantages including simplicity of revocation (removing a user from an object's ACL immediately revokes access) and intuitive resource-centric view. However, ACLs can become complex when many users have varying permissions across numerous objects, potentially leading to administrative overhead and performance implications when checking permissions for heavily shared resources.

### Capability Lists

A capability list represents a different approach where each user or process maintains a list of capabilities or tokens that specify their access rights to various objects. Each capability contains an identifier for the object and the rights the holder possesses over that object. When a process requests access to a resource, the system examines the process's capability list to verify appropriate permissions.

Capability-based systems provide efficient access checking since the system need only verify that the process possesses a valid capability for the requested object. However, capabilities pose challenges for revocation since the system must track all copies of a capability to effectively revoke access. Copying capabilities can propagate access rights beyond the original scope, complicating enforcement of the principle of least privilege.

### Authentication and Authorization

Authentication verifies the identity of users attempting to access the system, representing the first line of security defense. Common authentication mechanisms include passwords, smart cards, biometrics, and multi-factor authentication that combines multiple verification methods. Password-based authentication remains prevalent despite known vulnerabilities, prompting the development of techniques such as password hashing, salting, and complexity requirements to enhance security.

Authorization determines what an authenticated user can do within the system, implementing the access control policies defined by the protection model. After successful authentication, the operating system uses authorization mechanisms to enforce permissions and ensure users access only resources they are entitled to use. The separation of authentication and authorization follows the principle of least privilege, granting users only the minimum access necessary to perform their tasks.

### Encryption and Data Protection

Encryption transforms data into an unreadable format that can only be decrypted with the appropriate key, providing confidentiality protection for stored and transmitted data. Modern operating systems implement encryption at various levels including full disk encryption, file system encryption, and transport layer security for network communications. Encryption protects sensitive data even when physical security is compromised, forming a critical component of comprehensive security strategies.

### Principles of Protection

The principle of least privilege states that users and processes should be granted only the minimum permissions necessary to accomplish their tasks, limiting potential damage from accidental or malicious actions. This principle extends to system components, requiring that each part of the system operate with the fewest privileges needed for its function.

The principle of separation of privilege divides critical operations among multiple entities, requiring that several conditions be satisfied before access is granted. This approach prevents single points of failure and reduces the likelihood of unauthorized access through compromised credentials or system components.

### Security Models

The Bell-LaPadula model focuses on confidentiality, establishing rules that prevent information flow from higher security levels to lower security levels. The model defines two primary rules: the simple security property (no read up) prohibits reading information at a higher security level, and the star property (no write down) prevents writing information to a lower security level. This model is particularly relevant for military and government applications where information confidentiality is paramount.

The Biba integrity model addresses information integrity rather than confidentiality, preventing contamination of higher integrity data by lower integrity information. The model implements the simple integrity property (no read down) and the star integrity property (no write up), ensuring that trusted processes do not receive information from less trusted sources and that untrusted processes cannot modify higher integrity information.

### Types of Security Attacks

Denial of Service (DoS) attacks overwhelm system resources, making services unavailable to legitimate users. Distributed denial of service (DDoS) attacks coordinate multiple sources to amplify the attack impact. Buffer overflow attacks exploit vulnerabilities in software to inject malicious code and gain unauthorized system access. Malware including viruses, worms, trojans, and ransomware represents another category of threats that operating systems must defend against through security updates, antivirus software, and user education.

## Examples

### Example 1: UNIX File Permission System

Consider a file named "results.txt" with permission string "rw-r-----" belonging to user "student" and group "csstudents". This permission specification means the owner (student) can read and write the file, members of the csstudents group can read the file, and all other users have no permissions.

When user "student" attempts to read the file:
1. The system identifies the user as "student" through authentication
2. It determines that "student" is the file owner
3. Since the owner permission bits are "rw-", read access is granted
4. The file content is returned to the user process

When user "guest" (not owner, not in csstudents group) attempts to read the file:
1. The system identifies "guest" through authentication
2. It determines that "guest" is neither owner nor in the file's group
3. The system falls back to "other" permissions which are "---"
4. Access is denied, returning a permission denied error

### Example 2: Access Matrix Implementation

Suppose we have three users (A, B, C) and three files (File1, File2, File3). The access matrix would be:

| Subject | File1 | File2 | File3 |
|---------|-------|-------|-------|
| A       | read, write | read | write |
| B       | read | read, write | execute |
| C       | execute | read, write | read, write, execute |

Using ACLs, File1 would store: A: read,write; B: read; C: execute
Using Capability Lists, User A would store: File1: read,write; File2: read; File3: write

When user B attempts to read File2, the system checks B's capability list or File2's ACL, finds "read" permission, and grants access. When user C attempts to modify File1, the system finds only "execute" permission and denies the write operation.

### Example 3: Multi-Factor Authentication Flow

Consider a login system implementing two-factor authentication:

1. User enters username and password (first factor: something they know)
2. System validates password against stored hash
3. On successful password validation, system sends one-time password (OTP) to registered mobile device (second factor: something they have)
4. User enters OTP within the validity period
5. System validates OTP and establishes authenticated session
6. Session token is generated and associated with user permissions
7. Subsequent requests include session token for authorization

This process demonstrates defense in depth, where multiple authentication factors must be satisfied before access is granted. Even if an attacker obtains the password, they cannot access the system without the second factor.

## Exam Tips

Understanding the distinction between protection and security frequently appears in DU examinations. Protection refers to internal mechanisms controlling resource access, while security encompasses external defenses against threats.

The access matrix model is a fundamental concept that examiners expect students to explain clearly. Be prepared to draw and explain access matrices, and describe how ACLs and capability lists implement this model conceptually.

Remember that ACLs are object-centric (column-oriented) while capability lists are subject-centric (row-oriented). This distinction affects revocation strategies and performance characteristics.

The Bell-LaPadula model emphasizes confidentiality with "no read up, no write down" rules, while the Biba model addresses integrity with "no read down, no write up" principles. Know which security property each model prioritizes.

Authentication verifies identity (who you are), while authorization determines permissions (what you can do). This distinction is crucial for understanding security mechanisms.

The principle of least privilege requires granting minimum necessary permissions, reducing potential damage from compromised accounts or processes. Know how to apply this principle in practical scenarios.

For file permission questions in UNIX-like systems, remember the order: owner permissions first, then group permissions, then others. The permission bits (read=4, write=2, execute=1) combine to form numeric representations.

Understand common attack types including DoS attacks, buffer overflows, and malware. Know how operating systems defend against these threats through mechanisms like process isolation, memory protection, and security updates.