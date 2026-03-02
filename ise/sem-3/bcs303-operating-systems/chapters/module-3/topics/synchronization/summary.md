# Synchronization - Summary

## Key Definitions and Concepts

- **Race Condition:** Undesirable situation where program outcome depends on timing of concurrent events; multiple processes access shared data simultaneously with at least one write operation

- **Critical Section:** Code segment accessing shared resources that must not be executed by more than one process simultaneously

- **Semaphore:** Integer variable with atomic wait() and signal() operations; binary semaphores provide mutual exclusion, counting semaphores manage resource pools

- **Monitor:** High-level synchronization construct encapsulating shared data and procedures with automatic mutual exclusion and condition variables for waiting

- **Deadlock:** Permanent blocking state where processes wait indefinitely for resources held by other waiting processes

- **Safe State:** System state where there exists a sequence of process execution (safe sequence) that allows all processes to complete without deadlock

## Important Formulas and Theorems

- **Semaphore Operations:** wait(sem) decrements value, blocks if negative; signal(sem) increments value, wakes waiting process
- **Banker's Algorithm:** Need = Maximum - Allocation; Request is granted if (Request ≤ Need) AND (Request ≤ Available)
- **Deadlock Conditions:** Mutual Exclusion + Hold and Wait + No Preemption + Circular Wait = Deadlock possible

## Key Points

- Synchronization coordinates concurrent processes to prevent race conditions and maintain data consistency
- Semaphores solve critical section problems with minimal complexity; monitors provide higher-level abstraction
- Producer-Consumer requires tracking buffer state with empty/full semaphores plus mutex for mutual exclusion
- Dining Philosophers solutions must prevent both deadlock and starvation; common approaches include waiter, asymmetry, and limited simultaneous eating
- Banker's Algorithm requires advance knowledge of maximum resource needs; maintains safe state by never granting unsafe requests
- Deadlock prevention eliminates one of four necessary conditions; avoidance uses Banker's Algorithm; detection uses resource allocation graph or wait-for graph
- Starvation differs from deadlock—a waiting process may eventually get resources in starvation but never in deadlock

## Common Mistakes to Avoid

- Forgetting that semaphore wait() operation must check and decrement atomically—non-atomic implementation creates race conditions
- Confusing deadlock prevention with deadlock avoidance—the former removes conditions statically, the latter manages allocation dynamically
- In Banker's Algorithm, incorrectly calculating Need matrix or not checking both Request ≤ Need AND Request ≤ Available
- Not releasing acquired semaphores in all code paths; failing to signal after critical section causes permanent blocking
- Overlooking bounded waiting requirement when designing critical section solutions; solutions may be correct but not satisfy this criterion

## Revision Tips

- Practice writing semaphore implementations for Producer-Consumer and Readers-Writers until you can do so confidently without reference
- Memorize the four deadlock conditions and methods for handling deadlock—examiners frequently test this conceptual understanding
- Work through at least three Banker's Algorithm problems to master the step-by-step procedure for determining safety
- Create comparison tables distinguishing synchronization mechanisms, deadlock handling strategies, and classical problem constraints
- Review previous years' DU question papers to identify frequently tested patterns and expected answer depth