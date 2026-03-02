# **7 Using TCP/IP Sockets**

### Key Points

- **What are TCP/IP sockets?**
  - A endpoint for communication between two devices in a network
  - Used for sending and receiving data over IP networks
- **TCP/IP Socket Programming**
  - Establish a connection between two devices
  - Use sockets for communication between processes
- **Socket Types**
  - **Stream Sockets**: used for sending and receiving byte streams
  - **Datagram Sockets**: used for sending and receiving datagrams (small packets of data)
- **Socket Operations**
  - **SOCK_STREAM**: establish a connection-oriented communication
  - **SOCK_DGRAM**: establish a connectionless communication
- **Socket Addresses**
  - **IP Address**: a unique address for a device in a network
  - **Port Number**: a unique number for a process on a device
- **Socket Functions**
  - **socket()**: creates a new socket
  - **bind()**: binds a socket to a specific address and port
  - **listen()**: listens for incoming connections
  - **accept()**: accepts an incoming connection
  - **send()**: sends data to a socket
  - **recv()**: receives data from a socket

### Important Formulas and Definitions

- **TCP/IP Socket Formula**:
  - `socket() = (protocol, type) = (IP protocol number, socket type)`
- **Socket Address Formula**:
  - `IP Address = (network ID, host ID)`
  - `Port Number = (process ID, service ID)`
- **TCP/IP Socket Theorem**:
  - "A socket can be used to establish a connection with another socket on the same network"

### Quick Revision

- Establish a connection between two devices using TCP/IP sockets
- Use stream sockets for connection-oriented communication and datagram sockets for connectionless communication
- Use socket functions to create, bind, listen, accept, send, and receive data
- Use socket addresses to identify a socket's location in a network
