# Congestion Control in Computer Networks


## Table of Contents

- [Congestion Control in Computer Networks](#congestion-control-in-computer-networks)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Causes of Network Congestion](#causes-of-network-congestion)
  - [Effects of Congestion](#effects-of-congestion)
  - [Congestion Control vs. Flow Control](#congestion-control-vs-flow-control)
  - [Congestion Control Algorithms](#congestion-control-algorithms)
  - [TCP Congestion Control Mechanisms](#tcp-congestion-control-mechanisms)
  - [Explicit Congestion Notification (ECN)](#explicit-congestion-notification-ecn)
- [Examples](#examples)
  - [Example 1: Token Bucket Calculation](#example-1-token-bucket-calculation)
  - [Example 2: TCP Slow Start Analysis](#example-2-tcp-slow-start-analysis)
  - [Example 3: Leaky Bucket for Traffic Shaping](#example-3-leaky-bucket-for-traffic-shaping)
- [Exam Tips](#exam-tips)

## Introduction

Congestion control is one of the most critical aspects of computer networking, particularly in the context of the Internet and modern communication systems. When multiple users or applications share limited network resources such as bandwidth, router buffers, and processing capacity, the aggregate demand can exceed the available capacity, leading to a state known as network congestion. This phenomenon manifests as increased packet delays, packet losses, and reduced throughput, ultimately degrading the quality of service experienced by end-users.

In the early days of computer networking, the primary focus was on providing reliable data delivery between communicating hosts. However, as networks grew in scale and complexity, the issue of congestion became increasingly prominent. The seminal work by Van Jacobson and Michael Karels in 1988 laid the foundation for modern congestion control mechanisms, demonstrating that network collapse could occur if congestion was left unchecked. Today, congestion control is embedded in the Transmission Control Protocol (TCP) and is essential for maintaining network stability and fair resource allocation.

For CSE students studying Computer Networks, understanding congestion control is fundamental to comprehending how the Internet maintains reliability and efficiency. This topic covers the causes and effects of congestion, various congestion control algorithms, and the mechanisms employed by TCP to prevent and respond to network overload conditions.

## Key Concepts

### Causes of Network Congestion

Network congestion occurs due to multiple interrelated factors. The primary causes include:

1. **Insufficient Bandwidth**: When the total traffic demand exceeds the available link capacity, packets must wait in queues, leading to increased latency and potential buffer overflow.

2. **Router Buffer Overflow**: Routers maintain queues to handle burst traffic. When these queues become full, incoming packets are dropped. While packet drops are necessary for congestion signaling, excessive drops degrade performance.

3. **Slow Processing in Intermediate Nodes**: If routers cannot process and forward packets quickly enough due to limited CPU resources or inefficient routing algorithms, queues build up.

4. **Improper TCP Window Size**: A too-large sender window can overwhelm the network, while a too-small window underutilizes available bandwidth.

5. **Synchronized Packet Drops**: When multiple connections experience similar congestion and simultaneously reduce their sending rates, network utilization can drop dramatically, a phenomenon known as congestion collapse.

### Effects of Congestion

The consequences of network congestion are multifaceted:

- **Increased Round-Trip Time (RTT)**: Packets spend more time waiting in queues, extending end-to-end delay.
- **Packet Loss**: Buffer overflow results in packet drops, requiring retransmissions that further burden the network.
- **Throughput Degradation**: Effective throughput decreases as more resources are consumed by retransmissions and overhead.
- **Jitter**: Variable queuing delays cause inconsistent packet delivery times, affecting real-time applications.
- **Network Instability**: Uncontrolled congestion can lead to oscillatory behavior and potential network collapse.

### Congestion Control vs. Flow Control

It is essential to distinguish between congestion control and flow control, as students often confuse these related but distinct concepts:

- **Flow Control**: A mechanism to prevent the sender from overwhelming the receiver. It operates end-to-end, ensuring the receiver can keep up with the transmitted data (e.g., TCP's receive window mechanism).

- **Congestion Control**: A mechanism to prevent the sender from overwhelming the network. It operates across the entire path, ensuring the network can handle the transmitted data. Congestion control is more complex as it must deal with distributed information across multiple network elements.

### Congestion Control Algorithms

#### 1. Leaky Bucket Algorithm

The Leaky Bucket algorithm is a traffic shaping mechanism that controls the rate at which packets are admitted into the network. It conceptualizes a bucket with a hole at the bottom where water (packets) leaks at a constant rate, regardless of the input rate.

**Working Principle**:

- Packets arrive at the bucket and are stored temporarily
- The bucket has a finite capacity (buffer size)
- Packets leak out at a fixed rate (output rate)
- If the bucket is full, incoming packets are discarded

This algorithm transforms bursty traffic into smooth, constant-rate traffic, preventing sudden surges that can cause congestion. The Leaky Bucket is particularly useful for traffic policing and shaping in ATM networks and quality of service implementations.

#### 2. Token Bucket Algorithm

The Token Bucket is a more flexible variation that allows for bursty traffic while enforcing an average rate limit. The algorithm uses tokens, which are generated at a constant rate and required for transmitting packets.

**Working Principle**:

- Tokens are added to the bucket at a constant rate (ρ)
- The bucket has a maximum capacity (β)
- To transmit a packet of size n, n tokens must be removed from the bucket
- If insufficient tokens are available, the packet must wait

The Token Bucket permits short bursts of traffic when tokens are available while ensuring long-term compliance with the average rate. This makes it ideal for implementing quality of service guarantees in modern networks.

### TCP Congestion Control Mechanisms

TCP employs several sophisticated mechanisms to control congestion:

#### 1. Slow Start

When a TCP connection begins, the sender has no knowledge of the network capacity. Slow start addresses this by initially sending a small number of packets (typically one Maximum Segment Size) and exponentially increasing the sending rate until packet loss occurs.

- **Initial Congestion Window (cwnd)**: Typically set to 1 MSS (Maximum Segment Size)
- **Threshold (ssthresh)**: The value at which slow start ends and congestion avoidance begins
- **Behavior**: cwnd doubles every RTT by acknowledging each packet

#### 2. Congestion Avoidance

Once cwnd reaches the slow start threshold, TCP enters congestion avoidance mode. Here, cwnd increases linearly (typically by 1/cwnd per acknowledgment) to probe for additional available bandwidth without causing congestion.

#### 3. Fast Retransmit

When multiple duplicate acknowledgments are received (indicating a packet loss but continued data flow), TCP performs fast retransmit—retransmitting the missing segment without waiting for a timeout. This reduces the delay associated with loss detection.

#### 4. Fast Recovery

After fast retransmit, TCP enters fast recovery where it temporarily reduces cwnd (typically to half) and continues sending new packets until duplicate ACKs stop. This allows the connection to quickly resume normal operation after a single packet loss.

#### 5. TCP Reno and TCP Tahoe

- **TCP Tahoe**: Implements slow start, congestion avoidance, and fast retransmit. On loss detection, cwnd is reset to 1 MSS.
- **TCP Reno**: Adds fast recovery to Tahoe. On packet loss, cwnd is halved (multiplicative decrease), allowing faster recovery.

### Explicit Congestion Notification (ECN)

ECN is an extension to TCP that allows routers to explicitly signal congestion without dropping packets. When ECN is enabled:

- Routers mark packets with ECN bits when approaching congestion
- Receivers echo these marks back to senders
- Senders reduce their transmission rate proactively

ECN is particularly beneficial for real-time applications where packet loss is highly undesirable.

## Examples

### Example 1: Token Bucket Calculation

**Problem**: A Token Bucket has a token rate of 2 tokens per second and a bucket capacity of 10 tokens. If a burst of 8 packets arrives when the bucket is full, how many packets can be transmitted immediately, and what is the waiting time for the remaining packets?

**Solution**:

Given:

- Token rate (ρ) = 2 tokens/second
- Bucket capacity (β) = 10 tokens
- Burst size = 8 packets

Step 1: Since the bucket is full, it already contains 10 tokens.
Step 2: To transmit 8 packets, we need 8 tokens.
Step 3: After transmitting 8 packets, tokens remaining = 10 - 8 = 2 tokens.
Step 4: The sender can transmit 8 packets immediately (no waiting).
Step 5: For subsequent packets, tokens accumulate at 2 tokens/second.

If more packets arrive, the waiting time depends on token accumulation. For example, to send 1 more packet after the burst, the sender must wait until at least 1 token accumulates, which takes 0.5 seconds.

### Example 2: TCP Slow Start Analysis

**Problem**: A TCP connection starts with cwnd = 1 MSS and ssthresh = 16 MSS. Calculate the cwnd values over successive RTTs until congestion avoidance begins.

**Solution**:

Given:

- Initial cwnd = 1 MSS
- ssthresh = 16 MSS

RTT 1: cwnd = 1 MSS (send 1 segment, receive 1 ACK)
After ACK: cwnd = 1 + 1 = 2 MSS

RTT 2: cwnd = 2 MSS (send 2 segments, receive 2 ACKs)
After ACKs: cwnd = 2 + 2 = 4 MSS

RTT 3: cwnd = 4 MSS (send 4 segments, receive 4 ACKs)
After ACKs: cwnd = 4 + 4 = 8 MSS

RTT 4: cwnd = 8 MSS (send 8 segments, receive 8 ACKs)
After ACKs: cwnd = 8 + 8 = 16 MSS

At RTT 5, cwnd = 16 MSS equals ssthresh, so TCP transitions from slow start to congestion avoidance. In congestion avoidance, cwnd increases linearly (add 1 MSS per RTT instead of doubling).

### Example 3: Leaky Bucket for Traffic Shaping

**Problem**: A Leaky Bucket outputs at 1 Mbps and has a buffer capacity of 50 packets. If packets of 1000 bytes arrive at 4 Mbps for 20 milliseconds, determine whether packet loss occurs.

**Solution**:

Given:

- Output rate = 1 Mbps = 125,000 bytes/second
- Input rate = 4 Mbps = 500,000 bytes/second
- Burst duration = 20 ms = 0.02 seconds
- Buffer capacity = 50 packets = 50,000 bytes (assuming 1000 bytes/packet)

Step 1: Calculate bytes arriving during burst:
Bytes arriving = 500,000 × 0.02 = 10,000 bytes (10 packets)

Step 2: Calculate bytes transmitted during burst:
Bytes transmitted = 125,000 × 0.02 = 2,500 bytes

Step 3: Calculate buffer occupancy after burst:
Buffer used = 10,000 - 2,500 = 7,500 bytes = 7.5 packets

Since 7.5 packets < 50 packets (buffer capacity), no packet loss occurs. The bucket can accommodate this burst without dropping packets.

## Exam Tips

1. **Understand the Difference**: Clearly distinguish between congestion control (network-wide) and flow control (end-to-end). This is a common exam question.

2. **Algorithm Characteristics**: Remember that Leaky Bucket provides constant output rate (traffic shaping), while Token Bucket allows burstiness with average rate control.

3. **TCP Phases**: Know the TCP congestion control phases—slow start (exponential growth), congestion avoidance (linear growth), and their transition point (ssthresh).

4. **ECN Advantage**: For ECN questions, remember it allows congestion handling without packet loss, benefiting real-time applications.

5. **Formulas**: Know key formulas—Token Bucket burst size = bucket capacity + (token rate × maximum packet delay).

6. **Queueing Concepts**: Understand the relationship between queue length, packet arrival rate, and service rate in congestion scenarios.

7. **Visualize Dynamics**: Be able to draw and interpret graphs showing cwnd evolution during slow start and congestion avoidance phases.

8. **Real-world Applications**: Connect concepts to practical scenarios like video streaming, VoIP, and web browsing to demonstrate understanding.
