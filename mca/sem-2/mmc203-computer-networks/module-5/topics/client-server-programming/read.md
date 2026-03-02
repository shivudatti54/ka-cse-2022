# Client-Server Programming


## Table of Contents

- [Client-Server Programming](#client-server-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Sockets and Socket Types](#1-sockets-and-socket-types)
  - [2. Java Socket Classes](#2-java-socket-classes)
  - [3. TCP Server Implementation Steps](#3-tcp-server-implementation-steps)
  - [4. TCP Client Implementation Steps](#4-tcp-client-implementation-steps)
  - [5. InetAddress Class](#5-inetaddress-class)
  - [6. Multiple Client Server (Multi-threaded Server)](#6-multiple-client-server-multi-threaded-server)
  - [7. UDP Socket Programming](#7-udp-socket-programming)
- [Examples](#examples)
  - [Example 1: Simple TCP Echo Server](#example-1-simple-tcp-echo-server)
  - [Example 2: TCP Echo Client](#example-2-tcp-echo-client)
  - [Example 3: Multi-client Chat Server](#example-3-multi-client-chat-server)
- [Exam Tips](#exam-tips)

## Introduction

Client-server programming is a fundamental paradigm in network communication that forms the backbone of modern distributed computing and internet applications. This programming model involves two distinct entities: a **client** that initiates requests for services or resources, and a **server** that listens for and responds to these requests. The client-server architecture enables multiple clients to connect to a central server that provides shared resources, data, or computational services.

In the context of 's Computer Science curriculum, client-server programming primarily focuses on **socket programming**, which provides the low-level API for network communication between processes running on different machines. Socket programming allows developers to create network applications using TCP (Transmission Control Protocol) for reliable, connection-oriented communication or UDP (User Datagram Protocol) for faster, connectionless communication. Understanding socket programming is essential for developing various network applications such as web servers, chat applications, file transfer programs, and database connectivity systems. This topic carries significant weightage in examinations, with typically one full question appearing in the question paper.

## Key Concepts

### 1. Sockets and Socket Types

A **socket** is a communication endpoint that allows processes to communicate with each other, either on the same machine or across a network. In Java socket programming, there are two primary types of sockets:

- **TCP Socket (Stream Socket)**: Uses `Socket` class on client side and `ServerSocket` class on server side. Provides reliable, ordered, error-free communication with connection establishment before data transfer.

- **UDP Socket (Datagram Socket)**: Uses `DatagramSocket` class for both client and server. Provides connectionless, unreliable communication without guaranteed delivery or ordering.

### 2. Java Socket Classes

The Java.net package provides the following essential classes for socket programming:

| Class                        | Purpose                                                |
| ---------------------------- | ------------------------------------------------------ |
| `Socket`                     | Client-side TCP socket for connecting to servers       |
| `ServerSocket`               | Server-side socket that listens for client connections |
| `DatagramSocket`             | UDP socket for sending/receiving datagrams             |
| `InetAddress`                | Represents an IP address                               |
| `PrintWriter`                | Character stream output for sending text data          |
| `BufferedReader`             | Character stream input for receiving text data         |
| `InputStream`/`OutputStream` | Byte streams for binary data transfer                  |

### 3. TCP Server Implementation Steps

A TCP server follows these fundamental steps:

1. Create a `ServerSocket` object bound to a specific port number
2. Call `accept()` method to listen for and accept client connections
3. When a client connects, `accept()` returns a `Socket` object for communication
4. Obtain input/output streams from the Socket
5. Read from input stream and write to output stream
6. Close streams and sockets when communication completes

### 4. TCP Client Implementation Steps

A TCP client follows these steps:

1. Create a `Socket` object specifying server IP address and port number
2. Obtain input/output streams from the Socket
3. Write data to output stream (send to server)
4. Read response from input stream (receive from server)
5. Close streams and socket when done

### 5. InetAddress Class

The `InetAddress` class represents an IP address and provides methods to work with addresses:

```java
// Getting local host address
InetAddress addr = InetAddress.getLocalHost();
System.out.println("Host Name: " + addr.getHostName());
System.out.println("IP Address: " + addr.getHostAddress());

// Getting address by name
InetAddress serverAddr = InetAddress.getByName("www.example.com");
```

### 6. Multiple Client Server (Multi-threaded Server)

For handling multiple clients simultaneously, the server must create a new thread for each connected client:

```java
class ClientHandler extends Thread {
 private Socket clientSocket;
 public ClientHandler(Socket socket) {
 this.clientSocket = socket;
 }
 public void run() {
 // Handle client communication
 }
}

// In server code
while (true) {
 Socket clientSocket = serverSocket.accept();
 new ClientHandler(clientSocket).start();
}
```

### 7. UDP Socket Programming

UDP communication uses datagrams instead of streams:

**Server (UDP):**

```java
DatagramSocket serverSocket = new DatagramSocket(9876);
byte[] receiveData = new byte[1024];
DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
serverSocket.receive(receivePacket);
```

**Client (UDP):**

```java
DatagramSocket clientSocket = new DatagramSocket();
InetAddress IPAddress = InetAddress.getByName("localhost");
byte[] sendData = "Hello Server".getBytes();
DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
clientSocket.send(sendPacket);
```

## Examples

### Example 1: Simple TCP Echo Server

**Problem:** Write a Java TCP server that receives a message from client and echoes it back.

**Solution:**

```java
import java.io.*;
import java.net.*;

public class EchoServer {
 public static void main(String[] args) {
 try {
 ServerSocket serverSocket = new ServerSocket(5000);
 System.out.println("Server started. Waiting for clients...");

 Socket clientSocket = serverSocket.accept();
 System.out.println("Client connected: " + clientSocket.getInetAddress());

 // Get streams
 BufferedReader in = new BufferedReader(
 new InputStreamReader(clientSocket.getInputStream()));
 PrintWriter out = new PrintWriter(
 clientSocket.getOutputStream(), true);

 // Read and echo
 String message = in.readLine();
 System.out.println("Received: " + message);
 out.println("Echo: " + message);

 // Close
 in.close();
 out.close();
 clientSocket.close();
 serverSocket.close();
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
}
```

**Step-by-step Explanation:**

1. Server creates ServerSocket on port 5000
2. Calls accept() and waits for client connection
3. When client connects, obtains BufferedReader (input) and PrintWriter (output)
4. Reads message from client, prepends "Echo:" and sends back
5. Closes all resources in reverse order of creation

### Example 2: TCP Echo Client

**Problem:** Write a Java TCP client to connect to the echo server and send a message.

**Solution:**

```java
import java.io.*;
import java.net.*;

public class EchoClient {
 public static void main(String[] args) {
 try {
 // Connect to server
 Socket socket = new Socket("localhost", 5000);
 System.out.println("Connected to server");

 // Get streams
 BufferedReader in = new BufferedReader(
 new InputStreamReader(socket.getInputStream()));
 PrintWriter out = new PrintWriter(
 socket.getOutputStream(), true);

 // Send message
 String message = "Hello Server!";
 out.println(message);
 System.out.println("Sent: " + message);

 // Receive response
 String response = in.readLine();
 System.out.println("Received: " + response);

 // Close
 in.close();
 out.close();
 socket.close();
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
}
```

**Step-by-step Explanation:**

1. Creates Socket connecting to localhost on port 5000
2. Obtains input and output streams similar to server
3. Sends message using println() which sends across network
4. Reads response using readLine()
5. Properly closes all network resources

### Example 3: Multi-client Chat Server

**Problem:** Write a TCP server that handles multiple clients and broadcasts messages to all connected clients.

**Solution:**

```java
import java.io.*;
import java.net.*;
import java.util.Vector;

public class ChatServer {
 static Vector<PrintWriter> clients = new Vector<>();

 public static void main(String[] args) {
 try {
 ServerSocket serverSocket = new ServerSocket(8000);
 System.out.println("Chat Server started on port 8000");

 while (true) {
 Socket clientSocket = serverSocket.accept();
 System.out.println("New client: " + clientSocket.getInetAddress());

 PrintWriter out = new PrintWriter(
 clientSocket.getOutputStream(), true);
 clients.add(out);

 new ClientHandler(clientSocket, out).start();
 }
 } catch (IOException e) {
 e.printStackTrace();
 }
 }

 static class ClientHandler extends Thread {
 private Socket socket;
 private PrintWriter clientOut;

 ClientHandler(Socket s, PrintWriter out) {
 this.socket = s;
 this.clientOut = out;
 }

 public void run() {
 try {
 BufferedReader in = new BufferedReader(
 new InputStreamReader(socket.getInputStream()));
 String message;
 while ((message = in.readLine()) != null) {
 broadcast(message);
 }
 } catch (IOException e) {
 // Client disconnected
 }
 }

 void broadcast(String msg) {
 for (PrintWriter pw : clients) {
 pw.println(msg);
 }
 }
 }
}
```

**Step-by-step Explanation:**

1. Main server creates ServerSocket and enters infinite loop
2. When client connects, creates PrintWriter and adds to Vector
3. Creates new thread for each client to handle communication
4. Thread reads messages and broadcasts to all clients using Vector
5. Vector provides thread-safe storage of client output streams

## Exam Tips

1. **Remember port numbers**: Common ports include 80 (HTTP), 21 (FTP), 23 (Telnet), 5000/8000 (custom servers). Always use available ports above 1024 for custom applications.

2. **TCP vs UDP differences**: TCP is connection-oriented, reliable, ordered, slower; UDP is connectionless, unreliable, faster. Choose based on application needs.

3. **Exception handling**: All socket operations throw `IOException`, so proper try-catch blocks are essential. Don't forget to close resources in finally block.

4. **Order of operations**: Server must call accept() before client connects; client must create Socket before server accepts connection.

5. **Stream closure**: Always close streams in reverse order - close the outer stream first (BufferedReader/PrintWriter) then the Socket.

6. **InetAddress methods**: Know getByName(), getLocalHost(), getHostName(), getHostAddress() - frequently asked in exams.

7. **Multi-threading**: For multiple clients, each client should be handled in a separate thread. The ServerSocket.accept() returns a new Socket for each client.

8. **Input/Output streams**: Remember to use appropriate wrappers - BufferedReader for reading, PrintWriter for writing text data.

9. **UDP packet structure**: Unlike TCP streams, UDP uses DatagramPacket with explicit address and port specifications.

10. **Socket methods**: Know important methods like getInetAddress(), getPort(), getLocalPort(), getInputStream(), getOutputStream().
