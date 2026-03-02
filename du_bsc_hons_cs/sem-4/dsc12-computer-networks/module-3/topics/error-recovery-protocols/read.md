# Error Recovery Protocols

## Introduction

Error recovery protocols are fundamental mechanisms in data communication that ensure reliable end-to-end delivery of data across unreliable network links. In computer networks, the physical transmission medium is prone to various errors including bit flips, frame loss, duplication, and reordering. Without error recovery mechanisms, corrupted or lost data would corrupt application-level communications, making reliable network services impossible.

The University of Delhi Computer Science curriculum emphasizes three primary error recovery protocols: Stop-and-Wait ARQ (Automatic Repeat reQuest), Go-Back-N ARQ, and Selective Repeat ARQ. These protocols form the backbone of reliable data transmission in Data Link Layer and Transport Layer communications. Understanding these protocols is crucial for network engineers and software developers who design distributed systems. The protocols represent a classic tradeoff between complexity, throughput, and reliability—themes that appear repeatedly in computer science and appear frequently in DU examinations.

## Key Concepts

### Fundamentals of Error Control

Error control in networking encompasses two primary functions: error detection and error recovery. While error detection identifies corrupted frames (using CRC, checksums, or parity bits), error recovery mechanisms ensure that erroneous or lost frames are retransmitted correctly. The core challenge addressed by error recovery protocols is managing the acknowledgment system—when to retransmit, what to retransmit, and how to handle duplicates.

**Automatic Repeat reQuest (ARQ)** is the overarching principle where the receiver automatically requests retransmission of erroneous data. ARQ protocols combine error detection, positive acknowledgments, and retransmission timers to achieve reliability. Three variants exist: Stop-and-Wait, Go-Back-N, and Selective Repeat, each with distinct operational characteristics and performance profiles.

### Stop-and-Wait ARQ

Stop-and-Wait is the simplest error recovery protocol where the sender transmits a single frame and waits for acknowledgment before sending the next frame. The protocol operates as follows:

1. Sender transmits frame with sequence number N
2. Receiver receives frame, verifies checksum
3. If error-free, receiver sends positive acknowledgment (ACK N+1)
4. If corrupted, receiver discards frame and sends no acknowledgment
5. Sender maintains a timer after each transmission
6. If ACK not received within timeout, sender retransmits frame N

**Sequence Numbers**: Stop-and-Wait uses a 1-bit sequence number (0 or 1) because only one frame needs to be outstanding at any time. This alternating bit (also called piggybacking) helps identify duplicate frames—critical because acknowledgments can be lost, causing the sender to retransmit a frame the receiver has already accepted.

**Performance Analysis**: The protocol suffers from poor utilization of the channel. If the propagation delay is significantly larger than transmission time, the sender spends most time waiting. Channel utilization formula: U = (T_frame) / (T_frame + 2T_prop). For long-distance links, this utilization drops dramatically, necessitating more sophisticated protocols.

### Go-Back-N ARQ

Go-Back-N is a sliding window protocol that allows multiple outstanding frames, significantly improving throughput compared to Stop-and-Wait. The protocol maintains a sender window of size N, where N represents the maximum number of unacknowledged frames that can be transmitted.

**Sliding Window Mechanism**: The sender maintains three pointers: send base (oldest unacknowledged frame), next sequence number (next frame to send), and window size N. When the receiver successfully receives frame N, it sends ACK N+1 (cumulative acknowledgment). If frame N is corrupted, the receiver discards all subsequent frames (N+1, N+2, etc.) and sends Negative Acknowledgment (NAK N) or simply does not acknowledge, forcing the sender to retransmit from frame N.

**Retransmission Strategy**: Upon timeout for any unacknowledged frame or receipt of NAK, the sender goes back to the sequence number indicated and retransmits all frames from that point onward. This "go back" behavior gives the protocol its name. The receiver maintains an expected sequence number and accepts only frames matching this number in strict order.

**Sequence Number Field**: Go-Back-N requires ⌈log₂(N+1)⌉ bits for sequence numbers. For a window size of N, sequence numbers range from 0 to 2^n - 1, where n is the number of bits. Common implementations use sequence numbers modulo 2^k.

### Selective Repeat ARQ

Selective Repeat represents the most sophisticated and efficient ARQ protocol. Unlike Go-Back-N, Selective Repeat retransmits only the specific erroneous or lost frames, not all subsequent frames. This approach significantly improves throughput, especially when error rates are high or propagation delays are large.

**Receiver Window**: The receiver maintains a receive window identical to the sender's window size. It can accept frames in any order within the window—this is called "selective acceptance." When an out-of-order frame arrives, it's buffered (not discarded like Go-Back-N) until the missing frames fill the gap.

**Acknowledgments**: Selective Repeat uses both individual and cumulative acknowledgments. Selective Acknowledgment (SACK) explicitly identifies which frames have been received correctly, allowing the sender to know exactly which frames need retransmission. The basic ACK still indicates the next expected in-order frame.

**Sequence Number Space**: For Selective Repeat to work correctly without ambiguity, the sequence number space must be at least twice the window size (2N). This ensures that old frames with the same sequence number won't be confused with new transmissions. Mathematically: 2^k ≥ 2N where k is the number of sequence number bits.

### Comparative Analysis

| Aspect | Stop-and-Wait | Go-Back-N | Selective Repeat |
|--------|---------------|-----------|-------------------|
| Window Size | 1 | N | N |
| Retransmission | Single frame | All from error | Only error frame |
| Buffer at Receiver | Not needed | Not needed | Required |
| Sequence Bits | 1 bit | ⌈log₂(N+1)⌉ | ⌈log₂(2N)⌉ |
| Complexity | Lowest | Medium | Highest |
| Throughput | Lowest | Medium | Highest |

## Examples

### Example 1: Stop-and-Wait Scenario

**Problem**: Consider a Stop-and-Wait ARQ system with frame transmission time of 10ms and one-way propagation delay of 50ms. Calculate the channel utilization and the maximum throughput if the link bandwidth is 1 Mbps and frame size is 1000 bits.

**Solution**:

Given:
- Frame transmission time (Tt) = 1000 bits / 1 Mbps = 1 ms
- One-way propagation delay (Tp) = 50 ms
- Timeout value typically = Tt + 2Tp + processing = approximately 101 ms

Channel Utilization:
- Total cycle time = Tt + 2Tp = 1 + 100 = 101 ms
- Utilization (U) = Tt / (Tt + 2Tp) = 1 / 101 ≈ 0.99%

Maximum Throughput:
- Throughput = (Frame size × Utilization) / Time unit
- Throughput = 1000 bits × 0.0099 ≈ 9.9 bits/ms ≈ 9.9 Kbps
- This is only ~1% of the 1 Mbps link capacity!

This example demonstrates why Stop-and-Wait is inefficient for high-speed or long-distance networks—the sender waits idle for most of the time.

### Example 2: Go-Back-N Operation

**Problem**: A Go-Back-N system uses a 4-bit sequence number and window size of 16. The sender transmits frames 0 through 15. Frame 3 is corrupted, and frame 7's ACK is lost. Show how the protocol recovers.

**Solution**:

**Initial Transmission**: Sender transmits frames 0, 1, 2, 3, 4, 5, 6, 7 (send window allows 16 frames)

**Frame 3 Corrupted**: Receiver receives frames 0, 1, 2 successfully and sends ACKs 1, 2, 3. When frame 3 arrives corrupted:
- Receiver discards frame 3
- Receiver also discards frames 4, 5, 6 (out of order)
- Receiver sends NAK 3 (or simply doesn't acknowledge)
- Receiver's expected sequence remains 3

**Timeout at Sender**: After timeout for frame 3 (and subsequently for 4, 5, 6), sender retransmits starting from frame 3:
- Retransmits frames 3, 4, 5, 6, 7, 8...

**ACK 7 Lost**: If ACK for frame 7 (which was originally transmitted) is lost:
- Sender's timer for frame 7 expires
- Sender retransmits frames 7, 8, 9... (Go-Back-N behavior)
- Receiver already has frame 7 correctly, but Go-Back-N retransmits anyway
- Receiver accepts the duplicate (or discards based on implementation) but ACKs correctly

The key insight: Go-Back-N's simplicity comes at the cost of unnecessary retransmissions when errors occur mid-window.

### Example 3: Selective Repeat Analysis

**Problem**: Using Selective Repeat with sequence number space 0-7 and window size 3, show how the protocol handles: (a) Frame 2 lost, (b) Duplicate frame 4 received.

**Solution**:

**(a) Frame 2 Lost:**

1. Sender transmits frames 0, 1, 2, 3, 4
2. Receiver gets 0, 1 → sends ACK 2
3. Frame 2 lost → receiver doesn't ACK
4. Receiver gets 3, 4 → buffers them (out of order)
5. Sender's timer for frame 2 expires
6. Sender retransmits only frame 2
7. Receiver gets frame 2, now has 0, 1, 2, 3, 4 in sequence
8. Receiver sends cumulative ACK 5 (all received)
9. Sender slides window and continues

**(b) Duplicate Frame 4:**

1. Original frame 4 transmitted and ACK 5 received
2. Timeout occurs (ACK lost)
3. Sender retransmits frame 4 with sequence number 4
4. Receiver's window accepts frames with sequence 4-6 (if base is 3)
5. Frame 4 (duplicate) arrives
6. Receiver checks: Is 4 in receive window [3, 5]? Yes
7. Receiver delivers duplicate to application and sends ACK 5 again
8. No confusion occurs because sequence numbers distinguish duplicates

This demonstrates Selective Repeat's efficiency: only the lost frame retransmits, and duplicates are handled correctly through sequence numbering.

## Exam Tips

1. **Memorize the channel utilization formula** for Stop-and-Wait: U = T_frame / (T_frame + 2T_propagation). This frequently appears in DU examination numerical problems.

2. **Distinguish between the three protocols** in exam questions: Stop-and-Wait for simple/slow links, Go-Back-N for moderate reliability requirements, Selective Repeat for high-speed long-delay networks.

3. **Remember sequence number requirements**: Stop-and-Wait needs 1 bit, Go-Back-N needs ⌈log₂(N+1)⌉ bits, Selective Repeat needs ⌈log₂(2N)⌉ bits. DU frequently tests this formula.

4. **NAK vs ACK behavior**: In Go-Back-N, receiving NAK for frame i causes retransmission from frame i onwards. In Selective Repeat, NAK typically requests only that specific frame.

5. **Window size constraints**: For Selective Repeat to function correctly without ambiguity, the sequence number space must be at least twice the window size. This is crucial for preventing "window wraparound" problems.

6. **Cumulative vs Selective ACK**: Go-Back-N uses cumulative acknowledgments (ACK n acknowledges all frames up to n-1). Selective Repeat uses selective acknowledgments to identify exactly which frames were received.

7. **Timeout management**: Each unacknowledged frame has its own timer in Selective Repeat and Go-Back-N. In Stop-and-Wait, only one timer exists since only one frame is pending.

8. **Practice numerical problems**: DU exams consistently include numerical questions on utilization calculation, sequence number bit requirements, and protocol behavior analysis.