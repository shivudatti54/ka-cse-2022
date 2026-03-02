# System Model - Summary

## Key Definitions and Concepts

- **System Model**: A conceptual framework defining the structure, components, and interactions within a computer system
- **Uniprocessor System**: A system with a single CPU that executes instructions sequentially
- **Multiprocessor System**: A system with multiple CPUs capable of parallel execution (includes SMP and AMP)
- **Distributed System**: Multiple independent computers communicating over a network
- **Kernel Mode**: Privileged execution mode with full hardware access
- **User Mode**: Restricted mode requiring system calls for hardware access
- **Preemptible Resource**: Resource that can be taken away without causing failure (e.g., CPU time)
- **Non-Preemptible Resource**: Resource that cannot be taken away once allocated (e.g., printer)
- **Safe State**: A system state where there exists a sequence of process execution that allows all processes to complete without deadlock

## Important Formulas and Theorems

- **Safety Algorithm (Banker's Algorithm)**: Work = Available; Finish[i] = false for all i; Find process where Finish[i] = false and Need ≤ Work; If found, Work = Work + Allocation, Finish[i] = true; Repeat until all Finish[i] = true (safe) or no such process exists (unsafe)
- **Need Matrix**: Need[i][j] = Maximum[i][j] - Allocation[i][j]
- **Four Conditions for Deadlock**: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait

## Key Points

- System architecture (uniprocessor, multiprocessor, distributed) determines synchronization complexity
- Kernel mode and user mode separation provides protection and defines privilege boundaries
- Non-preemptible resources are primary contributors to deadlock situations
- Deadlock occurs only when all four conditions are simultaneously satisfied
- A safe state guarantees no deadlock, while an unsafe state may lead to deadlock
- The Banker's Algorithm requires advance knowledge of maximum resource needs
- Circular wait can be prevented by implementing a total ordering of resource types

## Common Mistakes to Avoid

- Confusing preemptible and non-preemptible resources in exam answers
- Forgetting that distributed systems use message passing, not shared memory, for communication
- Assuming deadlock is inevitable in unsafe states (unsafe states only may lead to deadlock)
- Mixing up the roles of Maximum, Allocation, and Need matrices in Banker's Algorithm
- Overlooking that hold-and-wait condition can be eliminated by requiring all resources to be requested simultaneously

## Revision Tips

- Practice drawing and analyzing resource allocation graphs for deadlock scenarios
- Memorize the four deadlock conditions and be able to provide examples of each
- Solve at least five Banker's Algorithm problems to become proficient in safety analysis
- Create comparison charts between uniprocessor, multiprocessor, and distributed systems
- Use the traffic intersection analogy to remember deadlock conditions visually