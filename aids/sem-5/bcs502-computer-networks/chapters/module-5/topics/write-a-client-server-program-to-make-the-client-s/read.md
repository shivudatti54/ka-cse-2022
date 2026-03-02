# **Write a Client-Server Program to Make the Client Send the File Name and to Make the Server Send Back the Contents of the Requested File if Present**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Client-Server Architecture](#clients-server-architecture)
3. [Sockets in Python](#sockets-in-python)
4. [Client-Server Program Code](#clients-server-program-code)
5. [Example Use Case](#example-use-case)
6. [Related Concepts](#related-concepts)

## **Introduction**

In computer networks, a client-server architecture is a fundamental concept where a client requests services from a server. In this topic, we will learn how to write a client-server program in Python to send file names from the client to the server and receive the contents of the requested file.

## **Client-Server Architecture**

The client-server architecture consists of two main components:

- **Client**: The client is the device that requests services from the server. It sends requests to the server and receives responses.
- **Server**: The server is the device that provides services to the client. It receives requests from the client and sends responses.

## **Sockets in Python**

In Python, sockets are used to establish communication between the client and server. Sockets are used for both connection-oriented and connectionless communication.

### Connection-Oriented Sockets

Connection-oriented sockets establish a connection between the client and server before data is sent.

### Connectionless Sockets

Connectionless sockets do not establish a connection before data is sent. Instead, data is sent directly to the server.

## **Client-Server Program Code**

Here is an example client-server program in Python that sends file names from the client to the server and receives the contents of the requested file:

### Server Code

```python
import socket
import os

def serve():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print('Waiting for connection...')

    # Accept connection
    client_socket, address = server_socket.accept()

    print('Connected to', address)

    # Receive file name from client
    file_name = client_socket.recv(1024).decode()
    print('Received file name:', file_name)

    # Check if file exists
    if os.path.exists(file_name):
        # Open file and send contents to client
        with open(file_name, 'r') as file:
            contents = file.read()
            client_socket.send(contents.encode())
            print('Sent file contents to client')
    else:
        client_socket.send('File not found'.encode())
        print('Sent file not found message to client')

    # Close sockets
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    serve()
```

### Client Code

```python
import socket

def send_file():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Send file name to server
    file_name = input('Enter file name: ')
    client_socket.send(file_name.encode())
    print('Sent file name to server')

    # Receive file contents from server
    contents = client_socket.recv(1024).decode()
    print('Received file contents:', contents)

    # Close socket
    client_socket.close()

if __name__ == '__main__':
    send_file()
```

## **Example Use Case**

Here's an example use case:

1.  Run the server program.
2.  Run the client program.
3.  Enter the file name when prompted.
4.  The server will send the contents of the requested file to the client.

## **Related Concepts**

- **TCP/IP**: TCP/IP is the protocol suite used for client-server communication.
- **Socket Programming**: Socket programming is the technique used to establish communication between the client and server.
- **File Transfer Protocol (FTP)**: FTP is a protocol used to transfer files between the client and server.

Note: This is a basic example of a client-server program in Python. In a real-world scenario, you would need to handle errors, implement security measures, and add more features as per your requirements.
