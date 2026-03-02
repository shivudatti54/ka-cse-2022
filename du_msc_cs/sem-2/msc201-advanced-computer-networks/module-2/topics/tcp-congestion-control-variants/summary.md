# TCP Congestion Control Variants

## Introduction
TCP congestion control is a set of algorithms designed to prevent network congestion by regulating the rate of data transmission. It is crucial for maintaining Internet stability and efficiency. The Delhi University syllabus for Advanced Computer Networks covers various TCP congestion control variants, each addressing specific network challenges.

## Key Concepts
- **Congestion Window (cwnd)**: Sender's limit on unacknowledged data.
- **Slow Start**: Exponentially increase cwnd until a loss is detected.
- **Congestion Avoidance**: Linearly increase cwnd to probe for available bandwidth.
- **Fast Retransmit**: Quickly retransmit lost packets based on duplicate ACKs.
- **Fast Recovery**: Adjust cwnd after loss recovery to maintain throughput.

## Main Variants
- **TCP Tahoe**: Foundation variant implementing slow start, congestion avoidance, and fast retransmit. Uses additive increase and multiplicative decrease (AIMD) for congestion control.
- **TCP Reno**: Enhances Tahoe with fast recovery, allowing quicker recovery from single packet loss by avoiding full slow start.
- **TCP NewReno**: Refines Reno to handle multiple packet losses in a single window by using partial acknowledgments to detect all lost packets.
- **TCP SACK**: Introduces selective acknowledgments, enabling receivers to explicitly specify out-of-order segments, improving efficiency in lossy networks.
- **TCP BIC** (Binary Increase Congestion): Designed for high-speed networks, uses binary search to rapidly increase cwnd while maintaining stability.
- **TCP CUBIC**: Default in modern operating systems, uses a cubic function for window growth, providing high scalability and fairness in long-distance, high-bandwidth networks.
- **TCP BBR** (Bottleneck Bandwidth and Round-trip propagation time): A model-based variant that estimates available bandwidth and minimum RTT to operate at the optimal congestion point, reducing latency.

## Conclusion
Understanding TCP congestion control variants is essential for network optimization. From loss-based algorithms like Reno and NewReno to modern approaches like CUBIC and BBR, these mechanisms ensure reliable data transmission across diverse network conditions, aligning with the advanced topics in the Delhi University MSc CS curriculum.