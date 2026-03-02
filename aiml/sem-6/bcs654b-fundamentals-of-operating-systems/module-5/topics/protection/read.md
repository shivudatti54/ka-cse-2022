# Protection in Operating Systems


## Table of Contents

- [Protection in Operating Systems](#protection-in-operating-systems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Domain of Protection](#domain-of-protection)
  - [Access Matrix Model](#access-matrix-model)
  - [Access Control Lists (ACLs)](#access-control-lists-acls)
  - [Capability Lists (Capabilities)](#capability-lists-capabilities)
  - [Protection Rings](#protection-rings)
  - [Authentication and Authorization](#authentication-and-authorization)
- [Examples](#examples)
  - [Example 1: Unix File Permissions](#example-1-unix-file-permissions)
  - [Example 2: Access Matrix Implementation](#example-2-access-matrix-implementation)
  - [Example 3: Setuid Mechanism](#example-3-setuid-mechanism)
- [Exam Tips](#exam-tips)

## Introduction

Protection in operating systems refers to the mechanisms and policies that control access to system resources, ensuring that processes operate within their authorized boundaries and preventing unauthorized access to sensitive data and system components. As operating systems evolved from single-user single-tasking systems to complex multi-user multi-tasking environments, the need for robust protection mechanisms became paramount. Without adequate protection, a malfunctioning or malicious process could corrupt data, crash the system, or access confidential information belonging to other users.

The fundamental goal of protection is to enforce the principle of least privilege, which states that every program and every user should operate using the minimum privileges necessary to complete their tasks. This principle, articulated by Saltzer and Schroeder in their seminal work on protection, forms the philosophical foundation upon which modern protection mechanisms are built. Protection mechanisms must balance security requirements with system usability, ensuring that legitimate operations are not unnecessarily hindered while preventing harmful ones.

This topic explores the theoretical foundations of protection, the various models and mechanisms employed by operating systems, and the practical implementation considerations that system designers must address. Understanding protection is essential for system administrators, security professionals, and software developers who need to build secure computing environments.

## Key Concepts

### Domain of Protection

A domain defines a set of objects and the operations that may be performed on those objects. In traditional Unix systems, each user is assigned a unique user identifier (UID), and processes execute in a domain determined by their effective UID. More sophisticated systems support multiple domains per user, allowing different protection contexts for different tasks. Domains can be hierarchical, where one domain may have all the privileges of another plus additional ones, or flat, where domains are independent of each other.

The relationship between domains and processes is dynamic. A process may transition between domains during execution, such as when a user process invokes a privileged system call or when a setuid program changes its effective user ID. This transition must be carefully controlled to prevent privilege escalation attacks where an attacker gains higher privileges than originally granted.

### Access Matrix Model

The access matrix provides a formal, abstract representation of protection state in a system. It is a two-dimensional matrix with domains as rows and objects as columns, where each cell contains the set of operations that the domain may perform on the object. This model, independently proposed by several researchers in the 1970s, offers a complete description of the system's protection state and serves as a specification language for protection policies.

The access matrix approach offers several advantages. It provides a uniform framework for representing diverse protection policies, allows centralized specification of access rights, and enables formal reasoning about system security properties. However, storing the entire matrix explicitly is impractical for large systems with many domains and objects, as most entries would be empty. Implementation typically uses more space-efficient representations such as access control lists (ACLs) or capability lists.

### Access Control Lists (ACLs)

An access control list associates with each object a list of domains and their permitted operations on that object. When a process attempts to access an object, the system checks the object's ACL to determine whether the process's domain has the required permission. Unix file permissions represent a simplified form of ACL, specifying read, write, and execute permissions for the owner, group, and others.

ACLs provide fine-grained control over object access and clearly show who can access each object and how. They are particularly useful for implementing complex policies where different users require different access levels to the same resource. However, ACLs can become unwieldy for objects with many authorized users, and determining all access rights for a particular user requires scanning multiple ACLs throughout the system.

### Capability Lists (Capabilities)

A capability is an unforgeable token that grants the holder specific access rights to an object. A capability list represents the set of capabilities held by a domain, effectively enumerating the objects it may access and the permitted operations on each. Unlike ACLs where access verification requires consulting the object's metadata, capabilities enable efficient access checks by embedding authorization directly in the reference to the object.

Capability-based systems offer several theoretical advantages, including the ability to easily transfer access rights between domains and efficient local access decisions. However, capabilities present challenges for revocation, where removing a user's access to an object requires locating and invalidating all existing capabilities. The Capsicum project has explored integrating capabilities into Unix-like systems while maintaining backward compatibility.

### Protection Rings

Many processor architectures support hierarchical protection domains called rings, where lower-numbered rings have more privileges than higher-numbered ones. The x86 architecture, for example, provides four privilege levels (rings 0-3), with ring 0 reserved for the most privileged operating system kernel and ring 3 for user applications. Intermediate rings may be used for system services or virtualization software.

The ring model enables a clear separation between trusted and untrusted code, with the kernel operating in the most privileged ring and user applications in the least privileged. Transitions between rings occur through carefully controlled gate mechanisms, and the hardware enforces memory protection between rings. This architecture forms the foundation of system security by ensuring that user code cannot directly access hardware resources or memory belonging to the kernel or other processes.

### Authentication and Authorization

Authentication verifies the identity of a user or process before granting access to protected resources. Common authentication mechanisms include passwords, cryptographic keys, biometrics, and hardware tokens. The operating system typically maintains authentication databases, such as the /etc/passwd and /etc/shadow files in Unix systems, which store credential information used during the authentication process.

Authorization determines what operations an authenticated user may perform on system resources. Given an authenticated identity, the system consults its protection policy to decide whether to grant access. This decision may depend on the user's identity, group memberships, object ownership, time of day, or other contextual factors. Well-designed systems separate authentication from authorization, allowing different policies to be applied without modifying authentication mechanisms.

## Examples

### Example 1: Unix File Permissions

Consider a file with permissions `rwxr-x---` owned by user `alice` in group `staff`. This notation represents an ACL where:
- Owner (alice): read, write, execute
- Group (staff): read, execute
- Others: no permissions

When user `bob` (not in group `staff`) attempts to read this file, the kernel checks the third category ("others") and finds no read permission, so the operation fails with a "Permission denied" error. When alice's process attempts the same operation, the kernel matches the first category (owner) and finds read permission granted. This simple ACL implementation demonstrates how protection policies translate into access decisions.

### Example 2: Access Matrix Implementation

Suppose a system has three domains (D1, D2, D3) and four objects (O1, O2, O3, O4). The access matrix might specify:
- D1: read, write O1; read O2
- D2: read, write, execute O1; read, write O2; execute O3
- D3: read O1; write O2; read, write, delete O4

Implementing this as ACLs would associate with each object its own permission list. For O1: D1 {read, write}, D2 {read, write, execute}, D3 {read}. Implementing as capabilities, each domain would carry tokens specifying its rights. Domain D1's capabilities would include references to O1 with read/write rights and O2 with read rights.

### Example 3: Setuid Mechanism

The Unix setuid mechanism demonstrates domain transitions. When a user runs a program with the setuid bit set (such as the `passwd` command), the process gains effective root privileges (UID 0) while the real user ID remains unchanged. This allows the program to access protected files like /etc/passwd or /etc/shadow to modify password data.

The kernel enforces this transition by setting the process's effective UID to the file's owner during execution. When the process completes or calls setuid to revert to the original UID, protection is restored. A vulnerability in a setuid program can therefore provide root access to unprivileged users, making careful programming essential for such programs.

## Exam Tips

1. **Understand the Access Matrix**: The access matrix is a fundamental conceptual model for protection. Know how to represent protection policies as an access matrix and understand the difference between rows (domains) and columns (objects).

2. **Distinguish ACLs from Capabilities**: Remember that ACLs associate permissions with objects (checking at the object's side), while capabilities associate objects with permissions (checking at the holder's side). Each has trade-offs in revocation, efficiency, and scalability.

3. **Principle of Least Privilege**: This is frequently tested. Always apply this principle when analyzing protection scenarios: users and processes should have only the minimum permissions necessary.

4. **Protection vs. Security**: Protection refers to internal system mechanisms enforcing access control, while security encompasses broader concerns including external threats, physical security, and policy enforcement. Know this distinction.

5. **Kernel vs. User Mode**: The distinction between kernel mode (ring 0) and user mode (ring 3) is fundamental to operating system protection. Know how the hardware supports this separation and what happens during system calls.

6. **File Permission Interpretation**: Be able to interpret Unix-style permissions (rwx, setuid, sticky bit) and explain how the kernel evaluates access requests based on ownership and permission bits.

7. **Capability Revocation Problem**: Understand why revoking capabilities is challenging compared to ACLs, and know some proposed solutions like indirection or version numbers.

8. **Trust Boundaries**: When analyzing system designs, identify trust boundaries where protection checks occur. Understanding what code operates in trusted domains versus untrusted domains is essential for security analysis.