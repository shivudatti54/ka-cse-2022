# Ethernet - Summary

## Key Definitions and Concepts

- **Ethernet:** A widely-used LAN technology standardized as IEEE 802.3, operating at the Physical and Data Link layers of the OSI model.

- **CSMA/CD:** Carrier Sense Multiple Access with Collision Detection—the media access protocol used in traditional half-duplex Ethernet to manage shared medium access.

- **MAC Address:** A unique 48-bit hardware address assigned to network interfaces, expressed as 12 hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E).

- **Collision Domain:** A network segment where concurrent transmissions cause collisions. Hubs create single collision domains; switches create separate domains per port.

- **Broadcast Domain:** The network area where broadcast frames reach all devices. Routers separate broadcast domains.

- **MAC Address Table:** A switch's internal database mapping MAC addresses to specific port numbers for frame forwarding.

## Important Formulas and Theorems

- **Minimum Ethernet Frame:** 64 bytes (512 bits), excluding preamble and SFD
- **Maximum Ethernet Frame:** 1518 bytes (including FCS)
- **Data Payload Range:** 46-1500 bytes
- **Frame Transmission Time:** Frame size (bits) ÷ Bandwidth (bps)
- **Round-trip Propagation Time:** 2 × (Distance ÷ Propagation Speed)
- **Minimum Frame Size Requirement:** Transmission time > Round-trip propagation time

## Key Points

1. Ethernet frame contains six main fields: Destination MAC, Source MAC, Type/Length, Data, and FCS (with Preamble/SFD).

2. The FCS field uses CRC-32 for error detection and can detect all burst errors of 32 bits or fewer.

3. CSMA/CD uses binary exponential backoff—waiting time doubles after each collision, up to 10 attempts.

4. Switches operate at Layer 2, learning MAC addresses dynamically and creating dedicated communication paths.

5. Full-duplex Ethernet eliminates collisions and does not require CSMA/CD.

6. Ethernet standards follow the format: Speed (Mbps)-BASE/broadband-Medium type (T=twisted pair, F=fiber).

7. Broadcast MAC address (FF:FF:FF:FF:FF:FF) reaches all devices in the same broadcast domain.

8. Minimum frame size of 64 bytes ensures collision detection works across maximum network diameter.

## Common Mistakes to Avoid

1. Confusing collision domains with broadcast domains—switches break collision domains but not broadcast domains.

2. Forgetting that MAC addresses are 48 bits (6 bytes), not 32 bits.

3. Assuming CSMA/CD is always used—modern full-duplex switched Ethernet doesn't require it.

4. Confusing the Type field (for protocol identification, >1500) with Length field (data length, ≤1500).

5. Ignoring the minimum frame size requirement—frames smaller than 64 bytes are considered "runts" and are discarded.

## Revision Tips

1. Draw the complete Ethernet frame structure from memory and label all fields with their byte sizes.

2. Practice explaining CSMA/CD in simple language—know the four steps: sense, transmit, detect, backoff.

3. Memorize the Ethernet standards naming convention: Speed-BASE-Medium.

4. Review previous years' DU question papers to understand the exam pattern and frequently asked topics.

5. Use packet capture tools like Wireshark to observe real Ethernet frames and reinforce theoretical knowledge.