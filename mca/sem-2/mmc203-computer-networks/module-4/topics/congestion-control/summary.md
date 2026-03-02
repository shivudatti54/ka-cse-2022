# Congestion Control in Computer Networks - Summary

## Key Definitions and Concepts

- **Congestion**: A state where network resources cannot handle the aggregate traffic demand, leading to packet delays, losses, and reduced throughput.
- **Congestion Control**: Mechanisms to prevent senders from overwhelming the network, operating across the entire transmission path.
- **Flow Control**: End-to-end mechanism preventing sender from overwhelming the receiver.
- **Congestion Window (cwnd)**: TCP parameter limiting the amount of unacknowledged data that can be sent.
- **Slow Start Threshold (ssthresh)**: Threshold value determining transition between slow start and congestion avoidance phases.

## Important Formulas and Theorems

- **Token Bucket Burst Size**: Maximum burst = bucket capacity + (token rate × maximum allowable delay)
- **TCP Slow Start**: cwnd doubles every RTT (exponential growth: cwnd = cwnd + MSS for each ACK)
- **TCP Congestion Avoidance**: cwnd increases by 1 MSS per RTT (linear growth: cwnd = cwnd + MSS²/cwnd for each ACK)
- **Multiplicative Decrease**: On packet loss, cwnd is reduced by half (cwnd = cwnd/2)

## Key Points

- Congestion occurs when demand exceeds network capacity, causing increased delays, packet loss, and throughput degradation.
- Leaky Bucket converts bursty traffic to constant-rate traffic; Token Bucket allows burstiness while enforcing average rate.
- TCP uses four main mechanisms: slow start (exponential cwnd growth), congestion avoidance (linear cwnd growth), fast retransmit, and fast recovery.
- ECN allows routers to signal congestion proactively without packet drops, benefiting real-time applications.
- Flow control operates end-to-end (sender-receiver), while congestion control operates across the entire network path.
- The transition from slow start to congestion avoidance occurs when cwnd reaches ssthresh.
- Queue management in routers is fundamental to congestion—overflow causes drops, while underflow represents underutilization.

## Common Mistakes to Avoid

- Confusing congestion control with flow control—they address different problems at different network layers.
- Forgetting that slow start uses exponential growth while congestion avoidance uses linear growth.
- Assuming Token Bucket drops packets immediately when full—it may also queue packets if tokens are insufficient.
- Overlooking that ECN requires support from both routers and end-hosts to function.

## Revision Tips

- Trace through TCP slow start with specific cwnd and ssthresh values to internalize the dynamics.
- Compare Leaky Bucket vs. Token Bucket with diagrams to remember their traffic shaping characteristics.
- Focus on distinguishing features: flow control is receiver-limited, congestion control is network-limited.
- Review the sequence of TCP's response to packet loss: timeout causes return to slow start; duplicate ACKs trigger fast retransmit and recovery.
- Practice numerical problems involving token bucket calculations and cwnd evolution for exam success.
