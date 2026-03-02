# **20.1-20.3 Revision Notes: Network Layer Services, Packet Switching, IPv4 Address, IPv4 Datagram, IPv6**

### Network Layer Services

- **Connectionless vs. Connection-Oriented**: Connectionless (e.g. IP), Connection-Oriented (e.g. TCP)
- **Reliable vs. Unreliable**: Reliable (e.g. TCP), Unreliable (e.g. UDP)
- **Error Detection and Correction**: Checksum, CRC, Forward Error Correction (FEC)

### Packet Switching

- **Packet Switching Model**: Network, Transport, Session, Presentation, Application
- **Packet Switching Advantages**:
  - Efficient use of bandwidth
  - Flexibility in network configuration
  - Improved reliability
- **Packet Switching Disadvantages**:
  - Error-prone
  - Header-overhead

### IPv4 Address

- **Classful IP Addressing**:
  - Class A (0.0.0.0 - 127.255.255.255)
  - Class B (128.0.0.0 - 191.255.255.255)
  - Class C (192.0.0.0 - 223.255.255.255)
  - Class D (224.0.0.0 - 239.255.255.255)
  - Class E (240.0.0.0 - 254.255.255.255)
- **Subnetting**: Masks, Network ID, Host ID

### IPv4 Datagram

- **IP Datagram Structure**:
  - Header: Source IP, Destination IP, Protocol, Checksum, Flags
  - Payload: Data to be transmitted
- **IP Datagram Size**: Header (20 bytes, 8 bytes for options), Payload

### IPv6

- **IPv6 Addressing**:
  - 128-bit address space
  - Unique address for each device
  - Hierarchical addressing
  - Link-local, Site-local, Global, Unique-Local addresses
- **IPv6 Header**:
  - Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Source IP, Destination IP
  - Optional extensions: Fragment offset, Hop-by-hop optimization, Destination extension header

### Important Formulas and Definitions

- **IP Fragmentation**: Divide large datagram into smaller fragments
- **IP Reassembly**: Reconstruct original datagram from fragmented packets
- **TCP Segment Size**: Maximum segment size (MSS)
- **UDP Port Numbers**: 0-65535 (65536 possible ports)

### Theorems

- **Pigeonhole Principle**: If n items are put into m containers, with n > m, then at least one container must contain more than one item
- **Fermat's Little Theorem**: If p is a prime number, then a^(p-1) ≡ 1 (mod p)
