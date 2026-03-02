## Revision Notes: Introduction to Transport Layer

### Introduction to Transport Layer

- The Transport Layer is the fourth layer of the OSI model and responsible for ensuring reliable data transfer between devices.
- Its primary functions are:
  - Segmentation and reassembly of data
  - Flow control to prevent network congestion
  - Error detection and correction
- Key Transport Layer Protocols:
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)

### Transport-Layer Protocols: Introduction

- **TCP (Transmission Control Protocol)**
  - Connection-oriented protocol
  - Guarantees reliable data transfer
  - Uses ACKs to confirm data receipt
  - Three-way handshake for establishing connection
- **UDP (User Datagram Protocol)**
  - Connectionless protocol
  - Provides best-effort delivery
  - No ACKs or error correction mechanisms

### Important Formulas:

- **TCP Packet Structure**:
  - Source Port (16 bits)
  - Destination Port (16 bits)
  - Sequence Number (32 bits)
  - Acknowledgment Number (32 bits)
- **TCP Header Size**:
  - 20 bytes for TCP Segment
  - 8 bytes for TCP Header

### Important Definitions:

- **Segment**: The basic unit of data transmission in TCP.
- **Stream**: A continuous sequence of data packets in a connectionless protocol.
- **Window**: The amount of data a device is willing to receive from the other end.

### Important Theorems:

- **TCP Sliding Window Protocol**: Ensures reliable data transfer and flow control by adjusting the window size based on the amount of data available.
- **TCP Congestion Control Algorithm**: Prevents network congestion by reducing the window size in response to high packet loss rates.
