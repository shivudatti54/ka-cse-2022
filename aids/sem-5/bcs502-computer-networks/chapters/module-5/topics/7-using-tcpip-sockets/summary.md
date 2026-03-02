# **TCP/IP Sockets Revision Notes**

## **Introduction**

- TCP/IP sockets are an essential component of computer networking.
- They enable communication between two devices on a network.

## **Key Concepts**

- **Socket**: A endpoint for communication between two devices (computer, server, etc.)
- **IP Address**: A unique identifier for a device on a network.
- **Port Number**: A unique identifier for a specific service or application.

## **Types of Sockets**

- **TCP (Transmission Control Protocol)**: Connection-oriented, reliable, and error-checked.
- **UDP (User Datagram Protocol)**: Connectionless, best-effort delivery, no error checking.

## **Socket Operations**

- **Bind**: Associate a socket with a specific IP address and port number.
- **Listen**: Set a socket to accept incoming connections.
- **Accept**: Accept an incoming connection and create a new socket.
- **Connect**: Establish a connection to a remote socket.
- **Send**: Transmit data from a local socket to a remote socket.
- **Receive**: Receive data from a remote socket.

## **Important Formulas and Definitions**

- **Socket Address Structure**: `struct sockaddr { ... }`
- **IP Address Structure**: `struct sockaddr_in { ... }`
- **TCP Header Structure**: `struct tcphdr { ... }`
- **UDP Header Structure**: `struct udphdr { ... }`

## **Theorems**

- **TCP Three-Way Handshake**: Establishes a connection between two devices.
- **TCP Connection Establishment**: Ensures reliable and error-checked communication.

## **Revision Tips**

- Understand the difference between TCP and UDP.
- Know the socket operations and their functions.
- Familiarize yourself with socket address structures and header formats.
