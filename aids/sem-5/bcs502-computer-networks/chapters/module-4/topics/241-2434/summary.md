# **24.1-24.3.4: Introduction to Transport Layer**

### Introduction

- **Definition:** The Transport Layer is the fourth layer of the OSI model, responsible for reliable data transfer between devices.
- **Functions:**
  - Provides reliable data transfer
  - Ensures error-free data transfer
  - Provides flow control and congestion avoidance

### Transport-Layer Protocols

- **TCP (Transmission Control Protocol)**
  - Connection-oriented protocol
  - Ensures reliable data transfer
  - Provides sequence numbers for reassembly of packets
  - Formula: `R = 2 * (C + H) + P`
  - Theorem: TCP guarantees delivery of packets within a certain time frame (RTT)
- **UDP (User Datagram Protocol)**
  - Connectionless protocol
  - Faster than TCP but less reliable
  - Formula: None
  - Theorem: UDP does not guarantee delivery of packets

### Key Concepts

- **Segmentation:** Breaking down data into smaller packets
- **Reassembly:** Reassembling packets at the receiving end
- **Flow Control:** Regulating the amount of data sent
- **Congestion Avoidance:** Preventing network congestion

### Important Formulas and Definitions

- **RTT (Round-Trip Time):** The time it takes for a packet to travel from the sender to the receiver and back.
- **C (Congestion Window):** The maximum amount of data that can be sent before the sender slows down.
- **H (Header Size):** The size of the TCP header.
- **P (Packet Loss):** The number of packets lost during transmission.
