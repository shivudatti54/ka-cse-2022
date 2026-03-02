# TCP Flow Control and Congestion Control

## Introduction

The Transmission Control Protocol (TCP) is a transport-layer protocol that provides reliable, connection-oriented communication between devices in a network. Two essential mechanisms in TCP are flow control and congestion control. Flow control ensures that a sender does not overwhelm a receiver with data, while congestion control prevents network congestion by regulating the amount of data sent.

## TCP Flow Control

Flow control is a mechanism that prevents a sender from sending data faster than the receiver can process it. TCP uses a sliding window protocol to implement flow control.

### Sliding Window Protocol

The sliding window protocol is a technique used by TCP to control the amount of data sent. The sender maintains a window of data that it can send, and the receiver maintains a window of data that it can receive. The sender sends data within its window, and the receiver sends acknowledgments (ACKs) for the data it receives.

### Window Size

The window size is the maximum amount of data that can be sent without receiving an ACK. The sender adjusts its window size based on the receiver's window size. If the receiver's window size is small, the sender reduces its window size to prevent overwhelming the receiver.

### Example

Suppose a sender has a window size of 1000 bytes, and the receiver has a window size of 500 bytes. The sender sends 1000 bytes of data, but the receiver can only process 500 bytes. The receiver sends an ACK for 500 bytes, and the sender reduces its window size to 500 bytes.

```
  +---------------+
  |  Sender  |
  +---------------+
           |
           |  1000 bytes
           v
  +---------------+
  |  Receiver  |
  +---------------+
           |
           |  ACK (500 bytes)
           v
  +---------------+
  |  Sender  |
  +---------------+
           |
           |  500 bytes
           v
```

## TCP Congestion Control

Congestion control is a mechanism that prevents network congestion by regulating the amount of data sent. TCP uses a combination of algorithms to implement congestion control.

### Slow Start Algorithm

The slow start algorithm is used to gradually increase the sender's window size. The sender starts with a small window size and increases it exponentially until it reaches a threshold.

### Congestion Avoidance Algorithm

The congestion avoidance algorithm is used to prevent network congestion. The sender maintains a congestion window (cwnd) that is adjusted based on the network conditions. If the network is congested, the sender reduces its cwnd.

### Fast Retransmit Algorithm

The fast retransmit algorithm is used to quickly retransmit lost packets. If the sender receives three duplicate ACKs, it assumes that a packet has been lost and retransmits it immediately.

### Fast Recovery Algorithm

The fast recovery algorithm is used to quickly recover from network congestion. If the sender detects congestion, it reduces its cwnd and enters a fast recovery phase.

### Example

Suppose a sender has a cwnd of 1000 bytes, and the network is congested. The sender reduces its cwnd to 500 bytes and enters a fast recovery phase.

```
  +---------------+
  |  Sender  |
  +---------------+
           |
           |  1000 bytes
           v
  +---------------+
  |  Network  |
  +---------------+
           |
           |  Congestion
           v
  +---------------+
  |  Sender  |
  +---------------+
           |
           |  500 bytes (fast recovery)
           v
```

## Comparison of Flow Control and Congestion Control

|             | Flow Control                               | Congestion Control                                                                           |
| ----------- | ------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Purpose     | Prevents sender from overwhelming receiver | Prevents network congestion                                                                  |
| Mechanism   | Sliding window protocol                    | Combination of algorithms (slow start, congestion avoidance, fast retransmit, fast recovery) |
| Window Size | Adjusted based on receiver's window size   | Adjusted based on network conditions                                                         |

## Exam Tips

- Understand the difference between flow control and congestion control.
- Know the algorithms used in TCP congestion control (slow start, congestion avoidance, fast retransmit, fast recovery).
- Be able to explain the sliding window protocol and how it is used in flow control.
- Practice drawing diagrams to illustrate the concepts.
