# 9.4.2) Deadlocks: System Model, Characterization, and Handling Methods

===========================================================

### Introduction

Deadlocks are a type of failure in a computer system where two or more processes are unable to proceed because each is waiting for the other to release a resource. Deadlocks can occur in operating systems, leading to system crashes or freezes. In this topic, we will discuss the system model of deadlocks, characterization methods, and handling methods.

### System Model of Deadlocks

---

The system model of deadlocks is a theoretical model that describes the behavior of a deadlock. The model consists of five processes and five resources.

### Processes and Resources

- **Processes**: P1, P2, P3, P4, P5
- **Resources**: R1, R2, R3, R4, R5

### Deadlock Scenario

1.  P1 requests R1 and R2.
2.  P2 requests R3 and R4.
3.  P3 requests R5 and R1.
4.  P4 requests R2 and R3.
5.  P5 requests R4 and R5.

### Characterization Methods

---

There are several methods to characterize deadlocks, including:

### 1. Banker's Algorithm

The Banker's Algorithm is a method to detect deadlocks by checking the availability of resources. The algorithm uses a matrix to represent the resource availability and the resource requests of each process.

|     | R1  | R2  | R3  | R4  | R5  |
| --- | --- | --- | --- | --- | --- |
| P1  | 1   | 1   | 0   | 0   | 0   |
| P2  | 0   | 0   | 1   | 1   | 0   |
| P3  | 0   | 0   | 0   | 0   | 1   |
| P4  | 0   | 1   | 1   | 0   | 0   |
| P5  | 1   | 0   | 0   | 1   | 0   |

### 2. Resource Allocation Graph (RAG)

The Resource Allocation Graph (RAG) is a directed graph that represents the resource allocation of each process. The graph is constructed by drawing an edge from a process to a resource if the process requests the resource.

### Handling Deadlocks

---

There are several methods to handle deadlocks, including:

### 1. Abort and Restart

The abort and restart method involves aborting the processes involved in the deadlock and restarting the system.

### 2. Rollback Recovery

The rollback recovery method involves rolling back the transactions of the processes involved in the deadlock.

### 3. Priority Inheritance

The priority inheritance method involves giving priority to the process that is holding the resource and is involved in the deadlock.

### 4. Resource Preemption

The resource preemptive method involves preemting the resource from the process that is holding it and is involved in the deadlock.

### Best Practices

---

To prevent deadlocks, follow these best practices:

- Always acquire resources in a consistent order.
- Avoid holding onto resources for an extended period.
- Monitor the system for deadlocks and take corrective action.

### Conclusion

---

Deadlocks can be a significant issue in operating systems, leading to system crashes or freezes. Understanding the system model of deadlocks, characterization methods, and handling methods is crucial to prevent and handle deadlocks. By following best practices and using the right handling methods, you can ensure that your system remains stable and responsive.
