# **23.1- 23.2: Introduction to the Transport Layer**

## **23.1 Introduction to the Transport Layer**

The Transport Layer is the fourth layer of the OSI model and is responsible for ensuring reliable data transfer between devices over the network.

### Definition:

The Transport Layer is a logical layer that provides a connection-oriented or connectionless service between devices, ensuring that data is delivered in the correct order and that errors are detected and corrected.

### Functions:

- Provides a connection between devices
- Ensures reliable data transfer
- Delivers data in the correct order
- Detects errors and corrects them

### Types of Transport Layer Protocols:

- **Connection-Oriented**: Establishes a connection between devices before data transfer begins. Examples include TCP (Transmission Control Protocol) and SDP (Session Description Protocol).
- **Connectionless**: Does not establish a connection before data transfer begins. Examples include UDP (User Datagram Protocol) and DCCP (Datagram Congestion Control Protocol).

## **23.2 Transport-Layer Protocols: Introduction**

### TCP (Transmission Control Protocol)

TCP is a connection-oriented protocol that provides reliable data transfer between devices. It ensures that data is delivered in the correct order and that errors are detected and corrected.

#### Key Features:

- **Connection Establishment**: TCP establishes a connection between devices before data transfer begins.
- **Segmentation**: TCP breaks data into small segments and assigns sequence numbers to each segment.
- **Acknowledgments**: TCP sends acknowledgments to devices to confirm receipt of data.
- **Error Detection**: TCP uses checksums to detect errors in data transmission.

### UDP (User Datagram Protocol)

UDP is a connectionless protocol that provides best-effort delivery of data between devices. It does not guarantee delivery of data, but it provides fast transmission of data.

#### Key Features:

- **Connectionless**: UDP does not establish a connection before data transfer begins.
- **Datagrams**: UDP sends data in the form of datagrams, which are small packets of data.
- **No Acknowledgments**: UDP does not send acknowledgments to devices.
- **No Error Detection**: UDP relies on the network to detect errors in data transmission.

### Other Transport-Layer Protocols

Other transport-layer protocols include:

- **SCTP (Stream Control Transmission Protocol)**: Provides reliable data transfer between devices and is designed for real-time applications.
- **DCCP (Datagram Congestion Control Protocol)**: Provides reliable data transfer between devices and is designed for internet applications.
- **SPX ( Sequential Package Exchange)**: Provides reliable data transfer between devices and is designed for internet applications.

### Best Practices:

- **Use TCP for Reliable Applications**: Use TCP for applications that require reliable data transfer, such as file transfer and email.
- **Use UDP for Best-Effort Applications**: Use UDP for applications that require fast transmission of data, such as online gaming and video streaming.
- **Use SCTP for Real-Time Applications**: Use SCTP for applications that require real-time data transfer, such as voice over IP and video conferencing.
