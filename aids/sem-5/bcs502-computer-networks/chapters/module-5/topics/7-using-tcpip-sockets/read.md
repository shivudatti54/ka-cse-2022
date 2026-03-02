# 7 Using TCP/IP Sockets

=====================================================

## Introduction

---

TCP/IP sockets are a fundamental concept in computer networking that enables communication between devices over the internet. In this section, we will explore the different uses of TCP/IP sockets.

## What are TCP/IP Sockets?

---

TCP/IP sockets are endpoints for communication between two devices (computer, smartphone, etc.) in a network. They provide a way for devices to send and receive data over the internet.

### Definition

A socket is a endpoint of a connection between two devices in a network. It is a software construct that provides a connection between two devices.

### Types of Sockets

- **Stream Sockets**: Used for sending and receiving continuous data streams.
- **Datagram Sockets**: Used for sending and receiving messages, which can be of varying sizes.
- **Raw Sockets**: Used for sending and receiving raw packets of data.

## Creating a TCP/IP Socket

---

To create a TCP/IP socket, you need to use the `socket()` function in your programming language of choice.

### Code Example

Here is an example of how to create a TCP/IP socket in Python:

```python
import socket

# Create a new socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("localhost", 12345))

# Listen for incoming connections
server_socket.listen(5)
```

## Sending and Receiving Data over a TCP/IP Socket

---

Once you have created a TCP/IP socket, you can send and receive data over it.

### Code Example

Here is an example of how to send and receive data over a TCP/IP socket in Python:

```python
import socket

# Create a new socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 12345))

# Send data to the server
client_socket.send(b"Hello, server!")

# Receive data from the server
data = client_socket.recv(1024)
print(data.decode())

# Close the socket
client_socket.close()
```

## TCP/IP Socket States

---

A TCP/IP socket can be in one of several states:

- **LISTENING**: The socket is listening for incoming connections.
- **CONNECTED**: The socket is connected to a remote device.
- **CLOSED**: The socket is closed and cannot be used.

### Code Example

Here is an example of how to print the current state of a TCP/IP socket in Python:

```python
import socket

# Create a new socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print the current state of the socket
print(socket.getsostate(server_socket))
```

## TCP/IP Socket Errors

---

TCP/IP sockets can raise several types of errors:

- **connection refused**: The remote device refused to establish a connection.
- **connection timed out**: The connection timed out before a response was received.
- **connection reset**: The connection was reset by the remote device.

### Code Example

Here is an example of how to handle errors when using a TCP/IP socket in Python:

```python
import socket

# Create a new socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(("localhost", 12345))
except socket.error as e:
    print(f"Error: {e}")
```

## Raw Sockets

---

Raw sockets are a type of TCP/IP socket that allows you to send and receive raw packets of data.

### Code Example

Here is an example of how to use a raw socket in Python:

```python
import socket

# Create a new raw socket object
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# Send a raw packet of data
raw_socket.sendto(b"Hello, world!", ("localhost", 12345))

# Receive raw data from the socket
data, address = raw_socket.recvfrom(1024)
print(data.decode())
```

## Datagram Sockets

---

Datagram sockets are a type of TCP/IP socket that allows you to send and receive messages of varying sizes.

### Code Example

Here is an example of how to use a datagram socket in Python:

```python
import socket

# Create a new socket object
datagram_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
datagram_socket.sendto(b"Hello, server!", ("localhost", 12345))

# Receive a message from the server
data, address = datagram_socket.recvfrom(1024)
print(data.decode())
```
