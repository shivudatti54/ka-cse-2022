# **Revision Notes: 24.3.6-24.3.9 - Transport Layer**

### Introduction

- **Transport Layer**: highest layer in OSI model, responsible for reliable data transfer
- **Transport-Layer Protocols**: protocols that operate on transport layer, ensuring reliable data transfer

### 24.3.6: Synchronous Connection-Oriented (SCO) and Asynchronous Connection-Less (ACL) Protocols

- **SCO Protocol**:
  - connection-oriented, synchronous
  - ensures reliable data transfer
  - uses CS-protocol for error detection and correction
- **ACL Protocol**:
  - connectionless, asynchronous
  - does not guarantee delivery order or error detection

### 24.3.7: Transmission Control Protocol (TCP)

- **TCP**:
  - connection-oriented, synchronous
  - ensures reliable, error-checked, and error-recovered data transfer
  - uses ACK-ACK protocol for error detection and correction
- **Key Parameters**:
  - Segment size (S)
  - Maximum segment size (MSS)
  - Window size (W)
  - Checksum (C)
  - Sequence number (Seq)

### 24.3.8: User Datagram Protocol (UDP)

- **UDP**:
  - connectionless, asynchronous
  - does not guarantee delivery order or error detection
  - uses checksum (C) for error detection
- **Key Parameters**:
  - Maximum UDP datagram size (M)
  - Checksum (C)

### 24.3.9: Congestion Control

- **Congestion Control**: prevents network congestion by controlling the amount of data sent
- **Key Theorems**:
  - Kelly's Theorem: states that the optimal rate of transmission is the minimum rate that satisfies the congestion constraint
  - Yeh's Theorem: states that the optimal rate of transmission is the minimum rate that satisfies the bandwidth-delay product constraint
