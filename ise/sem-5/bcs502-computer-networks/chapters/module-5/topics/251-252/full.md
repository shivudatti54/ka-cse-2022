# 25.1-25.2: Introduction to Protocol Data Units (PDUs) and Frame Format

## 25.1: Protocol Data Units (PDUs)

A Protocol Data Unit (PDU) is a fundamental concept in computer networking that represents the basic data unit transmitted between two devices on a network. PDUs are the building blocks of network communication, allowing devices to exchange information and services.

### Types of PDUs

There are several types of PDUs, including:

- **Frame**: A frame is the most common type of PDU and consists of a header, payload, and trailer. It is used in Ethernet networks.
- **Packet**: A packet is similar to a frame but has a smaller header and is used in IP networks.
- **Cell**: A cell is a type of PDU used in Frame Relay networks.
- **SDU**: A Service Data Unit (SDU) is a type of PDU used in Frame Relay networks.

### Characteristics of PDUs

PDUs have several characteristics that define them, including:

- **Length**: The length of a PDU can vary depending on the type of network and the specific protocol being used.
- **Header**: The header of a PDU contains control information, such as source and destination addresses, and error-checking data.
- **Payload**: The payload of a PDU contains the actual data being transmitted.
- **Trailer**: The trailer of a PDU contains error-checking data and other control information.

### Example of a Frame

Here is an example of a frame in Ethernet:

```
  +---------------+
  |  Header     |
  |  (Source MAC  |
  |   Destination  |
  |   Type and LEN) |
  +---------------+
  |  Payload     |
  |  (Data being  |
  |   transmitted)  |
  +---------------+
  |  Trailer     |
  |  (CRC and Pad) |
  +---------------+
```

## 25.2: Frame Format

A frame is the most common type of PDU and consists of a header, payload, and trailer. The frame format is as follows:

### Header

The header of a frame contains the following information:

- **Source MAC address**: The MAC address of the device that sent the frame.
- **Destination MAC address**: The MAC address of the device that received the frame.
- **Type and LEN**: The type of frame (e.g., Ethernet) and the length of the frame.
- **Sequence number**: A sequence number that indicates the order in which frames are transmitted.

### Payload

The payload of a frame contains the actual data being transmitted.

### Trailer

The trailer of a frame contains the following information:

- **CRC**: A cyclic redundancy check (CRC) that is used to detect errors in transmission.
- **Pad**: Padding bytes that are added to the end of the frame to make its length a multiple of the frame size.

### Frame Format Diagram

Here is a diagram of the frame format:

```
  +---------------+
  |  Header     |
  |  (6 bytes)   |
  |  +--------+  |
  |  |  Source  |
  |  |  MAC     |
  |  |  Address  |
  |  +--------+  |
  |  |  Destination  |
  |  |  MAC     |
  |  |  Address  |
  |  +--------+  |
  |  |  Type and  |
  |  |  LEN     |
  |  +--------+  |
  |  |  Sequence  |
  |  |  Number   |
  |  +--------+  |
  +---------------+
  |  Payload     |
  |  (variable)  |
  +---------------+
  |  Trailer     |
  |  (4 bytes)   |
  |  +--------+  |
  |  |  CRC     |
  |  |  (2 bytes) |
  |  +--------+  |
  |  |  Pad     |
  |  |  (variable) |
  |  +--------+  |
  +---------------+
```

## Case Study: Ethernet Frame Format

Ethernet frames are the most common type of frame in Ethernet networks. The Ethernet frame format is as follows:

- **Header** (6 bytes): The header contains the source MAC address, destination MAC address, type and length, and sequence number.
- **Payload** (variable): The payload contains the actual data being transmitted.
- **Trailer** (4 bytes): The trailer contains the CRC and padding.

Here is an example of an Ethernet frame:

```
  +---------------+
  |  Header     |
  |  (6 bytes)   |
  |  +--------+  |
  |  |  Source  |
  |  |  MAC     |
  |  |  Address  |
  |  +--------+  |
  |  |  Destination  |
  |  |  MAC     |
  |  |  Address  |
  |  +--------+  |
  |  |  Type and  |
  |  |  LEN     |
  |  +--------+  |
  |  |  Sequence  |
  |  |  Number   |
  |  +--------+  |
  +---------------+
  |  Payload     |
  |  (variable)  |
  +---------------+
  |  Trailer     |
  |  (4 bytes)   |
  |  +--------+  |
  |  |  CRC     |
  |  |  (2 bytes) |
  |  +--------+  |
  |  |  Pad     |
  |  |  (variable) |
  |  +--------+  |
  +---------------+
```

## Applications

PDUs are used in a wide range of applications, including:

- **Ethernet networks**: PDUs are used to transmit data between devices on an Ethernet network.
- **IP networks**: PDUs are used to transmit data between devices on an IP network.
- **Frame Relay networks**: PDUs are used to transmit data between devices on a Frame Relay network.

## Further Reading

- **"Computer Networking: A Top-Down Approach"** by Jim Kurose and Keith Ross
- **"Networking: Fundamentals and Modern Technologies"** by Larry L. Peterson and Bruce S. Davie
- **"Computer Networks"** by Andrew S. Tanenbaum and David J. Wetherall

## Exercises

1. Describe the difference between a frame and a packet.
2. Explain the purpose of the header, payload, and trailer in a PDU.
3. Describe the format of an Ethernet frame.
4. Explain the purpose of the CRC in a PDU.
5. Discuss the advantages and disadvantages of using PDUs in different types of networks.

## Solutions

1. A frame is a type of PDU that contains a header, payload, and trailer, while a packet is a type of PDU that contains a header and payload, but not a trailer.
2. The header contains control information, such as source and destination addresses, and error-checking data. The payload contains the actual data being transmitted. The trailer contains error-checking data and other control information.
3. The Ethernet frame format consists of a header (6 bytes), payload (variable), and trailer (4 bytes).
4. The CRC is used to detect errors in transmission by calculating the cyclic redundancy check (CRC) of the PDU.
5. PDUs are used in Ethernet networks, IP networks, and Frame Relay networks. They have advantages such as ease of transmission and error detection, but disadvantages such as potential for collisions and errors in transmission.
