# Introduction to Transport Layer

=====================================

## Overview of Transport Layer

---

The Transport Layer is the fourth layer of the OSI model and is responsible for providing reliable data transfer between devices on a network. It ensures that data is delivered in the correct order and that errors are detected and corrected.

## Functions of Transport Layer

---

- Ensures reliable data transfer between devices
- Provides error detection and correction
- Ensures data is delivered in the correct order
- Provides flow control to prevent network congestion
- Provides congestion control to prevent network congestion

## Transport-Layer Protocols

---

### Introduction

---

Transport-layer protocols are responsible for providing the functions of the transport layer. There are two main transport-layer protocols:

- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

### TCP (Transmission Control Protocol)

---

TCP is a connection-oriented protocol that ensures reliable data transfer between devices. It establishes a connection between devices before data is sent, and it ensures that data is delivered in the correct order.

- **Connection Establishment:** TCP establishes a connection between devices before data is sent.
- **Segmentation and Reassembly:** TCP breaks down data into smaller segments and reassembles them at the receiving end.
- **Error Detection and Correction:** TCP uses error-checking mechanisms to detect and correct errors.
- **Flow Control:** TCP uses flow control to prevent network congestion.

### UDP (User Datagram Protocol)

---

UDP is a connectionless protocol that does not establish a connection before data is sent. It is faster than TCP but does not guarantee reliable data transfer.

- **No Connection Establishment:** UDP does not establish a connection before data is sent.
- **No Error Detection and Correction:** UDP does not have error-checking mechanisms.
- **No Flow Control:** UDP does not have flow control mechanisms.

## Key Concepts

---

### Segmentation

- Segmentation is the process of breaking down data into smaller segments.
- Segmentation is used by TCP to prevent network congestion.
- Segmentation can be done at the application layer or at the transport layer.

### Reassembly

- Reassembly is the process of reassembling segments at the receiving end.
- Reassembly is used by TCP to ensure data is delivered in the correct order.
- Reassembly can be done at the receiving end.

### Flow Control

- Flow control is the mechanism used to prevent network congestion.
- Flow control is used by TCP to regulate the amount of data sent by a device.
- Flow control can be done using windowing or congestion avoidance algorithms.

### Congestion Control

- Congestion control is the mechanism used to prevent network congestion.
- Congestion control is used by TCP to regulate the amount of data sent by a device.
- Congestion control can be done using algorithms such as slow-start and congestion avoidance.

### Acknowledgments

- Acknowledgments are used by TCP to confirm receipt of data.
- Acknowledgments are used by TCP to ensure data is delivered in the correct order.
- Acknowledgments can be sent by the receiving device using the ACK packet.
