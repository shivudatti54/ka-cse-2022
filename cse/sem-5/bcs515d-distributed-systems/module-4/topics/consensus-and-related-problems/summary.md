# Consensus and Related Problems - Summary

## Key Definitions and Concepts

- **Consensus**: A fundamental problem in distributed systems where multiple processes must agree on a single value despite failures and asynchrony.
- **Byzantine Generals Problem**: A classic problem illustrating the challenges of achieving consensus when some processes may behave arbitrarily (maliciously).
- **Paxos Algorithm**: A family of consensus protocols designed for crash fault tolerance in asynchronous networks.
- **Raft**: A consensus algorithm designed for understandability, organizing consensus around a strong leader.

## Important Formulas and Theorems

- **Byzantine Fault Tolerance**: N > 3F, where N = total processes and F = faulty processes. Minimum required: 3F + 1 nodes.
- **Majority Quorum**: More than N/2 votes required for decision in a system of N processes.
- **Paxos Safety**: If a proposal with value V is chosen, then every proposal issued or accepted by any proposer with a higher number has value V.

## Key Points

1. Consensus requires three properties: Agreement (all decide same value), Validity (proposed value must be accepted), and Termination (all eventually decide).

2. The Byzantine Generals Problem demonstrates that achieving consensus with arbitrary failures requires more resources than with simple crash failures.

3. With N processes, Byzantine consensus requires at least 3F + 1 processes to tolerate F Byzantine failures.

4. Paxos achieves consensus through Prepare, Accept, and Learn phases using promises and majority voting.

5. Raft simplifies consensus by enforcing strong leader semantics - all log entries flow from leader to followers.

6. Raft handles leader election through randomized timeouts and term-based voting, ensuring at most one leader per term.

7. Log replication in Raft requires acknowledgment from a majority of followers before committing entries.

8. Practical applications of consensus include distributed databases (etcd, Consul), blockchain systems, and distributed file systems.

## Common Mistakes to Avoid

- Confusing crash failures with Byzantine failures - they require different consensus approaches.
- Forgetting that Paxos guarantees safety but not always liveness in asynchronous networks.
- Assuming consensus is always achievable instantly - termination is a critical property.
- Misremembering the Byzantine formula - it's N > 3F, not N ≥ 3F.

## Revision Tips

- Focus on understanding why consensus is hard: asynchrony, failures, and lack of a shared clock make coordination difficult.
- Remember the three consensus properties (Agreement, Validity, Termination) as the criteria for any correct protocol.
- Practice drawing the state diagrams for Raft leader election and Paxos phases.
- Review the relationship between failure models and algorithm requirements.
- Study how real systems like etcd use Raft for distributed configuration management.
