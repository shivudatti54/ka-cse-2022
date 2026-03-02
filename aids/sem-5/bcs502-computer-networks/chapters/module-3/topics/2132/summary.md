# **21.3.2 Revision Notes**

### Overview

- The Network Layer provides logical connectivity between hosts.
- It defines end-to-end communication between devices.
- Services offered by the Network Layer:
  - Routing
  - Fragmentation
  - Reassembly
  - Error detection and correction
  - Flow control

### Packet Switching

---

- Each packet is assigned a source and destination IP address.
- Packets are forwarded through the network based on their IP routes.
- Packet switching allows for efficient use of network resources.

### IPv4 Address and IPv4 Datagram

---

- IPv4 address: a 32-bit address that uniquely identifies a device.
- IPv4 datagram: a packet of data that contains an IP header and a payload.

### IPv6 Address and IPv6 Datagram

---

- IPv6 address: a 128-bit address that provides a much larger address space than IPv4.
- IPv6 datagram: similar to IPv4 datagram, but with an IPv6 header.

### Important Formulas and Definitions

---

- **IP Header Fields**:
  - Version (4 bits)
  - Header Length (4 bits)
  - Type of Service (8 bits)
  - Total Length (16 bits)
  - Identification (16 bits)
  - Flags (3 bits)
  - Fragment Offset (13 bits)
  - TTL (8 bits)
  - Protocol (8 bits)
  - Checksum (16 bits)
- **IPv4 Address Format**: `xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx`
- **IPv6 Address Format**: `xxxxxxxxxxxxx:xxxxxxxxxxxxx:xxxxxxxxxxxxx:xxxxxxxxxxxxx`

### Important Theorems

---

- **Store-and-Forward Theorem**: devices forward packets to the next device in the network.
- **Cut-Through Theorem**: devices forward packets without buffering.

### Quick Revision Tips

---

- Understand the concepts of packet switching and logical connectivity.
- Familiarize yourself with IPv4 and IPv6 addresses and datagrams.
- Know the key fields in the IP header and their functions.
- Review the formulas and definitions for IP addresses and datagrams.
