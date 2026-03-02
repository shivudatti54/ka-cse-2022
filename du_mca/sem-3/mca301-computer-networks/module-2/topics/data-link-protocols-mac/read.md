# Data Link Protocols - MAC Layer

## Introduction
The Medium Access Control (MAC) sublayer is a critical component of the data link layer (Layer 2) in computer networks. It governs how network devices access and share a common transmission medium, preventing data collisions while ensuring fair resource allocation. In modern networks where multiple devices compete for bandwidth - from Ethernet LANs to WiFi networks and cellular systems - MAC protocols directly impact network efficiency, throughput, and scalability.

MAC protocols become particularly crucial in shared medium environments like:
- Wireless networks (802.11 WiFi)
- Ethernet LANs (CSMA/CD)
- Satellite communications
- IoT sensor networks

The choice of MAC protocol affects key performance metrics including latency (5G targets <1ms), channel utilization (Ethernet achieves ~90%), and energy efficiency (critical for IoT devices). With emerging technologies like 5G NR and Wi-Fi 6 implementing advanced MAC schemes like OFDMA, understanding these protocols is essential for network architects and protocol developers.

## Key Concepts

1. **Channel Partitioning Protocols**
   - **TDMA (Time Division Multiple Access)**: Divides channel into time slots (used in GSM)
   - **FDMA (Frequency Division Multiple Access)**: Allocates frequency bands (traditional cable TV)
   - **CDMA (Code Division Multiple Access)**: Uses orthogonal codes (3G cellular)

2. **Random Access Protocols**
   - **ALOHA**: Pure & Slotted variants
     - Pure ALOHA: S = G × e^(-2G) (Max throughput 18.4%)
     - Slotted ALOHA: S = G × e^(-G) (Max 36.8%)
   - **CSMA Protocols**:
     - CSMA/CD (Collision Detection): Ethernet's backbone
     - CSMA/CA (Collision Avoidance): 802.11's four-way handshake

3. **Controlled Access Protocols**
   - **Token Passing**: IEEE 802.5 Token Ring
   - **Polling**: Master-slave configuration in Bluetooth

4. **Modern Hybrid Protocols**
   - OFDMA (Orthogonal Frequency Division Multiple Access): Wi-Fi 6/802.11ax
   - NOMA (Non-Orthogonal Multiple Access): 5G mMTC

## Examples

**Example 1: ALOHA Throughput Calculation**
Problem: Calculate max throughput for Pure vs Slotted ALOHA
Solution:
- Pure: Max at G=0.5 → S=0.5×e^(-1) ≈ 0.184 (18.4%)
- Slotted: Max at G=1 → S=1×e^(-1) ≈ 0.368 (36.8%)

**Example 2: CSMA/CD Backoff Algorithm**
Scenario: 3 collisions occurred in Ethernet
Calculate backoff time:
- k = min(10, 3) → 3
- R = rand(0, 2³-1) = rand(0,7)
- Backoff = R × 512 bit times
If R=5 → 5×51.2μs = 256μs (for 10Mbps Ethernet)

**Example 3: CSMA/CA in WiFi**
Step-by-step:
1. Station senses channel (DIFS = 50μs)
2. Random backoff (Contention Window: 15-1023 slots)
3. RTS-CTS exchange (optional)
4. Data transmission
5. ACK reception (SIFS = 10μs)

## Exam Tips
1. Always mention whether network is wired/wireless when discussing MAC protocols
2. For throughput questions, remember ALOHA maxima (18.4%/36.8%)
3. CSMA/CD vs CSMA/CA: Detection vs Avoidance + wired vs wireless
4. Token Ring efficiency formula: τ = T/(T + τ_ring)
5. In numericals, convert units carefully (bps, μs, meters for propagation delay)
6. Modern protocols: Mention 802.11ax (OFDMA) and 5G relevance
7. For essays, compare MAC approaches using metrics: delay, fairness, scalability