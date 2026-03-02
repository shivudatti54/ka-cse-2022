# 7 Using TCP/IP Sockets

=====================================

## Introduction

---

TCP/IP sockets are a fundamental concept in computer networks, enabling communication between devices over IP networks.

## Key Points

---

### Definitions

- **Socket**: A endpoint for communication between two devices (computer, phone, etc.) in a network.
- **TCP/IP**: Transmission Control Protocol/Internet Protocol, a suite of communication protocols used to interconnect networks.

### Sockets Types

---

- **Datagram Sockets**: Connectionless, used for applications requiring fast data transfer (e.g., DNS, DHCP).
- **Stream Sockets**: Connection-oriented, used for applications requiring reliable data transfer (e.g., TCP).

### TCP/IP Socket Creation

---

- **SOCK_CREATE**: Creates a new socket.
- **Socket Address Structure**: `struct sockaddr` contains address information (IP address and port number).

### TCP/IP Socket Operations

---

- **bind()**: Binds a socket to a specific address and port.
- **listen()**: Sets a socket to listen for incoming connections.
- **accept()**: Accepts an incoming connection and creates a new socket.
- **connect()**: Establishes a connection to a remote socket.
- **send()**: Sends data over a socket.
- **recv()**: Receives data over a socket.

### TCP/IP Socket Properties

---

- **SOCK_KEEPALIVE**: Enables or disables keepalive messages to detect idle connections.
- **SOCK_NonBLOCK**: Makes a socket non-blocking, allowing it to return immediately if data is not available.
- **SOCK_ReuseADDR**: Allows a socket to reuse an address that has been closed.

### Important Formulas and Theorems

---

- **TCP Segment Size**: `mss = max(576, 1460 - (ip header size + tcph header size))`
- **TCP Window Size**: `max(1024, 65535 - (ip header size + tcph header size + max segment size))`
- **UDP Header Size**: `8 + (header length field)`

### Key Theorems

---

- **TCP Connection Establishment**: A connection is established when a client initiates a three-way handshake with a server.
- **UDP Connection Establishment**: A connection is not established in UDP, as it is connectionless.
