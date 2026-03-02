# Data Link Protocols - MAC Layer - Summary

## Key Definitions and Concepts
- MAC: Sub-layer managing shared medium access
- Contention: Device competition for channel access
- PDU: Protocol Data Unit (Frame at data link layer)
- DIFS/SIFS: Inter-frame spacing in 802.11

## Important Formulas and Theorems
- Pure ALOHA: S = G × e^(-2G)
- Slotted ALOHA: S = G × e^(-G)
- Ethernet Efficiency: η = 1/(1 + 5t_prop/t_trans)
- Token Ring Efficiency: τ = T/(T + τ_ring)
- CSMA/CD Backoff: R × 512 bit-times, R ∈ [0,2^k-1]

## Key Points
- CSMA/CD used in wired, CSMA/CA in wireless networks
- Maximum throughput: Slotted ALOHA (36.8%) > Pure ALOHA (18.4%)
- 802.11 uses virtual carrier sensing (NAV) with RTS/CTS
- Token Ring achieves 100% utilization under heavy load
- Modern Wi-Fi 6 uses OFDMA for multi-user parallel access
- 5G NOMA allows power-domain multiplexing
- Ethernet frame size: 64-1518 bytes (excluding preamble)

## Common Mistakes to Avoid
- Confusing CSMA/CD (detection) with CSMA/CA (avoidance)
- Forgetting slot time differences: WiFi (9μs) vs Ethernet (51.2μs)
- Misapplying ALOHA formulas to carrier-sensed protocols
- Ignoring propagation delay in efficiency calculations

## Revision Tips
- Practice throughput calculations using ALOHA equations
- Make comparative tables: TDMA vs FDMA vs CDMA
- Diagram CSMA/CA flow with RTS-CTS-DATA-ACK
- Memorize key percentages (18.4%, 36.8%, 802.11 DIFS=50μs)
- Relate protocols to real systems: Ethernet, WiFi, LTE