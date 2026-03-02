# Remote Procedure Call (RPC)

## Introduction

Remote Procedure Call (RPC) is a fundamental paradigm in distributed computing that allows a program to execute code on a remote system as if it were a local function call. Developed originally by Birrell and Nelson in 1984, RPC abstracts the complexity of network communication, enabling programmers to write distributed applications without dealing with low-level socket programming, data serialization, and inter-process communication details.

In the context of 's Computer Science & Engineering curriculum, RPC represents one of the earliest and most influential middleware technologies that bridges the gap between local and distributed computing. Understanding RPC is essential because it forms the foundation for modern distributed systems, web services, and microservices architectures. Most contemporary distributed frameworks, including CORBA, DCOM, Java RMI, and various web service implementations, trace their origins to the fundamental concepts introduced by RPC.

The importance of RPC in today's computing landscape cannot be overstated. Cloud computing, distributed databases, and service-oriented architectures all rely on principles first established by RPC. When you use cloud storage, stream media, or access distributed applications, RPC mechanisms work behind the scenes to coordinate operations across multiple servers. For a CSE engineer, mastering RPC concepts is crucial for designing and implementing scalable, distributed applications that form the backbone of modern enterprise computing.

## Key Concepts

### Architecture of RPC

The RPC architecture follows a client-server model where the client process initiates a procedure call that executes on a remote server. The entire process involves several distinct phases:

1. **Client Stub Generation**: The client application makes what appears to be a local procedure call. However, this call is actually directed to a client-side stub that packages the procedure parameters.

2. **Parameter Marshalling (Serialization)**: The client stub converts (marshals) the procedure parameters into a standardized format suitable for network transmission. This involves converting complex data structures into a byte stream.

3. **Message Transmission**: The marshalled request is sent across the network to the remote server using transport protocols like TCP or UDP.

4. **Server Stub Processing**: The server receives the request and passes it to the server stub, which unmarshals the parameters and locates the actual procedure to execute.

5. **Procedure Execution**: The server executes the requested procedure using the unmarshalled parameters.

6. **Result Return**: The procedure results are marshalled by the server stub and sent back to the client.

7. **Client Stub Completion**: The client stub unmarshals the results and returns them to the calling client application as if it were a regular function return value.

### Stub and Skeleton

The stub functions as a proxy for the remote procedure on the client side, while the skeleton serves as the corresponding proxy on the server side. Together, they hide all network communication details from the application programmer. Stubs are typically generated automatically from interface definition language (IDL) specifications, making RPC systems type-safe and platform-independent.

### Interface Definition Language (IDL)

IDL serves as a language-agnostic interface specification that defines the data types and procedure signatures available for remote invocation. Popular IDL standards include CORBA IDL, DCE IDL, and Protocol Buffers. The IDL compilation process generates both client and server stubs, ensuring type compatibility across different programming languages and platforms.

### Data Representation and Marshalling

Different systems use different data representations (little-endian vs big-endian, floating-point formats, character encodings). RPC systems employ External Data Representation (XDR) standards to ensure data can be correctly interpreted across heterogeneous systems. Marshalling involves converting data structures into a linear byte sequence, while unmarshalling performs the reverse operation.

### Binding and Location Services

Before making RPC calls, the client must locate the appropriate server. This process, called binding, can be accomplished through several methods:

- **Static Binding**: The client knows the server's network address at compile time
- **Dynamic Binding**: The client queries a registry (like portmap/rpcbind) to locate available servers
- **Message Queues**: Asynchronous RPC using persistent message storage

### RPC Semantics

RPC systems can provide different levels of reliability:

- **At-most-once**: The procedure executes zero or one time, preventing duplicate executions
- **At-least-once**: The procedure executes at least once, but may execute multiple times
- **Exactly-once**: The procedure executes exactly once, combining both delivery guarantees

Most practical RPC implementations aim for at-most-once semantics to prevent duplicate executions that could cause data inconsistency.

### Types of RPC

1. **Synchronous RPC**: The client blocks until it receives the server's response
2. **Asynchronous RPC**: The client continues execution while waiting for the response, often using callbacks or futures
3. **One-way RPC**: The client sends a request but does not wait for any response (fire-and-forget)

## Examples

### Example 1: Simple RPC Call Flow

Consider a banking application where a client needs to check an account balance:

**Step 1: IDL Definition**

```
// bank.idl
struct AccountInfo {
 long account_number;
 string holder_name;
 double balance;
};

program BANKPROG {
 version BANKVERS {
 AccountInfo GET_BALANCE(long) = 1;
 } = 1;
} = 100000;
```

**Step 2: Client Request Processing**

```
// Client Code
AccountInfo info = get_balance(12345);
// Internally performs:
// 1. Pack account_number (12345) into XDR format
// 2. Send RPC request to server at known address
// 3. Wait for response (blocking)
```

**Step 3: Server Processing**

```
// Server receives request
// 1. Unmarshall account_number from request
// 2. Look up account in database
// 3. Create AccountInfo with balance
// 4. Marshall AccountInfo into XDR
// 5. Send response to client
```

**Result**: The client receives the account information as if `get_balance()` were a local function, completely abstracted from network operations.

### Example 2: Parameter Marshalling

Suppose we need to transfer parameters with complex data types:

```
// Complex structure with multiple types
struct TransferRequest {
 long from_account;
 long to_account;
 double amount;
 timestamp trans_time;
};

// Client calling remote transfer
TransferRequest req;
req.from_account = 1001;
req.to_account = 1002;
req.amount = 5000.00;
req.trans_time = current_time();

boolean success = perform_transfer(req);
```

**Marshalling Process**:

1. Convert `from_account` (1001) to 4-byte network order
2. Convert `to_account` (1002) to 4-byte network order
3. Convert `amount` (5000.00) to IEEE 754 double-precision format
4. Convert `trans_time` to 64-bit Unix timestamp
5. Concatenate all fields into a byte stream
6. Append length prefix and checksum

### Example 3: Handling RPC Failures

A robust RPC client must handle network failures gracefully:

```
// Client with failure handling
try {
 AccountInfo info = get_balance(12345);
 display(info.balance);
} catch (RPCException e) {
 // Network unreachable
 if (e.getErrorCode() == RPC_TIMEOUT) {
 // Retry with exponential backoff
 retry_with_backoff();
 } else if (e.getErrorCode() == SERVER_UNAVAILABLE) {
 // Try alternate server
 connect_to_backup_server();
 }
} catch (NetworkException e) {
 // Physical network failure
 notify_user_of_offline_status();
}
```

## Exam Tips

1. **Remember the RPC call flow sequence**: Client stub → Marshalling → Network transmission → Server stub → Execution → Response → Unmarshalling → Client result

2. **Distinguish between stub and skeleton**: Client stub handles client-side serialization; skeleton handles server-side deserialization and procedure dispatch

3. **Understand XDR purpose**: External Data Representation standardizes data format across heterogeneous systems (different architectures and operating systems)

4. **Know RPC reliability semantics**: At-most-once (most common), At-least-once, Exactly-once - understand when each is appropriate

5. **IDL is language-agnostic**: Interface Definition Language defines interfaces independent of programming language, enabling cross-language RPC

6. **Difference between synchronous and asynchronous RPC**: Synchronous blocks the client; asynchronous allows continued execution

7. **Binding is essential before calling**: Clients must locate servers through static or dynamic binding before making RPCs

8. **RPC vs Local Procedure Call**: RPC adds network delay, potential failures, and requires serialization that local calls don't need

9. **Portmapper/rpcbind function**: Maps program numbers to network ports, enabling dynamic server discovery

10. **Timeout and retry mechanisms**: Essential for handling network failures in distributed RPC systems
