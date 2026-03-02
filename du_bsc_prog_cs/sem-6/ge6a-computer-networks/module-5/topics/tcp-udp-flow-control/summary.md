# TCP and UDP Flow Control - Summary

## Key Definitions and Concepts

- **Flow Control:** Mechanism to prevent the sender from overwhelming the receiver by matching transmission rate to receiver's processing capacity
- **Sliding Window Protocol:** TCP's method allowing multiple packets to be in transit before requiring acknowledgments
- **Receive Window (rwnd):** Buffer space available at the receiver, advertised in TCP header
- **Zero Window:** Condition when receiver's buffer is full; sender must wait before transmitting more data
- **Window Probe:** Small packet sent by sender to check if receiver's window has reopened

## Important Formulas and Theorems

- **Stop-and-Wait Efficiency:** `Efficiency = Tt / (Tt + 2Tp)` where Tt = transmission time, Tp = propagation delay
- **Effective TCP Window:** `Window = min(rwnd, cwnd)` — minimum of receiver window and congestion window
- **TCP Header Size:** 20-60 bytes (minimum 20 bytes without options)
- **UDP Header Size:** Fixed 8 bytes (no flow control fields)

## Key Points

- TCP provides reliable, ordered delivery with built-in flow control through the sliding window mechanism
- UDP is connectionless, unreliable, and has NO built-in flow control—application must handle it
- TCP's Window Size field is 16 bits (65,535 bytes), extendable with window scaling
- Stop-and-Wait is simple but inefficient for high-latency networks
- Go-Back-N retransmits all frames after a loss; Selective Repeat retransmits only lost frames
- Flow control prevents receiver buffer overflow; congestion control prevents network overload
- Zero window situation triggers persist timer and window probes to prevent deadlocks

## Common Mistakes to Avoid

1. Confusing flow control with congestion control—they serve different purposes
2. Thinking UDP has flow control—it does not; packets can be dropped silently
3. Forgetting that TCP effective window is the minimum of rwnd and cwnd
4. Assuming Stop-and-Wait is efficient for real networks—it works only for very low latency links

## Revision Tips

1. Draw the TCP three-way handshake and label how window size is communicated
2. Practice numerical problems on Stop-and-Wait efficiency calculation
3. Create a comparison table: TCP vs UDP flow control mechanisms
4. Remember: Flow control = receiver-focused, Congestion control = network-focused
5. Review TCP header diagram and identify which fields relate to flow control