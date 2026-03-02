# Transmission Modes and Devices in Computer Networks - Summary

## Key Definitions and Concepts

- **Transmission Mode**: The direction of data flow between communicating devices over a network connection—can be simplex (one-way), half-duplex (two-way but not simultaneous), or full-duplex (simultaneous two-way).

- **Network Device**: Hardware components that enable communication between computers and other devices on a network, each operating at specific OSI model layers.

- **Collision Domain**: A network segment where data packets can collide when transmitted simultaneously—larger collision domains reduce network efficiency.

- **Broadcast Domain**: The network area within which a broadcast packet reaches all nodes—routers segment broadcast domains while hubs and switches do not.

- **MAC Address**: A unique 48-bit hardware address assigned to network interface cards, used for frame forwarding at Layer 2.

## Important Formulas and Theorems

- **Bandwidth in Full-Duplex**: Total bandwidth = Number of ports × Port bandwidth (e.g., 8-port 10 Mbps switch = 80 Mbps total throughput vs. 10 Mbps shared in hub)

- **Maximum Cable Length with Repeaters**: Each repeater extends cable length by the maximum segment length (e.g., 100BASE-TX = 100 meters per segment)

## Key Points

- Hubs and repeaters operate at Layer 1 (Physical Layer), switches and bridges at Layer 2 (Data Link Layer), and routers at Layer 3 (Network Layer).

- Switches provide dedicated bandwidth to each port and support full-duplex communication, eliminating collisions entirely.

- Full-duplex mode doubles effective bandwidth compared to half-duplex as data flows simultaneously in both directions.

- Routers connect different networks and use IP addresses for routing decisions, while switches connect devices within the same network using MAC addresses.

- Gateways connect dissimilar networks with different protocols, while routers connect networks using the same protocols.

- Each port on a switch creates a separate collision domain; each interface on a router creates a separate broadcast domain.

- Access Points bridge wireless stations to wired Ethernet networks, enabling Wi-Fi connectivity.

## Common Mistakes to Avoid

- Confusing hubs with switches—hubs broadcast to all ports while switches use MAC address tables to forward selectively.

- Incorrectly associating OSI layers with devices—remember that bridges and switches are Layer 2, not Layer 1 devices.

- Assuming all network devices segment broadcast domains—only routers (and Layer 3 devices) do this.

- Confusing routers with gateways—routers connect similar networks; gateways connect dissimilar networks with protocol translation.

## Revision Tips

1. Create a comparison table of all network devices listing their OSI layer, function, and effect on collision/broadcast domains.

2. Practice drawing network diagrams with different device combinations and explaining data flow through each device type.

3. Memorize real-world examples: walkie-talkies (half-duplex), telephone (full-duplex), TV broadcast (simplex).

4. Solve previous year DU question papers to understand the exam pattern and frequently tested concepts.