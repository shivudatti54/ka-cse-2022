# Global States in Distributed Systems

## Introduction

In distributed systems, understanding the global state of the system at any instant is fundamental to solving many practical problems such as deadlock detection, termination detection, checkpointing, and debugging. However, unlike centralized systems where a single global clock provides a consistent view of the system state, distributed systems present unique challenges due to the absence of global time and the inherent communication delays between processes.

The concept of global state encompasses the collective states of all processes and communication channels in a distributed system at a particular moment. Since processes operate asynchronously and communicate through message passing, capturing a consistent global snapshot becomes a non-trivial task. A naive approach of collecting local states from all processes simultaneously is impossible because there is no global clock to synchronize these observations.

The study of global states involves understanding how to capture consistent snapshots of distributed computations, how to reason about the ordering of events across processes, and how these concepts apply to practical distributed algorithms. This topic builds directly upon the foundation of logical time and happened-before relations introduced in earlier modules.

## Key Concepts

### Local State and Channel State

Each process in a distributed system maintains a **local state**, which consists of the values of all local variables and program counters at that process. The local state of a process changes only when an event occurs at that process—whether an internal event, a send event, or a receive event.

**Channel state** refers to the collection of messages that have been sent but not yet received. When a process sends a message, it enters the channel; when the message is received, it leaves the channel. The channel state is dynamic and changes as messages traverse the communication medium.

### Consistent Global State

A global state is a collection of local states of all processes together with the states of all channels. However, not all such collections represent valid states of the distributed system. A **consistent global state** (or **consistent cut**) satisfies the condition that if an event e is included in the state of process P, then all events that causally precede e must also be included in the states of some processes in the global state.

Formally, a global state G is consistent if for every receive event r in G, the corresponding send event s is also in G. This ensures that no message appears to be received before it is sent—a violation that would make the state physically impossible.

### Happened-Before Relation and Consistent Cuts

The **happened-before relation** (denoted →) defines a partial order among events in a distributed system. If event a happens-before event b (a → b), then b cannot occur before a in any consistent global state. A **cut** of a distributed computation is a set of events that is closed under the happened-before relation—if an event belongs to the cut, then all events that happened-before it must also belong to the cut.

The **frontier of a cut** consists of the events at each process that are included in the cut. A consistent cut has a frontier that passes through channels at appropriate points, ensuring that every message received is also sent within the cut.

### Chandy-Lamport Snapshot Algorithm

The Chandy-Lamport algorithm is a classic approach for recording a consistent global state of a distributed system without stopping the computation. The algorithm assumes FIFO delivery of messages and that channels are bidirectional.

The algorithm works as follows:
1. Any process can initiate the snapshot by recording its own local state
2. The initiating process sends marker messages on all outgoing channels
3. When a process receives a marker for the first time, it records its local state (if not already done) and forwards markers on all other outgoing channels
4. Messages received after the marker but before recording local state are recorded as channel state
5. The algorithm terminates when all processes have recorded their local states and all channels have been traversed by markers

### Lattice of Global States

The set of all consistent global states forms a lattice (a partially ordered set where every pair has a unique least upper bound and greatest lower bound). The initial state (no events processed) is at the bottom, and the final state (all events processed) is at the top. Each edge in the lattice represents the occurrence of an event at some process, causing a transition from one consistent state to another.

This lattice structure is useful for reasoning about properties like termination and for visualizing the space of possible global states the system can pass through during execution.

## Examples

### Example 1: Consistent vs Inconsistent State

Consider a system with two processes P and Q communicating via channel C. Suppose at some point:
- P has sent messages m1 and m2
- Q has received m1 but not m2
- m2 is in transit from P to Q

A **consistent state** would include P's state after sending both messages, Q's state after receiving m1, and channel C containing message m2. An **inconsistent state** would be one where Q's state shows receipt of m1, but the channel state does not include m2—this would imply m2 was received without being sent.

### Example 2: Chandy-Lamport Snapshot

Consider three processes P, Q, and R in a ring configuration. When P initiates a snapshot:
1. P records its local state S₁
2. P sends marker to Q
3. Q receives marker, records its local state S₂, sends marker to R
4. R receives marker, records its local state S₃, sends marker back to P
5. Meanwhile, regular messages continue flowing; messages arriving at processes after their local state is recorded form the channel state

The collected states {S₁, S₂, S₃} along with the channel states captured during marker propagation form a consistent global snapshot.

### Example 3: Termination Detection

Consider a distributed algorithm where processes iteratively refine their local state and send updates to neighbors. To detect termination, we need to verify that all processes are in a "terminated" local state and no messages are in transit.

Using global state concepts, termination is detected when a global state shows: (i) every process is in a terminal local state, and (ii) all channels are empty. This requires collecting both local states and channel states—a task directly addressed by snapshot algorithms.

## Exam Tips

1. **Understand the definition of consistent global state**: Remember that a global state is consistent if and only if for every receive event in the state, the corresponding send event is also present.

2. **Distinguish between local state and channel state**: Local state refers to process variables, while channel state refers to messages in transit. Both must be captured for a complete global snapshot.

3. **Remember the role of markers in Chandy-Lamport**: Markers serve to delineate the point in time at which local state is captured and help identify messages that should be recorded as channel state.

4. **Know why FIFO ordering matters**: The Chandy-Lamport algorithm requires FIFO channels because it relies on markers arriving in order to correctly identify which messages belong in channel state.

5. **Understand the lattice structure**: The consistent global states form a lattice where moving upward in the lattice represents processing more events. This helps visualize possible system behaviors.

6. **Apply happened-before relation**: Use the happened-before relation (→) to determine whether a cut is consistent—if the cut is closed under →, it represents a valid global state.

7. **Connect to practical applications**: Know that global state concepts apply to checkpointing, deadlock detection, termination detection, and distributed debugging.