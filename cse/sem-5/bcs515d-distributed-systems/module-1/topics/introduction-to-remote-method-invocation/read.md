# Introduction to Remote Method Invocation (RMI)

## Introduction

Remote Method Invocation (RMI) is a Java-based API that allows an object running in one Java Virtual Machine (JVM) to invoke methods on an object running in a different JVM, possibly on different machines. RMI enables the development of distributed Java applications by providing transparent remote communication between objects, making it appear as if all objects are running within the same JVM.

RMI is a fundamental technology in distributed computing that follows the remote procedure call (RPC) model but is specifically designed for object-oriented Java programs. Introduced in JDK 1.1, RMI has evolved to become a key mechanism for building client-server applications in Java. It allows developers to write distributed programs using the same syntax and semantics as local method calls, thereby simplifying the complexity of network programming.

The importance of RMI in modern computing cannot be overstated. It forms the backbone of many enterprise applications, enables microservices communication, and serves as the foundation for more complex distributed frameworks. Understanding RMI is crucial for CSE students as it provides insights into how distributed systems work, how network communication is abstracted, and how object-oriented principles can be extended across network boundaries.

## Key Concepts

### Architecture of RMI

RMI follows a layered architecture that handles the complexity of network communication:

1. **Application Layer**: Contains the actual remote interfaces and implementations that users define and use.

2. **Stub and Skeleton Layer**: Acts as the proxy for remote objects. The stub (client-side) acts as a proxy for the remote object, while the skeleton (server-side) is responsible for dispatching calls to the actual remote implementation.

3. **Remote Reference Layer**: Manages references to remote objects and handles remote object invocation semantics.

4. **Transport Layer**: Handles the actual network communication, using TCP/IP connections between client and server.

### Components of RMI

**Remote Interface**: Every remote object must implement a remote interface that extends `java.rmi.Remote`. This interface declares the methods that can be invoked remotely. All remote methods must throw `RemoteException` to handle network failures.

**Remote Object Implementation**: The actual implementation class that provides the functionality. It must extend `UnicastRemoteObject` (or another remote object implementation) and implement the remote interface.

**Stub**: A client-side proxy that represents the remote object. It serializes the method parameters, sends the request to the server, receives the results, and deserializes the return values.

**Skeleton**: A server-side proxy that receives requests from stubs, unmarshals the parameters, invokes the actual implementation, and returns the results.

**RMI Registry**: A naming service that allows clients to look up remote objects by name. The registry runs on the server and maintains a mapping between object names and remote object references.

### RMI Registry

The RMI registry is a simple naming service that binds remote objects to names. Clients can look up objects by their names using the `Naming` class. The registry typically runs on port 1099 by default. Key methods include:

- `bind(String name, Remote obj)`: Binds a name to a remote object
- `rebind(String name, Remote obj)`: Rebinds a name (useful for updating)
- `lookup(String name)`: Retrieves a remote object reference
- `unbind(String name)`: Removes the binding

### Working Mechanism of RMI

The RMI mechanism works through a series of carefully orchestrated steps:

1. **Server Setup**: The server creates a remote object implementation and registers it with the RMI registry using a name.

2. **Client Lookup**: The client uses the `Naming.lookup()` method to obtain a reference to the remote object from the registry.

3. **Stub Creation**: When the client requests the remote object, the registry returns the stub object (serialized reference).

4. **Method Invocation**: The client calls methods on the stub as if it were the actual object.

5. **Parameter Marshaling**: The stub serializes (marshals) the method parameters and sends them over the network to the skeleton.

6. **Server Processing**: The skeleton receives the request, unmarshals the parameters, and invokes the actual method on the remote object.

7. **Result Return**: The return value is serialized and sent back to the stub, which deserializes and returns it to the client.

### Steps to Create an RMI Application

1. **Define Remote Interface**: Create an interface extending `Remote` and declare all methods that will be accessed remotely.

2. **Implement Remote Object**: Create a class that implements the remote interface and extends `UnicastRemoteObject`.

3. **Create Server Program**: Instantiate the remote object and bind it to the RMI registry.

4. **Create Client Program**: Use `Naming.lookup()` to obtain the remote object reference and invoke methods.

5. **Generate Stub and Skeleton**: Use the `rmic` compiler to generate stub and skeleton classes.

6. **Start Registry and Run**: Start the RMI registry, then run the server and client programs.

### Garbage Collection in RMI

RMI includes a distributed garbage collector (DGC) that automatically cleans up remote objects when they are no longer referenced. It uses a lease-based system where remote objects are given a lease time, and clients must renew these leases periodically to keep the objects alive.

## Examples

### Example 1: Simple Calculator Remote Object

**Step 1: Define Remote Interface (Calculator.java)**

```java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {
 int add(int a, int b) throws RemoteException;
 int subtract(int a, int b) throws RemoteException;
 int multiply(int a, int b) throws RemoteException;
 int divide(int a, int b) throws RemoteException;
}
```

**Step 2: Implement Remote Object (CalculatorImpl.java)**

```java
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalculatorImpl extends UnicastRemoteObject implements Calculator {

 public CalculatorImpl() throws RemoteException {
 super();
 }

 @Override
 public int add(int a, int b) throws RemoteException {
 return a + b;
 }

 @Override
 public int subtract(int a, int b) throws RemoteException {
 return a - b;
 }

 @Override
 public int multiply(int a, int b) throws RemoteException {
 return a * b;
 }

 @Override
 public int divide(int a, int b) throws RemoteException {
 if (b == 0) {
 throw new RemoteException("Division by zero not allowed");
 }
 return a / b;
 }
}
```

**Step 3: Create Server (CalculatorServer.java)**

```java
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class CalculatorServer {
 public static void main(String[] args) {
 try {
 // Create remote object
 CalculatorImpl calculator = new CalculatorImpl();

 // Create registry on port 1099
 LocateRegistry.createRegistry(1099);

 // Bind the remote object to the registry
 Naming.bind("rmi://localhost:1099/CalculatorService", calculator);

 System.out.println("Server is ready and waiting for clients...");
 } catch (Exception e) {
 e.printStackTrace();
 }
 }
}
```

**Step 4: Create Client (CalculatorClient.java)**

```java
import java.rmi.Naming;

public class CalculatorClient {
 public static void main(String[] args) {
 try {
 // Look up the remote object
 Calculator calculator = (Calculator) Naming.lookup("rmi://localhost:1099/CalculatorService");

 // Invoke remote methods
 System.out.println("Addition: 10 + 5 = " + calculator.add(10, 5));
 System.out.println("Subtraction: 10 - 5 = " + calculator.subtract(10, 5));
 System.out.println("Multiplication: 10 * 5 = " + calculator.multiply(10, 5));
 System.out.println("Division: 10 / 5 = " + calculator.divide(10, 5));

 } catch (Exception e) {
 e.printStackTrace();
 }
 }
}
```

### Example 2: Handling Remote Exceptions and Callbacks

```java
// Remote interface with callback support
public interface CallbackInterface extends Remote {
 void notifyClient(String message) throws RemoteException;
}

// Server implementation with callback
public class NotificationServiceImpl extends UnicastRemoteObject
 implements CallbackInterface {

 public NotificationServiceImpl() throws RemoteException {
 super();
 }

 @Override
 public void notifyClient(String message) throws RemoteException {
 System.out.println("Notification received: " + message);
 }

 // Method that performs work and notifies client
 public void processTask(CallbackInterface callback) throws RemoteException {
 // Perform some task
 System.out.println("Processing task...");

 // Notify client upon completion
 callback.notifyClient("Task completed successfully!");
 }
}
```

## Exam Tips

1. **Remember RMI Architecture Layers**: The four layers - Application, Stub/Skeleton, Remote Reference, and Transport - are frequently asked in exams. Know the function of each layer.

2. **Key Difference Between Stub and Skeleton**: Stub is client-side proxy that marshals requests; skeleton is server-side proxy that unmarshals requests and dispatches to implementation.

3. **Remote Interface Requirements**: Always remember that remote interfaces must extend `Remote` marker interface, and all methods must throw `RemoteException`.

4. **RMI Registry Port**: Default port 1099 is important. Understand how `Naming.bind()` and `Naming.lookup()` work.

5. **Serialization in RMI**: Parameters and return values are serialized (marshaled) automatically. Only serializable objects can be passed as parameters.

6. **rmic Compiler**: The `rmic` tool generates stub and skeleton classes from the implementation class. This is a common exam question.

7. **UnicastRemoteObject**: Remember that remote objects typically extend `UnicastRemoteObject` to become remotely accessible via TCP.

8. **Advantages of RMI**: Transparent location transparency, type safety, object passing, automatic serialization, and garbage collection for remote objects.

9. **Limitations**: RMI is Java-only, has performance overhead, and is not suitable for high-performance distributed computing compared to modern frameworks.

10. **Common Errors**: Remember to start the RMI registry before running the server (`start rmiregistry` or `LocateRegistry.createRegistry()`).
