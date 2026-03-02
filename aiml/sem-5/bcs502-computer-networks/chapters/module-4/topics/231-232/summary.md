# 23.1- 23.2: Introduction to Transport Layer

=============================================

### Key Concepts

- **Transport Layer**: fourth layer of the OSI model, responsible for reliable data transfer between endpoints.
- **Connection-Oriented**: establishes a connection between sender and receiver before data transfer.
- **Connectionless**: does not establish a connection before data transfer.

### Transport-Layer Protocols

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented
  - Reliable data transfer
  - Segments data into smaller packets
  - Ensures error-free delivery
- **UDP (User Datagram Protocol)**:
  - Connectionless
  - Fast data transfer
  - No guarantee of delivery

### Key Formulas and Definitions

- **Packet Size**: maximum amount of data that can be sent in a single packet
- **Segment Size**: maximum amount of data that can be sent in a single segment
- **Window Size**: number of packets that can be sent without acknowledging receipt
- **Round-Trip Time (RTT)**: time taken for a packet to travel from sender to receiver and back
- **Throughput**: amount of data transferred per unit time

### Theorems

- **Piggybacking Theorem**: states that a sender can transmit multiple packets in a single transmission.
- **Sliding Window Theorem**: states that a sender can transmit multiple packets in a single transmission, with the receiver acknowledging receipt of each packet.

### Important Notes

- TCP is generally used for reliable data transfer, while UDP is used for fast data transfer.
- TCP and UDP have different approaches to error detection and correction.
- The transport layer provides a reliable means of data transfer between endpoints.
