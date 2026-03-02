# **Deadlock Detection and Recovery from Deadlock**

## **Definition and Theorem**

- **Deadlock**: A situation where two or more processes are blocked indefinitely, each waiting for the other to release resources.
- **Banker's Theorem**: A deadlock can occur if and only if there is a cycle in the resource allocation graph.

## **Detection Methods**

- **Wife Test**: A process P is said to be a "wife" of process Q if P holds a resource and Q requests the same resource.
- **Wait-for Graph**: A directed graph where edges represent the waiting relationship between processes.

## **Deadlock Detection Algorithms**

- **Ewens Algorithm**: Uses the wait-for graph to detect deadlocks.
- **Liu and Luh Algorithm**: Uses the banker's theorem and the wait-for graph to detect deadlocks.

## **Recovery Methods**

- **Preemptive Scheduling**: Force a process to release its resources and continue execution.
- **Process Termination**: Terminate the processes involved in the deadlock.
- **Resource Preemption**: Preempt the resources held by the processes involved in the deadlock.

## **Formulas and Notations**

- **Resource Allocation Matrix**: A matrix where each row represents a process and each column represents a resource.
- **Banker's Formula**: A set of equations used to determine the availability of resources.
- **Deadlock Detection Formula**: A formula used to detect deadlocks in the wait-for graph.

## **Key Points**

- A deadlock can be detected using the wait-for graph and the banker's theorem.
- Deadlock recovery methods include preemptive scheduling, process termination, and resource preemption.
- The banker's formula and deadlock detection formula are used to analyze resource allocation and detect deadlocks.
