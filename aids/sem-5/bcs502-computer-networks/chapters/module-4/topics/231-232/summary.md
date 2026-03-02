# **Revisions Notes for 23.1-23.2: Introduction to Transport Layer**

### Overview

- The Transport Layer is the fourth layer of the OSI model, responsible for reliable data transfer between devices.
- It ensures error-free, sequential delivery of data between endpoints.

### Key Concepts

- **Transport-Layer Protocols**:
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)
- **Transport Layer Functions**:
  - Segmentation and reassembly of data
  - Error detection and correction
  - Flow control and congestion avoidance
- **Transport Layer Services**:
  - Connection establishment and termination
  - Reliable data transfer

### Important Formulas and Definitions

- **TCP Header**:
  - Source Port (16 bits)
  - Destination Port (16 bits)
  - Sequence Number (32 bits)
  - Acknowledgment Number (32 bits)
  - Data (varies)
- **UDP Header**:
  - Source Port (16 bits)
  - Destination Port (16 bits)
  - Length (16 bits)
  - Checksum (16 bits)
- **Connection Establishment**:
  - Handshake sequence: SYN, SYN-ACK, ACK
- **Flow Control**:
  - Maximum Segment Size (MSS)
  - Window Size

### Theorems

- **TCP Retransmission**:
  - If a segment is lost or corrupted, the receiver sends a duplicate ACK
  - If no duplicate ACK is received, the sender retransmits the segment
- **UDP Acknowledgment**:
  - No acknowledgment is sent for lost or corrupted packets

### Key Points

- Transport Layer protocols ensure reliable data transfer
- TCP provides connection-oriented, error-checked, and sequential delivery
- UDP provides connectionless, best-effort delivery
- Transport Layer functions ensure error-free data transfer
- Transport Layer services establish and terminate connections.
