# Global States - Summary

## Key Definitions

- **Local State**: The values of all local variables and program counter at a process at a specific point in execution
- **Channel State**: The collection of messages that have been sent but not yet received on a communication channel
- **Global State**: The combined local states of all processes and the states of all channels at a given instant
- **Consistent Global State**: A global state where for every receive event included, the corresponding send event is also included
- **Consistent Cut**: A set of events closed under the happened-before relation
- **Happened-Before Relation (→)**: A partial order where a → b if event a causally influences event b

## Important Formulas

- A global state S = (L, C) where L = {l₁, l₂, ..., lₙ} is the set of local states and C = {c₁, c₂, ..., cₘ} is the set of channel states

- Consistency condition: ∀ receive event r ∈ S, send(r) ∈ S

- Cut frontier: The boundary events at each process that delimit the cut

## Key Points

1. Distributed systems lack global time, making simultaneous state observation impossible

2. A consistent global state ensures physical plausibility—no message appears received before being sent

3. The Chandy-Lamport algorithm captures consistent snapshots without halting the computation

4. Marker messages in the snapshot algorithm help identify messages in transit (channel state)

5. FIFO channels are required for Chandy-Lamport to correctly identify which messages are "in flight"

6. The lattice of consistent global states provides a framework for reasoning about all possible system behaviors

7. Global state concepts are foundational for checkpointing, termination detection, and debugging

8. The happened-before relation defines which events can be simultaneously observed in a consistent way

## Common Mistakes

1. **Confusing local and global state**: Remember that global state includes both local states AND channel states

2. **Ignoring messages in transit**: A common error is capturing only process states, forgetting that messages traveling between processes are part of the system state

3. **Assuming simultaneous observation is possible**: In distributed systems, "simultaneous" is meaningless without defining the time ordering; consistent cuts address this

4. **Forgetting FIFO requirement**: The Chandy-Lamport algorithm specifically requires FIFO channels; it does not work with non-FIFO channels without modification