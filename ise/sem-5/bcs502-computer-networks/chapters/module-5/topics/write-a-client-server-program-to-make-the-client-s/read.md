# **Computer Networks**

**Module:** @#@#@#@#
**Topic:** Client-Server Program for File Sharing
**Date:** 12082024
**Study Material:**

## **Introduction**

In computer networks, client-server architecture is a widely used model where a client machine requests services from a server machine. In this topic, we will explore how to create a client-server program to share files between the client and server.

## **Client-Server Architecture**

A client-server architecture consists of two types of machines:

- **Client:** A machine that requests services from a server.
- **Server:** A machine that provides services to clients.

**Key Components:**

- **Client:** Sends a request to the server.
- **Server:** Receives the request, processes it, and sends the response back to the client.

## **Sockets and TCP/IP**

To establish a connection between the client and server, we use sockets and TCP/IP protocols.

- **Sockets:** A socket is a endpoint for communication between two devices (client and server) in a network.
- **TCP/IP:** TCP/IP (Transmission Control Protocol/Internet Protocol) is a suite of protocols used for communication over the internet.

## **Client-Server Program for File Sharing**

To create a client-server program for file sharing, we will use Python programming language.

### Server Code

```python
import socket
import os

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port number
    server_socket.bind(('127.0.0.1', 12345))

    # Listen for incoming connections
    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    # Accept incoming connections
    client_socket, address = server_socket.accept()

    print(f"Connection from {address} has been established.")

    # Receive file name from client
    file_name = client_socket.recv(1024).decode('utf-8')

    print(f"Received file name: {file_name}")

    # Check if file exists
    if os.path.exists(file_name):
        # Send file contents to client
        with open(file_name, 'rb') as file:
            file_contents = file.read()

        client_socket.send(file_contents)

        print("File contents sent successfully.")
    else:
        print("File not found.")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_server()
```

### Client Code

```python
import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 12345))

    # Send file name to server
    file_name = input("Enter the file name: ")
    client_socket.send(file_name.encode('utf-8'))

    # Receive file contents from server
    file_contents = client_socket.recv(1024)

    print("Received file contents:")
    print(file_contents.decode('utf-8'))

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
```

**How to Run the Program:**

1.  Run the server program first.
2.  Run the client program.
3.  Enter the file name when prompted.
4.  The client will receive the file contents from the server.

**Key Concepts:**

- **Sockets:** Endpoints for communication between devices in a network.
- **TCP/IP:** Protocol suite for communication over the internet.
- **Client-Server Architecture:** Model where a client machine requests services from a server machine.
- **File Sharing:** Program that allows clients to request and receive files from a server.
