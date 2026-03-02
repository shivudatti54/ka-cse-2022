# Module 4: TCP Connections

## Introduction

Transmission Control Protocol (TCP) is one of the core protocols of the Internet protocol suite (TCP/IP). It operates at the transport layer (Layer 4) and is renowned for providing reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating over an IP network. Fundamental to this reliability is the way TCP establishes, manages, and terminates connections between a client and a server. This process is crucial for virtually all web browsing, email, and file transfer activities.

## Core Concepts of TCP Connections

A TCP connection is a full-duplex, logical communication channel between two processes. Its life cycle can be broken down into three distinct phases: Connection Establishment, Data Transfer, and Connection Termination.

### 1. Connection Establishment: The Three-Way Handshake

Before any data can be exchanged, a connection must be established. TCP uses a three-step process called the **three-way handshake** to synchronize sequence numbers and negotiate parameters, ensuring both ends are ready for communication.

- **Step 1: SYN** - The client sends a TCP segment to the server with the `SYN` (Synchronize) flag set to `1`. This segment contains a random initial sequence number (e.g., `Seq = x`) from the client.
- **Step 2: SYN-ACK** - The server acknowledges the client's request by sending a segment back with both the `SYN` and `ACK` (Acknowledgment) flags set. It contains its own random initial sequence number (e.g., `Seq = y`) and sets the Acknowledgment number to `x + 1` (`Ack = x + 1`).
- **Step 3: ACK** - The client sends a final acknowledgment segment back to the server with the `ACK` flag set. The Acknowledgment number is set to `y + 1` (`Ack = y + 1`). At this point, the connection is established, and data transfer can begin.

**Why is this necessary?** This handshake prevents old or duplicate connection requests from being misinterpreted as new, valid requests, a problem known as "delayed duplicate" packets.

### 2. Data Transfer

Once the connection is established, the two hosts can exchange data. TCP breaks the application data into segments, each with a header containing sequence and acknowledgment numbers.

- **Sequence Number:** Identifies the order of the bytes sent in the segment, ensuring the receiver can reassemble them correctly, even if packets arrive out of order.
- **Acknowledgment Number:** Tells the sender the next sequence number the receiver expects to receive, confirming all prior bytes have been received correctly. This is the basis for TCP's reliability through **Positive Acknowledgment with Retransmission (PAR)**. If a sender does not receive an ACK for a packet within a timeout period, it assumes the packet was lost and retransmits it.
- **Flow Control:** TCP uses a sliding window mechanism for flow control. The receiver advertises a _window size_ in every ACK, telling the sender how much data it can accept. This prevents the sender from overwhelming the receiver's buffer.

### 3. Connection Termination: The Four-Way Handshake

TCP connections are symmetrical; both ends must independently close their half of the connection. This is typically done using a **four-way handshake**.

- **Step 1: FIN** - The client (or either host wishing to terminate) sends a segment with the `FIN` (Finish) flag set, indicating it has no more data to send.
- **Step 2: ACK** - The server acknowledges the `FIN` by sending an `ACK` back.
- **Step 3: FIN** - When the server is also ready to terminate, it sends its own `FIN` segment.
- **Step 4: ACK** - The client acknowledges the server's `FIN`, and after a waiting period (to allow for any delayed segments), the connection is fully closed.

A connection can also be aborted abruptly using a segment with the `RST` (Reset) flag.

## Key Points & Summary

| Feature           | Description                                                                                                            |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **Purpose**       | Provides reliable, connection-oriented, byte-stream communication between two endpoints.                               |
| **Establishment** | Uses a **Three-Way Handshake** (`SYN`, `SYN-ACK`, `ACK`) to synchronize sequence numbers and establish the connection. |
| **Reliability**   | Achieved through **Sequence Numbers**, **Acknowledgment Numbers**, and **Retransmission** of lost segments.            |
| **Flow Control**  | Implemented using a **Sliding Window** mechanism to prevent receiver overflow.                                         |
| **Termination**   | Uses a **Four-Way Handshake** (`FIN`, `ACK`, `FIN`, `ACK`) to gracefully close the connection from both ends.          |
| **State**         | The connection is **full-duplex**; data can flow in both directions simultaneously.                                    |

**In summary,** a TCP connection is a carefully managed conversation. The three-way handshake ensures a synchronized start, the data transfer phase guarantees reliable and orderly delivery with built-in flow control, and the four-way handshake ensures a clean and agreed-upon finish. Understanding this lifecycle is fundamental to grasping how reliable network applications are built.
