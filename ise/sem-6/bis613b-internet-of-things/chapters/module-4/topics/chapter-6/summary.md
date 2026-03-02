## Chapter 6 Revision Notes: IoT Application Transport Methods

### Introduction

- IoT Application Transport Methods refer to the protocols used to transmit data between devices in the Internet of Things (IoT) network.
- This chapter focuses on the Transport Layer protocols used in IoT applications.

### Transport Layer Protocols

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented protocol
  - Ensures reliable data transfer
  - Uses sequence numbers and acknowledgments
  - Formula: `Rtt = (S + D) / B`
- **UDP (User Datagram Protocol)**:
  - Connectionless protocol
  - Faster than TCP, but may not guarantee delivery
  - Formula: `Rtt = (D + S) / B`

### Application Transport Methods

- **CoAP (Constrained Application Protocol)**:
  - Designed for constrained networks and devices
  - Similar to HTTP, but with a smaller overhead
- **MQTT (Message Queue Telemetry Transport)**:
  - Popular protocol for IoT devices
  - Uses a publish-subscribe model for message exchange

### Key Concepts

- **Segmentation and Reassembly**: breaking down data into smaller segments for transmission
- **Flow Control**: regulating the amount of data transmitted at one time
- **Windowing**: using a sliding window to control the amount of data transmitted

### Theorems and Definitions

- **Theorem: TCP three-way handshake**: three packets are exchanged to establish a connection
- **Definition: Handshake sequence**: a series of packets that establish a connection
- **Definition: Acknowledgment packet**: a packet sent by the receiver to acknowledge received data

### Important Formulas

- `Rtt = (S + D) / B` (TCP round-trip time formula)
- `Rtt = (D + S) / B` (UDP round-trip time formula)

### Key Terms

- ** LAT (Latency)**: the delay between sending and receiving data
- **Jitter**: the variation in latency
- **Bandwidth**: the maximum amount of data that can be transmitted per unit time
