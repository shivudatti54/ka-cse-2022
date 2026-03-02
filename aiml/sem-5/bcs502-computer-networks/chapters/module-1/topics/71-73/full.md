# **7.1 – 7.3: Network Topology, Network Models, and Network Protocols**

### 7.1: Network Topology

Network topology refers to the physical or logical arrangement of devices in a network. It describes how devices are connected to each other and the relationships between them. There are several types of network topologies, each with its own strengths and weaknesses.

#### Types of Network Topologies

1. **Bus Topology**
   - A single cable connects all devices in a linear sequence.
   - All devices share the same communication medium.
   - Example: Local Area Network (LAN) using a coaxial cable.
2. **Star Topology**
   - All devices connect to a central device, called a hub or switch.
   - Data transmission occurs between devices and the hub/switch.
   - Example: Many modern LANs use a star topology.
3. **Ring Topology**
   - Devices are connected in a circular configuration.
   - Data transmission occurs in one direction around the ring.
   - Example: Some older LANs used a ring topology.
4. **Mesh Topology**
   - Each device connects to every other device.
   - Data transmission occurs between any two devices.
   - Example: Not commonly used due to its high cost and complexity.
5. **Hybrid Topology**
   - Combines two or more different topologies.
   - Example: A LAN with a star topology for the core and a bus topology for the perimeter.

#### Advantages and Disadvantages of Each Topology

| Topology | Advantages                                      | Disadvantages                                                 |
| -------- | ----------------------------------------------- | ------------------------------------------------------------- |
| Bus      | Easy to install, low cost                       | Difficult to troubleshoot, vulnerable to single-point failure |
| Star     | Centralized management, easy to install         | Dependent on the hub/switch, can be expensive                 |
| Ring     | Provides fault tolerance, easy to install       | Limited scalability, vulnerable to single-point failure       |
| Mesh     | Provides high reliability, easy to manage       | Expensive, complex to install and maintain                    |
| Hybrid   | Combines the advantages of different topologies | Can be complex to install and manage                          |

### 7.2: Network Models

Network models are conceptual representations of a network that help designers and administrators understand how a network functions. There are several network models, each with its own strengths and weaknesses.

#### Types of Network Models

1. **Physical Model**
   - Describes the physical components of a network.
   - Example: A diagram of a network showing the cables, switches, and routers.
2. **Logical Model**
   - Describes the logical components of a network.
   - Example: A diagram of a network showing the devices, protocols, and services.
3. **Conceptual Model**
   - Describes the functions and services provided by a network.
   - Example: A diagram of a network showing the applications, users, and data flows.

#### Advantages and Disadvantages of Each Model

| Model      | Advantages                                                                  | Disadvantages                                                         |
| ---------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Physical   | Provides a clear understanding of the network's physical components         | Can be complex and difficult to update                                |
| Logical    | Provides a clear understanding of the network's logical components          | May not accurately represent the network's functions and services     |
| Conceptual | Provides a high-level understanding of the network's functions and services | May not provide enough detail about the network's physical components |

### 7.3: Network Protocols

Network protocols are sets of rules and procedures that govern how data is transmitted and received over a network. There are several types of network protocols, each with its own strengths and weaknesses.

#### Types of Network Protocols

1. **Transport Layer Protocols**
   - Relied on to establish, maintain, and terminate connections between devices.
   - Example: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
2. **Routing Protocols**
   - Used to determine the best path for data to travel between devices.
   - Example: RIP (Routing Information Protocol), OSPF (Open Shortest Path First).
3. **Network Access Protocols**
   - Used to manage access to the network.
   - Example: DHCP (Dynamic Host Configuration Protocol), PPP (Point-to-Point Protocol).

#### Advantages and Disadvantages of Each Protocol

| Protocol | Advantages                                                            | Disadvantages                          |
| -------- | --------------------------------------------------------------------- | -------------------------------------- |
| TCP      | Provides reliable, error-checked data transfer                        | Can be slow, complex to implement      |
| UDP      | Provides fast, best-effort data transfer                              | May not provide reliable data transfer |
| RIP      | Simple to implement, provides basic routing functionality             | May not provide optimal routing        |
| OSPF     | Provides more advanced routing functionality, supports large networks | Can be complex to implement            |

### Case Study: Network Topology and Protocol Selection

A company is building a new LAN for its employees. The company has 20 employees, and they need to decide on a network topology and protocols.

- Advantages of Star Topology:
  - Easy to install and manage
  - Provides centralized management
- Disadvantages of Star Topology:
  - Dependent on the hub/switch
  - Can be expensive
- Advantages of TCP:
  - Provides reliable, error-checked data transfer
- Disadvantages of TCP:
  - Can be slow
  - Complex to implement

Based on the company's requirements, the company decides to use a star topology with a hub/switch and TCP for data transfer. This provides a reliable, error-checked data transfer while also being easy to install and manage.

### Further Reading

- "Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall
- "Network Protocols: A Programmer's Guide" by Richard Stevens
- "TCP/IP Illustrated" by W. Richard Stevens
- "Routing in Theory and Practice" by John D. Case et al.

### Diagrams

- Figure 7.1: Bus Topology Diagram
- Figure 7.2: Star Topology Diagram
- Figure 7.3: Logical Model of a Network
- Figure 7.4: Transport Layer Protocol Diagram (TCP)
- Figure 7.5: Routing Protocol Diagram (RIP)
