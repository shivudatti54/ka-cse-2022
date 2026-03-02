# Flow Control - Summary

## Key Definitions

- **Flow Control**: A mechanism that regulates the rate of data transmission from sender to receiver to prevent buffer overflow at the receiver.
- **Stop-and-Wait Protocol**: A flow control method where the sender transmits one frame and waits for acknowledgment before sending the next.
- **Sliding Window Protocol**: A flow control mechanism allowing multiple frames to be in transit simultaneously within a defined window.
- **Bandwidth-Delay Product (BDP)**: The maximum amount of data that can be in transit at once, calculated as Bandwidth × Round-Trip Time.
- **Receive Window (rwnd)**: The TCP field indicating available buffer space at the receiver for incoming data.
- **Go-Back-N ARQ**: A sliding window protocol where the sender retransmits all frames from the lost frame onward.
- **Selective Repeat ARQ**: A sliding window protocol where only the specific lost or corrupted frames are retransmitted.

## Important Formulas

- **Stop-and-Wait Utilization**: U = T_tx / (T_tx + 2 × T_prop)
- **Bandwidth-Delay Product**: BDP = Bandwidth (bits/s) × RTT (seconds)
- **Minimum Window Size**: W_min = BDP / Segment_Size
- **Effective Throughput**: Throughput = (Window_Size × Segment_Size) / RTT

## Key Points

1. Flow control prevents the receiver from being overwhelmed by regulating sender transmission rate based on receiver capacity.

2. Stop-and-wait is simple but inefficient for high-bandwidth or high-latency networks due to idle waiting time.

3. Sliding window protocols improve efficiency by allowing multiple outstanding frames, with utilization approaching 100% with optimal window size.

4. Go-Back-N retransmits all frames after a loss, while Selective Repeat selectively retransmits only lost frames.

5. TCP uses the receive window (rwnd) field in ACK packets to advertise available buffer space to the sender.

6. The TCP window scale option extends the maximum window size beyond 65,535 bytes for high-speed networks.

7. Zero window advertisement occurs when receiver buffers are full, pausing sender transmission until buffers free up.

8. Flow control operates at the data link layer and transport layer, while congestion control operates at the network level.

9. The actual TCP throughput is constrained by the minimum of the receive window and the congestion window.

10. Buffer management is critical for effective flow control, with buffer pressure monitoring enabling dynamic window adjustment.

## Common Mistakes

1. **Confusing flow control with congestion control**: Flow control addresses receiver limitations, while congestion control addresses network router overload.

2. **Ignoring propagation delay in throughput calculations**: Many students only consider transmission time and miss the significant impact of propagation delay.

3. **Incorrect window size interpretation**: The window size represents unacknowledged frames, not total frames sent.

4. **Forgetting sequence number requirements**: Sliding window protocols require sequence numbers to handle duplicates and out-of-order delivery correctly.