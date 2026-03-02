# Remote Invocation

## Introduction

### Definition

Remote invocation is a technique used in distributed systems to invoke methods or procedures on a remote machine as if they were part of the local system. It allows a client to call a procedure on a server, even if they are not in the same location.

### Key Concepts

- **Client-Server Architecture**: A client requests a service from a server, which then performs the requested operation and returns the result to the client.
- **Distributed Systems**: A collection of interconnected computers that work together to achieve a common goal.
- **Remote Procedure Call (RPC)**: A procedure call mechanism that allows a program to invoke a procedure on a remote machine.

## Request-Reply Protocols

### Definition

Request-reply protocols are used in remote invocation to enable communication between a client and a server. The client sends a request to the server, which then processes the request and sends a reply back to the client.

### Key Components

- **Request**: A message sent from the client to the server, typically containing the procedure to be invoked and any required parameters.
- **Reply**: A message sent from the server to the client, typically containing the result of the invoked procedure.
- **Protocol**: A set of rules governing the format, syntax, and semantics of the request-reply messages.

### Example

Suppose we have a client that wants to invoke a procedure called `addNumbers` on a server, which is running on a different machine. The client sends a request message to the server, containing the procedure name and two numbers to add. The server processes the request, invokes the `addNumbers` procedure, and sends a reply message back to the client, containing the result of the addition.

```markdown
## Request

| Procedure Name: addNumbers |
| Number 1: 5 |
| Number 2: 7 |

## Reply

| Result: 12 |
```

## Remote Procedure Call (RPC)

### Definition

Remote Procedure Call (RPC) is a procedure call mechanism that allows a program to invoke a procedure on a remote machine. It provides a way for a client to call a procedure on a server, even if they are not in the same location.

### Key Components

- **Procedure**: A block of code that performs a specific task.
- **Client**: A program that requests a procedure to be invoked on a server.
- **Server**: A program that provides the procedure to be invoked by the client.
- **RPC Framework**: A set of libraries and protocols that enable RPC.

### Example

Suppose we have a client that wants to invoke a procedure called `getWeather` on a server, which is running on a different machine. The client sends an RPC request to the server, containing the procedure name and any required parameters. The server processes the request, invokes the `getWeather` procedure, and sends a reply message back to the client, containing the result.

```markdown
## Request

| Procedure Name: getWeather |
| Location: New York |

## Reply

| Weather: Sunny |
```

## Introduction to Remote Method Invocation (RMI)

### Definition

Remote Method Invocation (RMI) is a technique used in distributed systems to invoke methods on a remote object as if they were part of the local system. It allows a client to call a method on a remote object, even if they are not in the same location.

### Key Concepts

- **Remote Object**: An object that provides methods that can be invoked remotely.
- **RMI Framework**: A set of libraries and protocols that enable RMI.
- **Stub**: A proxy object that acts as an interface to the remote object.
- **Skeleton**: A server-side object that provides the actual methods to the client.

### Example

Suppose we have a client that wants to invoke a method called `greet` on a remote object, which is running on a different machine. The client creates a stub object, which acts as an interface to the remote object. The client sends a request to the stub object, containing the method name and any required parameters. The stub object forwards the request to the skeleton object, which invokes the `greet` method on the remote object and sends a reply message back to the client.

```markdown
## Client Code

// Create a stub object
Stub stub = new Stub(remoteObject);

// Invoke the greet method
stub.greet("John");
```

```markdown
## Server Code

// Create a skeleton object
Skeleton skeleton = new Skeleton(remoteObject);

// Define the greet method
public void greet(String name) {
System.out.println("Hello, " + name + "!");
}
```

Note: The above server code is a simplified example and may not include all the necessary components of a full-fledged RMI implementation.
