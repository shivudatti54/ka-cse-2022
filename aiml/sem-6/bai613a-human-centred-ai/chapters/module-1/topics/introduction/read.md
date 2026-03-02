# Introduction to Distributed Systems: Characterization and Remote Invocation

## 1. Characterization of Distributed Systems

### 1.1 Introduction
A **distributed system** is a collection of independent computers that appears to its users as a single coherent system. These computers, often referred to as *nodes* or *hosts*, are connected through a network and coordinate their actions by passing messages. The key goal is to share resources and provide integrated services to users.

**Key Definition:** "A distributed system is one in which components located at networked computers communicate and coordinate their actions only by passing messages." - Coulouris, Dollimore, Kindberg, and Blair

### 1.2 Focus on Resource Sharing
Resource sharing is the fundamental motivation behind distributed systems. This includes sharing:
- **Hardware resources** (e.g., printers, storage, processors)
- **Software resources** (e.g., applications, databases, files)
- **Data and information** (e.g., web pages, documents)

The **client-server model** is a common architecture for resource sharing:
```
+--------+      Request      +---------+
| Client | ----------------->| Server  |
|        | <-----------------|         |
+--------+      Response     +---------+
```

The **peer-to-peer model** is an alternative where all nodes act as both clients and servers:
```
+---------+    +---------+    +---------+
|  Peer   |----|  Peer   |----|  Peer   |
|   A     |    |   B     |    |   C     |
+---------+    +---------+    +---------+
      |            |            |
      +-------------------------+
```

### 1.3 Challenges in Distributed Systems
Distributed systems face several unique challenges:

| Challenge | Description | Example |
|-----------|-------------|---------|
| **Heterogeneity** | Systems differ in hardware, OS, programming languages | Integrating Windows and Linux systems |
| **Concurrency** | Multiple clients access shared resources simultaneously | Multiple users editing the same document |
| **Openness** | System can be extended and implemented in various ways | Adding new services to the web |
| **Security** | Protecting resources from unauthorized access | Secure online banking transactions |
| **Scalability** | System can handle growth in users and resources | Supporting millions of users on social media |
| **Failure Handling** | System continues operating despite component failures | Website remaining available if one server fails |
| **Transparency** | System hides complexity from users | User doesn't know which server fulfilled their request |

**Transparency Types:**
- Access: Hide differences in data representation
- Location: Hide where resource is located
- Migration: Hide that resource may move
- Relocation: Hide that resource may move while in use
- Replication: Hide that multiple copies exist
- Concurrency: Hide that resource may be shared
- Failure: Hide failure and recovery of components

## 2. Remote Invocation

### 2.1 Introduction
Remote invocation enables processes on different machines to communicate and invoke procedures/methods on each other. It's the foundation for building distributed applications.

### 2.2 Request-Reply Protocols
Request-reply protocols provide a pattern for communication between clients and servers:

```
Client:
1. Create request message
2. Send to server
3. Wait for reply
4. Process reply

Server:
1. Wait for request
2. Process request
3. Create reply message
4. Send reply to client
```

**Message Structure:**
```
+----------------+----------------+----------------+
|  Message Type  |  Request ID   |     Data       |
| (Request/Reply) |  (for matching)|  (Parameters)  |
+----------------+----------------+----------------+
```

### 2.3 Remote Procedure Call (RPC)
RPC allows a program to call a procedure on a remote server as if it were a local procedure.

**RPC Mechanism:**
```
+---------------------+          +---------------------+
|    Client Machine   |          |    Server Machine   |
| +----------------+ |          | +----------------+ |
| | Client Process | |          | | Server Process | |
| | +------------+ | |          | | +------------+ | |
| | | Client Stub| | |          | | | Server Stub| | |
| | +------------+ | |          | | +------------+ | |
| +----------------+ |          | +----------------+ |
+---------------------+          +---------------------+
         |                                  |
         |  1. Call local stub procedure   |
         | ------------------------------> |
         |                                  |
         |  2. Marshal parameters          |
         | ------------------------------> |
         |                                  |
         |  3. Send message to server      |
         | ==============================> |
         |                                  |
         |  4. Unmarshal parameters        |
         | ------------------------------> |
         |                                  |
         |  5. Call actual procedure       |
         | ------------------------------> |
         |                                  |
         |  6. Execute procedure           |
         |                                  |
         |  7. Marshal return values       |
         | <------------------------------ |
         |                                  |
         |  8. Send reply to client        |
         | <============================== |
         |                                  |
         |  9. Unmarshal return values     |
         | <------------------------------ |
         |                                  |
         | 10. Return to client process    |
         | <------------------------------ |
```

**Key RPC Components:**
- **Client Stub:** Represents the server procedure on the client side
- **Server Stub:** Represents the client on the server side
- **Marshalling:** Packaging parameters into a message
- **Unmarshalling:** Extracting parameters from a message

**RPC Issues:**
- Parameter passing (value vs. reference)
- Data representation differences
- Error handling (network vs. application errors)
- Performance overhead

### 2.4 Introduction to Remote Method Invocation (RMI)
RMI extends the RPC concept to object-oriented systems, allowing invocation of methods on remote objects.

**RMI vs RPC:**
| Aspect | RPC | RMI |
|--------|-----|-----|
| Paradigm | Procedural | Object-oriented |
| Unit | Procedures | Objects/Methods |
| Parameters | Simple data types | Objects (may need serialization) |
| Location | Server | Remote object |
| Binding | Interface | Object reference |

**Java RMI Example:**
```java
// Define remote interface
public interface Calculator extends Remote {
    public int add(int a, int b) throws RemoteException;
}

// Implement remote object
public class CalculatorImpl extends UnicastRemoteObject implements Calculator {
    public CalculatorImpl() throws RemoteException {}
    public int add(int a, int b) { return a + b; }
}

// Client usage
Calculator calc = (Calculator) Naming.lookup("rmi://server/Calculator");
int result = calc.add(5, 3);
```

## 3. Exam Tips
1. **Understand the key characteristics** of distributed systems and be able to explain each with examples
2. **Differentiate between transparency types** - create a mnemonic to remember all 7 types
3. **Draw and explain the RPC process** - practice drawing the diagram and explaining each step
4. **Compare RPC and RMI** - focus on their differences in paradigm and implementation
5. **Remember the challenges** - be prepared to discuss how each challenge affects system design
6. **Use specific examples** - when explaining concepts, use real-world examples like web browsing, cloud services, or distributed databases