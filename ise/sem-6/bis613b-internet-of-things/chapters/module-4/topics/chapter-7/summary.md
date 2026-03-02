### Chapter-7] Internet of Things - Application Transport Methods

#### Overview

This chapter focuses on application transport methods for the Internet of Things (IoT). It explores the transport layer protocols and their applications in IoT.

#### Key Points

- **Transport Layer Protocols:**
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)
  - SCTP (Stream Control Transmission Protocol)
  - DCCP (Datagram Congestion Control Protocol)
- **IoT-Specific Transport Protocols:**
  - CoAP (Constrained Application Protocol)
  - LWM2M (Lightweight Machine-to-Machine)
  - MQTT (Message Queuing Telemetry Transport)
- **Advantages and Disadvantages:**
  - TCP: reliable, but slow and complex
  - UDP: fast, but unreliable and best-effort delivery
  - SCTP: multi-homing and multipath support
  - DCCP: congestion control and header compression
- **Application Transport Methods:**
  - **CoAP:** constrained application protocol for constrained networks and devices
  - **LWM2M:** lightweight machine-to-machine protocol for IoT devices
  - **MQTT:** lightweight messaging protocol for constrained networks

#### Important Formulas and Definitions

- **TCP Header:** 20 bytes (sequence number, acknowledgment number, etc.)
- **UDP Header:** 8 bytes (source port, destination port, etc.)
- **SCTP Header:** 20 bytes (association identifier, etc.)
- **DCCP Header:** 20 bytes (connection identifier, etc.)

#### Theorems and Concepts

- **TCP Three-Way Handshake:** Establishes a connection between two devices
- **UDP Connectionless:** Does not establish a connection before transmitting data
- **SCTP Multipath Support:** Allows multiple paths between devices
- **DCCP Header Compression:** Reduces transmission overhead

#### Quick Revision Tips

- Understand the differences between TCP, UDP, SCTP, and DCCP
- Familiarize yourself with CoAP, LWM2M, and MQTT
- Know the advantages and disadvantages of each transport protocol and application transport method
