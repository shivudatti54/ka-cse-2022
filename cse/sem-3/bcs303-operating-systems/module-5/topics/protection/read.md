# Protection in Operating Systems

## Introduction

Protection refers to a mechanism for controlling the access of programs, processes, or users to the resources defined by a computer system. Protection is an internal problem -- how do we provide controlled access to programs and data stored in a computer system? This is distinct from security, which deals with external threats.

In a multiprogramming environment, multiple users share the system. Protection ensures that each shared resource (CPU, memory, files, devices) is used only in accordance with the policies established by the system designer and administrator.

---

## Goals of Protection

The primary goals of a protection system are:

1. **Prevent unauthorized access** to shared resources
2. **Ensure that each component** of the system uses resources only in ways consistent with stated policies
3. **Detect and prevent misuse** -- both intentional and accidental violations
4. **Improve reliability** by catching interface errors between components early
5. **Distinguish between authorized and unauthorized usage** through policy enforcement

Protection policies define "who can access what and how." Protection mechanisms provide the tools to enforce those policies.

> **Key Distinction:** Protection mechanisms determine **how** to enforce policies. The policies themselves determine **what** is to be enforced. This separation is important for flexibility.

---

## Principle of Least Privilege

The **Principle of Least Privilege** states that programs, users, and systems should be given just enough privileges to perform their tasks -- no more.

- A user who only needs to read a file should not be given write access
- A process that only needs access to one directory should not have access to the entire file system
- System daemons should run with the minimum set of privileges they need

**Benefits:**

- Limits damage from bugs or malicious code
- Reduces the attack surface
- Makes auditing easier
- Contains failures to a smaller scope

**Example:** In Unix/Linux, a web server runs as a non-root user (e.g., `www-data`) so that even if it is compromised, the attacker has limited access.

---

## Domain of Protection

### What is a Protection Domain?

A **domain** defines a set of objects and the types of operations that may be invoked on each object. In other words:

```
Domain = { (object, rights-set) }
```

Where:

- **Object** = any named resource (file, printer, CPU, memory segment)
- **Rights-set** = subset of all valid operations on that object (read, write, execute, etc.)

### Process-Domain Association

A process executes within a protection domain at any given time. The domain specifies the resources the process may access. There are three models:

1. **Static association:** Each process is bound to one fixed domain for its entire lifetime
2. **Dynamic association:** A process can switch between domains during execution (more flexible but requires a domain-switching mechanism)
3. **Domain as a user:** Each user is a domain. When a process runs on behalf of a user, it operates in that user's domain

**Examples of domains in real systems:**

- **Unix:** Each user ID defines a domain. The `setuid` bit allows temporary domain switching
- **Windows:** Access tokens define the domain of each process

---

## Access Matrix Model

The **Access Matrix** is a general model for protection. It provides a framework that the OS can use to define and enforce protection policies.

```
 OBJECTS
 ┌──────────┬──────────┬──────────┬──────────┐
 │ File F1 │ File F2 │ Printer │ Domain │
 │ │ │ │ Switch │
 ┌────────────┼──────────┼──────────┼──────────┼──────────┤
 │ Domain D1 │ read │ read │ │ switch │
 │ │ write │ │ │ to D2 │
 ├────────────┼──────────┼──────────┼──────────┼──────────┤
D│ Domain D2 │ read │ │ print │ switch │
O│ │ │ │ │ to D3 │
M├────────────┼──────────┼──────────┼──────────┼──────────┤
A│ Domain D3 │ │ read │ │ │
I│ │ │ write │ │ │
N├────────────┼──────────┼──────────┼──────────┼──────────┤
S│ Domain D4 │ read │ │ print │ switch │
 │ │ write │ │ │ to D1 │
 └────────────┴──────────┴──────────┴──────────┴──────────┘
```

**Structure:**

- **Rows** = protection domains (users/processes)
- **Columns** = objects (files, devices, memory segments, domains)
- **Entry Access(Di, Oj)** = set of operations that a process executing in domain Di can invoke on object Oj

If `Access(D1, F1) = {read, write}`, then a process in domain D1 can read and write file F1.

### Operations on the Access Matrix

The access matrix itself can be modified using special rights:

- **Copy right (\*):** A domain can copy an access right to another domain for the same object
- **Owner right:** A domain can add or remove any right in the column for that object
- **Control right:** A domain can modify rights in another domain's row
- **Transfer right:** A domain can transfer its rights to another domain

---

## Implementation of the Access Matrix

The full access matrix is typically large and sparse (most entries are empty). Storing it directly is wasteful. Four practical implementation approaches exist:

### 1. Global Table

Store the access matrix as a single table of ordered triples: `(domain, object, rights-set)`.

```
Global Table:
┌──────────┬──────────┬──────────────┐
│ Domain │ Object │ Rights │
├──────────┼──────────┼──────────────┤
│ D1 │ F1 │ read, write │
│ D1 │ F2 │ read │
│ D2 │ F1 │ read │
│ D2 │ Printer │ print │
│ D3 │ F2 │ read, write │
│ D4 │ F1 │ read, write │
│ D4 │ Printer │ print │
└──────────┴──────────┴──────────────┘
```

**Advantages:**

- Simple to implement

**Disadvantages:**

- Table is very large (domains x objects) even if most entries are empty
- Cannot be kept in main memory -- needs disk access (slow)
- Difficult to take advantage of groupings of objects or domains

### 2. Access Lists for Objects (ACL)

Each **object** stores a list of `(domain, rights-set)` pairs -- only non-empty entries.

```
File F1: ACL = [ (D1, {read,write}), (D2, {read}), (D4, {read,write}) ]
File F2: ACL = [ (D1, {read}), (D3, {read,write}) ]
Printer: ACL = [ (D2, {print}), (D4, {print}) ]
```

**Advantages:**

- Corresponds to columns of the access matrix
- Easy to determine who has access to a given object
- Easy to revoke access (modify the object's list)

**Disadvantages:**

- Difficult to determine all the rights of a particular domain (must check every object)
- Access checking may be slow if the list is long

**Real-world example:** Unix file permissions (owner, group, others) are a simplified ACL.

### 3. Capability Lists for Domains

Each **domain** stores a list of `(object, rights-set)` pairs -- the capabilities it holds.

```
Domain D1: Capabilities = [ (F1, {read,write}), (F2, {read}) ]
Domain D2: Capabilities = [ (F1, {read}), (Printer, {print}) ]
Domain D3: Capabilities = [ (F2, {read,write}) ]
Domain D4: Capabilities = [ (F1, {read,write}), (Printer, {print}) ]
```

A capability is like a "ticket" or "key" -- possession of a capability grants the holder the right to perform the specified operations on the object.

**Advantages:**

- Corresponds to rows of the access matrix
- Easy to determine all the access rights of a given domain
- Capabilities can be passed between processes (delegation)

**Disadvantages:**

- Difficult to determine all domains that have access to a given object (must check every domain)
- Revocation is difficult -- must track all distributed capabilities

### 4. Lock-Key Mechanism

A compromise between ACLs and capability lists:

- Each **object** has a list of unique bit patterns called **locks**
- Each **domain** has a list of unique bit patterns called **keys**
- A process in a domain can access an object only if the domain holds a key that **matches** one of the object's locks

```
Object F1: Locks = [ K1, K3 ]
Object F2: Locks = [ K2 ]
Domain D1: Keys = [ K1, K2 ] --> Can access F1 (has K1) and F2 (has K2)
Domain D2: Keys = [ K3 ] --> Can access F1 (has K3) only
Domain D3: Keys = [ K4 ] --> Cannot access F1 or F2
```

**Advantages:**

- Flexible -- easy to add/remove access by adding/removing keys or locks
- Compromise between ACL and capability approaches

**Disadvantages:**

- Requires careful management of keys and locks
- More complex to implement

---

## Comparison: Access List vs Capability List

| Feature                | Access List (ACL)           | Capability List                  |
| :--------------------- | :-------------------------- | :------------------------------- |
| **Stored with**        | Object (column of matrix)   | Domain (row of matrix)           |
| **Easy to determine**  | Who can access an object    | What a domain can access         |
| **Revocation**         | Easy (modify object's list) | Difficult (must find all copies) |
| **Access check**       | Check object's list         | Present capability as proof      |
| **Delegation**         | Difficult                   | Easy (pass capability)           |
| **Real-world example** | Unix file permissions       | Mach OS capabilities             |
| **Overhead**           | Per-object overhead         | Per-domain overhead              |

> **Most real systems use a combination:** ACLs are used when a file is first opened (to verify access), and a capability (file descriptor) is returned for subsequent operations.

---

## Revocation of Access Rights

Revocation is the removal of access rights from a domain. Key questions:

1. **Immediate vs. delayed:** Should revocation take effect immediately or at a later time?
2. **Selective vs. general:** Should it affect all users who have the right, or only a specific user?
3. **Partial vs. total:** Should a subset of rights be revoked, or all rights for an object?
4. **Temporary vs. permanent:** Should the right be revoked permanently, or can it be restored later?

### Revocation with Different Implementations

| Method         | Revocation Difficulty                                              |
| :------------- | :----------------------------------------------------------------- |
| **ACL**        | Easy -- just remove the entry from the object's access list        |
| **Capability** | Hard -- capabilities may have been copied and distributed widely   |
| **Lock-Key**   | Moderate -- change the lock on the object; old keys become invalid |

### Capability Revocation Techniques

Since capabilities are distributed, revoking them requires special techniques:

- **Reacquisition:** Periodically delete capabilities; processes must re-request them
- **Back-pointers:** Each object maintains pointers to all capabilities issued for it
- **Indirection:** Capabilities point to an indirect table entry rather than the object directly; revoke by clearing the table entry
- **Keys:** Associate a master key with each capability; revocation involves changing the master key

---

## Role-Based Access Control (RBAC)

Modern systems often use **RBAC** as a higher-level protection mechanism:

- Users are assigned to **roles** (e.g., student, faculty, admin)
- Roles are assigned **permissions** (access rights to objects)
- A user can activate one or more roles, gaining the combined permissions

```
Users ──→ Roles ──→ Permissions ──→ Objects

Example:
 User "Alice" ──→ Role "Faculty" ──→ {read, write} on "grades.db"
 User "Bob" ──→ Role "Student" ──→ {read} on "grades.db"
```

RBAC simplifies administration: instead of assigning permissions to each user individually, the admin assigns roles, and permissions follow.

---

## Key Points Summary

| Concept         | Key Idea                                            |
| :-------------- | :-------------------------------------------------- |
| Protection      | Controlling access to system resources              |
| Least Privilege | Grant only minimum necessary access                 |
| Domain          | Set of (object, rights) pairs                       |
| Access Matrix   | Rows = domains, Columns = objects, Entries = rights |
| Global Table    | Simple but large and wasteful                       |
| ACL             | Stored per-object; easy revocation                  |
| Capability List | Stored per-domain; easy delegation                  |
| Lock-Key        | Compromise; keys must match locks                   |
| Revocation      | Easy with ACL, difficult with capabilities          |
| RBAC            | Assign users to roles, roles to permissions         |

---

## Exam Tips

1. **Access Matrix diagram** is a very common exam question. Practice drawing it with domains as rows, objects as columns, and access rights in cells.
2. Know the **four implementations** of the access matrix (Global Table, ACL, Capability List, Lock-Key) and their trade-offs. Compare them.
3. **Principle of Least Privilege** is frequently asked as a short-answer question. Define it with an example.
4. **ACL vs Capability List comparison** is a classic 5-mark or 10-mark question. Use a comparison table.
5. **Revocation** is often combined with capability lists in exam questions -- know why revocation is hard with capabilities.
6. Remember that **protection != security**. Protection is internal (controlling access among users/processes). Security deals with external threats.
7. For numerical questions, you may be asked to construct an access matrix given a scenario with users, files, and permissions.
