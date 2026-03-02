# Network Models: OSI and TCP/IP - Summary

## Key Definitions and Concepts

- **OSI Model:** A seven-layer conceptual framework developed by ISO (1984) for standardizing network communication functions. Layers: Physical, Data Link, Network, Transport, Session, Presentation, Application.

- **TCP/IP Model:** A four-layer practical implementation model (Network Access, Internet, Transport, Application) that forms the basis of the modern Internet.

- **Encapsulation:** The process of adding layer-specific headers to data as it passes down the OSI model, creating PDUs (Protocol Data Units): Data → Segment → Packet → Frame → Bits.

- **De-encapsulation:** The reverse process where each layer strips its header and passes data upward to the next layer.

- **MAC Address:** A 48-bit physical address assigned to network interface cards (NICs), operating at the Data Link Layer.

- **IP Address:** A logical network address (IPv4: 32-bit, IPv6: 128-bit) for identifying devices at the Network Layer.

- **Port Number:** A 16-bit identifier at the Transport Layer for distinguishing specific applications and services.

## Important Formulas and Relationships

- **Socket = IP Address + Port Number** — uniquely identifies a specific process on a specific machine
- **PDU Mapping:** Application→Data, Transport→Segment/Datagram, Network→Packet, Data Link→Frame, Physical→Bits
- **Layer-Device Mapping:** Physical→Repeater/Hub, Data Link→Switch, Network→Router, All Layers→Gateway

## Key Points

1. The OSI model is a reference model (theoretical), while TCP/IP is the implementation model (practical)

2. Each OSI layer provides services to the layer above it and uses services from the layer below it

3. TCP provides reliable, connection-oriented communication with flow control and error recovery; UDP provides fast, connectionless communication without guarantees

4. Well-known ports: HTTP(80), HTTPS(443), FTP(21), SSH(22), SMTP(25), DNS(53), DHCP(67/68)

5. Switches operate at Layer 2 using MAC addresses; Routers operate at Layer 3 using IP addresses

6. The three-way handshake (SYN, SYN-ACK, ACK) establishes TCP connections

7. Physical addresses (MAC) are flat and location-dependent; Logical addresses (IP) are hierarchical and configurable

8. The Application Layer in TCP/IP combines OSI's Session, Presentation, and Application layers

## Common Mistakes to Avoid

1. Confusing PDU names — remember segment (TCP), datagram (UDP), packet (IP), frame (Data Link)

2. Believing OSI was implemented — TCP/IP came first in practice; OSI is just a reference model

3. Mixing up port numbers — HTTP is 80, HTTPS is 443, don't confuse them in exam answers

4. Forgetting that switches use MAC addresses (Layer 2) while routers use IP addresses (Layer 3)

5. Assuming all protocols at a layer work the same — TCP and UDP at Transport Layer have fundamentally different characteristics

## Revision Tips

1. Use mnemonics: "All People Seem To Need Data Processing" for OSI layers (bottom to top or top to bottom depending on preference)

2. Practice drawing and labeling the OSI/TCP/IP layer diagrams repeatedly until automatic

3. For each layer, remember: (a) PDU name, (b) Key protocol, (c) Addressing used, (d) Typical device

4. Solve past DU exam questions on this topic to understand the question patterns and marking schemes

5. Trace complete communication scenarios (web browsing, email) through all seven layers to reinforce understanding