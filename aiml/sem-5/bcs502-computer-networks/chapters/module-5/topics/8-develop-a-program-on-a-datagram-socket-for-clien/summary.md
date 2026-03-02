# Datagram Socket Client/Server Program

=====================================

### Overview

A datagram socket is a type of socket that is connectionless, meaning that there is no guarantee of delivery or order of packets. This program demonstrates a client-server architecture using datagram sockets to display messages on the client side.

### Key Points

- **Datagram Socket**:
  - Connectionless
  - No guarantee of delivery or order of packets
  - Used for unreliable data transfer
- **Client-Server Architecture**:
  - Client sends data to server
  - Server receives and processes data
  - Client receives response from server
- **Datagram Socket Functions**:
  - `sendto()`: sends data to server
  - `recvfrom()`: receives data from server
  - `bind()`: binds socket to address and port
  - `listen()`: sets socket to listen for incoming connections
- **Socket Address and Port**:
  - `AF_INET`: address family for IPv4
  - `SOCK_DGRAM`: socket type for datagrams
  - `struct sockaddr_in`: structure for socket address
- **Message Handling**:
  - `fork()`: creates a new process for server
  - `wait()`: waits for server process to finish

### Important Formulas and Definitions

- **Socket Buffer Size**: `BUFSIZE = 1024`
- **Datagram Library Function**: `sendto()`
- **Socket Address Structure**: `struct sockaddr_in { int sin_family; short sin_port; char sin_addr[INET_ADDRSTRLEN]; };`

### Theorems

- **TCP vs UDP**: TCP is connection-oriented and guarantees delivery, while UDP is connectionless and does not guarantee delivery.
- **Socket Programming**: socket programming involves creating a connection between two processes using sockets.

### Revision Notes

- Review client-server architecture
- Understand datagram socket functions and socket address structures
- Practice socket programming concepts
- Familiarize yourself with TCP vs UDP trade-offs.
