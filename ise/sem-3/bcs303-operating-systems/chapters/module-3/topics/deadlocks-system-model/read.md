# Deadlocks: System Model

=====================================

## Table of Contents

---

1. [Definition and Causes of Deadlocks](#definition-and-causes-of-deadlocks)
2. [System Model for Deadlocks](#system-model-for-deadlocks)
3. [Characteristics of Deadlocks](#characteristics-of-deadlocks)
4. [Detection and Prevention Techniques](#detection-and-prevention-techniques)
5. [Example: Bank Account System](#example-bank-account-system)

## Definition and Causes of Deadlocks

---

A deadlock is a situation when two or more processes are blocked indefinitely, each waiting for the other to release a resource.

### Causes of Deadlocks

- Mutual Exclusion: A process requires a resource that is held by another process.
- Hold and Wait: A process holds a resource and waits for another resource that is held by another process.
- No Preemption: The operating system does not allow the release of resources from one process to another.
- Circular Wait: A process waits for a resource that is held by another process, which in turn waits for a resource held by the first process.

## System Model for Deadlocks

---

The Banker's Algorithm is a classic example of a system model for deadlocks.

### Banker's Algorithm

The Banker's Algorithm is a deadlock detection and prevention algorithm that assigns resources to processes.

- Each process has a maximum number of resources it needs.
- The operating system checks if a process can be assigned a certain number of resources without causing a deadlock.
- If a process is assigned resources, it is said to be "safe".

### Rules for the Banker's Algorithm

1.  A process is safe if it can be assigned a certain number of resources without causing a deadlock.
2.  A process is not safe if it needs resources that are not available or if it needs more resources than it is allowed.
3.  A process is safe if it can be assigned resources without causing a deadlock.

## Characteristics of Deadlocks

---

- **A deadlock is a situation when two or more processes are blocked indefinitely**.
- **A deadlock is a situation when two or more processes are waiting for each other to release a resource**.
- **A deadlock is a situation when a process is waiting for a resource that is held by another process, which in turn is waiting for a resource held by the first process**.

## Detection and Prevention Techniques

---

- **Deadlock Detection:** Identify processes that are blocked and waiting for each other to release resources.
- **Deadlock Prevention:** Prevent processes from holding resources that other processes need.

### Detection Techniques

- **Banker's Algorithm:** Assign resources to processes and check if they are safe.
- **Worst-Case Scenario Analysis:** Analyze the worst-case scenario to detect potential deadlocks.

### Prevention Techniques

- **Resource Ordering:** Order resources to prevent cycles.
- **Resource Allocation:** Assign resources to processes in a way that prevents deadlocks.

## Example: Bank Account System

---

Suppose we have a bank account system with three processes: P1, P2, and P3.

| Process | Required Resources | Available Resources |
| :------ | :----------------- | :------------------ |
| P1      | R1, R2             | R1, R3              |
| P2      | R2, R3             | R2, R1              |
| P3      | R1, R3             | R1, R2              |

In this example, we can see that P1 needs R1 and R2, P2 needs R2 and R3, and P3 needs R1 and R3. If P1 is assigned R1 and R2, and P2 is assigned R2 and R1, a deadlock occurs.

To prevent this deadlock, we can assign resources in a way that prevents cycles. For example, we can assign R1 to P1 and R2 to P2, and then assign R3 to P3.

This way, we can prevent a deadlock from occurring.

In conclusion, a deadlock is a situation when two or more processes are blocked indefinitely, each waiting for the other to release a resource. The Banker's Algorithm is a classic example of a system model for deadlocks. Deadlocks can be detected and prevented using various techniques such as Banker's Algorithm, Worst-Case Scenario Analysis, Resource Ordering, and Resource Allocation.
