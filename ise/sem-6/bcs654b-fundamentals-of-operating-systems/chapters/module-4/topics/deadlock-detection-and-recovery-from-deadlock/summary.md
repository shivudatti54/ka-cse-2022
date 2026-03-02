# **Deadlock Detection and Recovery from Deadlock**

## **Definitions and Notations**

- **Deadlock**: A situation where two or more processes are unable to proceed because each is waiting for the other to release a resource.
- **Resource**: A limited quantity of a system component, such as memory, I/O device, or CPU time.
- **Banker's algorithm**: A method for managing resources in a multi-user environment.

## **Characterization of Deadlocks**

- **Livelock**: A situation where two or more processes are unable to proceed because each is waiting for the other to release a resource, but the processes are not actually holding each other's resources.
- **Racing condition**: A situation where two or more processes are competing for a resource, but the processes are not actually deadlocked.

## **Deadlock Detection Methods**

- **Waiting-for graph**: A directed graph used to model the relationships between processes and resources.
- **Banker's algorithm**: A method for detecting deadlocks by analyzing the availability of resources.
- **Resource allocation graph**: A graph used to model the allocation and deallocation of resources.

## **Formulas and Theorems**

- **Banker's algorithm formula**: `A[i] \geq r[i] \forall i \in [1, n]`
- **Deadlock detection theorem**: A process is deadlocked if and only if it is unable to acquire all the resources it needs.

## **Deadlock Recovery Methods**

- **Process termination**: Terminating a process that is deadlocked.
- **Resource preemption**: Preempting the resources held by a process that is deadlocked.
- **Resource allocation**: Allocating a resource to a process that is waiting for it.

## **Revision Tips**

- Understand the definitions and notations used in deadlock detection and recovery.
- Be familiar with the characterization of deadlocks, including livelock and racing conditions.
- Know the deadlock detection methods, including the waiting-for graph, banker's algorithm, and resource allocation graph.
- Understand the formulas and theorems used in deadlock detection, including the banker's algorithm formula and deadlock detection theorem.
- Be aware of the deadlock recovery methods, including process termination, resource preemption, and resource allocation.
