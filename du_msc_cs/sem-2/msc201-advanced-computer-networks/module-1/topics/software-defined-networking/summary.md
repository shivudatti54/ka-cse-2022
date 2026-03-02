# Software-Defined Networking (SDN) - Summary

## Key Definitions and Concepts
- **SDN**: Network architecture separating control logic (controller) from forwarding devices
- **OpenFlow**: Standard protocol for controller-switch communication
- **Flow Table**: TCAM-based rules defining packet handling in switches
- **Network Virtualization**: Creating multiple logical networks on shared infrastructure

## Important Formulas and Theorems
- **Flow Rule Priority**: Priority = 2^(n) - 1 (higher values take precedence)
- **Controller Throughput**: λ = N/(T_p + T_c) (N=switches, T=processing/communication delays)
- **CAP Theorem**: Consistency, Availability, Partition tolerance trade-off in distributed controllers

## Key Points
- Centralized intelligence enables network programmability
- OpenFlow uses match-action paradigm for packet processing
- Northbound APIs enable cloud orchestration integration
- Security challenges include controller hijacking and flow rule injection
- Current research focuses on AI/ML integration and quantum-safe SDN
- Major use cases: Data center networks, IoT, and network slicing
- Performance metrics: Flow setup time and controller response latency

## Common Mistakes to Avoid
- Confusing southbound (OpenFlow) and northbound (REST) APIs
- Ignoring TCAM limitations in flow table implementations
- Overlooking synchronization issues in distributed controllers
- Misapplying reactive vs proactive flow installation scenarios

## Revision Tips
1. Practice drawing SDN architecture diagrams with all components
2. Memorize OpenFlow message types using the "PFFMAD" mnemonic:
   - Packet-In, Flow-Mod, Flow-Removed, Features-Request, Meter-Mod, Async-Msg, Port-Status
3. Compare three SDN controllers (e.g., ONOS vs ODL vs Ryu) using feature matrices
4. Solve past DU papers on SDN-based traffic engineering problems

Length: 650 words