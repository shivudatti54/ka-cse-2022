# TCP/UDP Congestion Control - Summary

## Key Definitions and Concepts

- **Congestion Window (cwnd)**: TCP sender's limit on unacknowledged data; the primary mechanism for controlling send rate.
- **Slow Start Threshold (ssthresh)**: The threshold determining whether TCP uses slow start (exponential) or congestion avoidance (linear) growth.
- **AIMD (Additive Increase Multiplicative Decrease)**: TCP's core congestion control principle—gradually increase sending rate during good conditions, rapidly decrease on congestion detection.
- **Fast Retransmit**: TCP's mechanism to retransmit lost packets upon receiving three duplicate ACKs without waiting for timeout.
- **Fast Recovery**: TCP Reno's algorithm that maintains higher sending rate after fast retransmit rather than returning to slow start.

## Important Formulas and Theorems

- **Slow Start Growth**: cwnd doubles every RTT (cwnd = cwnd × 2)
- **Congestion Avoidance Growth**: cwnd increases by 1 MSS per RTT (cwnd = cwnd + MSS)
- **Multiplicative Decrease**: On loss detection, ssthresh = cwnd/2, cwnd = ssthresh (or cwnd = 1 for timeout)
- **Effective Window**: Actual send window = min(cwnd, rwnd)

## Key Points

- TCP implements four integrated congestion control algorithms; UDP provides no built-in congestion control.
- Slow Start uses exponential growth (cwnd doubles each RTT) until reaching ssthresh.
- Congestion Avoidance uses linear growth (+1 MSS per RTT) using AIMD principles.
- TCP Tahoe always enters slow start on any loss; TCP Reno uses fast recovery for duplicate ACK scenarios.
- Modern TCP variants like Cubic and BBR address high bandwidth-delay product networks differently.
- UDP applications requiring congestion control must implement it at the application layer.
- Timeout indicates more severe congestion than duplicate ACKs.

## Common Mistakes to Confuse

- **Confusing slow start and congestion avoidance**: Remember slow start is exponential (doubling), congestion avoidance is linear (+1 MSS/RTT).
- **Mixing up Tahoe and Reno**: Tahoe returns to cwnd=1 on any loss; Reno enters fast recovery on duplicate ACKs.
- **Forgetting rwnd**: The actual send window is min(cwnd, rwnd)—network isn't always the bottleneck.
- **Thinking UDP is always bad**: UDP is appropriate for real-time applications where latency matters more than reliability.

## Revision Tips

1. Draw the TCP state machine showing transitions between Slow Start, Congestion Avoidance, and Fast Recovery based on cwnd vs ssthresh and loss detection methods.

2. Practice calculating cwnd values over multiple RTTs for both slow start and congestion avoidance phases.

3. Memorize the key differences between Tahoe and Reno—these are frequently tested in exams.

4. Remember that modern networks use TCP Cubic (Linux/Windows default), not the classic Reno or Tahoe discussed in textbooks.