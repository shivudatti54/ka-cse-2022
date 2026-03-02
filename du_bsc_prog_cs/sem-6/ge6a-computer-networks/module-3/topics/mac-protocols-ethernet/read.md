# MAC Protocols and Ethernet

## Introduction

The Data Link Layer of the OSI model is responsible for node-to-node communication, error detection and correction, and flow control. Within this layer, the Media Access Control (MAC) sublayer addresses a fundamental challenge in computer networking: how to regulate access to a shared communication medium when multiple devices want to transmit simultaneously. This problem, known as the "multiple access problem," is central to local area network (LAN) design and implementation.

Ethernet, developed by Robert Metcalfe and David Boggs at Xerox PARC in 1973, emerged as the dominant LAN technology that solved these challenges through elegant yet simple protocols. Today, Ethernet powers virtually all wired local area networks in homes, offices, and data centers worldwide. Understanding MAC protocols and Ethernet is essential for any computer science student, as these technologies form the backbone of modern networking infrastructure. The concepts covered here appear frequently in DU semester examinations, with typical weightage of 8-12 marks.

This module examines the theoretical foundations of multiple access protocols, the practical implementation in Ethernet standards, and the evolution from early shared-medium networks to modern switched Ethernet architectures.

## Key Concepts

### 1. Multiple Access Protocols

When multiple devices share a common transmission medium (such as a coaxial cable in early Ethernet or the radio spectrum in wireless networks), protocols are needed to coordinate access and prevent data collisions. These are called Multiple Access Protocols or Channel Access Protocols.

#### ALOHA Protocol

Developed at the University of Hawaii for the ALOHAnet, ALOHA represents the simplest multiple access approach. In **Pure ALOHA**, a device transmits whenever it has data to send. If two or more transmissions overlap in time, a collision occurs and the data is corrupted. The sender detects collision through lack of acknowledgment (ACK) and retransmits after a random waiting period.

The maximum efficiency (throughput) of Pure ALOHA is only 18.4%, calculated as:

**S = G × e^(-2G)**

Where G is the average number of frames attempted per frame time. Maximum throughput occurs at G = 0.5, yielding S = 0.5 × e^(-1) ≈ 0.184.

**Slotted ALOHA** improves efficiency by synchronizing transmission times to discrete slots. Devices can only transmit at the beginning of a time slot, reducing the vulnerable period by half. Maximum efficiency becomes 36.8%:

**S = G × e^(-G)**

#### CSMA (Carrier Sense Multiple Access)

CSMA significantly improves efficiency by having devices listen to the channel before transmitting. If the channel is idle (no carrier detected), the device transmits; if busy, it waits until the channel becomes idle. This "listen before talk" approach reduces collisions but doesn't eliminate them entirely due to propagation delay.

**1-Persistent CSMA**: The most aggressive variant—upon sensing idle channel, transmit immediately with probability 1. High collision rate when many stations wait for channel.

**Non-Persistent CSMA**: If channel busy, wait random time before sensing again. Reduces collisions but increases delays.

**p-Persistent CSMA**: Used in slotted systems. If idle, transmit with probability p; with probability (1-p), wait for next slot.

#### CSMA/CD (Collision Detection)

Ethernet uses CSMA with Collision Detection. After starting transmission, a station monitors the channel for other transmissions. If collision detected, it immediately stops transmitting, sends a jam signal to ensure all stations recognize the collision, and then waits before retransmitting using the Binary Exponential Backoff algorithm.

The minimum frame size in CSMA/CD networks must satisfy: **Frame Size ≥ 2 × Propagation Delay × Bandwidth**

This ensures that collision detection works properly—the signal must still be "on the wire" when the transmitting station finishes sending the first bits.

#### CSMA/CA (Collision Avoidance)

Used in wireless networks (IEEE 802.11), CSMA/CA avoids collisions rather than detecting them. Stations use Request to Send (RTS), Clear to Send (CTS), and ACK frames to reserve the channel before data transmission.

### 2. Binary Exponential Backoff Algorithm

After detecting a collision, Ethernet uses this algorithm to calculate random waiting time before retransmission:

1. After first collision, choose random integer k from {0, 1}
2. After second collision, choose from {0, 1, 2, 3}
3. After nth collision (up to n=10), choose from {0, 1, 2, ..., 2^n - 1}
4. Wait k × 512 bit times before retransmitting
5. After 16 consecutive collisions, the frame is discarded and error reported

This algorithm provides exponential backoff, reducing collision probability as more stations experience collisions.

### 3. MAC Addresses

Every network interface controller (NIC) has a unique 48-bit MAC address, also called physical address or hardware address. Format: six groups of two hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E).

- **First 24 bits**: Organization Unique Identifier (OUI) - identifies manufacturer
- **Last 24 bits**: Device identifier assigned by manufacturer

Special addresses:
- **Broadcast**: FF:FF:FF:FF:FF:FF — sent to all devices on LAN
- **Multicast**: Least significant bit of first octet = 1

### 4. Ethernet Frame Structure

IEEE 802.3 frame format:

| Field | Size | Purpose |
|-------|------|---------|
| Preamble | 7 bytes | Synchronization pattern (10101010...) |
| SFD | 1 byte | Start Frame Delimiter (10101011) |
| Destination MAC | 6 bytes | Receiver's physical address |
| Source MAC | 6 bytes | Sender's physical address |
| Type/Length | 2 bytes | Protocol type (0x0800 = IPv4) or length |
| Data | 46-1500 bytes | Upper layer data (padding if needed) |
| FCS | 4 bytes | Frame Check Sequence (CRC-32) |

Maximum frame size: 1518 bytes (without preamble/SFD)
Minimum frame size: 64 bytes (including FCS)

### 5. Ethernet Standards

| Standard | Speed | Medium | Max Segment Length |
|----------|-------|--------|---------------------|
| 10BASE-5 | 10 Mbps | Thick coax (vampire taps) | 500m |
| 10BASE-2 | 10 Mbps | Thin coax (BNC connectors) | 185m |
| 10BASE-T | 10 Mbps | Category 3 UTP | 100m |
| 100BASE-TX | 100 Mbps | Category 5 UTP | 100m |
| 1000BASE-T | 1 Gbps | Category 5e/6 UTP | 100m |
| 10GBASE-T | 10 Gbps | Category 6a/7 | 100m |

Naming convention: `<speed>BASE-<medium type><number of pairs>`

### 6. Hubs vs Switches

**Hub (Repeater)**: Physical layer (Layer 1) device. Receives signal on one port, regenerates and broadcasts to ALL ports. All devices share collision domain and bandwidth. Half-duplex operation only.

**Switch (Bridge)**: Data link layer (Layer 2) device. Maintains MAC address table mapping addresses to ports. Forwards frames only to destination port. Creates separate collision domains per port. Full-duplex operation possible—no CSMA/CD needed in switched Ethernet.

### 7. CSMA/CD in Modern Networks

In contemporary switched Ethernet networks using full-duplex communication, CSMA/CD is effectively unnecessary since:
- Each port creates a dedicated collision domain
- Simultaneous sending and receiving is possible (full-duplex)
- No shared medium exists for collisions

However, CSMA/CD remains essential for understanding legacy half-duplex networks and troubleshooting network issues.

## Examples

### Example 1: Calculating Pure ALOHA Efficiency

**Problem**: In a Pure ALOHA system, the average number of frames transmitted per second is 1000. Each frame takes 2 milliseconds to transmit. Calculate the probability of successful transmission and system throughput.

**Solution**:

Given:
- Frame transmission time T = 2 ms = 0.002 seconds
- Frames transmitted per second = 1000
- So, frames attempted per frame time G = 1000 × 0.002 = 2 frames/frame time

Using Pure ALOHA formula: S = G × e^(-2G)
S = 2 × e^(-4) = 2 × 0.0183 = 0.0366

Probability of successful transmission P(success) = e^(-2G) = e^(-4) ≈ 0.0183

Throughput S = 0.0366 frames per frame time, or approximately 36.6 frames per second (since 0.0366 × 1000 = 36.6)

This demonstrates why pure ALOHA has very low efficiency (~3.66% at this load).

### Example 2: Ethernet Frame Analysis

**Problem**: A network administrator captures an Ethernet frame with the following header bytes (in hexadecimal):
`FF FF FF FF FF FF 00 1A 2B 3C 4D 5E 08 00 45 00 00 3C`

Analyze this frame by identifying: (a) Destination MAC address, (b) Source MAC address, (c) Upper layer protocol, and (d) What type of Ethernet frame this is.

**Solution**:

Breaking down the frame:
- Bytes 1-6 (FF FF FF FF FF FF): Destination MAC - Broadcast address
- Bytes 7-12 (00 1A 2B 3C 4D 5E): Source MAC - Individual device address
- Bytes 13-14 (08 00): Type field - indicates IPv4 (0x0800)

Answers:
(a) Destination MAC: FF:FF:FF:FF:FF:FF (Broadcast)
(b) Source MAC: 00:1A:2B:3C:4D:5E
(c) Upper layer protocol: IPv4 (0x0800 in network byte order)
(d) This is a standard Ethernet II frame (uses Type field instead of 802.3 Length field)

### Example 3: CSMA/CD Backoff Calculation

**Problem**: In an Ethernet network, Station A attempts to transmit a frame and experiences its 5th consecutive collision. Using the Binary Exponential Backoff algorithm, calculate the range of possible waiting times in bit times.

**Solution**:

For the 5th collision (n = 5):
- The backoff range is from 0 to (2^n - 1)
- Maximum n for calculation is min(5, 10) = 5
- Range: 0 to 2^5 - 1 = 0 to 31

Wait time k = random integer from {0, 1, 2, ..., 31}
Wait time in bit times = k × 512

Therefore:
- Minimum wait: 0 × 512 = 0 bit times
- Maximum wait: 31 × 512 = 15,872 bit times

The station will wait between 0 and 15,872 bit times before attempting retransmission. This exponential increase in waiting time reduces the probability of repeated collisions as the channel becomes more congested.

## Exam Tips

1. **Remember ALOHA efficiency formulas**: Pure ALOHA max efficiency = 18.4%, Slotted ALOHA = 36.8%. Don't confuse them in exam answers.

2. **Ethernet frame minimum size**: The 64-byte minimum exists because of CSMA/CD—ensure the frame is still "on the wire" during collision detection time.

3. **CSMA vs CSMA/CD vs CSMA/CA**: Know which technology uses which—Ethernet uses CSMA/CD, Wi-Fi uses CSMA/CA.

4. **Binary Exponential Backoff**: After n collisions, wait k × 512 bit times where k is chosen from {0, 1, ..., 2^n - 1}, capped at n=10.

5. **MAC address structure**: First 24 bits = OUI (manufacturer code), last 24 bits = device ID. FF:FF:FF:FF:FF:FF is broadcast.

6. **Switches vs Hubs**: Switches operate at Layer 2, create separate collision domains, enable full-duplex. Hubs are Layer 1, single collision domain, half-duplex.

7. **Ethernet Type field values**: Remember 0x0800 = IPv4, 0x0806 = ARP, 0x86DD = IPv6.

8. **Full-duplex switched Ethernet eliminates CSMA/CD**: Since no shared medium exists in switched networks, collisions are impossible and CSMA/CD becomes unnecessary.