# Respectively (OMP_SCHEDULE=static)

### Definition

- OMP_SCHEDULE=static: A scheduling policy used in OpenMP that assigns threads to a specific data structure (e.g., a grid or ring) and keeps them there for the entire execution of the program.
- Respectively: A scheduling strategy used in parallel algorithms where tasks are executed in a specific order, determined by a relative timing requirement.

### Key Points

- **OMP_SCHEDULE=static**:
  - Threads assigned to a specific data structure (e.g., grid, ring) for the entire execution.
  - No thread migration between tasks.
  - Useful for tasks with fixed sizes or shapes.
- **Respectively**:
  - Scheduling strategy based on relative timing requirements.
  - Tasks are executed in a specific order determined by their timing requirements.
  - Can improve parallelism by minimizing synchronization costs.

### Important Formulas and Definitions

- **Master-Worker Model**: A classic parallel programming paradigm where a master process creates and controls a set of worker processes.
  - Master: Creates and schedules tasks.
  - Worker: Executes tasks assigned by the master.
- **Critical Section**: A code segment that must be executed by only one thread at a time to avoid data corruption or inconsistency.
  - Example: Accessing shared variables.

### Theorems

- **Amdahl's Law**: A theorem used to estimate the maximum theoretical speedup that can be achieved in a parallel program.
  - S(S - p) ≤ 1, where S is the speedup and p is the proportion of the program executed in parallel.

### Revision Tips

- Focus on understanding the scheduling policies (OMP_SCHEDULE=static and respectfully) and their applications.
- Review the master-worker model and critical sections.
- Practice applying Amdahl's Law to estimate the maximum theoretical speedup.

By covering these key points, you'll be well-prepared for your exam on parallel computing.
