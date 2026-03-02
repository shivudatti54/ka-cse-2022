# Protection and Security in Operating Systems

## Introduction

Protection and security represent fundamental pillars of modern operating systems, ensuring that system resources remain available, reliable, and accessible only to authorized users and processes. While often used interchangeably, these concepts address different aspects of system integrity: protection focuses on controlling access to resources among processes within the system, while security deals with safeguarding the system from external threats and unauthorized access. In an era where computers handle sensitive personal data, financial transactions, and critical infrastructure, understanding these mechanisms has become essential for every computer science student.

The evolution of operating systems from simple batch processing to complex multi-user environments has necessitated increasingly sophisticated approaches to resource management and access control. Modern operating systems must balance usability with security, ensuring that legitimate users can perform their tasks efficiently while malicious actors are prevented from causing harm. The University of Delhi's curriculum recognizes this importance, dedicating substantial instructional time to these topics as part of the foundational computer science training.

This chapter examines the theoretical foundations of protection and security, explores practical implementation mechanisms, and discusses the challenges faced by system designers in creating secure computing environments. Students will gain understanding of access control models, authentication mechanisms, and the various security threats that operating systems must defend against.

## Key Concepts

### Fundamental Principles of Protection

Protection mechanisms determine how processes interact with system resources such as files, memory, CPU time, and devices. The core principle behind protection is the specification of access rights and the enforcement of those rights by the operating system. A well-designed protection system ensures that each process can access only those resources it is authorized to use, preventing both accidental and intentional interference between processes.

The domain of protection defines a set of objects and the operations that can be performed on them. Processes operate within domains, and each domain specifies which resources the process can access and what operations are permitted. The relationship between domains can be structured in various ways: a simple system might have just user and kernel domains, while more complex systems establish multiple privilege levels. The crucial aspect is that the operating system must be able to determine whether a particular access request from a process in a specific domain should be granted.

Access control matrices represent one formal method for specifying protection policies. This matrix lists all subjects (processes or users), all objects (resources), and the permissions granted for each subject-object pair. While conceptually simple, this approach becomes impractical for large systems due to the sheer size of the matrix. In practice, operating systems use more compact representations such as access control lists or capability lists.

### Access Control Lists (ACLs)

An access control list associates with each object a list of subjects and their permitted operations. When a process attempts to access an object, the system checks the object's ACL to determine whether the process's owner has the necessary permissions. Windows NT-based systems and many modern file systems use variations of ACLs for file protection.

ACLs offer several advantages: they clearly show who has access to each resource, permissions can be modified easily by the resource owner, and they provide fine-grained control over different operations. However, ACLs can become complex when many users need access to many resources, and checking permissions requires searching through potentially lengthy lists for each access attempt.

### Capability Lists (Capsules)

In contrast to ACLs, capability lists are associated with subjects rather than objects. Each process or user possesses a capability list that enumerates all resources the subject can access and the operations permitted on each. Unix and Linux systems implement a simplified form of this concept through file descriptors and the file descriptor table maintained by each process.

Capability-based systems are efficient because checking access rights requires simply verifying that a valid capability exists in the subject's list. However, capability revocation becomes challenging—if a user's access to a resource must be removed, the system must locate and invalidate all copies of the capability across the system. This revocation problem has limited the pure adoption of capability-based systems in mainstream operating systems.

### Security Threats and Attacks

Operating systems face numerous security threats ranging from external attacks to internal misuse. Understanding these threats is essential for designing effective security mechanisms. The main categories of security threats include unauthorized access, data breaches, malware, denial of service attacks, and social engineering.

Unauthorized access occurs when individuals gain access to system resources without proper authentication or authorization. This can result from weak passwords, exploited system vulnerabilities, or improper configuration. Once inside, attackers may steal data, modify information, or use the compromised system as a launching point for further attacks.

Malware encompasses various malicious software types including viruses, worms, trojans, ransomware, and spyware. These programs can damage systems, steal information, or provide backdoors for attackers. Operating systems implement various defenses against malware, including antivirus software, application whitelisting, and sandboxing techniques.

Denial of service attacks aim to make system resources unavailable to legitimate users. These attacks may flood systems with traffic, exploit software bugs to crash services, or consume system resources through malicious computation. Distributed denial of service attacks use multiple compromised systems to amplify the impact.

### Authentication Mechanisms

Authentication verifies the granting identity of users before access to system resources. The most common authentication method remains the password system, where users prove their identity by providing a secret known only to them. Modern password systems employ cryptographic hashing with salt values to protect stored passwords even if the system is compromised.

Multi-factor authentication enhances security by requiring multiple forms of verification. This typically combines something the user knows (password), something the user possesses (token or phone), and something the user is (biometric). Many systems now support two-factor authentication using SMS codes, authenticator applications, or hardware tokens.

Biometric authentication uses physical or behavioral characteristics such as fingerprints, facial recognition, or voice patterns. While convenient, biometric systems have limitations including false acceptance and false rejection rates, and unlike passwords, biometric features cannot be changed if compromised.

### Security Models and Policies

Formal security models provide theoretical foundations for implementing secure systems. The Bell-LaPadula model focuses on confidentiality, establishing simple security properties that prevent information flow from higher security levels to lower ones. The Biba model addresses integrity, ensuring that data modifications occur only through authorized processes.

The principle of least privilege states that processes should operate with the minimum permissions necessary to accomplish their tasks. This principle limits the potential damage from compromised processes or user errors. Implementing least privilege requires careful design of permission systems and user habits.

Role-based access control assigns permissions to roles rather than individual users. Users are then assigned roles based on their responsibilities. This approach simplifies administration in large organizations and aligns permission management with organizational structure.

## Examples

### Example 1: Unix/Linux File Permission System

The Unix file permission system demonstrates practical protection implementation. Each file has three sets of permissions—for the owner, group, and others—each containing read (r), write (w), and execute (x) permissions. These permissions are represented as a 9-bit pattern or as octal numbers.

Consider a file with permissions "rwxr-x---" belonging to user "student" and group "cs students". This translates to owner having full permissions (read, write, execute), group having read and execute only, and others having no permissions. The octal representation is 750.

When a process attempts to access this file, the system checks the process's effective user ID against the file's owner. If they match, owner permissions apply. Otherwise, the system checks the process's group ID against the file's group; if they match, group permissions apply. Otherwise, others permissions determine access. The root user bypasses these checks entirely.

To change permissions, the chmod command modifies the permission bits. For instance, "chmod 640 report.txt" sets owner read-write, group read-only, and others no access. This granular control enables precise protection of sensitive files.

### Example 2: Access Control List Implementation

Suppose a corporate document management system uses ACLs to control access to a project file. The ACL might specify: Manager (Alice): read, write, delete; Team Lead (Bob): read, write; Team Member (Charlie): read; Intern (David): no access.

When Charlie attempts to open the file, the system searches the ACL for Charlie's entry, finds "read" permission, and grants read-only access. If Charlie attempts to modify the file, the system denies the request because write permission is not present. When David attempts any access, the absence of any permission entry results in denial.

This ACL approach allows the manager to delegate access by adding entries for new team members. The owner maintains control over who can access the document and what operations they can perform. Modern systems extend this model with inheritance, where folder ACLs automatically apply to contained files unless explicitly overridden.

### Example 3: Authentication and Authorization Flow

When a user logs into a secure system, authentication and authorization work together. Consider a student accessing a grade portal:

First, the system prompts for credentials. The student enters username "ravi2024" and password. The system computes the password hash and compares it with the stored hash. If they match, authentication succeeds—the system now knows the user is "ravi2024".

Next, the authorization phase determines what the authenticated user can access. The system queries its user database to find ravi2024's role: "student". It then checks the grade portal's policy for students: students can view their own grades but cannot modify them, and cannot view other students' grades.

When ravi2024 requests the grade for course CS301, the system verifies ravi2024 is enrolled in CS301, confirms the operation is "read only", and returns the grade information. If ravi2024 attempts to modify the grade, the system denies the request because student role lacks write permission on grade records. This separation of authentication and authorization provides flexibility and security.

## Exam Tips

For the University of Delhi end semester examinations, students should focus on the following key areas:

1. DIFFERENTIATE BETWEEN PROTECTION AND SECURITY: Protection controls access among processes within the system, while security defends against external threats. Understand that protection is primarily an internal matter whereas security addresses external actors.

2. ACCESS CONTROL LIST VERSUS CAPABILITY LIST: Be prepared to explain both approaches, their advantages, and disadvantages. ACLs associate permissions with objects; capabilities associate permissions with subjects.

3. UNIX FILE PERPERMISSIONS: Know how to read and interpret permission strings like "rwxr-x---" and their octal equivalents. Understand how owner, group, and other permissions work together.

4. AUTHENTICATION METHODS: Understand password-based authentication, multi-factor authentication, and biometric authentication. Know the strengths and limitations of each approach.

5. SECURITY THREAT CATEGORIES: Be familiar with unauthorized access, malware, denial of service attacks, and social engineering. Understand basic attack vectors and motivations.

6. PRINCIPLE OF LEAST PRIVILEGE: This fundamental security principle states that processes and users should have only the minimum permissions necessary to complete their tasks.

7. FORMAL SECURITY MODELS: Know the Bell-LaPadula model (confidentiality) and Biba model (integrity) at a conceptual level. Understand simple security properties and star properties.

8. REVOCATION IN PROTECTION SYSTEMS: Understand the challenge of revoking access rights, particularly in capability-based systems where capabilities may be distributed.

9. DOMAIN CONCEPT IN PROTECTION: A domain defines a set of objects and the operations permitted on them. Processes operate within domains, and the protection system enforces domain boundaries.

10. DIFFERENCE BETWEEN AUTHENTICATION AND AUTHORIZATION: Authentication verifies identity (who you are), while authorization determines what you can do (what you are allowed to access).