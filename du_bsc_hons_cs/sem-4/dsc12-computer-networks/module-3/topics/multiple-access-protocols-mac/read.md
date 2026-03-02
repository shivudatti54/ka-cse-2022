# Multiple Access Protocols (MAC)

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In modern computer networks, multiple devices often share a common communication medium (channel) to transmit data. This shared medium can be a physical cable (like in Ethernet), a frequency band (like in wireless networks), or a satellite link. The fundamental challenge arises when two or more devices attempt to transmit data simultaneously, leading to **collision** and resulting in corrupted or lost data.

**Multiple Access Protocols** (also known as Medium Access Control or MAC protocols) are the set of rules and procedures that govern how multiple devices can access and use a shared communication channel without interfering with each other. These protocols determine when a device can transmit, how it detects collisions, and how it recovers from them.

### Real-World Relevance

- **Wi-Fi Networks**: Your smartphone and laptop simultaneously connect to a single wireless router using MAC protocols
- **Office Ethernet**: Multiple computers connected to a switch or hub
- **Mobile Networks**: Thousands of phones communicating with cell towers
- **Satellite Communication**: Multiple ground stations transmitting to a satellite

This topic is essential for the Delhi University BSc (Hons) Computer Science curriculum under the Computer Networks paper, specifically aligned with the NEP 2024 UGCF guidelines.

---

## 2. Need for Multiple Access Protocols

When multiple stations share a common broadcast channel, the following problems emerge:

1. **Channel Allocation**: Determining which station gets to use the channel
2. **Collision Management**: Handling situations when multiple stations transmit simultaneously
3. **Fairness**: Ensuring all stations get reasonable access to the channel
4. **Efficiency**: Maximizing channel utilization while minimizing delays

The MAC sublayer (Layer 2 in the OSI model) addresses these challenges through various protocols classified into three main categories.

---

## 3. Classification of MAC Protocols

```
MAC Protocols
├── Random Access Protocols (Contention-based)
│   ├── ALOHA
│   ├── Slotted ALOHA
│   ├── CSMA (Carrier Sense Multiple Access)
│   │   ├── 1-Persistent CSMA
│   │   ├── Non-Persistent CSMA
│   │   └── p-Persistent CSMA
│   ├── CSMA/CD (Collision Detection)
│   └── CSMA/CA (Collision Avoidance)
├── Controlled Access Protocols (Reservation-based)
│   ├── Reservation
│   ├── Polling
│   ├── Token Passing
│   │   ├── Token Ring (IEEE 802.5)
│   │   └── Token Bus (IEEE 802.4)
│   └── Ethernet (CSMA/CD)
└── Channelization Protocols
    ├── TDMA (Time Division Multiple Access)
    ├── FDMA (Frequency Division Multiple Access)
    └── CDMA (Code Division Multiple Access)
```

---

## 4. Random Access Protocols (Contention-Based)

Random access protocols allow stations to transmit data whenever they have it, but they must handle collisions that may occur. These are also called **contention-based protocols** because stations contend for channel access.

### 4.1 Pure ALOHA

Developed in the 1970s at the University of Hawaii for the ALOHAnet, this is the simplest random access protocol.

**How it Works:**
- When a station has a frame to send, it transmits immediately
- The station waits for an acknowledgment (ACK) from the receiver
- If no ACK is received within a timeout period, the station assumes a collision occurred
- The station then waits for a random amount of time (backoff) before retransmitting

**Vulnerable Period:**
- In Pure ALOHA, the vulnerable period is **2 × T**, where T is the frame transmission time
- This is because a collision can occur if another station starts transmitting up to T seconds before or after our transmission

**Maximum Efficiency:**
```
Maximum Throughput (S) = 0.184 (or 18.4%)
```

This low efficiency means Pure ALOHA is rarely used in practice today.

### 4.2 Slotted ALOHA

Slotted ALOHA improves upon Pure ALOHA by dividing time into discrete slots.

**How it Works:**
- Time is divided into slots of duration equal to one frame transmission time (T)
- Stations can only transmit at the beginning of a slot
- If a collision occurs, the station retransmits in a future slot after a random backoff

**Vulnerable Period:**
- The vulnerable period is reduced to **T** (half of Pure ALOHA)
- Collisions can only occur if another station transmits in the same slot

**Maximum Efficiency:**
```
Maximum Throughput (S) = 0.368 (or 36.8%)
```

**Example: Slotted ALOHA Efficiency Calculation**

```python
# Slotted ALOHA Throughput Simulation
import random
import math

def slotted_aloha_throughput(num_stations, num_slots, frame_rate):
    """
    Simulate Slotted ALOHA and calculate throughput
    
    Parameters:
    - num_stations: Number of competing stations
    - num_slots: Number of time slots to simulate
    - frame_rate: Average frames generated per slot per station
    """
    successful_transmissions = 0
    collisions = 0
    idle_slots = 0
    
    for slot in range(num_slots):
        # Each station decides to transmit with probability frame_rate
        transmitting_stations = sum(1 for _ in range(num_stations) 
                                    if random.random() < frame_rate)
        
        if transmitting_stations == 0:
            idle_slots += 1
        elif transmitting_stations == 1:
            successful_transmissions += 1
        else:
            collisions += 1
    
    throughput = successful_transmissions / num_slots
    return {
        'successful': successful_transmissions,
        'collisions': collisions,
        'idle': idle_slots,
        'throughput': throughput
    }

# Example: 100 stations, 10000 slots, 0.01 frame rate per slot
result = slotted_aloha_throughput(100, 10000, 0.01)
print(f"Slotted ALOHA Simulation Results:")
print(f"Successful transmissions: {result['successful']}")
print(f"Collisions: {result['collisions']}")
print(f"Idle slots: {result['idle']}")
print(f"Throughput: {result['throughput']:.4f}")
print(f"\nTheoretical maximum: {1/e:.4f} (where e ≈ 2.718)")
```

### 4.3 CSMA (Carrier Sense Multiple Access)

CSMA improves upon ALOHA by having stations listen to the channel before transmitting (carrier sensing).

**How it Works:**
1. Before transmitting, a station senses the channel
2. If the channel is idle (no carrier detected), the station transmits
3. If the channel is busy, the station waits until it becomes idle

**Variants of CSMA:**

#### (a) 1-Persistent CSMA
- When a station wants to transmit, it senses the channel
- If idle, it transmits immediately (probability = 1)
- If busy, it continues to sense until idle, then transmits immediately
- **Problem**: High collision probability when multiple stations are waiting

#### (b) Non-Persistent CSMA
- When a station wants to transmit, it senses the channel
- If idle, it transmits immediately
- If busy, it waits for a random amount of time before sensing again
- **Advantage**: Reduces collision probability
- **Disadvantage**: Increased delay

#### (c) p-Persistent CSMA
- Used in slotted channels (like discrete time systems)
- When a slot begins and the channel is idle:
  - Transmit with probability p
  - With probability (1-p), defer to the next slot
- If the channel becomes busy, wait and restart the algorithm

### 4.4 CSMA/CD (Collision Detection)

CSMA with Collision Detection is used in Ethernet networks (IEEE 802.3).

**How it Works:**
1. A station senses the channel before transmitting
2. If idle, it starts transmitting
3. While transmitting, it monitors the channel for collisions
4. If a collision is detected, it immediately stops transmitting
5. It then transmits a jamming signal to ensure all stations know about the collision
6. After jamming, it waits for a random backoff period before retransmitting

**Key Features:**
- **Collision Detection Time**: Must detect collision before transmission completes
- **Minimum Frame Size**: Ensures collision detection works (512 bits for 10 Mbps Ethernet)
- **Binary Exponential Backoff**: Algorithm for calculating random backoff

**Maximum Efficiency:**
```
Maximum Throughput ≈ 1 / (1 + 5a)  where a = propagation delay/transmission time
```

### 4.5 Binary Exponential Backoff Algorithm

This algorithm is used in Ethernet to determine the waiting time after a collision.

**Algorithm Steps:**

1. After the first collision, choose a random number r from {0, 1}
2. Wait for r × slot time (512 bit times)
3. If collision occurs again:
   - After 2nd collision: choose r from {0, 1, 2, 3}
   - After 3rd collision: choose r from {0, 1, 2, ..., 7}
   - After nth collision: choose r from {0, 1, ..., 2^n - 1}
4. Maximum number of attempts is 10 (after that, frame is discarded)

**Implementation Example:**

```python
import random
import math

class BinaryExponentialBackoff:
    def __init__(self, max_attempts=10, slot_time=51.2e-6):  # 51.2 μs for 10Mbps Ethernet
        self.max_attempts = max_attempts
        self.slot_time = slot_time
        self.collision_count = 0
    
    def calculate_backoff(self):
        """Calculate backoff time using Binary Exponential Backoff"""
        if self.collision_count >= self.max_attempts:
            print(f"Frame discarded after {self.max_attempts} collision attempts")
            return None
        
        # k = min(collision_count, 10)
        k = min(self.collision_count, 10)
        
        # Choose random r from [0, 2^k - 1]
        r = random.randint(0, (2 ** k) - 1)
        
        # Backoff time = r * slot_time
        backoff_time = r * self.slot_time
        
        return backoff_time
    
    def attempt_transmission(self):
        """Simulate a transmission attempt"""
        while self.collision_count < self.max_attempts:
            backoff = self.calculate_backoff()
            print(f"Attempt {self.collision_count + 1}: Waiting {backoff*1000:.2f} ms")
            
            # Simulate transmission (in reality, this would be actual network operation)
            # Assume collision occurs
            self.collision_count += 1
            
            if self.collision_count < self.max_attempts:
                print(f"Collision detected! Backing off...")
        
        print("Transmission failed - frame discarded")

# Example usage
backoff = BinaryExponentialBackoff()
backoff.attempt_transmission()
```

---

## 5. Controlled Access Protocols (Reservation-Based)

Controlled access protocols coordinate station access to prevent collisions entirely.

### 5.1 Token Passing

In token passing, a special frame called a **token** circulates among stations. Only the station possessing the token can transmit.

**Token Ring (IEEE 802.5):**
- Stations are connected in a logical ring
- Token circulates around the ring
- When a station receives the token:
  - If it has data to send, it attaches data to the token
  - Sends it to the destination
  - The token becomes "busy"
  - After acknowledgment, it releases the token
- If no data to send, it passes the token to the next station

**Token Bus (IEEE 802.4):**
- Stations are connected to a bus topology
- Token is passed logically (not physically in a ring)
- More complex but combines advantages of token passing and bus topology

**Advantages:**
- No collisions
- Guaranteed access (fairness)
- Predictable delays

**Disadvantages:**
- Token loss can bring down the entire network
- Additional overhead for token management

### 5.2 Polling

In polling, a central controller (primary station) asks each station (secondary station) if it has data to send.

**How it Works:**
1. Primary station sends a poll frame to a secondary station
2. Secondary station responds:
   - With data if it has any
   - With a negative poll if it has no data
3. Primary station moves to the next station
4. Process repeats

**Used in:** Classic IBM SNA networks, some wireless networks

---

## 6. Channelization Protocols

Channelization divides the available bandwidth among multiple users.

### 6.1 TDMA (Time Division Multiple Access)

TDMA divides the frequency band into time slots, with each station assigned one or more slots.

**How it Works:**
- Time is divided into frames
- Each frame is divided into slots
- Each station gets exclusive use of its assigned slot(s)
- Stations can transmit only during their assigned time

**Example (Simplified TDMA Frame):**

```
Frame 1          Frame 2          Frame 3
+---------+     +---------+     +---------+
| S1|S2|S3| --> | S1|S2|S3| --> | S1|S2|S3|
+---------+     +---------+     +---------+
   ↑  ↑  ↑
   |  |  └──> Station 3's slot
   |  └─────> Station 2's slot
   └────────> Station 1's slot
```

**Used in:** GSM (mobile), digital satellite systems, some military communications

### 6.2 FDMA (Frequency Division Multiple Access)

FDMA divides the frequency band into separate frequency channels.

**How it Works:**
- The total bandwidth is divided into non-overlapping frequency bands
- Each station is assigned a dedicated frequency band
- Stations can transmit simultaneously on their assigned frequencies

```
Frequency
    ^
    |  ┌─────┐  ┌─────┐  ┌─────┐
    |  │ Ch1 │  │ Ch2 │  │ Ch3 │
    |  │     │  │     │  │     │
    +--+─────┼──┼─────┼──┼─────┼──> Time
             Station 1  Station 2  Station 3
```

**Used in:** First-generation analog cellular systems, FM radio, satellite communication

### 6.3 CDMA (Code Division Multiple Access)

CDMA allows multiple stations to transmit simultaneously on the same frequency using unique codes.

**How it Works:**
- Each station is assigned a unique spreading code
- All stations transmit on the same frequency simultaneously
- The receiver uses the code to extract the intended signal
- Signals from other stations appear as noise

**Key Concepts:**
- **Spreading**: Each bit is expanded into multiple chips using the spreading code
- **Orthogonal Codes**: Codes that have zero cross-correlation (like Walsh codes)
- **Processing Gain**: Ratio of chip rate to data rate

**Example: Simple CDMA Encoding**

```python
import numpy as np

def cdma_encode(data_bits, spreading_code):
    """
    Encode data using CDMA spreading code
    
    Parameters:
    - data_bits: List of bits to transmit (0 or 1)
    - spreading_code: List of chips (+1 or -1)
    """
    encoded = []
    for bit in data_bits:
        if bit == 1:
            # Multiply by spreading code
            encoded.extend(spreading_code)
        else:
            # Invert spreading code for 0
            encoded.extend([-chip for chip in spreading_code])
    return encoded

def cdma_decode(received_signal, spreading_code):
    """
    Decode CDMA signal using the same spreading code
    
    Parameters:
    - received_signal: The encoded signal
    - spreading_code: The spreading code used for encoding
    """
    code_length = len(spreading_code)
    decoded_bits = []
    
    for i in range(0, len(received_signal), code_length):
        chip_segment = received_signal[i:i + code_length]
        # Correlate with spreading code
        correlation = sum(chip * code for chip, code in zip(chip_segment, spreading_code))
        # Decision: positive = 1, negative = 0
        bit = 1 if correlation > 0 else 0
        decoded_bits.append(bit)
    
    return decoded_bits

# Example
spreading_code = [1, -1, 1, -1]  # 4-chip spreading code
data = [1, 0, 1, 1]

# Encode
encoded = cdma_encode(data, spreading_code)
print(f"Original data: {data}")
print(f"Spreading code: {spreading_code}")
print(f"Encoded signal: {encoded}")

# Decode
decoded = cdma_decode(encoded, spreading_code)
print(f"Decoded data: {decoded}")

# Simulate interference (add noise from another station)
other_code = [1, 1, -1, -1]
other_data = [1, 0, 0, 1]
other_signal = cdma_encode(other_data, other_code)

# Add signals (simulating simultaneous transmission)
combined = [s1 + s2 for s1, s2 in zip(encoded, other_signal)]
decoded_with_interference = cdma_decode(combined, spreading_code)
print(f"\nWith interference from another station:")
print(f"Combined signal: {combined}")
print(f"Decoded (with interference): {decoded_with_interference}")
```

**Used in:** 3G mobile networks (WCDMA), GPS, IS-95 (cdmaOne)

---

## 7. Ethernet (IEEE 802.3)

Ethernet is the most widely used LAN technology, based on CSMA/CD.

### 7.1 Ethernet Frame Structure

```
┌──────────┬────────┬────────────┬─────────────┬──────────┬─────────┐
│ Preamble │  SFD   │ Dest Addr  │ Source Addr │  Length  │  Data   │
│ (7 bytes)│ (1 B)  │  (6 bytes) │  (6 bytes)  │ (2 bytes)│(46-1500)│
├──────────┼────────┼────────────┼─────────────┼──────────┼─────────┤
│          │        │            │             │          │         │
└──────────┴────────┴────────────┴─────────────┴──────────┴─────────┘
                                          │         │
                                    ┌─────┴────┐   │
                                    │  FCS     │   │
                                    │ (4 bytes)│   │
                                    └──────────┘   │
                                              Frame check sequence
```

- **Preamble**: 7 bytes of alternating 1s and 0s for synchronization
- **SFD (Start Frame Delimiter)**: 10101011 - marks frame start
- **Destination/Source Address**: 6-byte MAC addresses
- **Length/Type**: Length of data or protocol type
- **Data**: 46 to 1500 bytes
- **FCS**: 4-byte CRC checksum

### 7.2 Ethernet MAC Address

- 48-bit unique address assigned to each network interface
- Format: XX:XX:XX:XX:XX:XX (hexadecimal)
- First 24 bits: OUI (Organizationally Unique Identifier)
- Last 24 bits: Device identifier

### 7.3 Ethernet Evolution

| Standard    | Speed    | Medium                   | Max Distance |
|-------------|----------|--------------------------|--------------|
| 10BASE5     | 10 Mbps  | Thick coaxial cable     | 500m         |
| 10BASE2     | 10 Mbps  | Thin coaxial cable      | 185m         |
| 10BASE-T    | 10 Mbps  | Twisted pair            | 100m         |
| 100BASE-TX  | 100 Mbps | Twisted pair (Cat 5)   | 100m         |
| 1000BASE-T  | 1 Gbps   | Twisted pair (Cat 6)    | 100m         |
| 10GBASE-T   | 10 Gbps  | Twisted pair (Cat 6a)   | 100m         |

---

## 8. MACA (Medium Access Control for Wireless)

MACA is a wireless MAC protocol designed to avoid collisions in wireless networks.

### 8.1 Problems in Wireless Networks

- **Hidden Terminal Problem**: Station A and C cannot sense each other but both communicate with B
- **Exposed Terminal Problem**: Station B transmits to A, but C cannot transmit to D (thinking it would interfere)

### 8.2 MACA Protocol

MACA uses control frames (RTS/CTS) to reserve the channel:

1. **RTS (Request to Send)**: Sender sends a short control frame to receiver
2. **CTS (Clear to Send)**: Receiver responds with a CTS frame
3. **Data Transmission**: Sender transmits data
4. **ACK**: Receiver sends acknowledgment

### 8.3 MACA Flow

```
Station A                    Station B                   Station C
    |                            |                           |
    |------- RTS (A→B) --------->|                           |
    |                            |------- CTS (B→A) -------->|
    |<------ CTS (B→A) ---------|                           |
    |                            |                           |
    |======= DATA (A→B) ========>|                           |
    |                            |                           |
    |<------- ACK (B→A) --------|                           |
    |                            |                           |
    |                            |<------ Could send ------->|
    |                            |     (doesn't interfere)  |
```

**Advantages:**
- Solves hidden terminal problem
- CTS frames inform nearby stations to wait

**Used in:** IEEE 802.11 (Wi-Fi) as the basis for its MAC protocol

---

## 9. Key Differences Summary

| Protocol     | Access Method | Collision | Efficiency | Use Case           |
|--------------|---------------|-----------|------------|--------------------|
| Pure ALOHA   | Random        | Yes       | 18%        | Rarely used        |
| Slotted      | Random        | Yes       | 37%        | Rarely used        |
| CSMA         | Random        | Yes       | Variable   | Early networks     |
| CSMA/CD      | Random        | Detected  | High       | Ethernet           |
| Token Ring   | Controlled    | No        | Moderate   | Legacy LANs        |
| TDMA         | Controlled    | No        | High       | Cellular, satellite|
| FDMA         | Controlled    | No        | Moderate   | Analog cellular    |
| CDMA         | Controlled    | No        | High       | 3G mobile networks |

---

## 10. Key Takeaways

1. **Multiple Access Protocols** are essential for managing shared communication channels in computer networks.

2. **Random Access Protocols** (ALOHA, CSMA) allow contention but may experience collisions:
   - Pure ALOHA: Simple but inefficient (18% max)
   - Slotted ALOHA: Better efficiency (37% max)
   - CSMA: Carrier sensing reduces collisions
   - CSMA/CD: Adds collision detection (Ethernet)

3. **Binary Exponential Backoff** is crucial for handling repeated collisions in Ethernet networks.

4. **Controlled Access Protocols** (Token Ring, Token Bus) prevent collisions but require token management.

5. **Channelization** (TDMA, FDMA, CDMA) divides the channel among users without collision.

6. **Ethernet** (IEEE 802.3) uses CSMA/CD and is the dominant LAN technology with speeds from 10 Mbps to 100 Gbps.

7. **MACA** addresses wireless-specific problems using RTS/CTS exchange.

---

## 11. Multiple Choice Questions

### Level 1: Basic

1. **What is the maximum efficiency of Slotted ALOHA?**
   - a) 18%
   - b) 37%
   - c) 50%
   - d) 100%
   
   **Answer: b) 37%**

2. **Which protocol uses a token for channel access?**
   - a) CSMA/CD
   - b) ALOHA
   - c) Token Ring
   - d) FDMA
   
   **Answer: c) Token Ring**

3. **In CSMA, what does "carrier sensing" mean?**
   - a) Listening for collisions
   - b) Checking if the channel is idle before transmitting
   - c) Waiting for a random time
   - d) Detecting the token
   
   **Answer: b) Checking if the channel is idle before transmitting**

### Level 2: Intermediate

4. **What is the vulnerable period in Pure ALOHA?**
   - a) T
   - b) 2T
   - c) T/2
   - d) Infinite
   
   **Answer: b) 2T**

5. **Which IEEE standard defines Ethernet?**
   - a) 802.3
   - b) 802.5
   - c) 802.11
   - d) 802.15
   
   **Answer: a) 802.3**

6. **In Binary Exponential Backoff, after 4 collisions, the range of random numbers is:**
   - a) 0-7
   - b) 0-15
   - c) 0-3
   - d) 0-1
   
   **Answer: b) 0-15**

7. **What does RTS stand for in MACA protocol?**
   - a) Ready to Send
   - b) Request to Send
   - c) Receive to Send
   - d) Response to Send
   
   **Answer: b) Request to Send**

### Level 3: Advanced

8. **Which problem is solved by MACA's RTS/CTS mechanism?**
   - a) Bandwidth limitation
   - b) Hidden terminal problem
   - c) Token loss
   - d) Encryption
   
   **Answer: b) Hidden terminal problem**

9. **In CDMA, what ensures that signals from different users don't interfere?**
   - a) Different frequencies
   - b) Different time slots
   - c) Orthogonal spreading codes
   - d) Token passing
   
   **Answer: c) Orthogonal spreading codes**

10. **What is the minimum frame size in classic Ethernet to ensure collision detection?**
    - a) 64 bytes
    - b) 128 bytes
    - c) 256 bytes
    - d) 512 bytes
    
    **Answer: a) 64 bytes (512 bits)**

---

## 12. Flashcards

### Flashcard 1
**Q: What is the main disadvantage of Pure ALOHA?**

**A:** Pure ALOHA has a very low maximum efficiency of only 18.4% because the vulnerable period is 2T (double the frame transmission time), making it susceptible to a high number of collisions.

---

### Flashcard 2
**Q: Why is CSMA better than ALOHA?**

**A:** CSMA uses carrier sensing - stations listen to the channel before transmitting. This reduces the chance of collision compared to ALOHA where stations transmit without checking if the channel is busy.

---

### Flashcard 3
**Q: What is the purpose of the jamming signal in Ethernet?**

**A:** The jamming signal is transmitted when a collision is detected. It ensures that all stations are aware that a collision has occurred, so they don't continue transmitting and corrupt the data further.

---

### Flashcard 4
**Q: What is the difference between TDMA and FDMA?**

**A:** TDMA divides the channel into different TIME slots for different users, while FDMA divides the channel into different FREQUENCY bands. TDMA is used in digital systems, FDMA in analog systems.

---

### Flashcard 5
**Q: What is a MAC address?**

**A:** A Media Access Control (MAC) address is a unique 48-bit hardware address assigned to a network interface card (NIC). It is represented as six pairs of hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E).

---

### Flashcard 6
**Q: What problem does the Binary Exponential Backoff algorithm solve?**

**A:** After a collision, multiple stations may try to retransmit at the same time, causing another collision. Binary Exponential Backoff solves this by having each station wait a random amount of time before retrying, with the range of possible wait times doubling after each collision.

---

### Flashcard 7
**Q: Why is CSMA/CA used in wireless networks instead of CSMA/CD?**

**A:** In wireless networks, it's difficult to detect collisions while transmitting (due to the hidden terminal problem and signal strength issues). CSMA/CA (Collision Avoidance) tries to prevent collisions by using RTS/CTS exchange and random backoff rather than detecting them after they occur.

---

### Flashcard 8
**Q: What is the maximum number of transmission attempts in Ethernet before discarding a frame?**

**A:** In Ethernet, after 16 attempts (including the original transmission attempt), the frame is discarded. The Binary Exponential Backoff algorithm is used for up to 10 attempts (after which it continues trying with maximum range).

---

*End of Study Material*

---

**References:**
- Data Communications and Networking, Behrouz A. Forouzan
- Computer Networks, Andrew S. Tanenbaum
- Delhi University BSc (Hons) Computer Science Syllabus (NEP 2024 UGCF)
- IEEE 802 Standards (802.3, 802.5, 802.11)