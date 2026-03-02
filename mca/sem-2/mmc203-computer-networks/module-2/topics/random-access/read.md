# Random Access Protocols (Multiple Access)


## Table of Contents

- [Random Access Protocols (Multiple Access)](#random-access-protocols-multiple-access)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Need for Multiple Access Protocols](#need-for-multiple-access-protocols)
  - [Classification of MAC Protocols](#classification-of-mac-protocols)
  - [ALOHA Protocol](#aloha-protocol)
  - [Carrier Sense Multiple Access (CSMA)](#carrier-sense-multiple-access-csma)
  - [CSMA/CD (Collision Detection)](#csmacd-collision-detection)
  - [CSMA/CA (Collision Avoidance)](#csmaca-collision-avoidance)
- [How It Works](#how-it-works)
  - [CSMA/CD Operation in Ethernet](#csmacd-operation-in-ethernet)
  - [CSMA/CA Operation in WiFi](#csmaca-operation-in-wifi)
- [Examples](#examples)
  - [Example 1: Calculating ALOHA Efficiency](#example-1-calculating-aloha-efficiency)
  - [Example 2: Slotted ALOHA Comparison](#example-2-slotted-aloha-comparison)
  - [Example 3: CSMA/CD Minimum Frame Size](#example-3-csmacd-minimum-frame-size)
  - [Example 4: CSMA/CA Backoff Calculation](#example-4-csmaca-backoff-calculation)
- [Real-World Applications](#real-world-applications)
  - [Ethernet (IEEE 802.3) - CSMA/CD](#ethernet-ieee-8023---csmacd)
  - [WiFi (IEEE 802.11) - CSMA/CA](#wifi-ieee-80211---csmaca)
  - [Satellite Communication](#satellite-communication)
  - [IoT and Low-Power Networks](#iot-and-low-power-networks)
- [Exam Tips](#exam-tips)

## Introduction

In computer networks, when multiple devices share a common communication medium (such as a cable or wireless channel), there is a possibility that two or more devices may attempt to transmit simultaneously, leading to a collision. Multiple Access Protocols, also known as MAC (Medium Access Control) protocols, are mechanisms designed to coordinate access to a shared medium among multiple competing users. These protocols determine which device gets to transmit at what time, thereby avoiding or handling collisions efficiently.

Random Access Protocols, also called contention-based protocols, are a category of MAC protocols where any device can transmit at any time without any predetermined schedule. If collisions occur, they are detected and the devices involved attempt to retransmit after waiting for a random period. This approach is particularly useful in broadcast networks where the traffic is sporadic and the number of users may vary. The key advantage of random access protocols is their simplicity and suitability for bursty traffic patterns, though they may experience performance degradation under heavy load.

The evolution of random access protocols from the basic ALOHA system to sophisticated CSMA/CA used in modern wireless networks represents a continuous effort to maximize throughput while minimizing collisions. Understanding these protocols is essential for network engineers as they form the backbone of local area network technologies like Ethernet and WiFi, which dominate enterprise and consumer networking today.

## Key Concepts

### Need for Multiple Access Protocols

In a shared medium network, multiple stations (computers or devices) are connected to the same physical channel. When two or more stations transmit simultaneously, their signals overlap and become garbled, resulting in a collision. Without a proper protocol, collisions would be frequent, severely degrading network performance. Multiple access protocols provide the rules for orderly channel access, ensuring that data frames reach their destinations without excessive interference.

The shared medium can be a physical cable (as in traditional Ethernet) or the airwaves (as in wireless networks). In both cases, the available bandwidth is limited and must be shared among all users. The fundamental challenge addressed by MAC protocols is the "multiple access problem" - how to allocate a single communication channel among many competing users efficiently and fairly.

### Classification of MAC Protocols

MAC protocols are broadly classified into three categories:

1. **Controlled Access**: Stations take turns transmitting in a predetermined sequence (Token Passing, Polling)
2. **Random Access**: Stations compete for channel access, handling collisions when they occur (ALOHA, CSMA)
3. **Channelization**: The channel is divided into smaller sub-channels allocated to stations (FDMA, TDMA, CDMA)

Random access protocols fall under the contention-based category, where stations may have to contend (compete) for channel access.

### ALOHA Protocol

ALOHA, developed at the University of Hawaii in the 1970s, was one of the earliest random access protocols. It was designed for radio communication between computers distributed across the Hawaiian islands.

**Pure ALOHA**: In pure ALOHA, a station can transmit data whenever it has a frame to send. The station then waits for an acknowledgment. If no acknowledgment is received within a timeout period, the station assumes a collision occurred and retransmits the frame after a random waiting period. This random backoff is crucial to avoid synchronized retransmissions.

The vulnerable time (the period during which a frame is susceptible to collision) in pure ALOHA is **2T**, where T is the frame transmission time. If any other station transmits during this vulnerable period, a collision will occur.

**Slotted ALOHA**: To improve efficiency, slotted ALOHA divides time into discrete slots equal to the frame transmission time T. Stations can only transmit at the beginning of a slot. This reduces the vulnerable time to **T** (half of pure ALOHA), effectively doubling the maximum throughput.

The maximum efficiency (throughput) formulas are:
- Pure ALOHA: S = G × e^(-2G), where G is the average number of attempts per frame time. Maximum throughput occurs at G=0.5, giving Smax = 0.184 (18.4%)
- Slotted ALOHA: S = G × e^(-G), where maximum throughput occurs at G=1, giving Smax = 0.368 (36.8%)

### Carrier Sense Multiple Access (CSMA)

CSMA is an improvement over ALOHA where stations listen to the channel (carrier sensing) before transmitting. If the channel is sensed as idle, the station transmits; if busy, it waits until the channel becomes idle. This simple enhancement significantly reduces the probability of collisions.

**1-Persistent CSMA**: When a station has data to send, it senses the channel continuously. As soon as the channel becomes idle, it transmits immediately with probability 1. While this minimizes delay, it can cause collisions when multiple stations are waiting for the channel to become idle.

**Non-Persistent CSMA**: When the channel is busy, the station waits for a random amount of time before sensing again. This reduces collisions but increases delay. The station does not continuously sense the channel, allowing other stations to use it.

**p-Persistent CSMA**: Used in slotted channels. When a station finds the channel idle at the beginning of a slot, it transmits with probability p. With probability (1-p), it defers to the next slot and checks again. This provides a balance between efficiency and delay.

### CSMA/CD (Collision Detection)

CSMA with Collision Detection is used in Ethernet (IEEE 802.3) networks. In CSMA/CD, stations continue to listen to the channel while transmitting to detect collisions quickly. When a collision is detected, all transmitting stations immediately stop transmitting and send a jam signal to ensure all stations are aware of the collision. After sending the jam signal, each station waits for a random backoff period before attempting to retransmit.

**Minimum Frame Size**: For CSMA/CD to work effectively, the frame transmission time must be at least twice the maximum propagation delay (2τ). This ensures that a station can detect a collision before it finishes transmitting. In 10 Mbps Ethernet, the minimum frame size is 64 bytes (512 bits), requiring 51.2 μs for transmission. This corresponds to a maximum network segment length of 500 meters.

**Performance**: The maximum efficiency of CSMA/CD is approximately 1 / (1 + 5a), where a = propagation delay / transmission time. Under ideal conditions, efficiency can reach about 98.6%.

### CSMA/CA (Collision Avoidance)

CSMA with Collision Avoidance is used in wireless networks (IEEE 802.11 WiFi). Unlike CSMA/CD, wireless stations cannot reliably detect collisions while transmitting due to the hidden terminal problem and the near-far effect. Therefore, CSMA/CA attempts to avoid collisions rather than detect them.

**Mechanisms**:
- **Inter-Frame Space (IFS)**: Stations wait for a specified IFS period after the channel becomes idle. Different IFS values (SIFS, DIFS, EIFS) create priority levels.
- **Random Backoff**: After waiting the IFS, stations pick a random backoff counter and count down to zero. The station transmits only when the counter reaches zero.
- **RTS/CTS (Request to Send/Clear to Send)**: An optional mechanism to solve the hidden terminal problem. The sender sends an RTS frame, and the receiver responds with a CTS frame. Other stations that hear either RTS or CTS set their Network Allocation Vector (NAV) to reserve the channel.

**NAV (Network Allocation Vector)**: A virtual carrier sensing mechanism where stations maintain a timer indicating how long the channel will be reserved. This information is carried in the duration field of RTS, CTS, and data frames.

## How It Works

### CSMA/CD Operation in Ethernet

1. **Carrier Sensing**: When a station has a frame to transmit, it first monitors the network to check if any other station is transmitting (carrier sense).
2. **Collision Detection**: While transmitting, the station monitors the signal on the wire. If the signal voltage level exceeds normal (indicating multiple stations are transmitting), a collision is detected.
3. **Jam Signal**: Upon detecting a collision, the station immediately stops transmitting and sends a special 32-bit jam signal to ensure all other stations are aware of the collision.
4. **Backoff**: After sending the jam signal, the station enters a random backoff period (using binary exponential backoff algorithm) before attempting to retransmit.
5. **Retransmission**: After the backoff period, the station again senses the carrier and attempts transmission. If another collision occurs, the backoff range is doubled (up to a maximum), and the process repeats.

### CSMA/CA Operation in WiFi

1. **Channel Sensing**: The station senses if the medium is idle.
2. **Wait IFS**: If idle, the station waits for a DIFS (DCF Inter-Frame Space) period.
3. **Backoff Counter**: After DIFS, the station selects a random backoff window and begins counting down slots. If the channel becomes busy during counting, the counter pauses.
4. **Transmission**: When the counter reaches zero, the station transmits its frame.
5. **ACK**: The receiver, after receiving the frame correctly, waits for a SIFS and sends an acknowledgment (ACK).
6. **RTS/CTS (Optional)**: For larger frames, the optional RTS/CTS exchange may be used to reserve the channel and solve hidden terminal problems.

## Examples

### Example 1: Calculating ALOHA Efficiency

**Problem**: In a pure ALOHA system with a channel data rate of 1 Mbps and frame size of 1000 bits, calculate the maximum throughput and the vulnerable time.

**Solution**:
- Frame transmission time T = 1000 bits / 1,000,000 bits/sec = 1 ms = 10⁻³ seconds
- Maximum throughput Smax = 0.184 (18.4% of channel capacity)
- Maximum throughput in bps = 0.184 × 1 Mbps = 184 kbps
- Vulnerable time = 2T = 2 × 1 ms = 2 ms

**Answer**: Maximum throughput = 184 kbps, Vulnerable time = 2 ms

### Example 2: Slotted ALOHA Comparison

**Problem**: Compare the maximum throughput of pure ALOHA and slotted ALOHA when G (attempts per frame time) = 0.5.

**Solution**:
- For Pure ALOHA: S = G × e^(-2G) = 0.5 × e^(-1) = 0.5 × 0.368 = 0.184
- For Slotted ALOHA: S = G × e^(-G) = 0.5 × e^(-0.5) = 0.5 × 0.607 = 0.3035

**Answer**: Slotted ALOHA achieves approximately 65% better throughput (0.3035 vs 0.184) at G=0.5

### Example 3: CSMA/CD Minimum Frame Size

**Problem**: In a 10 Mbps Ethernet network with maximum cable length of 2500 meters and propagation speed of 2×10⁸ m/s, calculate the minimum frame size required for proper collision detection.

**Solution**:
- Propagation delay τ = Distance / Speed = 2500 m / (2×10⁸ m/s) = 12.5 μs
- Round-trip propagation time = 2τ = 25 μs
- Minimum frame transmission time ≥ 2τ = 25 μs
- At 10 Mbps: Minimum bits = 10 Mbps × 25 μs = 10×10⁶ × 25×10⁻⁶ = 250 bits
- Standard minimum = 512 bits (64 bytes), which is greater than calculated value

**Answer**: Minimum frame size = 64 bytes (512 bits)

### Example 4: CSMA/CA Backoff Calculation

**Problem**: In an 802.11 network, a station picks a random backoff value from the range [0, 15]. If the DIFS is 50 μs and each slot time is 9 μs, calculate the minimum and maximum waiting times before transmission.

**Solution**:
- Minimum waiting time = 0 slots × 9 μs = 0 μs (transmits after DIFS if channel idle)
- Maximum waiting time = 15 slots × 9 μs = 135 μs
- Total minimum waiting time = DIFS + slot backoff = 50 + 0 = 50 μs
- Total maximum waiting time = 50 + 135 = 185 μs

**Answer**: Minimum waiting time = 50 μs, Maximum waiting time = 185 μs

## Real-World Applications

### Ethernet (IEEE 802.3) - CSMA/CD

Ethernet is the most widely deployed LAN technology, using CSMA/CD with binary exponential backoff. Traditional 10BASE-T and 100BASE-TX Ethernet networks use CSMA/CD, though modern switched Ethernet operates in full-duplex mode, eliminating collisions entirely. The protocol ensures fair access in shared-medium configurations (like old 10BASE5 thick coax or hub-based networks). Ethernet frames include destination and source MAC addresses, type field, data, and CRC for error detection.

### WiFi (IEEE 802.11) - CSMA/CA

Wireless local area networks (WLANs) use CSMA/CA due to the inherent challenges of wireless communication. The Hidden Terminal Problem (where stations cannot sense each other due to distance or obstacles) is addressed through RTS/CTS exchange. WiFi networks support various data rates (up to 9.6 Gbps in 802.11ax) through adaptive modulation and coding. The protocol includes power management, encryption (WPA/WPA2/WPA3), and roaming capabilities.

### Satellite Communication

Modified ALOHA protocols are used in satellite communication systems where propagation delay is significant. S-ALOHA (Slotted ALOHA) provides better efficiency for these high-delay environments.

### IoT and Low-Power Networks

CSMA/CA principles are adapted in various IoT protocols like Zigbee (IEEE 802.15.4), where low-power devices need efficient channel access in congested environments.

## Exam Tips

1. **Remember the throughput formulas**: Pure ALOHA maximum = 18.4%, Slotted ALOHA maximum = 36.8%. These are frequently asked in university exams.

2. **Understand vulnerable time**: For Pure ALOHA, it's 2T; for Slotted ALOHA, it's T. This concept often appears in numerical problems.

3. **CSMA variants**: Know the difference between 1-persistent, non-persistent, and p-persistent CSMA. Non-persistent has lowest collisions but highest delay.

4. **CSMA/CD minimum frame size**: Remember that minimum frame size = 2 × propagation delay × bandwidth. This ensures collision detection works properly.

5. **CSMA/CA components**: Remember the key mechanisms - IFS (SIFS, DIFS), random backoff, RTS/CTS, and NAV.

6. **Ethernet vs WiFi**: Ethernet uses CSMA/CD (collision detection), while WiFi uses CSMA/CA (collision avoidance) due to wireless transmission challenges.

7. **Hidden Terminal Problem**: Understand how RTS/CTS in 802.11 solves this issue that CSMA/CD cannot address in wireless networks.

8. **Binary Exponential Backoff**: In Ethernet, after each collision, stations wait for a random time that doubles with each successive collision (up to 1024 slot times).

9. **Collision Domain**: Remember that a hub-based Ethernet creates a single collision domain, while switches create separate collision domains for each port.

10. **Carrier Sense**: Both CSMA/CD and CSMA/CA perform carrier sensing before transmission, but CSMA/CD can detect collisions during transmission while CSMA/CA cannot.