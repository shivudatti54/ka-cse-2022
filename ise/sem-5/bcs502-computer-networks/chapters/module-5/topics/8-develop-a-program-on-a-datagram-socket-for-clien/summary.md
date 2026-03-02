# **Datagram Sockets for Client/Server Program**

## **Key Points**

- **Datagram Sockets**: A connectionless socket, where data is sent as a stream of bytes, without guarantee of delivery or order.
- **Client/Server Architecture**: A program with a client and server, where the client sends messages to the server for processing.
- **Socket Programming**: A method of communication between two devices (client and server) using a network.
- **Datagram Sockets in Python**:
  - Use the `socket` module to create a datagram socket.
  - Use `sendto()` to send data to the server.
  - Use `recvfrom()` to receive data from the server.

## **Programming Steps**

1.  **Import the Socket Module**: Import the `socket` module to create a datagram socket.
2.  **Create a Datagram Socket**: Create a datagram socket using the `socket()` function.
3.  **Bind the Socket**: Bind the socket to a specific port using the `bind()` method.
4.  **Listen for Incoming Messages**: Listen for incoming messages using the `listen()` method.
5.  **Send Messages to the Server**: Send messages to the server using the `sendto()` method.
6.  **Receive Messages from the Server**: Receive messages from the server using the `recvfrom()` method.
7.  **Close the Socket**: Close the socket using the `close()` method.

## **Important Formulas and Definitions**

- **Socket Programming Formula**: `socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
- **Datagram Socket Definition**: A connectionless socket, where data is sent as a stream of bytes, without guarantee of delivery or order.
- **Client/Server Architecture Definition**: A program with a client and server, where the client sends messages to the server for processing.

## **Theorems**

- **Socket Programming Theorem**: The socket programming model ensures reliable communication between devices on a network.

## **Revision Tips**

- Focus on the key points, such as datagram sockets, client/server architecture, and socket programming.
- Practice creating a datagram socket and sending/receiving messages between a client and server.
- Review the important formulas, definitions, and theorems related to socket programming.
