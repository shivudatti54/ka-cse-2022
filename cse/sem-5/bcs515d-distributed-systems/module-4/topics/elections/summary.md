# Election Algorithms in Distributed Systems - Summary

## Key Definitions and Concepts

- **Election Algorithm:** A protocol that selects a coordinator or leader from a group of processes in a distributed system
- **Coordinator:** The designated process responsible for coordinating resource allocation, synchronization, and maintaining consistency
- **Bully Algorithm:** Election algorithm where the process with the highest ID becomes coordinator; uses direct messages to all higher-priority processes
- **Ring Algorithm:** Election algorithm using a logical ring structure where election messages circulate sequentially

## Important Formulas and Theorems

- **Bully Algorithm Message Complexity:** O(n²) in worst case, O(n) in best case
- **Ring Algorithm Message Complexity:** O(n) in all cases
- **Correctness Requirements:** Safety (at most one coordinator) and Liveness (eventual election if system stabilizes)

## Key Points

- Election algorithms are essential for fault tolerance in distributed systems when the coordinator fails
- The Bully Algorithm is simple but message-intensive, with the highest-ID process winning
- The Ring Algorithm organizes processes logically in a ring and passes election messages sequentially
- Both algorithms assume crash failures, reliable channels, and unique process IDs
- Safety ensures no split-brain scenarios; liveness ensures eventual coordinator election
- Real-world applications include distributed databases, cloud coordination services, and consensus protocols
- Bully Algorithm may cause disruption as higher-ID processes can dominate elections
- Ring Algorithm requires less message traffic but may be slower due to sequential propagation

## Common Mistakes to Avoid

- Confusing the direction of message passing in Ring Algorithm (messages pass through successor only)
- Thinking Bully Algorithm always requires O(n²) messages (best case is O(n))
- Assuming Byzantine failures (malicious behavior) - election algorithms typically handle crash failures only
- Forgetting that processes must have unique identifiers for election algorithms to work

## Revision Tips

- Draw the message flow diagrams for both algorithms to visualize the election process
- Memorize the message complexity formulas as they frequently appear in exams
- Practice working through examples with specific process IDs to understand the flow
- Remember the trade-offs: Bully is fast but expensive; Ring is slower but efficient
- Focus on understanding when and why elections are needed in distributed systems
