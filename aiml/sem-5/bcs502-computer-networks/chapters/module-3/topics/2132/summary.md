# **21.3.2 Revision Notes**

## **Network Layer Services**

- **Functionality**: Provides logical addressing, routing, and congestion control.
- **Services**:
  - Connectionless (e.g., IP, ICMP, IGMP)
  - Connection-oriented (e.g., TCP, UDP)

## **Packet Switching**

- **Definition**: A method of transmitting data in packets between devices.
- **Key characteristics**:
  - Packets are routed independently.
  - Packets may be lost or corrupted during transmission.
  - Packets are reconstructed at the receiving end.

## **IPv4 Addressing**

- **Definition**: A unique 32-bit address assigned to each device on a network.
- **Address format**: `xxx.xxx.xxx.xxx`
- **Address classes**:
  - A (0-126)
  - B (128-191)
  - C (192-223)
  - D (224-239)
  - E (240-254)

## **IPv4 Datagram**

- **Definition**: A packet of data transmitted over an IPv4 network.
- **Components**:
  - Header
  - Data
  - Trailer

## **Important Formulas and Definitions**

- **IP Header Format**:
  - Version (4 bits)
  - Header Length (4 bits)
  - Total Length (16 bits)
  - Identification (16 bits)
  - Flags (3 bits)
  - Fragment Offset (13 bits)
  - TTL (8 bits)
  - Protocol (8 bits)
  - Checksum (16 bits)
  - Source and Destination IPs (32 bits)
- **TCP Header Format**:
  - Source and Destination Ports (16 bits each)
  - Sequence Number (32 bits)
  - Acknowledgment Number (32 bits)
  - Data (variable)
  - Ack (1 bit)
  - PSH (3 bits)
  - RST (4 bits)
  - SYN (6 bits)
  - FIN (9 bits)

## **Theorems**

- **Hop Limit Theorem**: The hop limit of a packet decreases by 1 at each hop.
- **Packet Loss Theorem**: Packets may be lost or corrupted during transmission.

## **Key Terms**

- **Routing**: The process of forwarding packets between networks.
- **Subnetting**: The process of dividing a network into smaller sub-networks.
- **Masks**: Used to specify the subnet mask for subnetting.
