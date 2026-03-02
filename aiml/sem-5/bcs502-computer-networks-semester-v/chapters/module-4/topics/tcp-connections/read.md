# TCP Connections in Computer Networks

## Introduction

Transmission Control Protocol (TCP) is one of the core protocols of the Internet protocol suite (TCP/IP) and operates at the transport layer (Layer 4). It provides a reliable, connection-oriented, byte-stream service between applications running on hosts communicating over an IP network. The fundamental concept that enables this reliability is the **TCP Connection**. Before any data can be exchanged, a logical connection must be established between the two endpoints—a process often compared to making a telephone call.

## Core Concepts

### 1. The Three-Way Handshake: Connection Establishment

A TCP connection is established using a three-step process known as the **three-way handshake**. The primary goals are to synchronize sequence numbers (to keep track of data bytes) and exchange parameters (like Maximum Segment Size - MSS).

1.  **SYN (Synchronize):** The client sends a TCP segment to the server with the `SYN` flag set to 1. This segment contains a random initial sequence number (e.g., `seq = x`).
2.  **SYN-ACK (Synchronize-Acknowledge):** The server receives the SYN, allocates resources for the connection, and responds with its own segment. This segment has both the `SYN` and `ACK` flags set. It contains the server's random initial sequence number (e.g., `seq = y`) and an acknowledgment number set to `x + 1`.
3.  **ACK (Acknowledge):** The client receives the SYN-ACK, allocates its own resources, and sends a final acknowledgment segment back to the server with the `ACK` flag set. The acknowledgment number is set to `y + 1`. Data transfer can now begin.

This process ensures both sides agree on the initial sequence numbers and are ready to communicate.

**Example:**
*   **Client:** "I want to connect. My starting number is 1000 (SYN, seq=1000)."
*   **Server:** "Okay, I acknowledge your 1000 and am ready. My starting number is 5000 (SYN-ACK, ack=1001, seq=5000)."
*   **Client:** "Great, I acknowledge your 5000. Let's start talking (ACK, ack=5001)."

### 2. Data Transfer

Once the connection is established, data flows in full-duplex mode (both directions simultaneously). TCP uses several mechanisms to ensure reliable and ordered delivery:

*   **Sequencing:** Each byte of data is numbered. Segments carry the sequence number of their first data byte.
*   **Acknowledgements (ACKs):** The receiver sends ACK segments to inform the sender of the last *in-order* byte received. ACKs are cumulative (e.g., ACK 1501 means all bytes up to 1500 have been received).
*   **Flow Control:** Prevents a fast sender from overwhelming a slow receiver using a *sliding window* mechanism governed by the receiver's advertised window size (`rwnd`).
*   **Congestion Control:** Protects the network from congestion by dynamically adjusting the transmission rate using algorithms like Slow Start, Congestion Avoidance, and Fast Retransmit.

### 3. Connection Termination: The Four-Way Handshake

TCP connection termination uses a **four-step process** to gracefully close the connection, ensuring all data is delivered before closing.

1.  **FIN (Finish):** The client (or either host wishing to terminate) sends a segment with the `FIN` flag set, indicating it has no more data to send.
2.  **ACK:** The server acknowledges the FIN segment.
3.  **FIN:** After sending its own remaining data, the server sends its own FIN segment to the client.
4.  **ACK:** The client acknowledges the server's FIN. After a waiting period (to allow any stray segments to die out), both hosts release the allocated resources and the connection is fully closed.

This is often called a "four-way handshake." A simultaneous close scenario can combine steps, but the four-step process is the most common.

## Key Points / Summary

| Feature | Description |
| :--- | :--- |
| **Service Type** | Reliable, connection-oriented, byte-stream. |
| **Connection Establishment** | Uses a **Three-Way Handshake** (SYN, SYN-ACK, ACK). |
| **Purpose of Handshake** | To synchronize Sequence and Acknowledgment numbers and exchange parameters. |
| **Data Transfer** | Full-duplex. Uses sequencing, acknowledgments, flow control, and congestion control. |
| **Connection Termination** | Uses a **Four-Way Handshake** (FIN, ACK, FIN, ACK) for a graceful closure. |
| **Stateful Protocol** | Both endpoints maintain state information about the connection (sequence numbers, window size, etc.) in a Transmission Control Block (TCB). |
| **Socket Pair** | A connection is uniquely identified by a 4-tuple: **(Source IP, Source Port, Destination IP, Destination Port)**. |

Understanding TCP connections is fundamental for grasping how reliable network applications like web browsing (HTTP/HTTPS), email (SMTP), and file transfer (FTP) operate. The handshake and termination processes are critical for the reliable and orderly management of sessions between network devices.