# **24.1-24.3.4 Revision Notes: Computer Networks**

## **Introduction to Transport Layer**

- The transport layer is the fourth layer of the OSI model and is responsible for ensuring reliable data transfer between devices.
- It provides a reliable, error-checked, and sequenced delivery of data between devices.

## **Transport-Layer Protocols**

- **TCP (Transmission Control Protocol)**:
  - Ensures reliable, error-checked, and sequenced delivery of data.
  - Uses a connection-oriented approach, where a connection is established before data is sent.
  - Uses sequence numbers to ensure data is delivered in the correct order.
  - Uses acknowledgments to ensure data is received.
- **UDP (User Datagram Protocol)**:
  - Provides best-effort delivery of data.
  - Does not guarantee delivery or order of data.
  - Uses a connectionless approach, where no connection is established before data is sent.

## **Key Concepts and Formulas**

- **Throughput**: The amount of data that can be transferred per unit of time.
- **Bandwidth**: The amount of data that can be transmitted per unit of time.
- **Packet Switching**: A method of data transmission where data is broken into small packets and transmitted independently.
- **Error Detection and Correction**: Techniques used to detect and correct errors in data transmission.

## **Important Formulas and Theorems**

- **TCP Congestion Control Formula**: `cwnd = cwnd*0.5` (congestion window reduction)
- **UDP Header Format**: `Source port, Destination port, Length, Checksum, Flags`
- **TCP Three-Way Handshake**: `SYN - SYN-ACK - ACK`

## **Revision Tips**

- Focus on the key differences between TCP and UDP.
- Understand the concepts of connection-oriented and connectionless protocols.
- Practice calculating throughput and bandwidth.
- Review error detection and correction techniques.
