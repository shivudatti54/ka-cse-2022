# **Link Control: DLC Services**

## **Introduction**

Link control, also known as Data Link Layer (DLL) control, is a fundamental aspect of computer networking that ensures reliable data transfer between devices on a network. The Data Link Layer is responsible for framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols. In this comprehensive guide, we will delve into the details of link control, exploring its historical context, modern developments, and practical applications.

## **Historical Context**

The concept of link control dates back to the early 1970s, when the National Bureau of Standards (NBS) developed the first network protocol, called Network Control Protocol (NCP). NCP was designed to manage network communications, including framing, flow control, and error control. In the 1980s, the Internet Protocol (IP) was developed, which required a more robust link control mechanism. The Internet Engineering Task Force (IETF) developed the Data Link Layer protocol, which is now widely used in modern computer networks.

## **DLC Services**

The Data Link Layer provides several services to ensure reliable data transfer between devices on a network. These services are:

### Framing

Framing is the process of dividing data into manageable chunks called frames. Each frame consists of a header and a payload. The header contains control information, such as source and destination MAC addresses, frame sequence number, and error detection codes. The payload contains the actual data being transmitted.

**Example:**

Suppose we want to transmit a 1024-byte file over a network. We divide the file into 2048-byte frames, with each frame having a 64-byte header and a 1024-byte payload.

| Frame # | Header                                                    | Payload   |
| ------- | --------------------------------------------------------- | --------- |
| 1       | Source MAC, Destination MAC, Frame seq #, Error detection | Data 1    |
| 2       | Source MAC, Destination MAC, Frame seq #, Error detection | Data 2    |
| ...     | ...                                                       | ...       |
| 2048    | Source MAC, Destination MAC, Frame seq #, Error detection | Data 1024 |

### Flow Control

Flow control is the process of regulating the amount of data transmitted between devices on a network. It prevents network congestion and ensures that devices do not send more data than the receiving device can handle. Flow control is implemented using a handshake protocol, where devices exchange control messages to determine the available bandwidth.

**Example:**

Suppose we want to transmit data from Device A to Device B. We establish a flow control connection, where Device A sends a flow control packet to Device B, indicating the available bandwidth. Device B responds with a flow control acknowledgment packet, indicating the maximum amount of data it can receive. Device A then sends data frames, using the flow control packet to regulate the transmission rate.

### Error Control

Error control is the process of detecting and correcting errors that occur during data transmission. It ensures that data is delivered accurately and reliably. Error control is implemented using several techniques, including:

- **Parity bits**: Adding bits to data frames to detect single-bit errors.
- **Cyclic redundancy checks (CRCs)**: Calculating a checksum for data frames to detect errors.
- **Retransmission**: Sending duplicate data frames to detect and correct errors.

**Example:**

Suppose we transmit data frames over a network, but one frame is corrupted during transmission. We use CRC to detect the error and retransmit the frame.

### Connectionless and Connection-Oriented Protocols

Connectionless protocols, such as IP, do not establish a connection before transmitting data. Connectionless protocols use error control mechanisms, such as CRC, to detect errors. Connection-oriented protocols, such as TCP, establish a connection before transmitting data and use flow control and error control mechanisms to ensure reliable data transfer.

**Example:**

Suppose we want to transmit data from Device A to Device B using TCP. We establish a connection, using a three-way handshake to synchronize the devices. Once connected, we use flow control and error control mechanisms to ensure reliable data transfer.

### Data Link Layer Protocols

The Data Link Layer provides several protocols to manage data transfer between devices on a network. Some common protocols include:

- **Ethernet**: A connectionless protocol used for local area networks (LANs).
- **Token Ring**: A connection-oriented protocol used for LANs.
- **FDDI**: A connectionless protocol used for fiber distribution networks (FDNs).
- **IEEE 802.11**: A connectionless protocol used for wireless local area networks (WLANs).

## **High-Level Data Link (HDLC)**

High-Level Data Link (HDLC) is a connection-oriented protocol used for frame relay networks. HDLC establishes a connection before transmitting data and uses flow control and error control mechanisms to ensure reliable data transfer. HDLC is widely used in modern computer networks, including WANs and VPNs.

**Example:**

Suppose we want to transmit data from Device A to Device B using HDLC. We establish a connection, using a three-way handshake to synchronize the devices. Once connected, we use flow control and error control mechanisms to ensure reliable data transfer.

### Connectionless and Connection-Oriented Protocols

Connectionless protocols, such as IP, do not establish a connection before transmitting data. Connectionless protocols use error control mechanisms, such as CRC, to detect errors. Connection-oriented protocols, such as TCP, establish a connection before transmitting data and use flow control and error control mechanisms to ensure reliable data transfer.

**Example:**

Suppose we want to transmit data from Device A to Device B using TCP. We establish a connection, using a three-way handshake to synchronize the devices. Once connected, we use flow control and error control mechanisms to ensure reliable data transfer.

## **Modern Developments**

Modern computer networks use advanced link control mechanisms, including:

- **Quality of Service (QoS)**: Ensuring that data is delivered with guaranteed quality of service.
- **Multiprotocol Label Switching (MPLS)**: Using label switching to manage data transfer between devices on a network.
- **Software-Defined Networking (SDN)**: Using software to manage and control network traffic.

## **Applications**

Link control is essential for various applications, including:

- **Cloud Computing**: Ensuring that data is delivered reliably and securely between cloud servers.
- **Internet of Things (IoT)**: Managing data transfer between devices on an IoT network.
- **Virtual Private Networks (VPNs)**: Ensuring that data is delivered securely over a VPN connection.

## **Case Studies**

- **Google Fiber**: Google Fiber uses HDLC to ensure reliable data transfer between devices on its network.
- **Amazon Web Services (AWS)**: AWS uses QoS to ensure that data is delivered with guaranteed quality of service.
- **Cisco Systems**: Cisco Systems uses MPLS to manage data transfer between devices on its network.

## **Diagrams and Descriptions**

### Framing Diagram

Suppose we want to transmit a 1024-byte file over a network. We divide the file into 2048-byte frames, with each frame having a 64-byte header and a 1024-byte payload.

| Frame # | Header                                                    | Payload   |
| ------- | --------------------------------------------------------- | --------- |
| 1       | Source MAC, Destination MAC, Frame seq #, Error detection | Data 1    |
| 2       | Source MAC, Destination MAC, Frame seq #, Error detection | Data 2    |
| ...     | ...                                                       | ...       |
| 2048    | Source MAC, Destination MAC, Frame seq #, Error detection | Data 1024 |

### Flow Control Diagram

Suppose we want to transmit data from Device A to Device B. We establish a flow control connection, where Device A sends a flow control packet to Device B, indicating the available bandwidth. Device B responds with a flow control acknowledgment packet, indicating the maximum amount of data it can receive. Device A then sends data frames, using the flow control packet to regulate the transmission rate.

### Error Control Diagram

Suppose we transmit data frames over a network, but one frame is corrupted during transmission. We use CRC to detect the error and retransmit the frame.

### Connectionless and Connection-Oriented Protocols Diagram

Suppose we want to transmit data from Device A to Device B using TCP. We establish a connection, using a three-way handshake to synchronize the devices. Once connected, we use flow control and error control mechanisms to ensure reliable data transfer.

### HDLC Diagram

Suppose we want to transmit data from Device A to Device B using HDLC. We establish a connection, using a three-way handshake to synchronize the devices. Once connected, we use flow control and error control mechanisms to ensure reliable data transfer.

## **Further Reading**

- **"Computer Networks"** by Andrew S. Tanenbaum and David J. Wetherall
- **"Data Link Layer Protocols"** by Charles P. Pfister
- **"High-Level Data Link (HDLC)"** by Cisco Systems
- **"Quality of Service (QoS)"** by Cisco Systems
- **"Multiprotocol Label Switching (MPLS)"** by Cisco Systems
- **"Software-Defined Networking (SDN)"** by Cisco Systems
