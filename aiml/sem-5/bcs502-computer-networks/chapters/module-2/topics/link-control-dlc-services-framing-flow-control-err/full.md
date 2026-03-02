# Link Control: DLC Services

## Introduction

The Data Link Layer (DLL) is the second layer of the OSI model, responsible for providing error-free transfer of data frames between two devices on the same network or between two different networks. Link control is a critical aspect of the DLL, ensuring that data is transmitted efficiently and reliably. In this section, we will delve into the various DLC services, including framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols.

## **Framing**

Framing is the process of dividing data into frames, which are the basic units of data transmission. A frame consists of several fields, including:

- Source MAC address
- Destination MAC address
- Frame type (e.g., Ethernet or PPP)
- Sequence number
- Data
- Checksum

The framing process involves the following steps:

1.  **Data segmentation**: The data is divided into fixed-length segments, depending on the frame type.
2.  **Header creation**: A frame header is created, which includes the source and destination MAC addresses, frame type, and sequence number.
3.  **Data addition**: The data segments are added to the frame header.
4.  **Checksum calculation**: A checksum is calculated to verify the integrity of the frame.
5.  **Frame transmission**: The framed data is transmitted over the network.

Example:

| Frame Header                  | Data Segment 1      | Data Segment 2        | Checksum |
| ----------------------------- | ------------------- | --------------------- | -------- |
| Source MAC: 00:11:22:33:44:55 | Data: Hello, world! | Data: This is a test. | 0x1234   |

In this example, the frame header includes the source and destination MAC addresses, frame type (Ethernet), and sequence number. The data segments are added to the frame header, and a checksum is calculated to verify the integrity of the frame.

## **Flow Control**

Flow control is the process of regulating the amount of data that can be transmitted by a device. It ensures that the sender and receiver agree on the amount of data to be transmitted, preventing network congestion and errors.

There are two types of flow control:

- **Single-point flow control**: This type of flow control involves a single point of control, where the sender and receiver agree on the amount of data to be transmitted.
- **Multipoint flow control**: This type of flow control involves multiple points of control, where each device on the network regulates the amount of data it transmits.

## **Error Control**

Error control is the process of detecting and correcting errors that occur during data transmission. There are two types of error control:

- **Data link layer error control**: This type of error control involves the DLL detecting and correcting errors at the data link layer.
- **Network layer error control**: This type of error control involves the network layer detecting and correcting errors at the network layer.

## **Connectionless and Connection-Oriented Protocols**

Connectionless protocols, such as IP, do not establish a connection before data transmission. Connection-oriented protocols, such as TCP, establish a connection before data transmission.

## **Connection-Oriented Protocols**

Connection-oriented protocols establish a connection before data transmission. The connection establishment process involves the following steps:

1.  **Connection request**: The sender sends a connection request to the receiver.
2.  **Connection acknowledgment**: The receiver sends a connection acknowledgment to the sender.
3.  **Connection establishment**: The sender and receiver agree on the connection parameters.
4.  **Data transmission**: The sender transmits data to the receiver.

Example:

| Connection Establishment                           | Connection Acknowledgment                | Data Transmission      |
| -------------------------------------------------- | ---------------------------------------- | ---------------------- |
| Sender sends connection request                    | Receiver sends connection acknowledgment | Sender transmits data  |
| Sender and receiver agree on connection parameters |                                          | Receiver receives data |

## **Connectionless Protocols**

Connectionless protocols do not establish a connection before data transmission. The connectionless protocol involves the following steps:

1.  **Data transmission**: The sender transmits data to the receiver.
2.  **Data reception**: The receiver receives the data.
3.  **Error detection**: The receiver detects any errors in the data.

Example:

| Data Transmission     | Data Reception         | Error Detection         |
| --------------------- | ---------------------- | ----------------------- |
| Sender transmits data | Receiver receives data | Receiver detects errors |

## **Data Link Layer Protocols**

There are several data link layer protocols, including:

- **Ethernet**: Ethernet is a connection-oriented protocol that uses framing, flow control, and error control to transmit data.
- **PPP**: PPP (Point-to-Point Protocol) is a connection-oriented protocol that uses framing, flow control, and error control to transmit data.
- **HDLC**: HDLC (High-Level Data-Link Control) is a connection-oriented protocol that uses framing, flow control, and error control to transmit data.

## **High-Level Data Link Control (HDLC)**

High-Level Data Link Control (HDLC) is a connection-oriented protocol that uses framing, flow control, and error control to transmit data. HDLC is commonly used in PPP and Ethernet networks.

HDLC protocol stack:

```markdown
+---------------+
| Source MAC |
+---------------+
| Data |
+---------------+
| Sequence |
+---------------+
| HDLC Header |
+---------------+
| Checksum |
+---------------+
| Frame |
+---------------+
```

HDLC protocol steps:

1.  **Data segmentation**: The data is divided into fixed-length segments.
2.  **HDLC header creation**: An HDLC header is created, which includes the source and destination MAC addresses, sequence number, and connection control information.
3.  **Data addition**: The data segments are added to the HDLC header.
4.  **Checksum calculation**: A checksum is calculated to verify the integrity of the HDLC frame.
5.  **Frame transmission**: The HDLC frame is transmitted over the network.

Framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols are all critical aspects of the Data Link Layer. These protocols work together to ensure that data is transmitted efficiently and reliably over the network.

**Diagrams and Illustrations**

Here are some diagrams and illustrations to help illustrate the concepts discussed:

Framing Diagram:

```markdown
+---------------+
| Source MAC |
+---------------+
| Data |
+---------------+
| Sequence |
+---------------+
| HDLC Header |
+---------------+
| Checksum |
+---------------+
| Frame |
+---------------+
```

Flow Control Diagram:

```markdown
+---------------+
| Sender MAC |
+---------------+
| Data |
+---------------+
| Flow Control |
+---------------+
| Receiver MAC |
+---------------+
| Data |
+---------------+
```

Error Control Diagram:

```markdown
+---------------+
| Source MAC |
+---------------+
| Data |
+---------------+
| Error Detection|
+---------------+
| Error Correction|
+---------------+
| Receiver MAC |
+---------------+
| Data |
+---------------+
```

Connectionless and Connection-Oriented Protocols Diagram:

```markdown
+---------------+---------------+
| Sender MAC | Receiver MAC |
+---------------+---------------+
| Connection | Connection |
+---------------+---------------+
| Establishment | Establishment |
+---------------+---------------+
| Data Transmission | Data Transmission |
+---------------+---------------+
```

**Further Reading**

- **"Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall**
- **"Data Communications, Networks, and Distributed Systems" by John L. Hennessy and David A. Patterson**
- **"Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross**
- **"Data Link Layer Protocols" by IETF (Internet Engineering Task Force)**
