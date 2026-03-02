# MAC Protocols and Ethernet - Summary

## Key Definitions and Concepts

- **MAC (Media Access Control)**: Sublayer of Data Link Layer that controls how devices gain access to the shared transmission medium
- **Multiple Access Protocol**: Rules governing how multiple devices share a common communication channel
- **Collision**: When two or more transmissions overlap in time, corrupting data
- **CSMA/CD**: Carrier Sense Multiple Access with Collision Detection—Ethernet's access protocol
- **Binary Exponential Backoff**: Algorithm where waiting time doubles after each collision (k × 512 bit times, where k ∈ [0, 2^n-1])
- **MAC Address**: 48-bit unique physical address assigned to network interface (e.g., 00:1A:2B:3C:4D:5E)
- **Ethernet Frame**: Data unit at Data Link Layer with destination MAC, source MAC, type, data, and FCS fields
- **Hub**: Layer 1 device that broadcasts signals to all ports, creating single collision domain
- **Switch**: Layer 2 device that learns MAC addresses and forwards frames to specific ports

## Important Formulas and Theorems

- **Pure ALOHA Throughput**: S = G × e^(-2G), max = 18.4% at G = 0.5
- **Slotted ALOHA Throughput**: S = G × e^(-G), max = 36.8% at G = 1
- **CSMA/CD Minimum Frame Size**: Frame ≥ 2 × Propagation Delay × Bandwidth
- **Ethernet Frame Size**: 64 bytes minimum, 1518 bytes maximum (excluding preamble/SFD)
- **Backoff Calculation**: After n collisions, wait k × 512 bit times where k ∈ [0, 2^n - 1]

## Key Points

- Multiple access protocols solve the problem of coordinating shared medium usage among multiple transmitters
- ALOHA is simplest but inefficient (18.4% max); Slotted ALOHA doubles efficiency to 36.8%
- CSMA improves on ALOHA by sensing carrier before transmitting—reduces but doesn't eliminate collisions
- Ethernet uses CSMA/CD: listen before talk, detect collisions, jam signal, then backoff and retry
- MAC addresses are 48-bit identifiers: first 24 bits = manufacturer (OUI), last 24 bits = device
- Ethernet frame contains: Preamble (7B) + SFD (1B) + Dest MAC (6B) + Src MAC (6B) + Type/Length (2B) + Data (46-1500B) + FCS (4B)
- Ethernet standards follow naming: `<speed>BASE-<medium><pairs>`, e.g., 100BASE-TX = 100 Mbps, Baseband, Twisted Pair
- Switches operate at Layer 2, enable full-duplex communication, and eliminate need for CSMA/CD in modern networks

## Common Mistakes to Avoid

1. Confusing Pure ALOHA (18.4%) and Slotted ALOHA (36.8%) efficiency values—exams frequently test this distinction
2. Forgetting that CSMA/CD minimum frame size requirement exists due to collision detection timing constraints
3. Using "switch" and "hub" interchangeably—they operate at different layers with different collision behaviors
4. Not understanding that Ethernet Type field (0x0800 = IPv4) distinguishes from 802.3 Length field usage
5. Believing switches eliminate all network problems—they don't filter broadcast frames, which can cause broadcast storms

## Revision Tips

1. Draw the Ethernet frame structure from memory and label all fields with sizes—this frequently appears in exams
2. Practice calculating ALOHA efficiency using the formulas with different G values
3. Memorize the Binary Exponential Backoff process: after n collisions, choose k from {0 to 2^n-1}, wait k × 512 bit times
4. Know the common Ethernet Type values: 0x0800 (IPv4), 0x0806 (ARP), 0x86DD (IPv6)
5. Review difference between broadcast (FF:FF:FF:FF:FF:FF), multicast (LSB of first octet = 1), and unicast MAC addresses