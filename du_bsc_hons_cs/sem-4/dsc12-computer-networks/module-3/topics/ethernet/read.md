# Ethernet

## Introduction

Ethernet is the most widely used technology for Local Area Networks (LANs) worldwide, forming the backbone of modern computer networking. Developed originally at Xerox PARC in the 1970s and standardized by IEEE as 802.3, Ethernet has evolved from its original 10 Mbps specification to today's 400 Gbps and even 800 Gbps standards. For University of Delhi Computer Science students, understanding Ethernet is fundamental to grasping how data travels across local networks, a core concept in both theoretical examinations and practical networking scenarios.

The significance of Ethernet in contemporary networking cannot be overstated. It dominates the LAN market with approximately 90% of all networked connections using Ethernet technology. From connecting computers in a university laboratory to linking servers in data centers, Ethernet provides the reliable, cost-effective, and scalable foundation upon which modern communication systems operate. This topic not only prepares students for examination questions but also equips them with practical knowledge essential for network administration and design roles.

## Key Concepts

### Historical Development and Standards

Ethernet's journey began in 1973 when Robert Metcalfe at Xerox PARC conceived the idea of a local network system. The original Ethernet operated at 10 Mbps using coaxial cables and a bus topology. The IEEE 802.3 standard, first published in 1983, formalized the Physical and MAC (Medium Access Control) layer specifications. Over the decades, Ethernet has evolved through multiple generations: Fast Ethernet (100 Mbps in 1995), Gigabit Ethernet (1 Gbps in 1999), 10 Gigabit Ethernet (2002), 40/100 Gigabit Ethernet (2010), and the recent 400/800 Gigabit Ethernet standards (2017-2020).

### The Ethernet Frame Structure

The Ethernet frame is the fundamental unit of data transmission, comprising several critical fields that enable reliable communication. Understanding the frame structure is essential for troubleshooting and network analysis.

**Preamble (7 bytes):** A pattern of alternating 1s and 0s (10101010) that synchronizes the receiving station's clock with the incoming data stream.

**Start Frame Delimiter (SFD) (1 byte):** The sequence 10101011 marks the beginning of the frame and helps the receiver recognize the actual frame data.

**Destination Address (6 bytes):** The MAC address of the receiving interface. This is a unique 48-bit identifier assigned to each network interface card.

**Source Address (6 bytes):** The MAC address of the sending device.

**Type/Length Field (2 bytes):** Indicates either the length of the data payload (if values ≤ 1500) or the protocol type of the encapsulated data (for values > 1500). Common values include 0x0800 for IPv4 and 0x86DD for IPv6.

**Data Payload (46-1500 bytes):** Contains the actual higher-layer data. The minimum padding is added to ensure the frame meets the minimum size requirement.

**Frame Check Sequence (FCS) (4 bytes):** A CRC-32 checksum used for error detection. The transmitter calculates this value, and the receiver recalculates it to verify data integrity.

The minimum Ethernet frame size is 64 bytes (excluding preamble and SFD), while the maximum is 1518 bytes. Frames smaller than 64 bytes are called "runts," and those larger than 1518 bytes are called "giants."

### Carrier Sense Multiple Access with Collision Detection (CSMA/CD)

CSMA/CD is the fundamental media access control protocol that governs how devices share the common transmission medium in traditional Ethernet. This protocol ensures orderly access and handles collision scenarios when multiple devices attempt transmission simultaneously.

**Carrier Sense:** Before transmitting, a device "listens" to the network medium to check if it is idle. If another device is transmitting, the device waits until the medium becomes free.

**Multiple Access:** Multiple devices can attempt to access the network simultaneously, giving each equal opportunity to transmit.

**Collision Detection:** If two or more devices transmit simultaneously, a collision occurs on the network. Devices monitor the medium during transmission; if they detect a voltage level different from what they are transmitting, a collision has occurred.

**Backoff Algorithm:** Upon detecting a collision, devices immediately stop transmitting and wait for a random backoff period before attempting retransmission. This random wait time reduces the probability of another collision. The binary exponential backoff algorithm doubles the average wait time after each collision, up to a maximum of 10 attempts.

The CSMA/CD protocol is essential for half-duplex Ethernet operation. However, modern switched Ethernet typically operates in full-duplex mode, eliminating the need for CSMA/CD since collisions cannot occur in properly designed switched networks.

### MAC Addresses

Media Access Control (MAC) addresses are unique 48-bit identifiers assigned to network interface controllers (NICs) at the time of manufacture. These addresses are expressed as 12 hexadecimal digits, typically in the format XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX.

The first 24 bits (first six hexadecimal digits) represent the Organization Unique Identifier (OUI), assigned by IEEE to manufacturers. The remaining 24 bits are manufacturer-assigned serial numbers. For example, in the address 00:1A:2B:3C:4D:5E, the first three octets (00:1A:2B) identify Cisco Systems.

MAC addresses operate at Layer 2 of the OSI model and are used for communication within a local network segment. They are essential for Ethernet switching, where frames are forwarded based on destination MAC addresses.

### Ethernet Topologies

Ethernet originally used a **bus topology** where all devices connected to a single coaxial cable. This topology, used in 10BASE-5 (Thicknet) and 10BASE-2 (Thinnet), allowed any device to receive all transmissions but created a single point of failure—if the backbone cable was damaged, the entire network went down.

**Star topology** became the dominant Ethernet architecture, especially with the advent of twisted-pair cabling (Category 5e, Category 6, etc.). In star topology, each device connects to a central hub or switch. While this increases cabling requirements, it provides better fault isolation and easier troubleshooting. A failed cable affects only one device, not the entire network.

### Switched Ethernet

The introduction of Ethernet switches revolutionized network design by creating dedicated communication paths between devices. Unlike hubs that simply repeat incoming signals to all ports, switches examine the destination MAC address of each frame and forward it only to the appropriate port.

Switches maintain a **MAC address table** (also called a forwarding table) that maps MAC addresses to specific ports. When a frame arrives, the switch learns the source MAC address and records which port it came from. The switch then looks up the destination address in its table and forwards the frame accordingly.

This approach provides several advantages:
- **Full-duplex operation:** Simultaneous transmission and reception eliminate collisions
- **Increased bandwidth:** Each port provides dedicated bandwidth
- **Reduced collision domains:** Each port is its own collision domain
- **Better security:** Frames are not broadcast to unnecessary ports

### Collision Domains and Broadcast Domains

A **collision domain** is a network segment where collisions can occur. In traditional hub-based Ethernet, all devices share the same collision domain. Switches break up collision domains—each switch port represents a separate collision domain in half-duplex mode.

A **broadcast domain** is the network segment where broadcast frames (frames with destination MAC address FF:FF:FF:FF:FF:FF) are forwarded. Routers (Layer 3 devices) separate broadcast domains. Without proper network segmentation, excessive broadcast traffic can degrade network performance—a problem known as broadcast storms.

### Ethernet Standards Naming Convention

Ethernet standards follow a consistent naming convention: **Speed - Signaling Method - Media Type**

For example:
- **10BASE-T:** 10 Mbps, baseband signaling, twisted-pair cable
- **100BASE-TX:** 100 Mbps, baseband, two pairs of Category 5 twisted-pair (Fast Ethernet)
- **1000BASE-LX:** 1 Gbps, baseband, long-wavelength laser over single-mode or multimode fiber
- **10GBASE-T:** 10 Gbps, baseband, twisted-pair copper (Category 6a or 7)

## Examples

### Example 1: Frame Structure Analysis

Consider an Ethernet frame captured on a network: `FF:FF:FF:FF:FF:FF 00:1A:2B:3C:4D:5E 0800 45 00 00 3C 1C 46 40 00 80 06 00 00 C0 A8 01 0A C0 A8 01 01`

**Analysis:**
- Destination Address: FF:FF:FF:FF:FF:FF (Broadcast address - this is an ARP request)
- Source Address: 00:1A:2B:3C:4D:5E (The sender's MAC)
- Type/Length: 0x0800 (0x0800 = 2048 decimal, indicates IPv4)
- The remaining bytes represent the IPv4 packet encapsulated within the Ethernet frame

### Example 2: CSMA/CD Collision Scenario

Two workstations, A and B, are connected to a shared Ethernet segment using a hub. Both attempt to send data simultaneously:

1. Both stations check the carrier—initially, the line appears idle
2. Both begin transmission (Collision Detection Phase)
3. Both stations detect the collision (voltage irregularity)
4. Both immediately stop transmitting and send jam signals
5. Both calculate random backoff using the binary exponential algorithm:
   - First collision: Random number between 0-1 slot times
   - Second collision: Random number between 0-3 slot times
   - Third collision: Random number between 0-7 slot times
6. After their respective backoff periods, both retry

### Example 3: Minimum Frame Size Calculation

In a 10 Mbps Ethernet network with maximum cable length of 2500 meters and 4 repeaters:

**Given:**
- Network diameter = 2500 meters
- Signal propagation speed ≈ 200,000 km/s (2 × 10⁸ m/s)
- One-way propagation time = 2500 / (2 × 10⁸) = 12.5 microseconds
- Round-trip propagation time = 25 microseconds

**Required minimum frame transmission time:**
- For CSMA/CD to work, the transmitting station must still be transmitting when the collision signal returns
- Minimum frame size = Bandwidth × Round-trip time
- Minimum frame size = 10 Mbps × 25 μs = 10 × 10⁶ × 25 × 10⁻⁶ = 250 bits ≈ 32 bytes

The standard minimum is 64 bytes (512 bits), which provides a safety margin and accounts for signal degradation through repeaters.

## Exam Tips

1. **Frame Structure Memorization:** Remember all six fields of the Ethernet frame in order: Preamble (7B), SFD (1B), Destination MAC (6B), Source MAC (6B), Type/Length (2B), Data (46-1500B), FCS (4B). Total: 64-1518 bytes.

2. **CSMA/CD Process Order:** The correct sequence is: Sense → Transmit → Detect Collision → Jam → Backoff → Retry. This is frequently tested in DU examinations.

3. **Minimum Frame Size Justification:** Understand why 64 bytes is the minimum—it must take longer to transmit than the round-trip time for collision detection across the maximum network diameter.

4. **Broadcast vs. Collision Domains:** Remember that switches break collision domains but not broadcast domains; routers break both. This distinction is crucial for network design questions.

5. **Full-Duplex vs. Half-Duplex:** In full-duplex mode, CSMA/CD is disabled because simultaneous bidirectional communication eliminates collision possibility. This is a common exam question.

6. **MAC Address Structure:** The first 24 bits are OUI (manufacturer code), and the last 24 bits are NIC-specific. Recognize that broadcast MAC address is all 1s (FF:FF:FF:FF:FF:FF).

7. **Ethernet Standards Naming:** Be able to decode 10BASE-T, 100BASE-FX, 1000BASE-LX, etc. The first number is speed in Mbps, BASE indicates baseband, and the last letters indicate the physical medium.

8. **Switching vs. Hub Operation:** Remember that hubs are Layer 1 (Physical) devices that repeat signals to all ports, while switches are Layer 2 (Data Link) devices that forward based on MAC addresses.

9. **CRC Error Detection:** The Frame Check Sequence (FCS) uses CRC-32 and can detect all single-bit errors, double-bit errors, and odd numbers of bit errors within the frame.

10. **Real-World Applications:** Connect theoretical knowledge to practical scenarios—Ethernet remains the dominant LAN technology due to its simplicity, low cost, and continuous evolution.