# **Link Control: DLC Services**

## **Introduction**

Link control is a critical function of the Data Link Layer (DLL) in computer networks. It ensures the reliable transfer of data between two devices on a network by managing the transmission of data, detecting errors, and correcting them.

## **DLC Services**

The Data Link Layer provides several services to ensure the reliable transfer of data:

- **Framing**: The process of adding headers and trailers to frames to provide synchronization and error detection.
- **Flow Control**: The mechanism of regulating the amount of data transmitted between two devices to prevent network congestion.
- **Error Control**: The process of detecting and correcting errors that occur during data transmission.
- **Connectionless**: A mode of operation where data is transmitted without establishing a connection between devices.
- **Connection Oriented**: A mode of operation where a connection is established between devices before data transmission.

## **Framing**

Framing is the process of adding headers and trailers to frames to provide synchronization and error detection. A frame consists of the following components:

- **Header**: Contains information such as the destination MAC address, source MAC address, frame type, and error detection code.
- **Payload**: The actual data being transmitted.
- **Trailer**: Contains information such as the source MAC address, destination MAC address, and error detection code.

Example of a Frame:

```
Frame Header: 01101011 00000000 10010101 00000000
Payload: Data being transmitted (e.g., "Hello, World!")
Frame Trailer: 01101011 00000000 10010101 00000000
```

## **Flow Control**

Flow control is the mechanism of regulating the amount of data transmitted between two devices to prevent network congestion. There are two types of flow control:

- **Window-Size Method**: Each device has a window size that determines the maximum amount of data that can be transmitted at one time.
- **Token Buckets Method**: Each device has a token bucket that regulates the amount of data that can be transmitted.

Example of Flow Control:

```
Device A: Window size = 10 packets
Device B: Window size = 10 packets

Device A sends 5 packets to Device B
Device B acknowledges receipt of 5 packets
Device A sends 5 more packets to Device B
...
```

## **Error Control**

Error control is the process of detecting and correcting errors that occur during data transmission. There are two types of error control:

- **Checksum Method**: Each device calculates a checksum for the data being transmitted and compares it with the received checksum.
- **Cyclic Redundancy Check (CRC) Method**: Each device calculates a CRC for the data being transmitted and compares it with the received CRC.

Example of Error Control:

```
Device A: Calculates checksum for data being transmitted
Device B: Calculates checksum for received data
If checksums do not match, device A retransmits data
```

## **Data Link Layer Protocols**

There are several data link layer protocols, including:

- **Ethernet**: A connection-oriented protocol that uses framing, flow control, and error control to ensure reliable data transfer.
- **PPP (Point-to-Point Protocol)**: A connectionless protocol that uses framing, flow control, and error control to ensure reliable data transfer.
- **HDLC (High-Level Data-Link Control)**: A connection-oriented protocol that uses framing, flow control, and error control to ensure reliable data transfer.

## **High-Level Data Link (HDLC)**

HDLC is a connection-oriented protocol that uses framing, flow control, and error control to ensure reliable data transfer. HDLC frames consist of the following components:

- **Header**: Contains information such as the destination MAC address, source MAC address, frame type, and error detection code.
- **Payload**: The actual data being transmitted.
- **Trailer**: Contains information such as the source MAC address, destination MAC address, and error detection code.

Example of an HDLC Frame:

```
Frame Header: 01101011 00000000 10010101 00000000
Payload: Data being transmitted (e.g., "Hello, World!")
Frame Trailer: 01101011 00000000 10010101 00000000
```

## Key Concepts

- Framing: The process of adding headers and trailers to frames to provide synchronization and error detection.
- Flow Control: The mechanism of regulating the amount of data transmitted between two devices to prevent network congestion.
- Error Control: The process of detecting and correcting errors that occur during data transmission.
- Connectionless: A mode of operation where data is transmitted without establishing a connection between devices.
- Connection Oriented: A mode of operation where a connection is established between devices before data transmission.

## Other Relevant Topics

- Block Coding: A technique used to detect and correct errors that occur during data transmission.
- Cyclic Codes: A type of error-correcting code that uses cyclic redundancy checks to detect and correct errors.
- Data Link Layer: A layer of the OSI model that is responsible for framing, flow control, and error control.
- Ethernet: A connection-oriented protocol that uses framing, flow control, and error control to ensure reliable data transfer.
- PPP (Point-to-Point Protocol): A connectionless protocol that uses framing, flow control, and error control to ensure reliable data transfer.
- HDLC (High-Level Data-Link Control): A connection-oriented protocol that uses framing, flow control, and error control to ensure reliable data transfer.
