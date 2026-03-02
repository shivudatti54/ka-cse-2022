# REMOTE INVOCATION

### Introduction

- Remote Invocation: a method of invocation where a procedure or method is invoked on a remote object
- Enables communication between distributed systems
- Key characteristics: request-reply, asynchronous, and bounded response time

### Request-Reply Protocols

- Request-reply protocols:
  - Client sends a request to a server
  - Server processes the request and sends a response back to the client
- Common request-reply protocols:
  - RPC (Remote Procedure Call)
  - CORBA (Common Object Request Broker Architecture)
  - RMI (Remote Method Invocation)

### Remote Procedure Call (RPC)

- RPC:
  - A procedure call is made on a remote object as if it were local
  - The procedure call includes the procedure name, arguments, and return type
  - The remote procedure call is acknowledged by the remote object and a response is sent back
- Key benefits:
  - Enables distributed systems to communicate
  - Allows for modular and reusable code

### Introduction to Remote Method Invocation (RMI)

- RMI:
  - A programming technique that allows objects to communicate with each other remotely
  - Objects can be distributed across a network and invoke each other's methods
- Key benefits:
  - Enables modular and reusable code
  - Allows for distributed systems to communicate and collaborate

## Important Formulas and Definitions:

- **Definition of RPC**: A procedure call is made on a remote object as if it were local.
- **Definition of RMI**: A programming technique that allows objects to communicate with each other remotely.

## Theorems:

- **Theorem of RPC**: If a procedure call is made on a remote object, the response time is bounded by the round-trip time of the communication network.
- **Theorem of RMI**: If two objects communicate with each other using RMI, the communication latency is bounded by the latency of the network.
