# REMOTE INVOCATION

### Introduction

- Remote invocation is a fundamental concept in distributed systems, enabling communication between distributed components.
- It allows a program to execute a procedure or function on a remote system.

### Request-Reply Protocols

- A request-reply protocol is a communication model where a client sends a request to a server and receives a response.
- Characteristics:
  - Asynchronous communication
  - Single-round trip
  - Server is the source of response

### Remote Procedure Call (RPC)

- RPC is a remote procedure invocation mechanism that allows a program to execute a procedure on a remote system.
- Characteristics:
  - Client initiates request
  - Server processes request and returns result
  - Supports multiple communication protocols (e.g., TCP, UDP)

### Introduction to Remote Method Invocation

- Remote method invocation (RMI) is a technique for remote procedure call in object-oriented programming.
- Characteristics:
  - Enables remote invocation of methods on remote objects
  - Uses RPC or request-reply protocols to communicate between clients and servers
  - Supports polymorphism and encapsulation

### Important Formulas, Definitions, and Theorems

- Definition: Remote invocation is the ability of a program to execute a procedure or function on a remote system.
- Theorem: The Remote Procedure Call (RPC) model is an abstraction of the request-reply protocol.
- Formula: RPC latency = round-trip time + processing time + communication time

### Key Concepts

- Asynchronous communication
- Single-round trip
- Server-based response
- Client-initiated request
- Remote object invocation
- Polymorphism and encapsulation support
