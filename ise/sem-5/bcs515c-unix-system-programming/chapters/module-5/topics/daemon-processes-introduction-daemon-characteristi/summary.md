# **Daemon Processes: Revision Notes**

## **Introduction**

- A daemon process is a program that runs in the background, managing a system resource or providing a service.
- Daemons are also known as background processes or background services.

## **Daemon Characteristics**

- Runs in background, without user interaction.
- Typically runs as a service.
- Managed by system init daemon or process manager.
- Uses system resources, such as I/O devices or network interfaces.

## **Coding Rules**

- Handle errors and exceptions properly.
- Use threading or asynchronous I/O to minimize resource usage.
- Keep code modular and maintainable.
- Follow best practices for coding style and documentation.

## **Error Logging**

- Log errors and exceptions to a file or other logging mechanism.
- Use logging levels (e.g., DEBUG, INFO, ERROR) to categorize log messages.
- Implement logging rotation and archival to manage log size.

## **Client-Server Model**

- A client-server model is used to interact with a daemon process.
- The client sends requests to the daemon, which processes the requests and sends responses back to the client.
- The client-server model is commonly used in networked systems.

## **Important Formulas and Definitions**

- **Process ID (PID):** a unique identifier for a process.
- **Session ID (SID):** a unique identifier for a user session.
- **Socket:** a endpoint for communication between two processes.
- **Inter-Process Communication (IPC):** a mechanism for communication between processes.

**Theorem:**
Any daemon process must be designed to:

- Run indefinitely, without interruption.
- Use system resources efficiently.
- Handle errors and exceptions properly.
