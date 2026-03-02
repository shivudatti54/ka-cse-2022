# **Distributed Systems: Coordination and Agreement (Ch 15.1-15.5) Revision Notes**

## **Introduction**

- A distributed system is a collection of independent computers that appear to be a single coherent system to the user.
- Coordination and agreement are essential for achieving common goals in distributed systems.

## **Distributed Mutual Exclusion (Ch 15.1)**

- A distributed mutual exclusion problem is a problem where one process must have exclusive access to a shared resource.
- Two processes cannot access the resource simultaneously.
- Solutions:
  - Banker's algorithm
  - Dining philosophers problem

## **Consensus Protocol (Ch 15.2)**

- A consensus protocol is used to achieve agreement among processes in a distributed system.
- Examples:
  - Paxos protocol
  - Raft algorithm
- Key properties:
  - Agreement: all processes agree on a single value
  - Validity: the agreed value is valid
  - Termination: the protocol terminates for all processes

## **Byzantine Fault Tolerance (Ch 15.3)**

- Byzantine fault tolerance is a problem where some processes may fail or behave arbitrarily.
- Solutions:
  - Fault-tolerant consensus protocols
  - Quorum systems

## **Causal Consistency (Ch 15.4)**

- Causal consistency is a stronger property than agreement, requiring that events are causally related.
- Solutions:
  - Causal consistency protocols
  - Two-phase commit

## **Formulas and Definitions**

- **Definition:** A distributed system is a collection of independent computers that appear to be a single coherent system to the user.
- **Formula:** (not applicable)

## **Important Theorems**

- **Theorem 1:** If a distributed mutual exclusion protocol is correct, then it is also fair.
- **Theorem 2:** If a consensus protocol is correct, then it is also valid.

Note: This summary is a concise revision guide and is not an exhaustive treatment of the topic.
