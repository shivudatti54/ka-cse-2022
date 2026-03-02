# **Link Control: DLC Services**

## **Introduction**

Link control is a crucial function in the data link layer that ensures reliable data transfer between two devices on a network. It is responsible for managing the flow of data, detecting and correcting errors, and establishing and terminating connections. In this section, we will explore the different DLC services, including framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols.

## **Framing**

Framing is the process of dividing data into manageable units called frames. Each frame consists of a header, payload, and trailer. The header contains control information such as destination MAC address, source MAC address, frame source, and frame type. The payload is the actual data being transmitted, and the trailer contains error-checking information.

**Key Concepts:**

- **Frame format:** Destination MAC address, source MAC address, frame source, frame type, payload, trailer
- **Frame size:** Typically 1024-1536 bytes

Example:

| Frame Header      | Payload      | Frame Trailer     |
| ----------------- | ------------ | ----------------- |
| 00:11:22:33:44:55 | Hello World! | 00:66:77:88:99:AA |

## **Flow Control**

Flow control is a mechanism that prevents network congestion by regulating the amount of data transmitted by a device. It ensures that the sender and receiver agree on the amount of data to be transmitted before sending it. There are two types of flow control:

- **Window-based flow control:** The sender sends data in fixed-size packets, and the receiver acknowledges the packets it receives.
- **Sliding window flow control:** The sender and receiver agree on a window size, and the sender sends data until the window is full or the receiver indicates it has received all the data.

**Key Concepts:**

- **Window size:** The maximum amount of data that can be transmitted at one time
- **Acknowledgments:** The receiver acknowledges the packets it receives to indicate the sender to send more data

Example:

- Sender: Send 1024 bytes of data
- Receiver: Acknowledge 512 bytes of data
- Sender: Send next 512 bytes of data

## **Error Control**

Error control is a mechanism that detects and corrects errors that occur during data transmission. There are two types of error control:

- **Parity:** A bit is added to the data to ensure that an odd or even number of 1s are transmitted.
- **Checksum:** A calculated value is added to the data to ensure that it has not been altered during transmission.

**Key Concepts:**

- **Parity:** A bit added to the data to ensure an odd or even number of 1s are transmitted
- **Checksum:** A calculated value added to the data to ensure it has not been altered

## **Connectionless and Connection-Oriented Protocols**

Connectionless protocols establish a connection only when data is sent, while connection-oriented protocols establish a connection before data is sent.

**Key Concepts:**

- **Connectionless protocols:** IP, ICMP, IGMP
- **Connection-oriented protocols:** TCP, UDP

Example:

- Connectionless protocol: IP sends data without establishing a connection
- Connection-oriented protocol: TCP establishes a connection before sending data

## **Data Link Layer Protocols**

Data link layer protocols are responsible for framing, flow control, error control, and connectionless and connection-oriented protocols.

**Key Concepts:**

- **Data link layer protocols:** Ethernet, PPP, HDLC
- **Frame formats:** Vary depending on the protocol

Example:

| Protocol | Frame Format                           |
| -------- | -------------------------------------- |
| Ethernet | 48-bit MAC address, 14-byte trailer    |
| PPP      | 2-byte header, variable-length payload |

## **High-Level Data Link Control (HDLC)**

HDLC is a connection-oriented protocol that establishes a connection before data is sent. It uses a framing mechanism to divide data into frames, and it uses flow control to regulate the amount of data transmitted.

**Key Concepts:**

- **HDLC frame format:** 2-byte header, variable-length payload, 2-byte trailer
- **HDLC flow control:** Window size, acknowledgments

Example:

| HDLC Frame | Payload      |
| ---------- | ------------ |
| 01234567   | Hello World! |
| 89abcdef   | ...          |

In conclusion, link control is a critical function in the data link layer that ensures reliable data transfer between devices on a network. Understanding the DLC services, including framing, flow control, error control, connectionless and connection-oriented protocols, and data link layer protocols, is essential for designing and implementing efficient network protocols.
