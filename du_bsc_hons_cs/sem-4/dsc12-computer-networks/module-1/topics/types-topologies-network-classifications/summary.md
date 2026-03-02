# Types, Topologies, and Classifications of Computer Networks - Summary

## Key Definitions and Concepts

- **Network**: A collection of interconnected devices that share resources and communicate with each other.
- **Topology**: The arrangement or layout of nodes and connections in a computer network (physical or logical).
- **PAN (Personal Area Network)**: Smallest network type, ~10m range, using Bluetooth/NFC.
- **LAN (Local Area Network)**: Covers ~1km, high speed (100 Mbps-10 Gbps), owned by organizations.
- **MAN (Metropolitan Area Network)**: Covers a city, connects multiple LANs, uses SONET/FDDI.
- **WAN (Wide Area Network)**: Global coverage, Internet is the largest WAN, typically service provider-owned.
- **CAN (Campus Area Network)**: Between LAN and MAN, covers educational/corporate campuses.
- **VPN (Virtual Private Network)**: Creates secure encrypted tunnels over public networks.

## Important Formulas and Theorems

- **Full Mesh Connections**: n(n-1)/2 connections required for n nodes
- **Bus Topology**: Single backbone cable with terminators at both ends
- **Star Topology**: All nodes connect to central hub/switch
- **Ring Topology**: Circular connection with token-passing mechanism

## Key Points

1. **LAN is most common** in educational institutions and offices; star topology dominates modern LANs.
2. **Star topology advantages**: Easy troubleshooting, fault isolation, scalability; disadvantage: central device failure affects entire network.
3. **Bus topology disadvantages**: Single point of failure (backbone), limited cable length, difficult troubleshooting.
4. **Mesh topology** provides highest reliability through redundancy but has high cost.
5. **Hybrid topologies** combine multiple topologies to leverage their strengths.
6. **Transmission media**: Wired (twisted pair, coaxial, fiber) vs Wireless (Wi-Fi, Bluetooth, cellular).
7. **Network architecture**: Client-server (centralized) vs Peer-to-Peer (decentralized).
8. **VPN extends private networks** securely over the Internet using encryption.

## Common Mistakes to Avoid

1. Confusing PAN with LAN—PAN is personal (~10m), LAN is local (~1km).
2. Thinking VPN creates a physical network—it's a logical/virtual network overlay.
3. Assuming ring topology is obsolete—it's used in specific applications like SONET.
4. Forgetting that star topology requires more cabling than bus topology.
5. Ignoring the single point of failure in star topology (the central switch/hub).

## Revision Tips

1. Create comparison tables for network types (range, speed, ownership, examples).
2. Draw all topologies on paper and label their components repeatedly.
3. Practice scenario-based questions: "What network type/topology for a college with 3 buildings?"
4. Memorize IEEE standards: 802.3 (Ethernet), 802.11 (Wi-Fi), 802.15 (Bluetooth).
5. Relate concepts to real examples: your college Wi-Fi is a LAN, Delhi Metro network is MAN, Internet is WAN.