# Virtual Circuits and Datagrams: Addressing - Summary

## Key Definitions and Concepts

- **Virtual Circuit Switching**: A connection-oriented switching technique that establishes a dedicated logical path before data transfer, using Virtual Circuit Identifiers (VCIs) for forwarding. Examples: ATM, Frame Relay.

- **Datagram Switching**: A connectionless switching technique where each packet is routed independently with full destination addressing. Examples: IP, UDP.

- **MAC Address**: 48-bit hardware address used for local network communication (Layer 2), burned into network interface cards.

- **IP Address**: 32-bit (IPv4) or 128-bit (IPv6) logical address used for global network communication and routing.

- **VCI (Virtual Circuit Identifier)**: Short identifier used in virtual circuit networks to efficiently forward packets along established paths.

- **CIDR (Classless Inter-Domain Routing)**: Address allocation scheme that allows variable-length subnet masks (VLSM) for efficient IP address utilization.

## Important Formulas and Theorems

- **Usable Hosts Formula**: For a /n prefix, usable hosts = 2^(32-n) - 2 (subtract network and broadcast addresses)

- **Subnet Mask Calculation**: Default classes - Class A: /8 (255.0.0.0), Class B: /16 (255.255.0.0), Class C: /24 (255.255.255.0)

- **Binary Conversion**: IP addresses convert from dotted decimal to 32-bit binary for network/host boundary calculations

## Key Points

- Virtual circuits require connection setup and maintain per-connection state at routers; datagrams are stateless.

- In virtual circuits, packets use short VCIs rather than full destination addresses, enabling faster forwarding.

- Datagram networks are more resilient to failures since packets can take alternate paths.

- IP addresses are hierarchical (network + host portions), enabling scalable routing through route aggregation.

- MAC addresses are flat (no hierarchy) and function only within local broadcast domains.

- CIDR notation (e.g., /24) specifies the network prefix length and replaces classful addressing.

- IPv4 uses 32-bit addresses (approximately 4.3 billion addresses); IPv6 uses 128-bit addresses.

## Common Mistakes to Avoid

- Confusing MAC addresses (Layer 2, hardware) with IP addresses (Layer 3, logical)

- Forgetting to subtract 2 from host calculations (network and broadcast addresses are unusable)

- Thinking virtual circuits provide guaranteed delivery—they only guarantee path consistency

- Assuming all packets in a datagram flow take the same path (they may be routed independently)

- Confusing subnet mask with wildcard mask—they serve different purposes

## Revision Tips

1. Practice subnetting problems daily—speed and accuracy are essential for exams.

2. Create comparison tables between virtual circuits and datagrams to memorize key differences.

3. Draw the packet format differences: VC-based packets carry short identifiers, datagrams carry full addresses.

4. Remember real-world examples: ATM/Frame Relay (virtual circuits) vs. IP/Internet (datagrams).

5. Review previous year question papers to understand the exam pattern and important topics.