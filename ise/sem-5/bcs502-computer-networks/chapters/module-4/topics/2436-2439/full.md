# 24.3.6-24.3.9: Introduction to Transport Layer Protocols

=====================================================

## 24.3.6: Connection-Oriented Transport Layer Protocols

---

### Overview

Connection-oriented transport layer protocols are used to establish a reliable connection between two endpoints before data is sent. This type of protocol ensures that data is delivered in the correct order, and any errors or losses are detected and corrected.

### TCP (Transmission Control Protocol)

---

#### Overview

TCP is a connection-oriented protocol that provides a reliable data transfer service between devices. It ensures that data is delivered in the correct order, and any errors or losses are detected and corrected.

#### How TCP Works

---

1.  **Connection Establishment**: The process of establishing a connection between two devices involves the three-way handshake: SYN (synchronize), SYN-ACK (synchronize-acknowledgment), and ACK (acknowledgment).
2.  **Data Transmission**: Once the connection is established, data is transmitted in packets between the two devices.
3.  **Error Detection and Correction**: TCP uses a checksum to detect any errors in the data. If an error is detected, the receiving device sends an acknowledgement to the sending device, indicating that the data was not received correctly.

#### TCP Segments

---

TCP segments are used to transmit data between devices. Each segment has a header that contains the source and destination ports, sequence numbers, and checksum.

#### TCP Header Fields

---

- **Source Port**: The source port number.
- **Destination Port**: The destination port number.
- **Sequence Number**: The sequence number of the first byte of data in the segment.
- **Acknowledgment Number**: The sequence number of the next byte that the sender expects to receive.
- **Data**: The actual data being transmitted.
- **Checksum**: A checksum that detects any errors in the data.
- **Urgent Pointer**: A pointer to the urgent data in the segment.

#### TCP Flow Control

---

TCP uses a mechanism called flow control to prevent network congestion. The sender and receiver agree on a maximum amount of data that can be sent in a single segment.

#### TCP Windowing

---

TCP uses a sliding window mechanism to manage flow control. The sender and receiver agree on a window size, which is the maximum amount of data that can be sent in a single segment.

### UDP (User Datagram Protocol)

---

#### Overview

UDP is a connectionless protocol that provides best-effort delivery of data between devices. It does not guarantee that data will be delivered, and any errors or losses are not detected or corrected.

#### How UDP Works

---

1.  **Data Transmission**: UDP sends data in packets between devices without establishing a connection.
2.  **Error Detection**: UDP does not have a built-in error detection mechanism. The sender assumes that the receiver will detect any errors in the data.

#### UDP Applications

---

UDP is commonly used in applications that require fast and efficient data transfer, such as online gaming and video streaming.

## 24.3.7: Connectionless Transport Layer Protocols

---

### Overview

Connectionless transport layer protocols are used to transmit data between devices without establishing a connection. This type of protocol does not guarantee that data will be delivered, and any errors or losses are not detected or corrected.

### UDP (User Datagram Protocol)

---

#### Overview

UDP is a connectionless protocol that provides best-effort delivery of data between devices. It does not guarantee that data will be delivered, and any errors or losses are not detected or corrected.

#### How UDP Works

---

1.  **Data Transmission**: UDP sends data in packets between devices without establishing a connection.
2.  **Error Detection**: UDP does not have a built-in error detection mechanism. The sender assumes that the receiver will detect any errors in the data.

#### UDP Header Fields

---

- **Source Port**: The source port number.
- **Destination Port**: The destination port number.
- **Length**: The length of the UDP datagram.
- **Checksum**: A checksum that detects any errors in the data.
- **Data**: The actual data being transmitted.

#### UDP Fragmentation

---

UDP fragmentation is used to split large datagrams into smaller fragments that can be transmitted over networks with different maximum transmission unit (MTU) sizes.

## 24.3.8: Transport Layer Security (TLS)

---

### Overview

Transport Layer Security (TLS) is a cryptographic protocol that provides secure communication between devices over the internet. It is used to establish a secure connection between a client and a server.

### How TLS Works

---

1.  **Certificate Exchange**: The client and server exchange certificates to establish their identities.
2.  **Key Exchange**: The client and server exchange cryptographic keys to establish a shared secret.
3.  **Encryption**: The client and server use the shared secret to encrypt data transmitted between them.

### TLS Handshake

---

The TLS handshake is the process of establishing a secure connection between a client and a server. The handshake consists of the following steps:

1.  **Client Hello**: The client sends a "Client Hello" message to the server, which includes the client's supported protocol versions, cipher suites, and compression methods.
2.  **Server Hello**: The server responds with a "Server Hello" message, which includes the server's supported protocol versions, cipher suites, and compression methods.
3.  **Certificate**: The server sends its certificate to the client.
4.  **Key Exchange**: The client and server exchange cryptographic keys to establish a shared secret.
5.  **Change Cipher Spec**: The client and server send a "Change Cipher Spec" message to indicate that they have changed their cipher suites.
6.  **Finished**: The client and server send a "Finished" message to indicate that the handshake is complete.

### TLS Applications

---

TLS is commonly used in applications that require secure communication over the internet, such as online banking and e-commerce.

## 24.3.9: Transport Layer Protocols and Applications

---

### Overview

Transport layer protocols are used to provide reliable and efficient data transfer between devices. This chapter will explore the different transport layer protocols, their applications, and their historical context.

### Case Study: Email Transmission

---

Email transmission is a common application of transport layer protocols. When a user sends an email, the email is broken into packets and transmitted over the internet using TCP or UDP.

### Case Study: Online Gaming

---

Online gaming is another application of transport layer protocols. Online gaming uses TCP or UDP to transmit game data between devices.

### Further Reading

---

- TCP/IP Illustrated, Volume 1: The Protocols and the Internet Program (Kathy C. Russell, Russ Allbery, and Eric Allman)
- TCP/IP Network Administration (Kevin Tolly)
- Transport Layer Security (TLS) Guide (IETF)

### Diagrams

---

- Connection-oriented transport layer protocol diagram
- Connectionless transport layer protocol diagram
- TLS handshake diagram

### Exercises

---

1.  Describe the differences between connection-oriented and connectionless transport layer protocols.
2.  Explain the TLS handshake process.
3.  Describe the applications of transport layer protocols.
4.  Design a system that uses TCP for email transmission.
5.  Design a system that uses UDP for online gaming.
