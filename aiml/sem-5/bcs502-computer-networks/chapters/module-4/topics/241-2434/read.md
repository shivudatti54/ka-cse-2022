# 24.1-24.3.4: Introduction to Transport Layer

=====================================================

## Introduction to Transport Layer

---

The transport layer is the fourth layer of the OSI model and is responsible for providing reliable data transfer between devices. It ensures that data is delivered in the correct order and that errors are detected and corrected.

### Functions of Transport Layer

---

- Provides reliable data transfer
- Ensures data is delivered in the correct order
- Detects and corrects errors
- Provides flow control and congestion control
- Supports multiplexing and demultiplexing

### Transport Layer Protocols

---

There are two main transport layer protocols: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

### TCP (Transmission Control Protocol)

---

TCP is a connection-oriented protocol that ensures reliable data transfer. It establishes a connection between the sender and receiver before data is sent.

#### TCP Characteristics

---

- Connection-oriented
- Reliable
- Ordered delivery of data
- Error detection and correction
- Flow control and congestion control

#### TCP Examples

---

- HTTP (Hypertext Transfer Protocol) uses TCP to transfer data between web servers and clients
- FTP (File Transfer Protocol) uses TCP to transfer files between devices

### UDP (User Datagram Protocol)

---

UDP is a connectionless protocol that does not guarantee reliable data transfer. It is often used for applications that require fast data transfer, such as online gaming and video streaming.

#### UDP Characteristics

---

- Connectionless
- Unreliable
- No guarantee of ordered delivery
- No error detection or correction
- No flow control or congestion control

#### UDP Examples

---

- Online gaming uses UDP to transfer game data between devices
- Video streaming uses UDP to transfer video data between devices

### Comparison of TCP and UDP

---

| Feature          | TCP                                 | UDP                                   |
| ---------------- | ----------------------------------- | ------------------------------------- |
| Connection       | Connection-oriented                 | Connectionless                        |
| Reliability      | Reliable                            | Unreliable                            |
| Ordered Delivery | Ordered delivery                    | No guarantee of ordered delivery      |
| Error Detection  | Error detection and correction      | No error detection or correction      |
| Flow Control     | Flow control and congestion control | No flow control or congestion control |

In summary, TCP provides reliable data transfer and is often used for applications that require guaranteed delivery, such as file transfer and email. UDP provides fast data transfer and is often used for applications that require low latency, such as online gaming and video streaming.
