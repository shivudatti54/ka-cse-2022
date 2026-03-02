# TCP, UDP, and Congestion Control

## Introduction
Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) form the backbone of internet communication. TCP provides reliable, ordered data delivery through connection-oriented sessions, while UDP offers lightweight, connectionless datagram services. Congestion control mechanisms prevent network overload and ensure fair bandwidth allocation.

These protocols operate at the transport layer (Layer 4) of the OSI model. TCP's congestion control algorithms like AIMD (Additive Increase Multiplicative Decrease) and modern variants like BBR (Bottleneck Bandwidth and Round-trip propagation time) are critical for maintaining internet stability. UDP's lack of built-in congestion control makes it suitable for real-time applications like VoIP and video streaming where occasional packet loss is acceptable.

Understanding these protocols is essential for network optimization, application development, and troubleshooting. With 95% of internet traffic using TCP, professionals must master flow control, window management, and Quality of Service (QoS) implementations.

## Key Concepts
**TCP Features:**
- Connection-oriented three-way handshake (SYN, SYN-ACK, ACK)
- Sequence numbers and acknowledgments for reliable delivery
- Sliding window protocol for flow control
- Congestion control using congestion window (cwnd) and slow start threshold (ssthresh)

**UDP Characteristics:**
- Connectionless communication with no handshakes
- No guaranteed delivery or ordering
- Checksum for basic error detection
- Used in DNS, DHCP, and real-time multimedia

**Congestion Control Mechanisms:**
1. **Slow Start:** Exponential cwnd growth until ssthresh
2. **Congestion Avoidance:** Additive increase after ssthresh
3. **Fast Retransmit:** Triggered by 3 duplicate ACKs
4. **Fast Recovery:** Maintains flow during packet loss
5. **Explicit Congestion Notification (ECN):** Router-assisted congestion signaling

**TCP Variants:**
- Tahoe (original slow start)
- Reno (fast recovery)
- Cubic (Linux default, uses cubic function for window growth)
- BBR (Google's model-based congestion control)

## Examples

**Example 1: TCP Congestion Window Growth**
```
Initial cwnd = 1 MSS, ssthresh = 8 MSS
Phase 1: Slow Start
1. Send 1 segment → ACK received → cwnd=2
2. Send 2 segments → 2 ACKs → cwnd=4
3. Send 4 segments → 4 ACKs → cwnd=8 (reach ssthresh)

Phase 2: Congestion Avoidance
4. cwnd += 1 → 9 MSS
5. cwnd += 1 → 10 MSS
...
```

**Example 2: UDP Packet Loss Analysis**
A video streaming service sends 1000 packets via UDP:
- Network drop rate = 2%
- No retransmissions
Lost packets = 1000 × 0.02 = 20
Effective throughput = 980 packets/RTT
Application must handle jitter buffer for 20 missing frames

**Example 3: AIMD Convergence**
Two TCP flows share a 10 Mbps bottleneck:
- Flow A: 6 Mbps, Flow B: 4 Mbps
Packet loss occurs → both reduce by 50%
New rates: 3 Mbps and 2 Mbps
Additive increase: +1 Mbps each RTT
Eventually converges to fair 5 Mbps each

## Exam Tips
1. Always mention TCP header fields (sequence no, ACK no, window size) when explaining reliability
2. For numerical problems, remember cwnd units are typically in MSS (Maximum Segment Size)
3. Differentiate between flow control (receiver-side) and congestion control (network-side)
4. Draw packet diagrams for three-way handshake and four-way termination
5. When comparing TCP/UDP, use OSI layer perspective and application requirements
6. Memorize the congestion window formula: cwnd = min(receiver_window, congestion_window)
7. Recent exam trends include ECN and BBR algorithm questions