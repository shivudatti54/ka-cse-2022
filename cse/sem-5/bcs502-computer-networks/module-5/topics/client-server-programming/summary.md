# Client-Server Programming - Summary

## Key Definitions and Concepts

- **Socket**: A communication endpoint enabling processes to exchange data across a network
- **ServerSocket**: Java class that creates server-side sockets that listen for client connections on a specified port
- **Socket (Client)**: Java class representing client-side TCP connection to a server
- **TCP (Transmission Control Protocol)**: Connection-oriented protocol providing reliable, ordered, error-checked communication
- **UDP (User Datagram Protocol)**: Connectionless protocol offering faster but unreliable communication
- **InetAddress**: Java class representing an IP address (IPv4 or IPv6)
- **DatagramPacket**: Java class representing UDP packets containing data and destination address
- **Port Number**: 16-bit identifier (0-65535) distinguishing different applications on the same machine

## Important Formulas and Theorems

- **Port Range**: Well-known ports (0-1023), registered ports (1024-49151), dynamic/private ports (49152-65535)
- **Socket Creation**: `new Socket(serverIP, port)` - throws IOException if connection fails
- **Server Binding**: `new ServerSocket(port)` - throws IOException if port is busy
- **Accept Method**: `serverSocket.accept()` - blocks until client connects, returns new Socket for communication
- **Stream Acquisition**: `socket.getInputStream()` and `socket.getOutputStream()` for byte streams
- **UDP Packet**: `new DatagramPacket(buffer, length, address, port)` for sending

## Key Points

- TCP provides reliable, ordered delivery with connection establishment (three-way handshake); UDP is faster but no guarantees
- Server must create ServerSocket and call accept() before clients can connect
- Each client connection creates a new Socket object on the server side
- Multiple clients require multi-threading - each client handled by separate thread
- Always close resources in reverse order of creation: streams first, then sockets
- InetAddress.getLocalHost() returns the local machine's address; getByName() resolves hostname to IP
- UDP uses DatagramPacket instead of streams; each send/receive is independent
- Common ports: 80 (HTTP), 21 (FTP), 23 (Telnet), 5000/8000 (custom applications)
- BufferedReader with InputStreamReader wraps Socket's input stream for efficient text reading
- PrintWriter with autoFlush enabled sends data immediately when println() is called

## Common Mistakes to Avoid

1. **Forgetting to close resources**: Always close streams and sockets to prevent resource leaks; use try-with-resources or finally blocks

2. **Wrong port numbers**: Using privileged ports (below 1024) without admin rights causes exceptions; use ports above 5000 for testing

3. **Not handling IOException**: All socket operations throw checked exceptions; either catch them or declare throws in method signature

4. **Confusing TCP and UDP**: TCP requires accept()/connect() for connection establishment; UDP has no connection concept

5. **Blocking operations**: accept(), receive(), readLine() are blocking calls that wait indefinitely - design accordingly

## Revision Tips

1. Practice writing the basic TCP server-client pair from memory - this is the most common exam question

2. Remember the sequence: Server creates ServerSocket → calls accept() → Client creates Socket → Server obtains streams → Communication → Close

3. Know the exact classes and their packages: all socket classes are in java.net package

4. Understand when to use TCP (reliability needed) vs UDP (speed/cost priority)

5. Review multi-threaded server code - exam questions often ask for handling multiple clients

6. Memorize key methods: accept(), connect(), getInputStream(), getOutputStream(), getInetAddress(), getPort()

7. Go through previous question papers - socket programming consistently appears in Module-5
