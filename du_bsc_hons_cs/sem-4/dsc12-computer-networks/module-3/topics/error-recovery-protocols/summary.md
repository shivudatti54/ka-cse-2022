# Error Recovery Protocols - Summary

## Key Definitions and Concepts

- **Error Recovery Protocol**: A mechanism ensuring reliable data delivery by detecting errors and automatically requesting retransmission of corrupted or lost frames.

- **ARQ (Automatic Repeat reQuest)**: A protocol where the receiver automatically requests retransmission when errors are detected, without sender intervention.

- **Sliding Window Protocol**: A flow control mechanism allowing multiple frames to be in transit before receiving acknowledgments, improving channel utilization.

- **Cumulative ACK**: An acknowledgment confirming receipt of all frames up to a specific sequence number (used in Go-Back-N).

- **Selective ACK (SACK)**: An acknowledgment explicitly indicating which specific frames have been received correctly (used in Selective Repeat).

- **Sequence Number**: A numbering scheme for frames that enables detection of duplicates, lost frames, and correct ordering.

## Important Formulas and Theorems

- **Stop-and-Wait Channel Utilization**: U = T_frame / (T_frame + 2 × T_propagation)

- **Go-Back-N Sequence Bits**: ⌈log₂(N+1)⌉ bits (where N is window size)

- **Selective Repeat Sequence Bits**: ⌈log₂(2N)⌉ bits (window size N)

- **Selective Repeat Constraint**: 2^k ≥ 2N (sequence number space at least twice window size)

## Key Points

1. Error recovery protocols address frame loss, corruption, duplication, and reordering in network communication.

2. Stop-and-Wait uses a window size of 1, making it simple but inefficient for high-delay networks.

3. Go-Back-N retransmits all frames from the error point, using cumulative acknowledgments.

4. Selective Repeat retransmits only lost/damaged frames, maintaining higher throughput.

5. The receiver in Selective Repeat must buffer out-of-order frames until gaps are filled.

6. Sequence number space must be large enough to prevent ambiguity between old and new frame transmissions.

7. Timeout values must account for round-trip time (transmission + propagation + processing).

8. Trade-offs exist between protocol complexity, memory requirements, and throughput performance.

## Common Mistakes to Avoid

- Confusing cumulative and selective acknowledgments—cumulative ACKs acknowledge a range, selective ACKs specify individual frames.

- Forgetting that Go-Back-N discards all frames after an error, while Selective Repeat buffers them.

- Incorrectly calculating sequence number bits—remember the 2N requirement for Selective Repeat.

- Assuming longer timeouts always improve performance—excessively long timeouts delay error recovery.

- Overlooking that Stop-and-Wait requires only 1-bit sequence numbers due to its window size of 1.

## Revision Tips

1. Draw timing diagrams for each protocol to visualize frame transmission, acknowledgment, and timeout sequences.

2. Practice numerical problems on channel utilization and sequence number bit calculations—they appear frequently in exams.

3. Create a comparison table of all three protocols covering window size, retransmission strategy, buffer requirements, and complexity.

4. Understand why Selective Repeat needs twice the sequence number space as Go-Back-N—this is a classic exam question.

5. Review the relationship between propagation delay and protocol efficiency—higher delays favor sliding window protocols.