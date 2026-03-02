# Distributed Deadlocks - Summary

## Key Definitions and Concepts

- **Distributed Deadlock**: A deadlock situation in systems where processes compete for resources across multiple machines, with the wait-for graph spanning multiple sites
- **Wait-for Graph (WFG)**: Directed graph where nodes represent processes and edges indicate waiting relationships; a cycle indicates deadlock
- **Communication Deadlock**: Deadlock in message-passing systems where processes wait indefinitely for messages from each other
- **Probe Message**: In CMH algorithm, a message (initiator, sender, destination) used to detect cycles in the distributed wait-for graph

## Important Formulas and Theorems

- **Coffman Conditions**: Four necessary conditions for deadlock - Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait
- **CMH Probe Format**: (i, j, k) where i = initiator, j = sender, k = destination
- **Resource Ordering**: Assign global order to resources; processes must request in increasing order to prevent circular wait

## Key Points

- Distributed deadlocks are harder to detect than centralized deadlocks due to absence of global state and communication delays
- The Chandy-Misra-Haas algorithm is the most famous distributed deadlock detection algorithm using probe messages
- Deadlock prevention ensures one of the four Coffman conditions can never be satisfied (commonly circular wait via resource ordering)
- Deadlock avoidance makes runtime decisions based on current system state (e.g., distributed Banker's algorithm)
- Deadlock detection allows deadlocks but finds them and takes corrective action
- Communication deadlocks are common in MPI-based distributed systems
- False deadlocks may occur due to concurrent state changes and message delays during detection
- Message complexity in distributed detection is O(n²) or higher, making scalability a concern

## Common Mistakes to Avoid

- Confusing deadlock prevention with avoidance - they are fundamentally different approaches
- Assuming distributed deadlock detection can have complete global state - this is impossible by definition
- Forgetting that resource ordering must be global and strictly enforced
- Overlooking communication deadlocks in message-passing systems (only focusing on resource deadlocks)
- Believing that deadlock detection guarantees 100% accuracy (false detections are possible)

## Revision Tips

1. Practice drawing wait-for graphs for simple scenarios to understand deadlock identification
2. Memorize the probe message format in CMH algorithm for exam questions
3. Remember the four Coffman conditions as they form the basis for all deadlock handling strategies
4. Focus on understanding when to apply prevention vs detection vs avoidance
5. Review the differences between centralized and distributed deadlock handling
