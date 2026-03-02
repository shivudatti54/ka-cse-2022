# **Computer Networks**

## **Topic: Client-Server Program**

## **Introduction**

In computer networks, a client-server model is a widely used architecture where a client (requesting entity) sends a request to a server (responding entity) to access specific resources. In this topic, we will explore how to write a client-server program to send file names and receive the contents of the requested file.

## **Definitions**

- **Client**: A program that sends a request to a server to access a specific resource.
- **Server**: A program that responds to a client's request by providing the requested resource.
- **File Name**: The name of a file that contains data.
- **File Contents**: The data stored in a file.

## **Program Requirements**

- Write a client-server program that sends a file name from the client to the server.
- The server should receive the file name and send back the contents of the requested file if present.

## **Program Flow**

1.  The client sends a request to the server with the file name.
2.  The server receives the file name and checks if the file exists on the server.
3.  If the file exists, the server sends back the contents of the file to the client.
4.  If the file does not exist, the server sends a response to the client indicating that the file does not exist.

## **Client-Server Program**

### Server Code (in Python)

```python
# server.py

import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Arbitrary non-privileged port

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept incoming connections
        client_socket, address = server_socket.accept()
        print(f"Connected to {address}")

        # Receive file name from client
        file_name = client_socket.recv(1024).decode()
        print(f"Received file name: {file_name}")

        # Check if file exists
        if file_name in ["file1.txt", "file2.txt"]:
            with open(file_name, "rb") as file:
                file_contents = file.read()
            client_socket.sendall(file_contents)
            print(f"Sent file contents: {file_name}")
        else:
            client_socket.sendall(b"File not found".encode())
            print(f"Sent file not found response: {file_name}")

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
```

### Client Code (in Python)

```python
# client.py

import socket

def start_client():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Arbitrary non-privileged port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    # Send file name to server
    file_name = "file1.txt"
    client_socket.sendall(file_name.encode())
    print(f"Sent file name: {file_name}")

    # Receive file contents from server
    file_contents = client_socket.recv(1024).decode()
    print(f"Received file contents: {file_contents}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
```

## **Example Use Cases**

- Run the server program on your local machine.
- Run the client program on another machine with the same local machine's IP address.
- In the client program, enter the file name ("file1.txt" in this example).
- The client program will send the file name to the server.
- The server program will check if the file exists and send back the contents if present.
- The client program will receive the file contents and print it to the console.

## **Key Concepts**

- Socket programming
- Client-server architecture
- File name and file contents
- Server-side and client-side programming
- Networking fundamentals (IP address, port numbers, etc.)
