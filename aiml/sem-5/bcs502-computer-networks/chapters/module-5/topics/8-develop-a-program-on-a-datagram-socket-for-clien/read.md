# **Datagram Socket Client/Server Program**

## **Introduction**

In computer networks, Sockets are used to establish communication between two devices. A Datagram socket is a type of socket that allows data to be sent in packets and receives the packets in the same order they were sent. This study material will guide you through the development of a program that uses a datagram socket for client/server communication to display messages on the client side.

## **Key Concepts**

- **Socket**: A socket is an endpoint for communication between two devices (computer, phone, etc.) in a network.
- **Datagram**: A datagram is a single packet of data that is sent over a network.
- **Client/Server Model**: The client-server model is a widely used architecture for networked applications, where one device (the server) provides services to multiple devices (the clients).

## **Client/Server Communication using Datagram Socket**

### Client Side

The client side of the application consists of a program that sends messages to the server.

#### Code Example (Python)

```python
import socket

def send_message():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address and message
    server_address = ('localhost', 12345)
    message = "Hello, server!"

    # Send the message
    client_socket.sendto(message.encode(), server_address)

    # Receive the response
    data, server_address = client_socket.recvfrom(1024)
    print("Server response:", data.decode())

    # Close the socket
    client_socket.close()

# Call the function
send_message()
```

### Server Side

The server side of the application consists of a program that receives messages from the client and displays them.

#### Code Example (Python)

```python
import socket

def receive_messages():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the local address and port
    server_address = ('localhost', 12345)

    # Bind the socket to the address and port
    server_socket.bind(server_address)

    # Receive messages from the client
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print("Client message:", data.decode())

    # Close the socket
    server_socket.close()

# Call the function
receive_messages()
```

### Running the Program

To run the program, follow these steps:

1.  Compile the client and server programs separately.
2.  Run the server program first.
3.  Run the client program.
4.  The client will send a message to the server, which will display the message on the console.

## **Conclusion**

In this study material, we learned how to develop a program using a datagram socket for client/server communication to display messages on the client side. We covered the key concepts of sockets, datagrams, and the client/server model, and provided code examples for both the client and server sides of the application.
