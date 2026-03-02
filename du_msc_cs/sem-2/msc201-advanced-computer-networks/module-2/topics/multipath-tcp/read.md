# Multipath TCP (MPTCP)

## Introduction
Multipath TCP (MPTCP) is a revolutionary extension to traditional TCP that enables simultaneous use of multiple network paths between endpoints. Developed through IETF standardization (RFC 6824, RFC 8684), it addresses modern networking challenges where devices frequently have multiple network interfaces (Wi-Fi, cellular, Ethernet). 

For research-oriented CS students, MPTCP presents fascinating theoretical challenges in congestion control, path management, and security. Its importance lies in:
1. Bandwidth aggregation for high-throughput applications
2. Seamless failover between networks
3. Load balancing across heterogeneous networks
4. Enabling 5G network slicing and SDN architectures

Current research focuses on quantum-resistant MPTCP variants, AI-driven path selection, and integration with Named Data Networking architectures. Real-world deployments include Apple's iOS (since 2013), data center networks, and military communication systems.

## Key Concepts
1. **Subflows**: Independent TCP connections over different paths forming a single MPTCP connection
2. **Congestion Control Coupling**: Balanced congestion control across paths using algorithms like LIA (Linked Increase Algorithm) and OLIA (Optimized LIA)
3. **Packet Scheduling**: Strategies like Lowest-RTT-First (LowRTT) and Earliest Completion First (ECF)
4. **Path Management**: Dynamic discovery/add/remove of paths using ADD_ADDR options
5. **Security Considerations**: Sequence number space separation and cryptographic context binding
6. **Bufferbloat Mitigation**: Shared receive buffer management across subflows
7. **Cross-Layer Optimization**: Integration with MPTCP-aware middleboxes and SDN controllers

## Examples

**Example 1: Basic MPTCP Setup**
*Scenario:* Host A (Wi-Fi: 192.168.1.2, LTE: 10.0.0.2) connects to Server B (203.0.113.5) via both interfaces.

*Solution:*
1. Initial SYN on Wi-Fi interface with MP_CAPABLE option
2. Server responds with MP_CAPABLE + key
3. Host A sends ADD_ADDR option for LTE interface
4. Establish subflow via LTE using JOIN option
5. Data distribution using DSS (Data Sequence Signal) blocks

**Example 2: Congestion Control in MPTCP**
*Problem:* Two subflows with RTT 50ms and 100ms. Calculate congestion window growth using LIA.

*Solution:*
For coupled congestion control:
```
α = (w1 + w2) * (w1/R1² + w2/R2²)^(-1)
Δw = min(1/w1, α/(w1 + w2))
```
Where w=window size, R=RTT. This ensures fair bandwidth sharing with standard TCP flows.

## Exam Tips
1. Always compare MPTCP with TCP in answers (advantages: resilience, throughput; challenges: middlebox interference)
2. Understand the 3-way handshake with MP_CAPABLE option
3. Be prepared to derive congestion control equations for given scenarios
4. Know key IETF RFC numbers (6824, 8684) and their contributions
5. Discuss security aspects: SYN flooding attacks on multiple subflows
6. Explain buffer management strategies for heterogeneous networks
7. Recent trends: MPTCP in satellite networks, IoT deployments

Length: 2500 words