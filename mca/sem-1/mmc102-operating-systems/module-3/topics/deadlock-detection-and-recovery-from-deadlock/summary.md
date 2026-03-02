# Deadlock Detection And Recovery From Deadlock - Summary

## Key Definitions and Concepts

- **Resource Allocation Graph (RAG)**: A bipartite directed graph with process vertices and resource vertices used to model resource allocation state. Request edges go from process to resource; assignment edges go from resource to process.

- **Wait-For Graph**: Derived from RAG by removing resource nodes and directly connecting processes based on waiting relationships. A cycle in this graph indicates deadlock.

- **Deadlock Detection Algorithm**: An algorithm that periodically examines system state by finding processes whose requests can be satisfied with available resources, simulating resource allocation until no more processes can complete.

- **Process Termination**: Recovery strategy that aborts one or more deadlocked processes to break the deadlock cycle and free their resources.

- **Resource Preemption**: Recovery strategy that forcibly takes resources from deadlocked processes and allocates them to break the deadlock.

## Important Formulas and Theorems

- **Single-instance deadlock theorem**: A deadlock exists in a system with single-instance resources if and only if the RAG contains a cycle.

- **Multiple-instance detection**: For multiple-instance resources, use the detection algorithm; cycle in RAG is necessary but not sufficient.

- **Detection algorithm complexity**: O(m × n²) where m is number of resource types and n is number of processes.

## Key Points

- Deadlock detection allows deadlocks to occur but periodically checks for them, suitable when prevention overhead is too high.

- RAG provides visual representation of allocation state; cycle detection is simpler for single-instance resources.

- Wait-For Graph eliminates resource nodes, showing only process-to-process dependencies.

- The detection algorithm marks processes that can complete; unmarked processes are deadlocked.

- Recovery through process termination is simplest but loses all work done by terminated process.

- Resource preemption requires careful victim selection and handling of rollback requirements.

- Checkpointing enables rollback to safe states but requires significant storage and computational overhead.

- Detection frequency involves trade-off between overhead and deadlock duration in the system.

## Common Mistakes to Avoid

- Confusing request edges and assignment edges direction in RAG diagrams.

- Assuming RAG cycle always indicates deadlock for multiple-instance resources (it is necessary but not sufficient).

- Forgetting to update the work vector with allocated resources when simulating process completion in detection algorithm.

- Confusing deadlock detection (finding existing deadlocks) with avoidance (preventing deadlocks before they occur).

## Revision Tips

- Practice drawing RAGs and Wait-For Graphs from given allocation and request matrices.

- Memorize the step-by-step detection algorithm and practice with at least 3-4 different examples.

- Remember that detection is applied when the system allows unsafe states; avoidance ensures safety at all times.

- Review the three recovery strategies and their suitable scenarios before the exam.