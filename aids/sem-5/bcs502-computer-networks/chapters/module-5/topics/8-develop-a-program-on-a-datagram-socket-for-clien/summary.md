# **Datagram Socket Client/Server Program**

## **Overview**

Develop a program using a datagram socket for a client-server architecture to display messages on the client side.

## **Key Points**

- **Datagram Sockets**
  - Connectionless, best-effort delivery
  - No guarantee of delivery or order of packets
- **Client-Server Architecture**
  - Client: Sends messages to server
  - Server: Receives and displays messages
- **Program Components**
  - Client: `SOCK_DGRAM` socket, `bind()`, `connect()`, `send()`
  - Server: `SOCK_DGRAM` socket, `bind()`, `listen()`, `accept()`, `recv()`, `send()`
- **Message Display**
  - Use `print()` or `matplotlib` to display received messages
- **Error Handling**
  - Use `try-except` blocks to handle socket errors

## **Formulas and Definitions**

- **Datagram Socket Address**
  - `struct sockaddr_in` ( IPv4) or `struct sockaddr_in6` (IPv6)
- **Port Number**
  - 32-bit integer (0-65535)
- **Socket Options**
  - `SOCK_DGRAM` (connectionless, best-effort delivery)

## **Theorems and Concepts**

- **TCP vs. UDP**
  - TCP: Connection-oriented, guaranteed delivery
  - UDP: Connectionless, best-effort delivery
- **Socket Programming**
  - Create a socket, bind to a address and port, connect to a server, send and receive data

## **Revision Tips**

- Practice creating a datagram socket client-server program
- Understand connectionless and connection-oriented socket programming
- Review error handling techniques for socket programming
