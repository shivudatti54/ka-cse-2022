# Consensus Algorithms: Paxos and Raft - Summary

## Key Definitions and Concepts

- **Consensus**: Agreement among distributed nodes on a single value despite failures. Requires validity (proposed value must be chosen), agreement (all choose same value), and termination (all eventually decide).
- **Paxos**: Leslie Lamport's consensus algorithm using proposers, acceptors, and learners with two phases (Prepare/Promise and Accept/Accepted). Achieves safety through majority quorums.
- **Raft**: Consensus algorithm designed for understandability with three components: leader election, log replication, and safety. Uses strong leader model.
- **Term**: Logical clock in Raft; monotonically increasing number used to identify stale information and ensure only one leader per term.
- **Quorum**: Majority of nodes (n/2 + 1) required for Paxos promise/acceptance and Raft election/commit operations.

## Important Formulas and Theorems

- **Quorum Size**: For 2f+1 nodes, system tolerates f failures → quorum = f+1 = (n+1)/2
- **Election Timeout**: Randomized between 150-300ms in Raft to prevent split votes
- **Log Matching**: If logs agree on entry at index i with term t, they agree on all entries up to i
- **Leader Completeness**: If entry e is committed at term t, it appears in logs of all leaders for terms > t

## Key Points

1. Consensus is impossible in asynchronous systems with even a single crash failure (FLP impossibility) - algorithms add timing assumptions.

2. Paxos guarantees safety (no two values can be chosen) but may not terminate under certain network conditions.

3. Raft provides same safety guarantees as Paxos but with clearer structure: leader election, log replication, safety.

4. In Raft, only the leader can accept client requests; followers redirect to leader or return stale leader information.

5. Log entries in Raft are committed once majority acknowledge; committed entries are eventually applied to state machines.

6. If a follower receives AppendEntries with a previous index not matching its log, it rejects and triggers log reconciliation.

7. Raft's joint consensus allows membership changes without violating safety by transitioning through a combined old+new configuration.

8. Real-world systems: etcd/Consul (Raft), Google Spanner (Paxos variants), ZooKeeper (Zab).

## Common Mistakes to Avoid

1. **Confusing prepared and accepted**: In Paxos, "prepared" means acceptor promises not to accept lower-numbered proposals; "accepted" means the value is chosen.

2. **Thinking Raft eliminates partitioning**: Network partitions still cause split-brain scenarios; Raft handles this through leader election in majority partition only.

3. **Ignoring uncommitted entries**: In Raft, uncommitted entries from previous leader are not automatically discarded—they may be retained or overwritten depending on the new leader's log.

4. **Overlooking randomization**: Raft's randomized election timeouts are critical for avoiding repeated split votes; deterministic timeouts cause livelock.

## Revision Tips

1. Draw the message flow diagrams for Paxos (proposer ↔ acceptors) and Raft (leader ↔ followers) from memory.

2. Work through 3-node scenarios with different failure combinations to internalize the safety properties.

3. Compare Paxos vs Raft using a table of criteria (leader, understandability, membership changes).

4. Understand why FLP impossibility doesn't prevent practical systems—algorithms use timeouts, randomized leaders, or synchronous assumptions.

5. Review how etcd/Raft handles leader failure and recovery, especially the log reconciliation process.