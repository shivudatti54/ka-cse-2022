# **Link Control: DLC Services**

## **Introduction**

- Link control is a mechanism to manage data transfer between two devices on a network.
- It ensures reliable data transfer by controlling the flow of data packets.

## **Framing**

- Framing: adding headers and trailers to data packets to identify them as valid packets.
- Format of a frame:
  - Header (source MAC, destination MAC, sequence number, etc.)
  - Payload (data)
  - Trailer (checksum, etc.)
- Importance of framing:
  - Provides source and destination MAC addresses
  - Allows for error detection and correction

## **Flow Control**

- Flow control: regulates the amount of data that can be sent by a device at one time.
- How flow control works:
  - Device sends a "window" of data packets
  - Receiver acknowledges receipt of each packet
  - Device continues to send packets until window is full or error occurs
- Flow control protocols:
  - Slack (simple flow control)
  - Window/ACK (window flow control with acknowledgement)

## **Error Control**

- Error control: detects and corrects errors in data packets.
- Techniques:
  - Parity bits
  - Cyclic redundancy checks (CRCs)
  - Error detection codes (e.g., Reed-Solomon)
- Importance of error control:
  - Prevents data loss or corruption
  - Ensures data integrity

## **Connectionless and Connection-Oriented**

- Connectionless: no setup or teardown required; packets are sent independently.
- Connection-oriented: setup and teardown required; packets are sent in a sequence.
- Advantages and disadvantages:
  - Connectionless: faster data transfer, but more prone to errors.
  - Connection-oriented: ensures reliable data transfer, but slower.

## **Data Link Layer Protocols**

- Ethernet (connection-oriented)
- Point-to-Point Protocol (PPP) (connection-oriented)
- HyperText Transfer Protocol (HTTP) (connection-oriented)

## **High-Level Data Link Control (HDLC)**

- HDLC: a connection-oriented protocol that uses a fixed-length header and trailer.
- Format of a HDLC frame:
  - Header (16-bit sequence number, 2-bit flags)
  - Payload (data)
  - Trailer (2-bit flags, 16-bit sequence number)

## **Important Formulas and Definitions**

- **CRC (Cyclic Redundancy Check)**: a formula used to detect errors in data packets.
- **Slack**: the amount of data that can be sent by a device without receiving an acknowledgement.
- **Flow control window**: the amount of data that can be sent by a device before receiving an acknowledgement.
