# Mobile IP Handoff - Summary

## Key Definitions and Concepts

- **Mobile Node (MN):** A device that changes network attachment points while maintaining its permanent IP address (home address) for session continuity.

- **Home Address:** The permanent IP address assigned to a mobile node, used in application communications regardless of the node's current location.

- **Care-of Address (CoA):** A temporary address representing the mobile node's current network location; packets are tunneled to this address.

- **Home Agent (HA):** Router on the mobile node's home network that intercepts packets and tunnels them to the mobile node's care-of address.

- **Foreign Agent (FA):** Router on a foreign network that assists mobile nodes with mobility management; largely replaced by co-located addressing in modern implementations.

- **Handoff:** The process of transitioning a mobile node's connectivity from one access point to another while maintaining network session.

## Important Formulas and Theorems

- **Total Handoff Latency = Detection Time + Channel Acquisition + Authentication + Registration Time**

- **Packet Loss during handoff ≈ Handoff Latency × Packet Arrival Rate**

- Mobility Binding: A table entry in the HA associating Home Address ↔ Care-of Address with lifetime

## Key Points

- Mobile IP enables mobility by decoupling a device's identifier (home address) from its location (care-of address).

- Registration with the Home Agent is required whenever the mobile node obtains a new care-of address; this creates a mobility binding.

- Horizontal handoffs occur between same network types; vertical handoffs occur between different network technologies.

- Hierarchical Mobile IP (HMIP) improves performance for micro-mobility by introducing regional agents that reduce HA registration frequency.

- Fast Handoff protocols establish tunnels between old and new access routers before the mobile node completes movement.

- Mobile IPv6 eliminates the Foreign Agent concept, uses co-located addressing, and provides native route optimization.

- Security in Mobile IP relies on pre-shared secrets or PKI for authentication, with identification fields preventing replay attacks.

## Common Mistakes to Avoid

- Confusing the home address with the care-of address; the home address remains constant while the care-of address changes with network location.

- Assuming Foreign Agents are required in modern Mobile IP; co-located addressing has become the standard approach.

- Believing Mobile IP provides security by default; explicit security associations and protocols like IPsec must be configured.

- Confusing handoff with roaming; handoff specifically refers to real-time transition during active communication, while roaming may include authentication without active sessions.

## Revision Tips

1. Draw the complete Mobile IP architecture showing MN, FA, HA, and Correspondent Node, with arrows indicating packet flow for both standard routing and tunneled delivery.

2. Practice writing out the registration request and reply message exchanges, including all key fields and their purposes.

3. Create a comparison table for horizontal vs. vertical handoff, HMIP vs. standard Mobile IP, and Mobile IPv4 vs. Mobile IPv6.

4. Memorize the handoff latency formula and understand how each component contributes to total delay.

5. Review recent research papers on Mobile IP optimizations to understand current trends in the field.