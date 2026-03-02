# Remote Procedure Call (RPC) - Summary

## Key Definitions and Concepts

- **RPC (Remote Procedure Call)**: A protocol that enables a program to execute code on a remote system as if it were a local function call
- **Stub**: Client-side proxy that marshals parameters and sends requests to the server
- **Skeleton**: Server-side proxy that unmarshals requests and dispatches to the actual procedure
- **Marshalling**: Converting data structures and parameters into a network-compatible byte stream
- **IDL (Interface Definition Language)**: Language-agnostic specification for defining remote procedure interfaces
- **XDR (External Data Representation)**: Standard format for serializing data across heterogeneous systems
- **Binding**: Process of locating and connecting to the appropriate remote server

## Important Formulas and Concepts

- RPC Call Flow: Client Call → Client Stub → Marshalling → Network → Server Stub → Execution → Response → Unmarshalling → Client Result
- Reliability Semantics: At-most-once (prevents duplicates), At-least-once (guarantees execution), Exactly-once (ideal but complex)

## Key Points

- RPC abstracts network complexity, allowing programmers to write distributed applications without socket programming
- Stubs are generated automatically from IDL specifications, ensuring type safety
- XDR standardizes data representation across different CPU architectures and operating systems
- Binding can be static (compile-time address) or dynamic (runtime lookup via portmapper)
- Synchronous RPC blocks client until response; asynchronous allows concurrent processing
- One-way RPC (fire-and-forget) provides no guarantee of execution
- RPC failures require timeout mechanisms and retry strategies for reliability

## Common Mistakes to Avoid

- Confusing stub with skeleton (client-side vs server-side proxies)
- Assuming RPC is the same as local procedure call (network delays and failures must be handled)
- Forgetting that complex data types require explicit marshalling/unmarshalling
- Not considering failure scenarios in RPC design

## Revision Tips

- Draw the complete RPC architecture diagram and trace a sample call through each component
- Memorize the sequence: Client → Stub → Marshal → Network → Unmarshal → Server → Execute → Response
- Remember that IDL enables language independence while XDR enables system independence
- Focus on understanding when to use each RPC semantics (at-most-once is most common)
