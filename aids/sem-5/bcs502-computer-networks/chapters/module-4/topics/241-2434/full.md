# 24.1-24.3.4: Transport Layer Fundamentals

=====================================================

## Introduction

---

The transport layer, also known as the transport protocol layer, is the fourth layer of the OSI model and the fourth layer of the TCP/IP model. It is responsible for providing reliable data transfer between devices on a network. In this section, we will delve into the fundamentals of the transport layer, including its introduction, protocols, and applications.

## Historical Context

---

The transport layer was first introduced in the 1970s as part of the OSI model. The first transport layer protocol was the Transmission Control Protocol (TCP), which was designed to provide reliable, connection-oriented data transfer. In the 1980s, the Internet Protocol (IP) was developed, which eliminated the need for explicit routing and introduced the concept of packet switching.

## Transport Layer Protocols

---

The transport layer uses several protocols to ensure reliable data transfer. The most commonly used protocols are:

### 1. Transmission Control Protocol (TCP)

TCP is a connection-oriented protocol that ensures reliable, error-checked, and sequential delivery of data between devices. It uses a three-way handshake to establish a connection, and four-way handshake to terminate the connection.

- **Connection Establishment:**
  - The client sends a SYN (synchronize) packet to the server, indicating its intention to establish a connection.
  - The server responds with a SYN-ACK (synchronize-acknowledgment) packet, acknowledging the client's request.
  - The client responds with an ACK (acknowledgment) packet, confirming the establishment of the connection.

- **Data Transfer:**
  - The client and server exchange data in blocks, using a sequence number to ensure sequential delivery.

- **Connection Termination:**
  - The client sends a FIN (finish) packet to the server, indicating its intention to terminate the connection.
  - The server responds with an ACK packet, acknowledging the client's request.
  - The client and server exchange a three-way handshake to terminate the connection.

### 2. User Datagram Protocol (UDP)

UDP is a connectionless protocol that provides best-effort delivery of data between devices. It does not guarantee the delivery of data and does not provide error checking or retransmission.

- **Data Transfer:**
  - The client and server exchange data in packets, without establishing a connection.
  - The server may discard packets that are out of order or contain errors.

### 3. Stream Control Transmission Protocol (SCTP)

SCTP is a connection-oriented protocol that provides reliable, error-checked, and sequential delivery of data between devices. It supports multiple streams and can handle multiple simultaneous connections.

- **Connection Establishment:**
  - The client and server establish a connection using a two-way handshake.
  - The client and server exchange data in streams, using a sequence number to ensure sequential delivery.

- **Data Transfer:**
  - The client and server exchange data in streams, using a sequence number to ensure sequential delivery.

- **Connection Termination:**
  - The client sends a FIN packet to the server, indicating its intention to terminate the connection.
  - The server responds with an ACK packet, acknowledging the client's request.

## Transport Layer Applications

---

The transport layer has several applications, including:

- **File Transfer:** FTP (File Transfer Protocol) uses the transport layer to transfer files between devices.
- **Email:** SMTP (Simple Mail Transfer Protocol) uses the transport layer to transfer email messages between devices.
- **Telnet:** Telnet uses the transport layer to establish a connection between devices for remote access.

## Transport Layer Protocols in Action

---

### Example 1: TCP Connection Establishment

| Device | Action               | Packet Type | Sequence Number |
| ------ | -------------------- | ----------- | --------------- |
| Client | Establish connection | SYN         | 0               |
| Server | Acknowledge request  | SYN-ACK     | 123             |
| Client | Confirm connection   | ACK         | 123             |

### Example 2: UDP Data Transfer

| Device | Action               | Packet Type | Sequence Number |
| ------ | -------------------- | ----------- | --------------- |
| Client | Send data            | UDP         | 0               |
| Server | Receive data         | UDP         | 0               |
| Server | Discard out-of-order | UDP         | 0               |

### Example 3: SCTP Connection Establishment

| Device | Action               | Packet Type | Sequence Number |
| ------ | -------------------- | ----------- | --------------- |
| Client | Establish connection | INIT        | 0               |
| Server | Acknowledge request  | INIT-ACK    | 123             |
| Client | Confirm connection   | COOKIE-ACK  | 456             |
| Server | Confirm connection   | COOKIE-ACK  | 789             |

## Diagrams and Descriptions

---

### TCP Connection Establishment Diagram

```
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
           |                         |
           |  SYN                    |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Server      |       |  Client      |
  +-----------------+       +-----------------+
           |                         |
           |  SYN-ACK               |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
           |                         |
           |  ACK                   |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
```

### UDP Data Transfer Diagram

```
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
           |                         |
           |  UDP                    |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Server      |       |  Client      |
  +-----------------+       +-----------------+
           |                         |
           |  UDP                    |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Server      |       |  Client      |
  +-----------------+       +-----------------+
```

### SCTP Connection Establishment Diagram

```
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
           |                         |
           |  INIT                   |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Server      |       |  Client      |
  +-----------------+       +-----------------+
           |                         |
           |  INIT-ACK               |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
           |                         |
           |  COOKIE-ACK            |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Server      |       |  Client      |
  +-----------------+       +-----------------+
           |                         |
           |  COOKIE-ACK            |
           |                         |
           v                         v
  +-----------------+       +-----------------+
  |  Client      |       |  Server      |
  +-----------------+       +-----------------+
```

## Further Reading

---

- "Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall
- "Transport Layer Protocols" by Keith D. Cooper and Jerrold R. Schroeder
- "TCP/IP Illustrated" by William C. Y. Wang and Jeffrey D. Case

Note: The examples and diagrams provided are for illustrative purposes only and may not be representative of real-world scenarios.
