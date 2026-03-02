# TCP and UDP Flow Control

## Introduction

Flow control is a fundamental mechanism in computer networking that ensures data is transmitted at a rate that the receiver can handle. In the context of the Transport Layer (Layer 4 of the OSI model), flow control becomes critical because the sender and receiver often operate at different speeds and have different buffer capacities. Without proper flow control mechanisms, data can be lost, overwhelming either the receiver's buffer or the network itself.

In this topic, we examine how two major Transport Layer protocols—Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)—handle flow control. TCP, being a connection-oriented, reliable protocol, implements sophisticated flow control mechanisms including the sliding window protocol and the receiver's window size advertisement. UDP, in contrast, is a connectionless, unreliable protocol with minimal built-in flow control, placing the responsibility largely on the application layer.

Understanding flow control is essential for network engineers and developers designing distributed systems. For instance, when a high-speed server sends data to a mobile device with limited processing power, flow control prevents packet loss and ensures efficient utilization of network resources. This topic forms a crucial part of the University of Delhi Computer Science curriculum, with direct relevance to real-world networking scenarios and CUET/DU semester examinations.

## Key Concepts

### 1. Need for Flow Control

Flow control becomes necessary when there is a mismatch between the sender's transmission rate and the receiver's processing capacity. The receiver has a finite buffer (receive window) to store incoming data before passing it to the application layer. If the sender transmits faster than the receiver can process, buffer overflow occurs, leading to packet drops and retransmissions—an inefficient use of bandwidth.

Consider a scenario where a file server (with powerful hardware) sends a large file to an embedded device with limited memory. Without flow control, the server might flood the receiver, causing dropped packets and requiring retransmission, degrading overall performance.

### 2. TCP Flow Control Mechanism

TCP implements flow control through a sliding window protocol. The key components are:

**Receive Window (rwnd):** The amount of buffer space available at the receiver. The receiver advertises this value in the TCP header's "Window Size" field (16 bits, allowing values up to 65,535 bytes, though scaled windows can go higher with window scaling options).

**Sliding Window Protocol:** TCP uses a sliding window where the sender maintains three pointers:
- **Last byte acknowledged:** The last byte successfully received and acknowledged
- **Last byte sent:** The last byte sent but not yet acknowledged
- **Last byte usable:** The last byte that can be sent without waiting for permission

When the receiver acknowledges data, the window slides forward, allowing the sender to transmit more data. If the receiver's buffer fills up, it advertises a window size of zero, causing the sender to stop transmitting and wait for a window update.

**Zero Window and Window Probes:** When the receiver advertises a zero window, the sender enters a "persist" state and periodically sends tiny packets (window probes) to check if the receiver's window has reopened. This prevents deadlocks when window size updates are lost.

### 3. UDP Flow Control

UDP is a connectionless protocol that does not implement flow control in the traditional sense. It does not maintain connection state, does not perform acknowledgments, and does not have a window size field in its header. The UDP header consists of only 8 bytes: source port, destination port, length, and checksum.

Since UDP provides no flow control, if a sender transmits faster than the receiver can process, packets are simply dropped at the receiver's socket buffer. This can be advantageous for real-time applications (like video streaming or VoIP) where late data is useless—waiting for retransmission would cause more harm than good.

Applications using UDP must implement their own flow control at the application layer if needed. For example, RTP (Real-time Transport Protocol) includes mechanisms for rate adaptation.

### 4. Stop-and-Wait Protocol

This is the simplest flow control mechanism where the sender transmits one packet and waits for an acknowledgment before sending the next. While simple to implement, it suffers from poor efficiency as the channel remains idle during the round-trip time (RTT).

**Efficiency Formula:**
```
Efficiency = 1 / (1 + 2a) where a = propagation delay / transmission time
```

For high-bandwidth or high-latency links (like satellite connections), this becomes extremely inefficient.

### 5. Sliding Window Protocols

To improve efficiency, sliding window protocols allow multiple frames to be in transit simultaneously:

**Go-Back-N (GBN):** The sender can transmit N frames without receiving acknowledgments. If a frame is lost, all subsequent frames must be retransmitted. The receiver maintains only the sequence number of the expected frame.

**Selective Repeat (SR):** Only the lost frames are retransmitted. The receiver can accept out-of-order frames. This requires more complex receiver logic but offers better performance in error-prone networks.

### 6. Congestion Control vs. Flow Control

It is crucial to distinguish between flow control and congestion control:

- **Flow Control:** Concerned with the sender-receiver pair—prevents overwhelming the receiver
- **Congestion Control:** Concerned with the network—prevents overwhelming the network infrastructure (routers, links)

TCP implements both: flow control through the receive window (rwnd) and congestion control through the congestion window (cwnd). The effective window is the minimum of both: `Window = min(rwnd, cwnd)`.

### 7. TCP Header Fields for Flow Control

The TCP header includes critical fields for flow control:
- **Sequence Number:** Identifies each byte in the data stream
- **Acknowledgment Number:** Indicates next expected byte (cumulative ACK)
- **Window Size:** 16-bit field advertising receiver's buffer capacity
- **Flags:** SYN, ACK, FIN, RST, PSH, URG control connection behavior

With TCP Window Scaling (RFC 1323), the Window Size field can be scaled by a factor of 2^n, supporting windows up to 1 GB for high-bandwidth networks.

## Examples

### Example 1: TCP Window Size Calculation

**Problem:** A TCP receiver has a receive buffer of 16 KB. Currently, 10 KB of data is already in the buffer awaiting consumption by the application. The application reads 4 KB. What window size will the receiver advertise?

**Solution:**
- Total buffer: 16 KB = 16,384 bytes
- Current data in buffer: 10 KB = 10,240 bytes
- After application reads: 10,240 - 4,096 = 6,144 bytes remaining
- Available space: 16,384 - 6,144 = 10,240 bytes (10 KB)

The receiver will advertise a window size of 10 KB (10,240 bytes) in the TCP header's Window Size field.

### Example 2: Stop-and-Wait Efficiency

**Problem:** A 1 Mbps link has a one-way propagation delay of 50 ms. Packets are 1000 bits each. Calculate the efficiency of the Stop-and-Wait protocol.

**Solution:**
- Bandwidth = 1 Mbps = 10^6 bits/second
- Packet size = 1000 bits
- Transmission time (Tt) = 1000 / 10^6 = 1 ms = 0.001 seconds
- Round-trip time (RTT) = 2 × 50 ms = 100 ms = 0.1 seconds

For Stop-and-Wait:
```
Efficiency = Transmission time / (Transmission time + RTT)
Efficiency = 0.001 / (0.001 + 0.1) = 0.001 / 0.101 ≈ 0.99%
```

This extremely low efficiency (less than 1%) demonstrates why Stop-and-Wait is impractical for most networks.

### Example 3: Go-Back-N Scenario

**Problem:** Using Go-Back-N with N=4, the sender transmits frames 0, 1, 2, 3. Frame 1 is lost. The receiver receives frames 2 and 3. What happens?

**Solution:**
1. Sender transmits frames 0, 1, 2, 3 (all before receiving ACK for frame 1)
2. Receiver receives frame 0 → sends ACK 1 (expecting frame 1)
3. Frame 1 is lost → receiver discards frames 2 and 3
4. Receiver receives frame 2 → sends ACK 1 (cumulative ACK, still expecting frame 1)
5. Receiver receives frame 3 → sends ACK 1 again
6. After timeout for frame 1, sender retransmits frames 1, 2, 3 (entire window)
7. This wastes bandwidth retransmitting successfully received frames

This example illustrates Go-Back-N's inefficiency when errors occur frequently.

## Exam Tips

1. **Know the Difference:** Clearly distinguish between flow control (receiver-centric) and congestion control (network-centric). This is a frequent exam question.

2. **UDP Header Memorization:** Remember the 8-byte UDP header structure: Source Port (2 bytes), Destination Port (2 bytes), Length (2 bytes), Checksum (2 bytes). There is NO window size field.

3. **TCP Window Field:** The TCP window size field is 16 bits, allowing values 0-65,535 bytes. Be aware of TCP Window Scaling for modern high-speed networks.

4. **Zero Window Handling:** Understand how TCP handles zero window advertisements through persist timer and window probes—this prevents deadlocks.

5. **Sliding Window Variants:** Remember that Go-Back-N retransmits all subsequent frames after a loss, while Selective Repeat retransmits only the lost frame. Know when each is appropriate.

6. **Application Layer Flow Control:** For exam purposes, remember that UDP provides no flow control; applications must implement their own if required.

7. **Effective Window Concept:** The actual amount of data TCP can send is limited by `min(rwnd, cwnd)`, where rwnd is receiver's advertised window and cwnd is the congestion window.

8. **Real-world Examples:** Be prepared to give examples—video streaming uses UDP with application-layer error handling, while file transfers use TCP for reliability.