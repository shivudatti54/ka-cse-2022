# **Link Control: DLC Services**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Framing](#framing)
3. [Flow Control](#flow-control)
4. [Error Control](#error-control)
5. [Connectionless and Connection-Oriented](#connectionless-and-connection-oriented)
6. [Data Link Layer Protocols](#data-link-layer-protocols)
7. [High-Level Data Link Control (HDLC)](#high-level-data-link-control-hdlc)

## **Introduction**

Link control is a crucial aspect of data communication, ensuring that data is transmitted reliably and efficiently over a network. The Data Link Layer (DLC) is responsible for link control, and it provides several services to ensure error-free data transmission.

## **Framing**

Framing is the process of dividing data into frames, which are the basic units of data transmission. A frame consists of:

- **Header**: Contains control information, such as frame source and destination addresses, frame length, and error-checking information.
- **Payload**: Contains the actual data being transmitted.
- **Trailer**: Contains control information, such as frame sequence number and error-checking information.

The frame is transmitted over the network, and the receiving device checks the frame for errors using the error-checking information.

## **Flow Control**

Flow control is the process of controlling the amount of data transmitted over a link. This is necessary to prevent network congestion and ensure that data is transmitted at a rate that the receiving device can handle.

- **Stop-and-Wait**: The sender waits for an acknowledgement from the receiver before transmitting the next frame.
- **Sliding Window**: The sender and receiver agree on a window size, and the sender transmits data within the window size before receiving an acknowledgement.
- **Cwnd (Congestion Window)**: The sender and receiver agree on a window size, and the sender increases the window size as the congestion window increases.

## **Error Control**

Error control is the process of detecting and correcting errors that occur during data transmission. This is necessary to ensure that data is transmitted reliably and accurately.

- **Parity Bits**: One or more parity bits are added to the data to make it even or odd in number. The receiving device checks the parity bits to detect errors.
- **Check Sums**: The receiving device calculates a check sum and compares it with the received check sum to detect errors.
- **Cyclic Redundancy Checks (CRCs)**: The receiving device calculates a CRC and compares it with the received CRC to detect errors.

## **Connectionless and Connection-Oriented**

Connectionless transmission does not establish a connection between the sender and receiver before data transmission. The sender transmits data to the best available receiver.

- **Datagrams**: The sender transmits data in the form of datagrams, which are frames that contain the source and destination addresses and error-checking information.
- **Packet Switching**: The sender transmits data in packets, which are frames that contain the source and destination addresses and error-checking information.

Connection-oriented transmission establishes a connection between the sender and receiver before data transmission. The sender transmits data to the receiver through the established connection.

- **Synchronous Connection-Oriented (SCO)**: The sender and receiver establish a connection and agree on a timing protocol to synchronize data transmission.
- **Asynchronous Connection-Oriented (ACO)**: The sender and receiver establish a connection and agree on a timing protocol, but the sender transmits data at a rate that is not synchronized with the receiver.

## **Data Link Layer Protocols**

The Data Link Layer provides several protocols for link control, including:

- **HDLC (High-Level Data Link Control)**: A protocol that provides connection-oriented transmission and error control.
- **HDLC-II (High-Level Data Link Control II)**: A protocol that provides connection-oriented transmission and error control, with improved performance and efficiency.
- **LLC (Logical Link Control)**: A protocol that provides connection-oriented transmission and error control, with improved performance and efficiency.

## **High-Level Data Link Control (HDLC)**

HDLC is a protocol that provides connection-oriented transmission and error control. It is used to transmit data in frames, with each frame containing:

- **HDLC Header**: Contains the source and destination addresses, frame length, and error-checking information.
- **HDLC Payload**: Contains the actual data being transmitted.
- **HDLC Trailer**: Contains the error-checking information.

The receiving device checks the HDLC trailer for errors and discards any frames with errors. HDLC provides several benefits, including:

- **Improved Performance**: HDLC provides faster transmission speeds and improved error detection and correction.
- **Improved Efficiency**: HDLC reduces the overhead of error control and framing, improving network efficiency.
- **Improved Reliability**: HDLC provides reliable data transmission, with reduced errors and improved error detection and correction.
