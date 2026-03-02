# **Revision Notes: 23.1-23.2 - Computer Networks**

### Introduction

- The transport layer is the fourth layer of the OSI model.
- It provides reliable data transfer between devices.
- The transport layer provides end-to-end error-free delivery of data.

### Transport-Layer Protocols

- **TCP (Transmission Control Protocol)**
  - Connection-oriented
  - Segmentation and reassembly of data
  - Error-checked and corrected
  - Flow control and congestion control
- **UDP (User Datagram Protocol)**
  - Connectionless
  - Best effort delivery
  - No error-checking or correction

### Key Concepts

- **Segment**: The basic unit of data in TCP.
- **Sequence Number**: Used to identify the order of segments.
- **Acknowledge Number**: Used to acknowledge receipt of segments.
- **Window**: The amount of data that can be sent at one time.
- **Flow Control**: Prevents network congestion by limiting the amount of data sent.
- **Congestion Control**: Prevents network congestion by regulating the amount of data sent.

### Important Formulas

- **TCP Header**: `TCP Header = Source Port + Destination Port + Sequence Number + Acknowledgment Number + Data`
- **TCP Window**: `TCP Window = Maximum Segment Size (MSS) x Window Size`

### Definitions

- **Reliable Data Transfer**: Ensures that data is delivered correctly and in the correct order.
- **Error-Free Delivery**: Ensures that data is delivered without errors.

### Theorems

- **TCP Three-Way Handshake**: Establishes a connection between two devices.
  - `SYN` (Synchronize) packet sent by the client
  - `SYN-ACK` (Synchronize-Acknowledgment) packet sent by the server
  - `ACK` (Acknowledgment) packet sent by the client
