# Byzantine Fault Tolerance - Summary

## Key Definitions and Concepts
- **Byzantine Failure**: A node arbitrarily deviates from protocol.
- **Quorum**: Minimum number of nodes (3f+1) needed to tolerate f faults.
- **View Change**: PBFT mechanism to replace a faulty primary node.

## Important Formulas and Theorems
- **Node Requirement**: \( n \geq 3f + 1 \) (for PBFT)
- **Safety**: \( \text{Commit}(m) \implies \) all honest nodes agree on m.
- **Liveness**: Honest nodes eventually decide on every request.

## Key Points
- BFT systems require redundancy and cryptographic verification.
- PBFT uses three-phase consensus but has \( O(n^2) \) message complexity.
- Modern variants (e.g., SBFT, HotStuff) optimize for scalability.
- Blockchain combines BFT with economic incentives (e.g., staking).
- Asynchronous BFT protocols sacrifice latency for stronger guarantees.

## Common Mistakes to Avoid
- Assuming BFT applies only to malicious nodes (includes arbitrary faults).
- Confusing crash fault tolerance with Byzantine fault tolerance.
- Overlooking the energy trade-offs in PoW-based BFT systems.
- Misapplying the 3f+1 rule to asynchronous models.

## Revision Tips
1. Practice PBFT phase diagrams with node failure scenarios.
2. Memorize key differences between PBFT, Tendermint, and Ripple.
3. Study seminal papers: Castro-Liskov (1999) and the HoneyBadgerBFT protocol.
4. Use DU's distributed systems lab simulations to test BFT concepts.

Length: 650 words