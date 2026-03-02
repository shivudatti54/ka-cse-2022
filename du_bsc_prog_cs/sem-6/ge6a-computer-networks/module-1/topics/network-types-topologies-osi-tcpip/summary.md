# Network Types, Topologies, OSI & TCP/IP Model
## BSc Physical Science (CS) - Delhi University, NEP 2024
### Quick Revision Summary

---

## Introduction
This summary covers essential networking concepts required for Delhi University's Ge6A Computer Networks syllabus. Understanding network types, topologies, and protocol models forms the foundation of computer networking.

---

## Network Types (Based on Geographic Area)

- **PAN (Personal Area Network)** – Smallest network, coverage within a few meters (Bluetooth, IR)
- **LAN (Local Area Network)** – Limited to building/campus, high speed, low latency (Ethernet, Wi-Fi)
- **MAN (Metropolitan Area Network)** – Connects multiple LANs across a city (Cable TV, fiber links)
- **WAN (Wide Area Network)** – Spans large geographic areas, public/internet connectivity (Leased lines, satellite)
- **CAN (Campus Area Network)** – Interconnects multiple buildings in a university/campus

---

## Network Topologies

- **Bus Topology** – Single backbone cable, terminators at ends, cost-effective, prone to collisions
- **Star Topology** – All devices connected to central hub/switch, most common, easy to manage, failure of hub affects network
- **Ring Topology** – Circular data path, token passing mechanism, deterministic performance
- **Mesh Topology** – Every device connected to every other, highly reliable, expensive (partial/full mesh)
- **Tree Topology** – Hierarchical combination of star and bus, scalable
- **Hybrid Topology** – Combination of two or more topologies

---

## OSI Model (7 Layers)

1. **Physical** – Data transmission, cables, hubs, bits
2. **Data Link** – MAC addressing, switches, frames, error detection
3. **Network** – IP addressing, routers, packets, routing
4. **Transport** – TCP/UDP, segmentation, flow control, ports
5. **Session** – Session management, authentication
6. **Presentation** – Data formatting, encryption, compression
7. **Application** – User interface, HTTP, FTP, SMTP

---

## TCP/IP Model (4 Layers)

1. **Network Access/Link Layer** – Physical + Data Link (Ethernet, ARP)
2. **Internet Layer** – Network (IP, ICMP, IGMP)
3. **Transport Layer** – Transport (TCP, UDP)
4. **Application Layer** – Session + Presentation + Application (HTTP, DNS, SMTP)

---

## Key Comparison

| OSI Layer | TCP/IP Layer |
|-----------|--------------|
| Application, Presentation, Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link, Physical | Network Access |

---

## Conclusion
These concepts are fundamental for understanding how data communicates across networks. The OSI model provides a theoretical framework, while TCP/IP is the practical protocol suite used in today's internet. Familiarity with network types and topologies is essential for designing and troubleshooting networks.

*Reference: Delhi University BSc (Hons) Computer Science Syllabus, NEP 2024 - Ge6A Computer Networks*