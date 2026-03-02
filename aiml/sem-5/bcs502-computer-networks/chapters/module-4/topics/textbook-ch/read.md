# Introduction to Transport Layer

=====================================

## Overview of Transport Layer

---

The Transport Layer is the fourth layer of the OSI Model and is responsible for providing reliable data transfer between devices on a network. It ensures that data is delivered in the correct order and that errors are corrected.

## Transport Layer Protocols

---

The Transport Layer uses several protocols to ensure reliable data transfer. Some of the most common protocols are:

### TCP (Transmission Control Protocol)

- **Connection-Oriented**: Establishes a connection between devices before data transfer begins.
- **Reliable**: Ensures that data is delivered in the correct order and that errors are corrected.
- **Segments Data**: Divides data into small segments and assigns sequence numbers to each segment.
- **Error-Checking**: Uses error-checking mechanisms to detect and correct errors in data transmission.

### UDP (User Datagram Protocol)

- **Connectionless**: Does not establish a connection before data transfer begins.
- **Unreliable**: Does not guarantee that data will be delivered in the correct order or that errors will be corrected.
- **No Segmentation**: Does not segment data into small packets.
- **No Error-Checking**: Does not perform error-checking on data transmission.

### SCTP (Stream Control Transmission Protocol)

- **Connection-Oriented**: Establishes a connection between devices before data transfer begins.
- **Reliable**: Ensures that data is delivered in the correct order and that errors are corrected.
- **Multiple Streams**: Supports multiple streams of data over a single connection.

## Key Concepts

---

- **Segment**: The basic unit of data transmission in the Transport Layer.
- **Sequence Number**: A unique number assigned to each segment to ensure that data is delivered in the correct order.
- **Acknowledgment**: A response to a segment indicating that it was received correctly.
- **Retransmission**: The process of re-sending a segment if it was not received correctly.

## Example

---

Imagine two devices, A and B, that need to exchange data. They establish a connection using TCP and agree to use a sequence number to ensure that data is delivered in the correct order.

Device A sends a segment with sequence number 1 containing the data "Hello". Device B receives the segment and acknowledges it with an acknowledgment number 1, indicating that the data was received correctly.

Device A then sends a segment with sequence number 2 containing the data "World". Device B receives the segment and acknowledges it with an acknowledgment number 2, indicating that the data was received correctly.

The sequence of events is:

1.  Device A sends segment 1: "Hello"
2.  Device B receives segment 1 and acknowledges it with acknowledgment 1
3.  Device A sends segment 2: "World"
4.  Device B receives segment 2 and acknowledges it with acknowledgment 2
