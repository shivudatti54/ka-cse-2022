# 23.1-23.2: Introduction to Transport Layer

## 23.1: Introduction to Transport Layer

The Transport Layer is the fourth layer of the OSI model and is responsible for ensuring reliable data transfer between devices. It provides a reliable, error-checked, and congestion-controlled connection between the sender and receiver.

### History of Transport Layer

The Transport Layer was first introduced in the 1970s with the development of the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP). TCP was designed to provide a reliable connection-oriented service, while UDP was designed to provide a best-effort connectionless service.

### Requirements of Transport Layer

The Transport Layer has three primary requirements:

1. **Reliability**: The Transport Layer ensures that data is delivered correctly and in the correct order.
2. **Error-checking**: The Transport Layer detects and corrects errors that occur during data transmission.
3. **Congestion Control**: The Transport Layer prevents network congestion by regulating the amount of data sent by the sender.

### Functions of Transport Layer

The Transport Layer performs the following functions:

1. **Connection Establishment**: The Transport Layer establishes a connection between the sender and receiver.
2. **Data Segmentation**: The Transport Layer segments data into smaller packets to ensure reliable transfer.
3. **Error Detection and Correction**: The Transport Layer detects and corrects errors that occur during data transmission.
4. **Congestion Control**: The Transport Layer regulates the amount of data sent by the sender to prevent network congestion.

### Transport Layer Protocols

There are two primary Transport Layer protocols:

1. **Transmission Control Protocol (TCP)**: TCP is a connection-oriented protocol that ensures reliable data transfer. It uses segmentation, error-checking, and congestion control to ensure that data is delivered correctly.
2. **User Datagram Protocol (UDP)**: UDP is a connectionless protocol that provides best-effort service. It does not guarantee delivery or order of packets.

### Examples of Transport Layer Protocols

1. **TCP**: TCP is used in applications such as email, file transfer, and web browsing. It is widely used because it provides reliable and guaranteed delivery of data.
2. **UDP**: UDP is used in applications such as video streaming, online gaming, and VoIP. It is used because it provides fast and efficient transfer of data, even if some packets are lost or corrupted.

### Case Study: TCP vs. UDP in Online Gaming

Online gaming requires fast and efficient data transfer. UDP is often used in online gaming because it provides low latency and high throughput. However, UDP does not guarantee delivery of packets, which can lead to packet loss and corruption. In contrast, TCP provides guaranteed delivery of packets, but it can introduce latency and reduce throughput. In practice, a combination of TCP and UDP is often used in online gaming to balance reliability and performance.

## 23.2: Transport-Layer Protocols: Introduction

This section provides an in-depth look at the two primary Transport Layer protocols: TCP and UDP.

### Transmission Control Protocol (TCP)

#### Overview of TCP

TCP is a connection-oriented protocol that ensures reliable data transfer. It uses segmentation, error-checking, and congestion control to ensure that data is delivered correctly.

#### TCP Segmentation

TCP segments data into smaller packets to ensure reliable transfer. Each packet includes a sequence number, which ensures that packets are delivered in the correct order.

#### TCP Error Detection and Correction

TCP uses error-checking to detect errors that occur during data transmission. If an error is detected, TCP corrects the error and sends an acknowledgement to the sender.

#### TCP Congestion Control

TCP regulates the amount of data sent by the sender to prevent network congestion. TCP uses a sliding window approach to regulate data transfer.

#### TCP Connection Establishment

TCP establishes a connection between the sender and receiver using a three-way handshake. The sender sends a SYN packet to the receiver, which responds with a SYN-ACK packet. The sender then sends an ACK packet to confirm the connection.

#### TCP Connection Termination

TCP terminates a connection using a four-way handshake. The sender sends a FIN packet to the receiver, which responds with an ACK packet. The receiver then sends a FIN packet to confirm the termination of the connection.

#### TCP Applications

TCP is widely used in applications such as email, file transfer, and web browsing.

#### TCP Advantages

TCP provides reliable and guaranteed delivery of data, which makes it suitable for applications that require high reliability.

#### TCP Disadvantages

TCP introduces latency and reduces throughput, which can make it unsuitable for applications that require fast and efficient data transfer.

### User Datagram Protocol (UDP)

#### Overview of UDP

UDP is a connectionless protocol that provides best-effort service. It does not guarantee delivery or order of packets.

#### UDP Segmentation

UDP segments data into smaller packets to ensure efficient transfer. Each packet includes a source and destination port number, which identifies the sender and receiver.

#### UDP Error Detection

UDP does not use error-checking to detect errors that occur during data transmission. If an error occurs, the packet is discarded and retransmitted.

#### UDP Congestion Control

UDP does not regulate the amount of data sent by the sender to prevent network congestion. Instead, the network regulates data transfer to prevent congestion.

#### UDP Connection Establishment

UDP does not establish a connection between the sender and receiver. Instead, each packet is sent independently.

#### UDP Connection Termination

UDP does not terminate a connection. Instead, the sender and receiver can terminate the connection at any time.

#### UDP Applications

UDP is widely used in applications such as video streaming, online gaming, and VoIP.

#### UDP Advantages

UDP provides fast and efficient data transfer, which makes it suitable for applications that require low latency.

#### UDP Disadvantages

UDP does not guarantee delivery or order of packets, which can lead to packet loss and corruption.

### Examples of UDP in Practice

1. **Video Streaming**: Video streaming services such as YouTube and Netflix use UDP to provide fast and efficient video transfer.
2. **Online Gaming**: Online gaming platforms such as Steam and Xbox use UDP to provide fast and efficient data transfer.
3. **VoIP**: VoIP services such as Skype and Google Voice use UDP to provide fast and efficient voice transfer.

### Further Reading

- "TCP and UDP: A Tutorial" by Cisco
- "Transmission Control Protocol (TCP)" by Computer Networking: Theory, Practice, and Performance
- "User Datagram Protocol (UDP)" by IETF
