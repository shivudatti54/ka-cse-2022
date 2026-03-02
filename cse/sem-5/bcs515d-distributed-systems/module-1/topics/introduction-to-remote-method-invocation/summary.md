# Introduction to Remote Method Invocation (RMI) - Summary

## Key Definitions and Concepts

- **Remote Method Invocation (RMI)**: A Java API that enables method calls on objects running in different JVMs, possibly on different machines, providing transparent distributed computing.

- **Remote Interface**: An interface extending `java.rmi.Remote` that declares methods callable remotely; all methods must throw `RemoteException`.

- **Stub**: Client-side proxy that represents the remote object, serializes method parameters, sends requests to server, and deserializes responses.

- **Skeleton**: Server-side proxy that receives requests from stubs, unmarshals parameters, invokes the actual implementation, and returns results.

- **RMI Registry**: Naming service (default port 1099) that binds remote objects to names, allowing clients to lookup objects using `Naming` class.

- **Marshaling**: The process of serializing parameters and return values for transmission over the network.

## Important Formulas and Theorems

RMI uses standard Java serialization for parameter passing. The key mechanisms include:

- **UnicastRemoteObject**: Base class for remote objects using point-to-point TCP connections
- **LocateRegistry.createRegistry()**: Creates/returns RMI registry on specified port
- **Naming.bind()**: Binds remote object to a name in registry
- **Naming.lookup()**: Retrieves remote object reference from registry

## Key Points

1. RMI enables object-to-object communication across JVM boundaries using Java's object serialization.

2. The four RMI architecture layers handle different aspects: application logic, proxy generation, reference management, and network transport.

3. All remote methods must throw `RemoteException` to handle potential network failures.

4. The `rmic` compiler generates stub and skeleton classes from implementation classes.

5. RMI uses distributed garbage collection with a lease-based system to clean up unreferenced remote objects.

6. RMI provides location transparency - clients access remote objects using names, not physical addresses.

7. Parameters and return values must be serializable (implement `Serializable` interface).

8. The RMI registry typically runs on port 1099 and can be started programmatically or via command line.

## Common Mistakes to Avoid

1. **Forgetting to extend UnicastRemoteObject**: Remote object implementations must extend this class to become remotely accessible.

2. **Not throwing RemoteException**: All methods in remote interface must declare `throws RemoteException`.

3. **Forgetting to start RMI registry**: Server will fail if registry is not running before binding objects.

4. **Using non-serializable parameters**: Parameters passed to remote methods must implement `Serializable`.

5. **Incorrect URL format**: RMI URLs must use "rmi://" protocol prefix (e.g., "rmi://localhost:1099/ObjectName").

## Revision Tips

1. Practice writing the complete RMI application flow: Interface → Implementation → Server → Client.

2. Remember the sequence: Define Interface → Implement Class → Generate Stub/Skeleton → Start Registry → Run Server → Run Client.

3. Focus on understanding how stubs act as proxies and handle serialization transparently.

4. Review common exam questions on RMI architecture layers and their functions.

5. Memorize key classes: `Remote`, `RemoteException`, `UnicastRemoteObject`, `Naming`, `LocateRegistry`.
