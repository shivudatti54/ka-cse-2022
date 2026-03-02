# **Practical Component of IPCC - Experiments 1: Implementing a Point-to-Point Network**

**Key Points:**

- **Point-to-Point Network (PTPN)**:
  - A network where two nodes are directly connected using a single link
  - Each node has a dedicated connection to the other node
- **Duplex Links**:
  - A link that allows data to be transmitted in both directions simultaneously
  - Each link has two channels, one for transmitting data and one for receiving data

**Equipment Needed:**

- Three nodes (A, B, C)
- Three duplex links (AB, BC, AC)

## **Network Topology:**

- Node A is connected to Node B using link AB (duplex)
- Node B is connected to Node C using link BC (duplex)
- Node C is connected to Node A using link AC (duplex)

## **Formula:**

- Throughput (T) of a duplex link: T = 2 × Bandwidth (B)
- Where Bandwidth (B) is the amount of data that can be transmitted in one direction per second.

## **Theorem:**

- The total throughput of a point-to-point network is limited by the slowest link in the network.

**Important Terms:**

- **Node**: A device that connects to another node or devices to form a network.
- **Link**: A connection between two nodes.
- **Duplex**: A link that allows data to be transmitted in both directions simultaneously.

**Revision Tips:**

- Review the concept of point-to-point networks and duplex links.
- Practice calculating the throughput of a duplex link.
- Understand how the slowest link in a network affects the overall throughput.
