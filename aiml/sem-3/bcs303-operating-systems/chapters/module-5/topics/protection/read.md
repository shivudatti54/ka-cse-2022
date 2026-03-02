# Protection in File Systems

## Introduction

Protection in file systems is a critical aspect of operating system design that ensures the security and integrity of data stored on secondary storage devices. As multi-user computer systems became prevalent, the need to prevent unauthorized access to sensitive files and directories grew exponentially. Protection mechanisms form the backbone of any secure computing environment, governing which users can perform which operations on which files.

In the context of file systems, protection refers to the set of mechanisms and policies that control access to files and directories. These mechanisms prevent unauthorized users from reading, writing, executing, or deleting files they do not have permission to access. Without proper protection, the very concept of multi-user computing would be impractical, as any user could potentially access, modify, or delete another user's sensitive data.

The University of Delhi curriculum covers protection mechanisms as part of the file system module, recognizing that students must understand both the theoretical foundations and practical implementations of file protection. This topic becomes particularly relevant in today's interconnected world where data breaches can have severe consequences. Understanding protection mechanisms is essential for any computer science graduate, as these concepts form the foundation of modern operating system security.

## Key Concepts

### Access Matrix Model

The fundamental model for describing protection in operating systems is the access matrix. This is a two-dimensional matrix where rows represent domains (or users/groups) and columns represent objects (files, directories, or resources). Each cell in the matrix specifies the access rights that a particular domain has to a particular object.

The access matrix provides a clean, abstract representation of protection state. For example, if user Alice (domain) has read and write access to file "report.txt" (object), the cell at the intersection would contain {read, write}. This model is conceptually simple but can be inefficient to implement directly due to the potentially large size of the matrix in systems with many users and files.

There are two primary approaches to implementing the access matrix: access control lists (ACLs) and capability lists. Each approach has its advantages and trade-offs, which we will explore in detail.

### Access Control Lists (ACLs)

An Access Control List is associated with each object (file or directory) and contains a list of users or groups along with their access rights to that specific object. When a user attempts to access a file, the operating system checks the file's ACL to determine if the user has the required permissions.

The ACL approach is object-centric, meaning protection is defined at the level of each protected resource. In UNIX-like systems, this is implemented through permission bits (read, write, execute) for three categories: owner, group, and others. This simplified ACL provides basic protection without the overhead of maintaining complete ACLs for every file.

For example, consider a file "data.txt" with permissions "rw-r-----" (640 in octal). This means the owner has read and write permissions, members of the owning group have read-only access, and all other users have no access. The ACL conceptually looks like: {owner: rw, group: r, others: none}.

More sophisticated ACL implementations, as seen in Windows NTFS or modern UNIX systems with extended ACLs, can specify permissions for individual users or groups with fine-grained control. Extended ACLs can include specific deny rules, inheritance flags, and permissions for multiple groups.

### Capability Lists

In contrast to ACLs, capability lists are user-centric. Each user (or domain) possesses a capability list that enumerates all the objects they can access and the rights they have for each. The capability list is typically stored in the kernel and protected from direct user modification, ensuring that users cannot forge access rights.

The capability list approach is more efficient when users typically access only a small subset of the system's objects. Checking access involves simply locating the capability in the user's list rather than scanning an entire ACL. However, managing capabilities becomes complex when users need to access many objects or when sharing capabilities between processes is required.

### UNIX File Protection Mechanisms

UNIX file protection revolves around a simple yet effective scheme using permission bits. Each file has nine permission bits divided into three categories: owner (user), group, and others. Each category has three bits representing read (r), write (w), and execute (x) permissions.

The permission representation uses both symbolic notation (rwx r-x ---) and numeric notation (754). In numeric notation, each permission is assigned a value: read = 4, write = 2, execute = 1. The sum of these values within each category determines the permission set. For instance, rwx = 7 (4+2+1), rw- = 6 (4+2+0), r-x = 5 (4+0+1).

Additionally, UNIX systems implement special permission bits including the setuid bit, setgid bit, and sticky bit. The setuid bit allows a program to run with the owner's privileges, while setgid does the same with the group's privileges. The sticky bit, when set on a directory, restricts file deletion to the file owner, owner of the directory, or the root user.

### Access Rights and Protection Mechanisms

Various types of access rights can be controlled at the file system level. These include:

READ: The ability to view the contents of a file or directory listing.
WRITE: The ability to modify or delete file contents.
EXECUTE: The ability to run a file as a program.
APPEND: The ability to add data to the end of a file without modifying existing content.
DELETE: The ability to remove a file from the file system.
COPY: The ability to create a copy of the file.
OWNERSHIP: The ability to change ownership or permissions of a file.

Operating systems implement various protection mechanisms to enforce these rights. The most common include:
- User authentication (passwords, biometrics, tokens)
- Permission checking before every operation
- Encryption for data confidentiality
- Auditing and logging of access attempts
- Mandatory access control (MAC) in security-focused systems

### Domain and Protection Domains

A protection domain defines a set of objects and the operations that can be performed on them. Users or processes operate within domains, and the operating system enforces the access rules defined for each domain. Domains can be static (fixed throughout a process's lifetime) or dynamic (can change during execution).

In practical terms, a domain might correspond to a user account, a process, or a role. When you log into a system, you operate within your user domain. When you run a program with special privileges (like setuid), you temporarily operate in a different domain with elevated permissions.

## Examples

### Example 1: UNIX Permission Calculation

Consider a file named "project.c" owned by user "student" with group "cs2024" having the permission string "rw-rw-r--". Let's determine what operations each category can perform.

The permission string breaks down as:
- Owner (student): rw- = read + write = 4 + 2 = 6
- Group (cs2024): rw- = read + write = 4 + 2 = 6
- Others: r-- = read only = 4 + 0 + 0 = 4

Therefore, the numeric representation is 664. Now, if user "faculty" (not the owner and not in the cs2024 group) attempts to:
- Read the file: ALLOWED (others have read permission)
- Write to the file: DENIED (others only have read permission)
- Execute the file: DENIED (others do not have execute permission)

If the permissions were changed to "rwxr-x---" (750), the analysis would be:
- Owner: rwx = 7 (full permissions)
- Group: r-x = 5 (read and execute)
- Others: --- = 0 (no permissions)

In this case, a user not in the cs2024 group would be denied all access to the file.

### Example 2: ACL Implementation in Windows-style System

Suppose we have a file "budget.xlsx" with the following ACL entries:
- Administrator: Full Control
- Finance_Manager: Read, Write, Execute
- Accountant: Read, Write
- Intern: Read
- Everyone: Deny Write

When an intern attempts to modify the file:
1. System checks if Intern is a member of "Intern" group - YES
2. Intern has Read permission - ALLOWED to read
3. Intern attempts Write - DENIED (explicit Intern permission does not include Write)
4. Even though "Everyone" might have other permissions, explicit Deny takes precedence

This demonstrates how ACLs evaluate permissions in a specific order, with explicit deny rules overriding allow rules.

### Example 3: Access Matrix to ACL Conversion

Consider a simple system with two users (Alice, Bob) and three files (File1, File2, File3). The access matrix is:

|        | File1   | File2   | File3   |
|--------|---------|---------|---------|
| Alice  | Read,Write | Read    | Full    |
| Bob    | Read    | Read,Write | None    |

Converting to ACLs:
- File1 ACL: Alice: Read,Write | Bob: Read
- File2 ACL: Alice: Read | Bob: Read,Write
- File3 ACL: Alice: Full | Bob: None

Converting to Capability Lists:
- Alice's capabilities: File1 (Read,Write), File2 (Read), File3 (Full)
- Bob's capabilities: File1 (Read), File2 (Read,Write), File3 (None)

This example illustrates how the same protection policy can be represented in different formats, each suitable for different implementation strategies.

## Exam Tips

1. UNDERSTAND THE ACCESS MATRIX: The access matrix is the fundamental model. Remember it has domains (rows) and objects (columns). Be able to draw or explain it.

2. DIFFERENTIATE ACL AND CAPABILITY LISTS: ACL is object-centric (attached to files), while capability lists are subject-centric (attached to users). Know the advantages and disadvantages of each.

3. UNIX PERMISSION BITS ARE CRUCIAL: You must be able to interpret permission strings like "rwxr-x---" and convert between symbolic and numeric (octal) representations.

4. KNOW THE THREE CATEGORIES: Owner, Group, and Others (or "others" sometimes called "world") are the three categories in UNIX. Don't confuse them.

5. SPECIAL BITS MATTER: Remember setuid, setgid, and sticky bit. Understand when and why each is used.

6. ACCESS RIGHT TYPES: Be familiar with Read, Write, Execute, and other access rights like Append and Delete.

7. PERMISSION EVALUATION ORDER: In systems with ACLs, explicit deny rules take precedence over allow rules. This is a common exam point.

8. PRACTICE NUMERIC CONVERSION: Be able to quickly convert between permission strings and octal numbers. For example, rwxr-xr-x equals 755.