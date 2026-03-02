# Multiple Access Protocols (MAC Layer)

## Introduction

The **Medium Access Control (MAC) sublayer** in the Data Link Layer manages how multiple devices share a common communication channel without interference. Since a network medium (like Ethernet cable or wireless spectrum) can only carry one signal at a time, MAC protocols determine **which device gets to transmit and when**. This is critical for efficient network performance and collision management.

---

## Types of Multiple Access Protocols

### 1. Random Access Protocols
Devices compete for channel access with no predetermined order. Collisions may occur and are handled through specific mechanisms.

- **ALOHA**: 
  - Pure ALOHA: Transmit whenever data is ready; collisions possible
  - Slotted ALOHA: Time divided into slots; transmission only at slot beginning (double efficiency of Pure ALOHA)
  - **Vulnerable period**: Time during which collision can occur

- **CSMA (Carrier Sense Multiple Access)**:
  - Listen to channel before transmitting
  - **1-persistent CSMA**: Transmit immediately if idle
  - **Non-persistent CSMA**: Wait random time if busy
  - **p-persistent CSMA**: For slotted channels

- **CSMA/CD (Collision Detection)**:
  - Used in **Ethernet (IEEE 802.3)**
  - Stations detect collisions, stop transmission, and retransmit after random backoff
  - **Minimum frame size** required for proper collision detection

- **CSMA/CA (Collision Avoidance)**:
  - Used in **Wireless LANs (IEEE 802.11)**
  - Uses RTS/CTS handshake and ACK frames to avoid collisions
  - Includes **NAV (Network Allocation Vector)** for channel reservation

### 2. Controlled Access Protocols
Access is granted in an orderly manner, preventing collisions entirely.

- **Reservation**: Time divided into reservation intervals; devices reserve slots before transmission
- **Polling**: Central controller (master) invites each node to transmit
- **Token Passing**: A special frame (token) circulates; only token holder can transmit (used in **Token Ring, IEEE 802.5**)

### 3. Channelization
The available bandwidth is divided among multiple users.

- **FDMA (Frequency Division)**: Each user gets a dedicated frequency band
- **TDMA (Time Division)**: Users share frequency but get dedicated time slots
- **CDMA (Code Division)**: All users transmit simultaneously using unique codes; orthogonal codes allow separation

---

## Key Concepts for Exam

- **Hidden Terminal Problem**: Two nodes can't sense each other but both transmit to a common receiver → collision at receiver
- **Exposed Terminal Problem**: Node refrains from transmitting even though it wouldn't cause interference
- **Backoff Algorithm**: Binary Exponential Backoff in Ethernet; doubling wait range after each collision
- **Throughput**: Slotted ALOHA (~37%), Pure ALOHA (~18%), CSMA (up to 90% under ideal conditions)
- **MACA Protocol**: Uses RTS/CTS to solve hidden terminal problem

---

## Conclusion

Multiple Access Protocols form the backbone of shared communication channels. From simple ALOHA to sophisticated CSMA/CD and token-passing mechanisms, each protocol balances **efficiency, fairness, and complexity**. Understanding these protocols is essential for designing and troubleshooting both wired (Ethernet) and wireless (Wi-Fi) networks, making this a fundamental topic in computer networking for exam success.

---

*Reference: Delhi University BSc (Hons) CS - NEP 2024 UGCF Syllabus, Unit: Data Link Layer & LAN Technologies*