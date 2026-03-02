# Module 4: TCP Connections

**Subject:** Computer Networks
**Semester:** V

## 1. Introduction

Transmission Control Protocol (TCP) is one of the core protocols of the Internet protocol suite (TCP/IP) and operates at the transport layer (Layer 4). It is a connection-oriented, reliable, and byte-stream-based protocol. Before any data can be exchanged between two applications using TCP, a formal connection must be established. This process, along with its termination, is fundamental to ensuring the reliable data transfer that underpins most internet applications, from web browsing to email.

## 2. Core Concepts

A TCP connection is a logical pathway established between two endpoints, uniquely identified by a combination of an IP address and a port number for each end (a socket pair). The lifecycle of a TCP connection consists of three distinct phases:

### 2.1. Connection Establishment: The Three-Way Handshake

TCP uses a three-way handshake to establish a reliable connection. This process synchronizes sequence numbers and exchanges control information to prepare both sides for data transfer.

1.  **SYN (Synchronize):** The client initiates the connection by sending a TCP segment with the `SYN` flag set to 1. This segment includes a client-specific initial sequence number (e.g., `seq = x`).
2.  **SYN-ACK (Synchronize-Acknowledge):** The server receives the `SYN` segment. If it is willing to accept the connection, it responds with a segment that has both the `SYN` and `ACK` flags set. It acknowledges the client's sequence number (`ack = x + 1`) and sends its own initial sequence number (`seq = y`).
3.  **ACK (Acknowledge):** The client receives the `SYN-ACK` and sends back a final acknowledgment segment with the `ACK` flag set. It acknowledges the server's sequence number (`ack = y + 1`). At this point, the connection is established, and data transfer can begin.

**Example:** Imagine a phone call. You dial the number (SYN), the person on the other end answers and says "Hello?" (SYN-ACK), and you respond with "Hi, it's me!" (ACK). The conversation (data transfer) can now start.

### 2.2. Data Transfer

Once the connection is established, full-duplex data transfer can occur. TCP provides reliability through:
*   **Sequence Numbers:** Each byte of data is numbered.
*   **Acknowledgements (ACKs):** The receiver sends ACK segments to confirm successful receipt of data. An ACK number signifies that all data up to that sequence number has been received.
*   **Retransmission:** If the sender does not receive an ACK within a timeout period, it assumes the data was lost and retransmits it.
*   **Flow Control:** Using a sliding window mechanism, TCP ensures the sender does not overwhelm the receiver by sending data faster than it can process.
*   **Congestion Control:** TCP dynamically adjusts its transmission rate to avoid overloading the network.

### 2.3. Connection Termination: The Four-Way Handshake

TCP connection termination is a four-step process, often called a four-way handshake. This allows each side to terminate its send stream independently.

1.  **FIN (Finish):** When a client has no more data to send, it sends a segment with the `FIN` flag set (e.g., `seq = u`).
2.  **ACK:** The server receives the `FIN` and acknowledges it by sending an `ACK` (`ack = u + 1`). At this point, the connection is half-closed; the client cannot send more data, but the server can still send.
3.  **FIN:** Once the server is also ready to terminate, it sends its own `FIN` segment (e.g., `seq = w`).
4.  **ACK:** The client receives the `FIN` and sends a final `ACK` (`ack = w + 1`). After a waiting period (to allow any stray segments to die off), the connection is fully closed and resources are freed.

## 3. TCP Connection States

Throughout this lifecycle, both endpoints transition through a series of well-defined states (e.g., `LISTEN`, `SYN_SENT`, `SYN_RCVD`, `ESTABLISHED`, `FIN_WAIT_1`, `CLOSE_WAIT`, `LAST_ACK`, `TIME_WAIT`). These states are crucial for network administrators to diagnose connection issues using tools like `netstat`.

## 4. Key Points & Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Protocol** | Connection-oriented, reliable, byte-stream transport protocol. |
| **Handshake** | **Establishment:** Three-way handshake (SYN, SYN-ACK, ACK).<br>**Termination:** Four-way handshake (FIN, ACK, FIN, ACK). |
| **Identifiers** | A connection is uniquely identified by a socket pair: (Source IP, Source Port, Destination IP, Destination Port). |
| **Reliability** | Achieved through sequence numbers, acknowledgments, retransmissions, and checksums. |
| **Control Mechanisms** | Employs **flow control** (sliding window) and **congestion control** to manage data flow. |
| **State** | Each endpoint maintains a state machine (e.g., ESTABLISHED, TIME_WAIT) to manage the connection. |

**In summary,** the TCP connection setup and teardown processes are fundamental to providing a reliable communication channel. The three-way and four-way handshakes ensure that both parties are synchronized and agree on the state of the connection before any data is exchanged and before the connection is finally closed. Understanding these mechanisms is essential for debugging network applications and appreciating how reliable data transfer is achieved on the internet.