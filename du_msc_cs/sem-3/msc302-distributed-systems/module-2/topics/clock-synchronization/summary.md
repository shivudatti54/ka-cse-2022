# Clock Synchronization - Summary

## Key Definitions and Concepts
- **Physical Clock**: Real-time measurement synchronized to UTC
- **Logical Clock**: Event ordering without real-time guarantees (Lamport/vector)
- **Clock Drift**: Divergence due to oscillator imperfections
- **Happens-Before (→)**: Partial ordering of events (Lamport, 1978)

## Important Formulas and Theorems
- **Lamport Clock Rules**:
  - On event: C = C + 1
  - On send: C = C + 1 before sending
  - On receive: C = max(local C, received C) + 1
- **NTP Offset**: θ = (T2 - T1 + T3 - T4)/2
- **Vector Clock Update**: V[i] = max(V_local[i], V_received[i]) for all i

## Key Points
- Physical clocks require synchronization to mitigate drift (NTP/PTP)
- Lamport clocks enforce partial ordering but not causality
- Vector clocks detect concurrent events via component-wise comparison
- NTP uses hierarchical strata with statistical delay compensation
- TrueTime API provides ε bounds (typically 1-7ms) for global consistency
- Byzantine clocks require redundancy and majority voting
- Hybrid clocks (e.g., HLC) combine physical timestamps with logical counters

## Common Mistakes to Avoid
- Confusing logical clocks with physical time guarantees
- Forgetting to increment Lamport counters before sending messages
- Misapplying vector clock comparison operators (≤ vs <)
- Ignoring network jitter in NTP offset calculations

## Revision Tips
1. Practice Lamport/vector clock problems using event diagrams
2. Derive NTP's θ and δ formulas from timestamp exchange
3. Compare Spanner's TrueTime with NTP's synchronization approach
4. Study the hybrid logical clock paper (Kulkarni et al., 2014)

Length: 400-800 words