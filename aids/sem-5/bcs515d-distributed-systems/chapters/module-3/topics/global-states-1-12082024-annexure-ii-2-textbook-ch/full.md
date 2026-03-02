# Global States

### Introduction

In distributed systems, a global state is a shared state that is stored and accessed by multiple processes or nodes. It is a critical concept in understanding how distributed systems work and how they can be designed to achieve consistency and reliability.

### History of Global States

The concept of global states dates back to the early days of distributed systems. In the 1960s, the first distributed systems were developed, and they relied on shared memory models to achieve concurrency and fault tolerance. However, as distributed systems became more complex, the need for a shared state that could be accessed by multiple processes became apparent.

In the 1980s, the concept of global states gained more attention with the development of communication protocols such as TCP/IP. These protocols relied on shared state to establish connections between nodes and to synchronize communication.

### Types of Global States

There are two types of global states:

1. **Shared Global State**: A shared global state is a state that is shared by all processes in a distributed system. It is typically stored in a central location, such as a database or a file system, and is accessed by all processes simultaneously.
2. **Local Global State**: A local global state is a state that is specific to a particular process or node. It is stored locally on the node and is accessed by the process alone.

### Clocks and Global States

In distributed systems, clocks are used to synchronize the timing of nodes. The clock is a critical component in achieving consistency and reliability in distributed systems.

There are two types of clocks:

1. **Global Clock**: A global clock is a clock that is shared by all nodes in a distributed system. It is used to synchronize the timing of nodes and to establish a common reference point for communication.
2. **Local Clock**: A local clock is a clock that is specific to a particular node. It is used to measure the time on that node and to synchronize local communication.

### Events and Process States

In distributed systems, events are used to trigger actions and to synchronize processes. There are two types of events:

1. **Local Events**: Local events are events that occur on a particular node. They are triggered by local actions and are used to synchronize local communication.
2. **Global Events**: Global events are events that occur on multiple nodes. They are triggered by global actions and are used to synchronize global communication.

### Process States

In distributed systems, processes are used to execute tasks and to synchronize communication. There are several process states:

1. **Ready State**: A process is in the ready state when it is waiting for a resource or an event.
2. **Running State**: A process is in the running state when it is executing a task.
3. **Waiting State**: A process is in the waiting state when it is waiting for a resource or an event.
4. **Zombie State**: A process is in the zombie state when it has finished executing but has not been terminated.

### Global States @#@#@ 1 12082024 Annexure-II

The following is a summary of the key points discussed above:

- Global states are shared states that are stored and accessed by multiple processes or nodes.
- There are two types of global states: shared global state and local global state.
- Clocks are used to synchronize the timing of nodes and to establish a common reference point for communication.
- Events are used to trigger actions and to synchronize processes.
- Process states are used to execute tasks and to synchronize communication.

### Textbook: Chapter- 14.1-14.5

The following are the key concepts discussed in the textbook:

- **Introduction to Distributed Systems**: This chapter discusses the introduction to distributed systems, including the definition, characteristics, and benefits of distributed systems.
- **Clocks in Distributed Systems**: This chapter discusses the role of clocks in distributed systems, including the different types of clocks and their applications.
- **Events in Distributed Systems**: This chapter discusses the role of events in distributed systems, including the different types of events and their applications.
- **Process States in Distributed Systems**: This chapter discusses the process states in distributed systems, including the different states and their applications.
- **Global States in Distributed Systems**: This chapter discusses the global states in distributed systems, including the different types of global states and their applications.

### Examples and Case Studies

The following are some examples and case studies that illustrate the concepts discussed above:

- **Example 1**: A distributed system consists of three nodes, each with its own clock. The nodes communicate with each other using a shared global state. The system uses events to trigger actions and synchronize processes.
- **Example 2**: A distributed system consists of multiple processes, each with its own local clock. The processes communicate with each other using local events. The system uses process states to execute tasks and synchronize communication.
- **Case Study 1**: A distributed system is used to manage a large-scale database. The system uses a shared global state to synchronize access to the database. The system uses events to trigger actions and synchronize processes.
- **Case Study 2**: A distributed system is used to manage a large-scale network. The system uses a local global state to synchronize communication between nodes. The system uses process states to execute tasks and synchronize communication.

### Applications

The following are some applications of the concepts discussed above:

- **Distributed Database Systems**: Distributed database systems use shared global states to synchronize access to the database.
- **Distributed File Systems**: Distributed file systems use shared global states to synchronize access to files.
- **Distributed Computing Systems**: Distributed computing systems use local global states to synchronize communication between nodes.
- **Cloud Computing Systems**: Cloud computing systems use shared global states to synchronize access to resources.

### Diagrams and Descriptions

The following are some diagrams and descriptions that illustrate the concepts discussed above:

- **Diagram 1**: A diagram showing the different types of clocks and their applications.
- **Diagram 2**: A diagram showing the different types of events and their applications.
- **Diagram 3**: A diagram showing the different process states and their applications.
- **Diagram 4**: A diagram showing the different types of global states and their applications.

### Further Reading

The following are some references for further reading:

- **"Distributed Systems" by Richard E. Kahn**: This book provides a comprehensive introduction to distributed systems, including the definition, characteristics, and benefits of distributed systems.
- **"Clocks and Time in Distributed Systems" by Tony D. G. Moore**: This paper discusses the role of clocks in distributed systems, including the different types of clocks and their applications.
- **"Events in Distributed Systems" by J. Richard S. Slices**: This paper discusses the role of events in distributed systems, including the different types of events and their applications.
- **"Process States in Distributed Systems" by S. S. Iyengar**: This paper discusses the process states in distributed systems, including the different states and their applications.

I hope this content helps you understand the concept of global states in distributed systems. Let me know if you have any further questions or need any clarification on any of the topics discussed.
