# **24.1-24.3.4: Transport Layer Services**

### Introduction

The Transport Layer, also known as the Transport Layer Protocol, is the fourth layer of the OSI model and the fifth layer of the TCP/IP model. It provides reliable data transfer between devices over an IP network. The Transport Layer services include connection establishment, data segmentation, and error detection and correction.

### Transport-Layer Protocols: Introduction

There are several transport-layer protocols, including:

- **TCP (Transmission Control Protocol)**: a connection-oriented protocol that provides reliability and error detection.
- **UDP (User Datagram Protocol)**: a connectionless protocol that provides best-effort delivery.
- **SCTP (Stream Control Transmission Protocol)**: a connection-oriented protocol that provides multiplexing and multiplexing.

### Connection Establishment

Connection establishment is the process of setting up a connection between two devices before data transfer can occur. This involves the exchange of control packets between the devices to establish a connection.

### Connection Termination

Connection termination is the process of breaking down the connection between two devices after data transfer is complete. This involves the exchange of control packets between the devices to terminate the connection.

### Data Segmentation

Data segmentation is the process of breaking down large data packets into smaller packets before transmission. This is necessary because the Transmission Control Protocol (TCP) requires that data packets be of a specific size to ensure reliable transmission.

### Error Detection and Correction

Error detection and correction are essential functions of the Transport Layer. These functions involve detecting errors in data packets and correcting them before transmission.

### Key Concepts

- **Segmented Data**: data packets that are broken down into smaller packets before transmission.
- **Control Packets**: packets that contain control information, such as connection establishment and termination.
- **Error Detection**: the process of detecting errors in data packets.
- **Error Correction**: the process of correcting errors in data packets.

### Example

Suppose we want to send a file from device A to device B using the TCP protocol. The process of sending the file would involve the following steps:

1.  Connection establishment: device A and device B exchange control packets to establish a connection.
2.  Data segmentation: the file is broken down into smaller packets, each of which is of a specific size.
3.  Data transmission: the packets are transmitted over the IP network.
4.  Error detection and correction: the receiving device checks each packet for errors and corrects them if necessary.
5.  Connection termination: the connection is terminated when the data transfer is complete.

## **Key Transport-Layer Protocols**

### TCP (Transmission Control Protocol)

- **Connection-oriented**:TCP establishes a connection before data transfer can occur.
- **Reliable**:TCP ensures that data packets are delivered in the correct order and without errors.
- **Connection termination**:TCP terminates the connection after data transfer is complete.

### UDP (User Datagram Protocol)

- **Connectionless**:UDP does not establish a connection before data transfer can occur.
- **Best-effort delivery**:UDP provides best-effort delivery, but does not guarantee that data packets will be delivered.
- **Multiplexing**:UDP supports multiplexing, which allows multiple data streams to be transmitted over the same connection.

### SCTP (Stream Control Transmission Protocol)

- **Connection-oriented**:SCTP establishes a connection before data transfer can occur.
- **Multiplexing**:SCTP supports multiplexing, which allows multiple data streams to be transmitted over the same connection.
- **Reliability**:SCTP provides reliable data transfer, similar to TCP.

## **Transport-Layer Services**

### Connection Establishment

- **Three-way handshake**:the exchange of control packets between devices to establish a connection.
- **Connection refusal**:the process of refusing a connection request.

### Data Segmentation

- **Segment size**:the maximum size of a data packet.
- **Fragmentation**:the process of breaking down large data packets into smaller packets.

### Error Detection and Correction

- **Checksum**:a mathematical formula used to detect errors in data packets.
- **Error correction**:the process of correcting errors in data packets using techniques such as forward error correction.
