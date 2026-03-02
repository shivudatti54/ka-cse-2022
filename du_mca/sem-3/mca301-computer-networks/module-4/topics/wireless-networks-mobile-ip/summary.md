# Wireless Networks and Mobile IP - Summary

## Key Definitions and Concepts

- **Wireless Networks:** Communication networks using radio waves for connectivity without physical cables, classified as WPAN (10m, Bluetooth), WLAN (100m, Wi-Fi), WMAN (city-wide, WiMAX), and WWAN (wide-area, cellular).

- **Mobile IP:** Network protocol enabling mobile devices to maintain connectivity while moving between networks by separating the home address from the current network location.

- **Care-of Address (CoA):** Temporary address assigned to a mobile node in a foreign network, used for packet tunneling.

- **Home Agent:** Router on the mobile node's home network that intercepts and tunnels packets destined for the mobile node when it is away.

- **Foreign Agent:** Router in a foreign network that assists the mobile node, providing a care-of address and facilitating tunneling (IPv4 only).

- **Mobility Binding:** Table entry at the home agent mapping the mobile node's home address to its current care-of address.

## Important Formulas and Theorems

- **Registration Lifetime:** Mobile IP registrations expire and require renewal (typical: 3600 seconds). The mobile node should re-register before expiration.

- **Tunneling Overhead:** Mobile IP encapsulation adds 20 bytes (IPv4) or 40 bytes (IPv6) to each packet header when tunneled through the home agent.

- **Wi-Fi Data Rates:** 802.11b (11 Mbps), 802.11g (54 Mbps), 802.11n (600 Mbps), 802.11ac (3.46 Gbps), 802.11ax (9.6 Gbps).

## Key Points

- Wireless networks operate in unlicensed spectrum (2.4 GHz, 5 GHz for Wi-Fi) requiring no licensing but experiencing interference.

- Mobile IP achieves transparency by allowing the mobile node to retain its permanent IP address regardless of attachment point.

- Three Mobile IP phases: Agent Discovery (detect network), Registration (inform home agent of location), Tunneling (forward packets to current location).

- Triangle routing problem: All traffic to mobile node must route through home agent, causing inefficiency.

- IPv6 Mobile IP includes built-in route optimization, eliminating triangular routing.

- CSMA/CA is used in Wi-Fi for medium access, unlike wired Ethernet's CSMA/CD.

- Wi-Fi security has evolved from WEP (broken) to WPA2 (AES encryption) to WPA3 (enhanced security).

## Common Mistakes to Avoid

- Confusing Care-of Address with Home Address—the CoA changes as the mobile node moves, while the Home Address remains constant.

- Forgetting that Mobile IP requires changes only to the mobile node and home agent; correspondent nodes operate normally.

- Assuming Foreign Agents are used in IPv6—they are not; IPv6 uses stateless autoconfiguration for CoA.

- Confusing the registration lifetime with session lifetime—registrations expire and require renewal.

## Revision Tips

1. Create a diagram showing the complete Mobile IP flow: Correspondent → Home Agent (tunnel) → Foreign Agent → Mobile Node.

2. Practice explaining Mobile IP operation in simple terms as if teaching a classmate.

3. Memorize the three Mobile IP phases and what happens in each.

4. Review the differences between IPv4 and IPv6 Mobile IP implementations.

5. Know the Wi-Fi standard evolution with their frequency bands and data rates.