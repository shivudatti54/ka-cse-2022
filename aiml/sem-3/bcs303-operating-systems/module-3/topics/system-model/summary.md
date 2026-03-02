# System Model in Operating Systems - Summary

## Key Definitions

- **System Model**: A conceptual framework defining the structure, components, and interactions within a computing system for analysis purposes.

- **Process**: An executing program treated as an independent entity with its own program counter, registers, stack, and address space.

- **Resource**: Any system component (CPU, memory, I/O devices, locks) that a process requires to complete execution.

- **Preemptible Resource**: Resources that can be taken away from a process without causing harm (e.g., CPU time, memory).

- **Non-Preemptible Resource**: Resources that cannot be forcibly taken away once allocated (e.g., printers, file locks).

- **Resource Allocation Graph (RAG)**: A directed graph showing the current allocation and request state of resources to processes.

## Important Formulas

There are no specific formulas for this topic, but key relationships include:

- **Available Resources** = Total Resources - Allocated Resources
- **Request Edge**: Pᵢ → Rⱼ (process waiting)
- **Assignment Edge**: Rⱼ → Pᵢ (resource allocated)

## Key Points

1. A **uniprocessor system** has one CPU; processes share it through context switching. A **multiprocessor system** has multiple CPUs enabling true parallel execution.

2. The **four Coffman conditions** (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) are **necessary** for deadlock—all must be present.

3. **Hold and Wait** means processes keep allocated resources while waiting for additional ones—this is a key deadlock-causing behavior.

4. **Circular Wait** exists when processes form a waiting chain: P₁→R₁→P₂→R₂→...→Pₙ→Rₙ→P₁.

5. In a **Resource Allocation Graph**, a cycle indicates **potential** deadlock; with single-instance resources, a cycle **confirms** deadlock.

6. With **multiple instances** of resources, a cycle is necessary but not sufficient for deadlock—sufficient available resources may break the cycle.

7. Deadlock is primarily a problem of **non-preemptible resources**; preemptible resources can be reclaimed without causing issues.

8. The system model provides **abstraction** that enables formal analysis of synchronization and deadlock problems.

## Common Mistakes

1. **Confusing preemptible and non-preemptible resources**: Remember that CPU time is preemptible (via scheduler), but a printer once allocated is not.

2. **Assuming every cycle means deadlock**: With multiple resource instances, a cycle may not lead to deadlock if resources can be granted to break the wait chain.

3. **Forgetting all four conditions must hold**: Missing any one of the Coffman conditions means deadlock cannot occur.

4. **Ignoring the number of instances**: The same scenario can be deadlock-free or deadlocked depending on whether resources have single or multiple instances.

5. **Confusing request and assignment edges**: Request edge goes from process to resource (arrow points to resource); assignment edge goes from resource to process (arrow points to process).