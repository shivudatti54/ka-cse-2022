## Revision Notes: Transport Layer (Ch)

### Introduction

- The transport layer is the fourth layer of the OSI model and provides reliable data transfer between devices.
- It ensures error-free data transfer and provides congestion control.

### Transport-Layer Protocols: Introduction

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented, reliable, and error-checked data transfer.
  - Three-way handshake for establishing connections.
  - Segmentation and reassembly of data.
- **UDP (User Datagram Protocol)**:
  - Connectionless, best-effort delivery, and no error checking.
  - Little to no overhead for establishing connections.

### Key Concepts

- **Sockets**: Endpoints for communication between devices.
- **Port Numbers**: Unique identifiers for sockets (16,000 available).
- **Flow Control**: Mechanism to prevent network congestion.
- **Congestion Control**: Mechanism to prevent network congestion (e.g., TCP's slow-start algorithm).

### Important Formulas and Definitions

- **Packet Loss** (PL): The number of packets lost during transmission.
- **Packet Delay** (PD): The time it takes for a packet to travel from sender to receiver.
- **Throughput** (T): The rate at which data is transmitted.
- **Bandwidth** (B): The maximum amount of data that can be transmitted per unit time.
- **Jitter** (J): The variation in packet delay.

### Theorems

- **Store-and-Forward Theorem**: A packet is stored in a buffer at the sender's end until it is acknowledged by the receiver.
- **TCP's Slow-Start Algorithm**: A mechanism to prevent network congestion by reducing the amount of data transmitted during the initial phase of a connection.
