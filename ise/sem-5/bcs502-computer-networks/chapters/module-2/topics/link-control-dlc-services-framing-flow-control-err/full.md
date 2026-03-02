# Link Control: DLC Services

## Introduction

The Data Link Layer (DLL) is the second layer of the OSI model and is responsible for providing reliable data transfer between two devices on the same network. The DLL provides several services that ensure error-free data transfer, including framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols. In this section, we will dive deeper into each of these services and explore their historical context, applications, and modern developments.

### Framing

Framing is the process of adding headers and trailers to data frames to provide them with the necessary information to be transmitted over the network. The frame header contains control information such as source and destination MAC addresses, frame type (e.g., packet or frame), and error-checking codes.

**Frame Structure:**

| Field                   | Description                               |
| ----------------------- | ----------------------------------------- |
| Source MAC Address      | The MAC address of the sender             |
| Destination MAC Address | The MAC address of the receiver           |
| Frame Type              | The type of frame (e.g., packet or frame) |
| Error-Checking Code     | A code used to detect and correct errors  |
| Data                    | The actual data being transmitted         |

Example of a Frame Structure:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Frame Type |
| Address | MAC Address | |
+---------------+---------------+---------------+
| Error-Checking| Data | |
| Code | | |
+---------------+---------------+---------------+
```

### Flow Control

Flow control is the process of regulating the amount of data that can be transmitted between two devices to prevent network congestion and collisions. There are two types of flow control:

- **Connectionless Flow Control:** This type of flow control uses a packet-based approach to regulate data transmission. The sender sends packets with a sequence number to the receiver, who responds with an acknowledgement packet to indicate that the packet was received correctly.
- **Connection-Oriented Flow Control:** This type of flow control uses a connection-oriented approach to regulate data transmission. The sender and receiver establish a connection before data transmission begins, and the receiver sends back the amount of data that can be safely received without error.

**Flow Control Algorithms:**

- **CART (Cyclic Redundancy Check Algorithm for Transmission)**: This algorithm uses a cyclic redundancy check (CRC) to detect errors in data transmission.
- **SLIP (Serial Line Interface Protocol)**: This algorithm uses a packet-based approach to regulate data transmission over serial lines.

Example of Flow Control:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Acknowledgement|
| Address | MAC Address | Packet |
+---------------+---------------+---------------+
```

### Error Control

Error control is the process of detecting and correcting errors that occur during data transmission. There are two types of error control:

- **Connectionless Error Control:** This type of error control uses a packet-based approach to detect and correct errors. The sender sends packets with error-checking codes, which are used to detect and correct errors.
- **Connection-Oriented Error Control:** This type of error control uses a connection-oriented approach to detect and correct errors. The sender and receiver establish a connection before data transmission begins, and the receiver sends back the amount of data that can be safely received without error.

**Error Control Algorithms:**

- **Cyclic Redundancy Check (CRC):** This algorithm uses a CRC to detect errors in data transmission.
- **Forward Error Correction (FEC):** This algorithm uses a FEC to detect and correct errors in data transmission.

Example of Error Control:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Error-Checking|
| Address | MAC Address | Code |
+---------------+---------------+---------------+
```

### Connectionless and Connection-Oriented Protocols

Connectionless protocols, such as ping and traceroute, do not establish a connection before data transmission begins. Connection-oriented protocols, such as TCP and UDP, establish a connection before data transmission begins.

**Connectionless Protocols:**

- **Ping:** This protocol sends packets to a destination IP address and measures the time it takes for the packets to return.
- **Traceroute:** This protocol sends packets to a destination IP address and measures the time it takes for the packets to return, along with the IP address of each router that the packets pass through.

**Connection-Oriented Protocols:**

- **TCP (Transmission Control Protocol):** This protocol establishes a connection before data transmission begins and ensures that data is delivered reliably.
- **UDP (User Datagram Protocol):** This protocol establishes a connection before data transmission begins but does not ensure that data is delivered reliably.

Example of Connectionless and Connection-Oriented Protocols:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Protocol |
| Address | MAC Address | |
+---------------+---------------+---------------+
```

## Data Link Layer Protocols

The data link layer protocols are used to regulate data transmission and ensure reliable data transfer. Some common data link layer protocols include:

- **Ethernet:** This protocol is used to transmit data over Ethernet networks.
- **Token Ring:** This protocol is used to transmit data over Token Ring networks.
- **FDDI (Fiber Distributed Data Interface):** This protocol is used to transmit data over FDDI networks.

**Data Link Layer Protocols Example:**

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Protocol |
| Address | MAC Address | |
+---------------+---------------+---------------+
```

## High-Level Data Link Layer (HDLL)

The high-level data link layer (HDLL) is a proposed protocol that would replace the current data link layer protocols. The HDLL would provide a more efficient and reliable way of transmitting data over networks.

**HDLL Features:**

- **Framing:** The HDLL would provide a more efficient framing mechanism to reduce overhead and improve data transfer rates.
- **Flow Control:** The HDLL would provide a more efficient flow control mechanism to reduce errors and improve data transfer rates.
- **Error Control:** The HDLL would provide a more efficient error control mechanism to reduce errors and improve data transfer rates.

**HDLL Example:**

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | HDLL Protocol |
| Address | MAC Address | |
+---------------+---------------+---------------+
```

## Conclusion

In conclusion, the data link layer provides several services that ensure reliable data transfer between two devices on the same network. Framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols are all important components of the data link layer. The high-level data link layer is a proposed protocol that would replace the current data link layer protocols and provide a more efficient and reliable way of transmitting data over networks.

**Further Reading:**

- **"Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall**
- **"Data Communications, Networks, and Distributed Systems" by William Stallings**
- **"Computer Networks: Protocol and Architecture" by Douglas Comer**

## Diagrams and Examples

The following diagrams and examples illustrate the concepts discussed in this section:

### Frame Structure Diagram:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Frame Type |
| Address | MAC Address | |
+---------------+---------------+---------------+
| Error-Checking| Data | |
| Code | | |
+---------------+---------------+---------------+
```

### Flow Control Diagram:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Acknowledgement|
| Address | MAC Address | Packet |
+---------------+---------------+---------------+
```

### Error Control Diagram:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Error-Checking|
| Address | MAC Address | Code |
+---------------+---------------+---------------+
```

### Connectionless and Connection-Oriented Protocols Diagram:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Protocol |
| Address | MAC Address | |
+---------------+---------------+---------------+
```

### Data Link Layer Protocols Diagram:

```markdown
+---------------+---------------+---------------+
| Source MAC | Destination | Protocol |
| Address | MAC Address | |
+---------------+---------------+---------------+
```
