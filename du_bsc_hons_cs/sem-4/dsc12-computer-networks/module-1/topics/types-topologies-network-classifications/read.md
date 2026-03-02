# Types, Topologies, and Classifications of Computer Networks

## Introduction

Computer networks form the backbone of modern digital communication, enabling devices worldwide to exchange information seamlessly. Understanding the fundamental classifications, types, and topologies of networks is essential for any computer science student, particularly in the context of the University of Delhi's BSc (H) Computer Science program. This topic forms the foundation upon which advanced networking concepts are built.

The evolution of computer networks from simple point-to-point connections to complex global internetworks demonstrates the remarkable progress in communication technology. Whether you are browsing the internet on your smartphone at Delhi's Connaught Place, attending a virtual lecture at Miranda House, or transferring files between computers in a college laboratory, you are interacting with different types of networks configured in various topologies. This chapter explores the systematic classification of networks based on geographical scope, the physical or logical arrangement of devices (topologies), and other distinguishing characteristics that define their operational capabilities.

## Key Concepts

### Classification of Networks by Geographical Scope

**Personal Area Network (PAN)** represents the smallest and most personal network type, typically spanning an individual's workspace. With a range of about 10 meters, PANs connect personal devices such as smartphones, tablets, smartwatches, and Bluetooth earphones. Technologies like Bluetooth (IEEE 802.15), Infrared, and NFC (Near Field Communication) power PANs. Consider the scenario where you connect your wireless earbuds to your smartphone while traveling on the Delhi Metro—this constitutes a PAN in operation.

**Local Area Network (LAN)** is confined to a small geographical area such as a building, office, or campus. LANs offer high speed (typically 100 Mbps to 10 Gbps) and low latency, making them ideal for sharing resources like printers, files, and internet connections within an organization. The computer labs at SRCC, the Wi-Fi network at Hindu College, or the wired Ethernet connection in a Delhi University department all represent LANs. LANs utilize technologies such as Ethernet (IEEE 802.3) and Wi-Fi (IEEE 802.11). The characteristic features of LANs include limited coverage (usually up to 1 km), exclusive ownership, and high data transfer rates.

**Metropolitan Area Network (MAN)** covers a larger geographical area than LAN, typically spanning a city or large campus. MANs interconnect multiple LANs and provide high-speed connectivity across metropolitan regions. The Delhi Metro's automated fare collection system and the cable television network across Delhi are practical examples of MANs. The Delhi University Campus Network connecting various colleges within the University could be considered a MAN. SONET (Synchronous Optical Network), FDDI (Fiber Distributed Data Interface), and ATM (Asynchronous Transfer Mode) are common technologies used in MANs.

**Wide Area Network (WAN)** encompasses large geographical areas, often countries or continents. The Internet itself is the largest example of a WAN. Organizations with multiple branch offices across India or globally rely on WANs for communication. Leased lines, satellite links, and MPLS (Multi-Protocol Label Switching) are technologies employed in WANs. Unlike LANs and MANs, WANs are typically owned by service providers (like BSNL, Airtel, Jio) who lease bandwidth to customers. WANs offer broader coverage but generally at lower speeds and higher costs compared to LANs.

**Campus Area Network (CAN)** lies between LAN and MAN, covering educational campuses, military bases, or corporate parks. The entire University of Delhi campus network connecting its various colleges and departments exemplifies a CAN. CANs are optimized for high-speed interconnectivity within a geographically localized but multi-building environment.

**Virtual Private Network (VPN)** deserves special mention as it extends private networks across public infrastructure. VPNs create secure encrypted tunnels over the internet, enabling remote employees to access organizational resources as if they were physically present on the LAN. With the rise of remote work and online classes (especially post-pandemic), VPNs have become essential for DU students accessing college resources from home.

### Network Topologies

Network topology refers to the arrangement of nodes (computers, switches, routers) and the connections between them. Topologies can be physical (actual layout of cables) or logical (data flow pattern).

**Bus Topology** (also called Linear Bus) connects all devices along a single cable called the "bus" or "backbone." Terminators at both ends absorb signals to prevent reflection. Data transmitted by any node travels in both directions along the bus, and all other nodes receive it. The destination node accepts the data while others ignore it. Advantages include simplicity, low cost, and ease of implementation for small networks. However, limitations are significant: if the backbone cable fails, the entire network collapses; performance degrades with increased nodes; and troubleshooting becomes difficult. Thicknet (10BASE5) and Thinnet (10BASE2) are older Ethernet implementations using bus topology.

**Star Topology** dominates modern networking environments. In this configuration, all devices connect to a central hub or switch. When a node sends data, it goes to the central device, which then forwards it to the destination node. This topology offers several advantages: failure of one node doesn't affect others; easy to add or remove devices; and simpler troubleshooting (problems typically isolate to the central device or individual links). However, the central device becomes a single point of failure—if the switch fails, the entire network goes down. Most modern LANs in DU colleges use star topology with Ethernet switches. The main drawback is higher cabling cost due to multiple connections to the center.

**Ring Topology** connects devices in a circular fashion, where each node connects to exactly two others, forming a ring. Data travels around the ring in one direction (unicast) or both directions (dual ring). Token Ring (IEEE 802.5) and FDDI networks historically used this topology. Each node waits for a "token" before transmitting, preventing collisions. Advantages include equal access for all nodes and predictable performance. However, failure of any link or node can disrupt the entire network. Modern implementations often use dual rings for redundancy, as seen in SONET networks.

**Mesh Topology** provides redundant connections between devices. In a **full mesh**, every node connects to every other node, offering maximum redundancy but high cost (for n nodes, n(n-1)/2 connections). A **partial mesh** connects some nodes to multiple others, balancing cost and reliability. Mesh topology is commonly used in WANs where reliability is critical, such as routing in the Internet backbone. Wireless mesh networks are increasingly used in smart city deployments. The Internet's router-level topology approximates a mesh structure.

**Tree Topology** (also called Hierarchical Topology) combines characteristics of bus and star topologies. It features a root node at the top, connected to child nodes, which in turn connect to subordinate nodes, forming a hierarchical structure. This topology suits large networks like those in universities with multiple departments. It supports easy expansion and segmented network management. However, if the root node fails, entire segments become disconnected. Cable length and complexity increase with the network size.

**Hybrid Topology** combines two or more different topologies to leverage the advantages of each. Large organizations often employ hybrid topologies—for example, star topology within departments interconnected via a backbone ring. The Internet itself exhibits hybrid characteristics, combining various topologies at different levels.

### Other Network Classifications

**By Transmission Medium:** Networks can be classified as wired (using Ethernet cables like Cat5e, Cat6, Cat6a, or fiber optics) or wireless (using radio waves, microwaves, or infrared). The Wi-Fi in DU libraries represents wireless networking, while computer labs typically use wired connections for reliability.

**By Architecture:** Client-Server architecture involves central servers providing services to client machines (common in colleges where file servers store student data). Peer-to-Peer (P2P) architecture treats all nodes as equal, as seen in BitTorrent networks and small office file sharing.

**By Protocol Stack:** Networks using TCP/IP (the Internet's foundation) or other protocols like IPX/SPX (legacy NetWare networks) fall into this category.

**By Ownership:** Private networks (owned by organizations for internal use) contrast with Public networks (like the Internet, accessible to everyone).

## Examples

**Example 1: Classifying a University Network Scenario**

Consider the following situation: The Computer Science Department at a DU college has 50 computers in its lab, all connected via Ethernet cables to a central switch located in the server room. The department's network is connected to the college's main server through a fiber optic link. The college internet is provided via a leased line from an ISP.

*Solution:*
- The 50-computer lab network: **LAN** (Local Area Network), using **Star Topology** (all connected to central switch)
- The connection between departments: Could be part of a **CAN** (Campus Area Network)
- The ISP connection for internet access: **WAN** link
- The internal college network: **Private Network**
- Transmission medium: **Wired** (Ethernet cables and fiber optics)

**Example 2: Identifying Topology in a Small Office**

A small startup in Nehru Place has 5 computers. They connect a router to the internet, and each computer connects via Ethernet cable to a switch that is connected to the router. Analyze the topology.

*Solution:*
- Between computers and switch: **Star Topology** (all connect to central switch)
- Between switch and router: **Star Topology** (switch connects to router as another node)
- Overall network: **Hybrid** (combination of star topologies)

**Example 3: Calculating Full Mesh Connections**

If an organization wants to implement full mesh topology for 8 computers in its network room, how many connections are required?

*Solution:*
For full mesh with n nodes: Number of connections = n(n-1)/2
= 8(8-1)/2 = 8×7/2 = 28 connections

This explains why full mesh is impractical for large networks—it requires 28 cables for just 8 devices!

## Exam Tips

1. **Understand the difference between LAN, MAN, and WAN clearly**—this is frequently asked in DU exams. Remember: LAN is your college lab, MAN is your city network, WAN is the Internet.

2. **Know the typical ranges and speeds** for each network type. PAN: ~10m, LAN: ~1km, MAN: ~100km, WAN: global. Speeds decrease as coverage increases.

3. **Topology selection depends on requirements**: For reliability-critical applications, consider mesh; for cost-sensitive small networks, bus or star works; for large hierarchical organizations, tree topology is appropriate.

4. **Star topology dominates modern networks**—in exams, when asked about the most common LAN topology, the answer is Star.

5. **Remember the advantages and disadvantages of each topology**—examiners frequently ask "Explain star topology with advantages and disadvantages" or "Compare bus and ring topologies."

6. **VPN is not a physical network type** but a virtual overlay—it creates a logical private network over public infrastructure.

7. **Transmission media classification**: Wired includes twisted pair, coaxial, fiber optic; Wireless includes radio waves, microwave, satellite, infrared.

8. **Token Ring vs Ethernet**: Token Ring uses logical ring topology (with concentrators appearing as star), while Ethernet traditionally used bus but now predominantly uses star.

9. **Practical application questions**: You may be asked to recommend a network type/topology for specific scenarios (e.g., "Design a network for a DU college with 3 buildings, 500 students").

10. **Understand Single Point of Failure concept**: In star topology, the central hub/switch is a single point of failure; in bus topology, the backbone cable failure affects all nodes.