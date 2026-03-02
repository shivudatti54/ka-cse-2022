# **24.1-24.3.4: Introduction to the Transport Layer**

### Key Concepts

- **Definition**: The transport layer is the fourth layer of the OSI model and is responsible for reliable data transfer between devices.
- **Functions**:
  - Segmentation and reassembly of data
  - Flow control
  - Multiplexing and demultiplexing
- **Protocols**:
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)

### Important Formulas and Definitions

- **TCP Window Size**: `W = 2 \* SMT \* (1 + MTU/144)`, where `SMT = maximum segment size`
- **TCP Round-Trip Time (RTT)**: `RTT = 2 \* (time to transmit + time to receive)`
- **UDP Header**: `UDP header = 8 (source port) + 8 (destination port) + 12 (length) + 8 (check sum)`
- **TCP Connection Establishment**: `SYN -> SYN-ACK -> ACK`

### Important Theorems

- **TCP Congestion Control**: Thompson's algorithm (slow-start and congestion avoidance)
- **UDP Congestion Control**: No built-in congestion control mechanism

### Key Terms

- **Segment**: A unit of data containing a header and payload.
- **Reassembly**: The process of reassembling fragmented data.
- **Flow Control**: The mechanism of regulating the amount of data that can be sent in a single transmission.
- **Multiplexing**: The process of sending multiple signals over a single communication channel.

This summary should provide a concise revision guide for the key concepts, formulas, definitions, and theorems related to the transport layer.
