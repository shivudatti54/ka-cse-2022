# Multipath TCP (MPTCP) - Summary

## Key Definitions and Concepts
- Subflow: Independent TCP connection within MPTCP session
- DSS: Data Sequence Signal (metadata for packet reassembly)
- LIA/OLIA: Congestion control algorithms ensuring TCP-friendliness
- MP_CAPABLE: Initial handshake option for MPTCP negotiation
- Fallback: Mechanism to revert to standard TCP when middleboxes block MPTCP

## Important Formulas and Theorems
- **Coupled Congestion Control**: 
  ∑(w_i/R_i) = ∑(w_j/R_j) ∀ flows in same bottleneck
- **Throughput Bound**: 
  T ≤ min(∑B_i, C) where B_i=path bandwidth, C=application demand
- **Buffer Sizing**: 
  B ≥ ∑(w_max^i × RTT_max) across all subflows

## Key Points
- Enables simultaneous use of multiple network interfaces
- Maintains backward compatibility with TCP
- Requires OS-level implementation (Linux kernel ≥5.6 has full support)
- Apple's implementation uses private API with different congestion control
- Path manager daemon handles interface changes dynamically
- Security requires binding subflows through cryptographic keys
- Middleboxes (NATs, firewalls) can disrupt MPTCP operation

## Common Mistakes to Avoid
1. Assuming all subflows share same congestion window
2. Overlooking TCP options exhaustion (maximum 40 bytes)
3. Ignoring middlebox interference in network simulations
4. Confusing sequence numbers (data-level vs subflow-level)

## Revision Tips
1. Use Linux `iproute2` to practice MPTCP setup commands
2. Compare MPTCP congestion control variants using ns-3 simulations
3. Study Wireshark captures of MPTCP handshakes
4. Review IETF drafts on MPTCP QUIC integration

Length: 650 words