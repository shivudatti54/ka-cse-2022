# Transmission Modes and Network Devices
**Computer Networks - Delhi University (NEP 2024 UGCF)**

---

## Introduction
Transmission modes and network devices form the foundational concepts in computer networking, defining how data is transferred between devices and how networks are interconnected. These topics are essential for understanding network architecture and communication protocols.

---

## Transmission Modes

Transmission modes define the direction of data flow between communicating devices.

### Types of Transmission Modes:

- **Simplex**
  - Data flows in one direction only
  - Example: Keyboard to computer, TV broadcasting

- **Half-Duplex**
  - Data flows in both directions but not simultaneously
  - Example: Walkie-talkie, Ethernet hubs

- **Full-Duplex (Duplex)**
  - Data flows simultaneously in both directions
  - Example: Telephone conversation, Ethernet switches

### Key Factors Affecting Transmission:
- Bandwidth
- Transmission medium
- Distance
- Signal quality

---

## Network Devices

### 1. Repeater
- Amplifies and regenerates weak signals
- Operates at Physical Layer (Layer 1)
- Extends network distance
- Does not filter traffic

### 2. Hub
- Multiport repeater
- Operates at Physical Layer (Layer 1)
- Broadcasts data to all ports
- Creates collision domains
- **Type:** Active, Passive, Intelligent

### 3. Bridge
- Connects two network segments
- Operates at Data Link Layer (Layer 2)
- Filters traffic using MAC addresses
- Reduces collision domains

### 4. Switch
- Multiport bridge
- Operates at Data Link Layer (Layer 2)
- Creates dedicated collision domains
- Learns MAC addresses (CAM table)
- **Types:** Unmanaged, Managed, Layer 3

### 5. Router
- Connects different networks
- Operates at Network Layer (Layer 3)
- Uses IP addresses for routing
- Creates broadcast domains
- Determines best path (routing protocols)

### 6. Gateway
- Connects dissimilar networks
- Operates at all layers (Application Layer)
- Translates between different protocols
- Example: Email gateway, Protocol converter

### 7. Other Devices
- **NIC (Network Interface Card):** Connects device to network
- **Access Point:** Enables wireless connectivity
- **Modem:** Converts digital to analog signals

---

## OSI Model Reference (Delhi University Syllabus)

| Device | OSI Layer |
|--------|-----------|
| Repeater, Hub | Layer 1 (Physical) |
| Bridge, Switch | Layer 2 (Data Link) |
| Router | Layer 3 (Network) |
| Gateway | Layer 4-7 (Transport to Application) |

---

## Conclusion
Understanding transmission modes (simplex, half-duplex, full-duplex) is crucial for designing efficient communication systems. Network devices from simple hubs to sophisticated routers form the backbone of modern networks, each serving specific functions at different OSI layers. Mastery of these concepts is essential for network design, troubleshooting, and optimization in real-world scenarios.