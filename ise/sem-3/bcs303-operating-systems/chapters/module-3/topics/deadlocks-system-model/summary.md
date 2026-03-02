# Deadlocks: System Model

### Definitions

- **Deadlock**: A situation where two or more processes are blocked indefinitely, each waiting for the other to release resources.
- **Resource**: A limited commodity that can be acquired by multiple processes.
- **Hold**: A process holding a resource.

### System Model

- **Dining Philosophers Problem**: A classic example of a deadlock scenario, where five philosophers sit around a table with five plates of food, each with a fork on either side.
- **Banker's Problem**: A scheduling algorithm that prevents deadlocks by assigning resources to processes based on availability.

### Key Concepts

- **Resource Allocation Graph (RAG)**: A directed graph representing resource availability and allocation.
- **Resource Matrix (RM)**: A matrix representing the availability and allocation of resources.
- **Banker's Algorithm**:
  - **Safe State**: A state where no process will deadlock.
  - **Safe Sequence**: A sequence of resource allocations that lead to a safe state.
- **Ferrante's Theorem**: A necessary condition for a process to be in a safe state.

### Important Formulas

- **Holding Time**: The minimum time a process can hold a resource.
- **Turnaround Time**: The time a process spends waiting for resources to be released.

### Key Theorems

- **Banker's Theorem**: A process will not deadlock if it can be assigned resources based on availability.
- **Dilworth's Theorem**: A process will deadlock if it cannot be assigned resources based on availability.

### Revision Tips

- Understand the difference between holding and availability of resources.
- Visualize the resource allocation graph and matrix.
- Apply the Banker's Algorithm to determine safe states and sequences.
- Recall Ferrante's Theorem and Banker's Theorem to evaluate deadlock conditions.
