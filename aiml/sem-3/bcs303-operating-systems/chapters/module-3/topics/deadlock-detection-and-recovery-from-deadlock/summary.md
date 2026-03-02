# **Deadlock Detection and Recovery from Deadlock**

## **Definitions and Key Concepts**

- **Deadlock**: A situation where all processes are waiting for each other to release resources, resulting in no process making progress.
- **Resource Allocation Graph (RAG)**: A directed graph that represents the allocation of resources among processes.
- **Banker's Algorithm**: A dynamic priority scheduling algorithm that prevents deadlocks by allocating resources dynamically.

## **Detection Methods**

- **Dining Philosophers Problem**: A classic deadlock scenario where philosophers sit at a table with chopsticks representing resources.
- **Resource Locks**: A process is considered deadlocked if it holds all the resources it needs.
- **Waiting for Resource**: A process is deadlocked if it is waiting for a resource held by another process.

## **Recovery Methods**

- **Abort Process**: Terminate a process that is deadlocked.
- **Rollback Recovery**: Revert the process to a previous state where it was not deadlocked.
- **Resource Preemption**: Take away resources from a process that is deadlocked.
- **Prioritize Processes**: Prioritize processes based on their priority.

## **Important Formulas and Theorems**

- **Banker's Algorithm Formula**: `i <= max[j] * aij`
- **Deadlock Theorem**: A deadlock occurs if and only if there is a cycle in the RAG.

## **Key Points**

- Deadlock detection involves analyzing the RAG to identify cycles and waiting-for relationships.
- Deadlock recovery involves aborting or rolling back processes to prevent further progression.
- Banker's Algorithm is a dynamic priority scheduling algorithm that prevents deadlocks by allocating resources dynamically.
- Deadlocks can be avoided by prioritizing processes and using resource locks to prevent cycles in the RAG.
