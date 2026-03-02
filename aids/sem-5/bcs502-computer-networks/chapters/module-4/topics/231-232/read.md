# **23.1- 23.2: Introduction to Transport Layer**

### 23.1 Introduction to Transport Layer

#### Definition

The Transport Layer is the fourth layer of the OSI model and is responsible for reliable data transfer between devices on a network. It ensures that data is delivered in the correct order and that errors are detected and corrected.

#### Functions

- Provides reliable data transfer between devices
- Ensures data is delivered in the correct order
- Detects and corrects errors in data transmission
- Provides flow control and congestion control
- Ensures multiplexing and demultiplexing of data

#### Key Concepts

- **Reliability**: The ability of the transport layer to ensure that data is delivered correctly and in the correct order.
- **Error Detection**: The process of detecting errors in data transmission.
- **Error Correction**: The process of correcting errors that are detected in data transmission.
- **Flow Control**: The process of controlling the amount of data that is sent at any given time.
- **Congestion Control**: The process of preventing network congestion by controlling the amount of data that is sent.

### 23.2 Transport-Layer Protocols

#### Introduction

Transport-layer protocols are used to establish, maintain, and terminate connections between devices on a network. They provide reliable data transfer and ensure that data is delivered in the correct order.

#### Types of Transport-Layer Protocols

- **Connection-Oriented Protocols**: These protocols establish a connection between the sender and receiver before data is sent. Examples include TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- **Connectionless Protocols**: These protocols do not establish a connection before data is sent. Examples include ICMP (Internet Control Message Protocol) and IGMP (Internet Group Management Protocol).

#### Key Transport-Layer Protocols

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented protocol
  - Ensures reliable data transfer
  - Provides flow control and congestion control
- **UDP (User Datagram Protocol)**:
  - Connectionless protocol
  - Provides best-effort delivery
  - Used for applications that require low latency
- **SCTP (Stream Control Transmission Protocol)**:
  - Connection-oriented protocol
  - Provides reliable data transfer
  - Used for applications that require multiple streams of data

#### Key Features of Transport-Layer Protocols

- **Segmentation and Reassembly**: The process of dividing data into small segments and reassembling them at the receiving end.
- **Acknowledgments and Retransmissions**: The process of sending acknowledgments and retransmitting data that is lost or corrupted during transmission.
- **Flow Control**: The process of controlling the amount of data that is sent at any given time.
- **Congestion Control**: The process of preventing network congestion by controlling the amount of data that is sent.
