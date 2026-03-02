# **Computer Networks Study Material: 2.1 - 2.3**

### 2.1: Network Topology

#### Definition:

Network topology refers to the physical and logical arrangement of devices in a computer network.

#### Types of Network Topology:

- **Bus Topology:** A single cable connects all devices in a linear sequence.
- **Star Topology:** Devices are connected to a central hub or switch.
- **Ring Topology:** Devices are connected in a circular configuration.
- **Mesh Topology:** Each device is connected to every other device.

#### Advantages and Disadvantages:

| **Topology** | **Advantages**                               | **Disadvantages**                         |
| ------------ | -------------------------------------------- | ----------------------------------------- |
| Bus          | Easy to install and maintain, cost-effective | Limited scalability                       |
| Star         | Easy to install, maintain, and troubleshoot  | Central point of failure                  |
| Ring         | High-speed data transfer                     | Limited scalability, difficult to install |
| Mesh         | High availability, scalability               | Expensive, complex installation           |

#### Real-World Example:

A bank's network uses a star topology with a central server connected to multiple workstations through a hub. This setup provides easy maintenance and troubleshooting but may have a single point of failure.

### 2.2: Network Models

#### Definition:

A network model is a simplified representation of a computer network, used for analysis, design, and troubleshooting.

#### Network Models:

- **Physical Model:** Represents the physical components of a network.
- **Logical Model:** Represents the data flow and communication between devices.
- **Network Topology Model:** Represents the physical and logical arrangement of devices.

#### Examples of Network Models:

- **Entity-Relationship Diagram (ERD):** A graphical representation of the logical structure of a network.
- **Data Flow Diagram (DFD):** A visual representation of the data flow and communication between devices.

#### Real-World Example:

An IT department uses a logical model to design and troubleshoot a network. The ERD provides a graphical representation of the logical structure of the network, while the DFD helps identify data flow and communication issues.

### 2.3: Network Protocols

#### Definition:

Network protocols are sets of rules and procedures that govern data communication between devices on a network.

#### Types of Network Protocols:

- **Application Layer Protocols:** Used for data communication between applications (e.g., HTTP, FTP).
- **Transport Layer Protocols:** Ensure reliable data transfer between devices (e.g., TCP, UDP).
- **Network Layer Protocols:** Route data between devices on different networks (e.g., IP, ICMP).
- **Link Layer Protocols:** Manage data transfer between devices on the same network (e.g., Ethernet, Wi-Fi).

#### Real-World Example:

When a user sends an email, the email client uses an application layer protocol (SMTP) to send the email to the mail server. The mail server then uses a transport layer protocol (TCP) to communicate with the recipient's email client.

#### Key Concepts:

- **IP Address:** A unique identifier for each device on a network (IPv4: 32-bit, IPv6: 128-bit).
- **Port Number:** A unique identifier for a specific application or service (e.g., HTTP: 80, FTP: 21).
- **Packet Switching:** A technique used by network protocols to divide data into small packets and transmit them over the network.

#### Key Protocols:

- **TCP (Transmission Control Protocol):** Ensures reliable data transfer between devices.
- **UDP (User Datagram Protocol):** Provides best-effort delivery of data, often used for real-time applications (e.g., video streaming, online gaming).
- **HTTP (Hypertext Transfer Protocol):** A protocol used for data communication between web servers and clients (e.g., web browsers).
