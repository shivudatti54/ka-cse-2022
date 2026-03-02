# **Datagram Protocol and Transmission Control Protocol**

### Overview

- Datagram Protocol (UDP):
  - Connectionless protocol
  - No guarantee of delivery or order of packets
  - Suitable for applications with low latency and high packet loss tolerance
- Transmission Control Protocol (TCP):
  - Connection-oriented protocol
  - Ensures delivery and order of packets
  - Suitable for applications with guaranteed delivery and low packet loss

### Services

- **UDP Services:**
  - Best-effort delivery
  - No flow control or error control
- **TCP Services:**
  - Reliable delivery
  - Flow control
  - Error control
  - Sequence number and acknowledgement

### Features

- **UDP Features:**
  - Small header size
  - Fast transmission
- **TCP Features:**
  - Large header size
  - Slower transmission
  - Guaranteed delivery and sequence number

### Segmentation

- **Segment Size:** 536 bytes (max) or 68 bytes (min)
- **Segmentation Algorithm:**
  - Divide data into fixed-size segments
  - Add source and destination ports, sequence numbers, and checksums

### TCP Connections

- **Three-way Handshake:**
  1.  SYN (synchronize) packet sent from client to server
  2.  SYN-ACK (synchronize-acknowledgment) packet sent from server to client
  3.  ACK (acknowledgment) packet sent from client to server
- **Connection Establishment:**
  - Server confirms connection with ACK packet
  - Client sends data over established connection

### Flow Control

- **Window Size:** Maximum amount of data that can be sent without receiving an ACK
- **Flow Control Algorithm:**
  - Client sends data in small chunks (segments)
  - Server sends ACK or NACK (negative acknowledgement) packets

### Error Control

- **Checksum:** Calculates and verifies integrity of segments
- **Acknowledgement:** Client sends ACK packet to confirm receipt of segment
- **NACK:** Server sends NACK packet to request retransmission of segment

### Congestion Control

- **Slow Start:** Gradually increases window size to prevent overloading network
- **Congestion Avoidance:** Fights congestion by reducing window size or pausing transmission
- **Fast Retransmit:** Quickly retransmits lost segments to minimize delay
