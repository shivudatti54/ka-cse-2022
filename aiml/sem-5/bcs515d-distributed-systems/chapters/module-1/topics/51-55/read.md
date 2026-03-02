# **5.1: Introduction to Distributed Systems**

**Definition:** A distributed system is a collection of independent computers that seem like a single, cohesive system to the user. They are connected through communication networks and can share resources, communicate with each other, and work together to achieve a common goal.

**Characteristics:**

- Autonomous: Each node in the system operates independently and makes its own decisions.
- Distributed: The system is spread across multiple locations, which can be geographically dispersed.
- Communication: Nodes in the system communicate with each other to share resources and coordinate actions.
- Parallelism: The system can process multiple tasks simultaneously, improving overall performance.

**Example:** A network of bank ATMs that can work together to process transactions and provide services to customers.

## **5.2: Types of Distributed Systems**

### **1. Client-Server System**

In a client-server system, one node (the server) provides services to multiple nodes (clients) that request resources or services.

**Characteristics:**

- Client: Requests resources or services from the server.
- Server: Provides resources or services to clients.
- Communication: Clients send requests to the server, which responds with the requested resources or services.

**Example:** A web browser (client) requesting information from a web server.

### **2. Peer-to-Peer System**

In a peer-to-peer system, all nodes are equal and can communicate with each other directly.

**Characteristics:**

- All nodes are equal and can communicate with each other.
- No central server or authority exists.
- Communication: Nodes can communicate directly with each other.

**Example:** A network of computers sharing files and resources.

### **3. Distributed Database System**

In a distributed database system, multiple nodes store and manage data in a shared database.

**Characteristics:**

- Multiple nodes store and manage data in a shared database.
- Data is replicated across multiple nodes for redundancy and availability.
- Communication: Nodes communicate with each other to access and update data.

**Example:** A network of databases sharing data and providing services to applications.

## **5.3: Advantages of Distributed Systems**

### **1. Scalability**

Distributed systems can scale horizontally, adding more nodes to handle increased workload.

### **2. High Availability**

Distributed systems can provide high availability, as nodes can continue to function even if one node fails.

### **3. Flexibility**

Distributed systems can be more flexible, as nodes can be added or removed as needed.

### **4. Fault Tolerance**

Distributed systems can provide fault tolerance, as nodes can continue to function even if one node fails.

## **5.4: Challenges of Distributed Systems**

### **1. Communication Overhead**

Distributed systems can experience communication overhead, as nodes need to communicate with each other.

### **2. Synchronization**

Distributed systems can experience synchronization problems, as nodes need to coordinate their actions.

### **3. Security**

Distributed systems can experience security challenges, as nodes need to protect themselves from unauthorized access.

### **4. Complexity**

Distributed systems can be more complex, as nodes need to work together to achieve a common goal.

# **5.5: Conclusion**

Distributed systems offer many benefits, including scalability, high availability, flexibility, and fault tolerance. However, they also present challenges, such as communication overhead, synchronization, security, and complexity. By understanding the characteristics, advantages, and challenges of distributed systems, we can design and implement systems that meet the needs of our applications and users.
