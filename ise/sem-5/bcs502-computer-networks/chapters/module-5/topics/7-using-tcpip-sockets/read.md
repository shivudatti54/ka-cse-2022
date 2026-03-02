# 7 Using TCP/IP Sockets

=====================================================

## Introduction

---

TCP/IP sockets are a fundamental concept in computer networking, allowing applications to communicate with each other over a network. In this section, we will delve into the world of TCP/IP sockets, exploring their definition, types, and usage.

## Definition

---

A TCP/IP socket is a endpoint for communication between two devices (computer, phone, etc.) in a network. It provides a way for applications to send and receive data over a network using the Transmission Control Protocol (TCP) and the Internet Protocol (IP).

## Types of TCP/IP Sockets

---

There are two primary types of TCP/IP sockets:

- **Stream sockets**: These sockets provide a connection-oriented service, where a connection is established between the two endpoints before data is sent. Stream sockets are suitable for applications that require guaranteed delivery of data, such as file transfers.
- **Datagram sockets**: These sockets provide a connectionless service, where data is sent without establishing a connection first. Datagram sockets are suitable for applications that require fast transmission of data, such as online gaming.

## Creating a TCP/IP Socket

---

To create a TCP/IP socket, you need to:

- Import the necessary libraries (e.g., `socket` module in Python)
- Create a socket object using the `socket.socket()` function
- Specify the address family (e.g., `AF_INET` for IPv4) and the socket type (e.g., `SOCK_STREAM` for a stream socket)
- Bind the socket to a local address and port number
- Listen for incoming connections

### Example (Python)

```python
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port number
server_socket.bind(('localhost', 8080))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on port 8080")

while True:
    # Accept an incoming connection
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} established")

    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    # Send data back to the client
    client_socket.sendall(b"Hello from server!")
```

## Sending and Receiving Data

---

To send data over a TCP/IP socket, you can use the `sendall()` method. To receive data, you can use the `recv()` method.

### Example (Python)

```python
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
client_socket.connect(('localhost', 8080))

# Send data to the server
client_socket.sendall(b"Hello from client!")

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# Close the socket
client_socket.close()
```

## Conclusion

---

In this section, we have explored the concept of TCP/IP sockets, including their definition, types, and usage. We have also provided examples of creating a TCP/IP socket, sending and receiving data, and handling incoming connections. By mastering the art of TCP/IP sockets, you can build robust and reliable network applications.
