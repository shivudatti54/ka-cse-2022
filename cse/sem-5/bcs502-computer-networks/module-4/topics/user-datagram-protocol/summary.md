# User Datagram Protocol (UDP) - Summary

## Key Definitions and Concepts

- **User Datagram Protocol (UDP)**: A connectionless, unreliable transport layer protocol that provides minimal overhead communication without guaranteed delivery, ordering, or error recovery.

- **Connectionless Protocol**: UDP does not establish a connection before sending data; datagrams can be sent immediately without handshake procedures.

- **Best-Effort Delivery**: UDP makes no guarantees about packet delivery, allowing packets to be lost, duplicated, or received out of order.

- **Port Numbers**: 16-bit identifiers (0-65,535) used to multiplex data to specific application processes on a host.

## Important Formulas and Theorems

- **UDP Header Size**: Always 8 bytes (fixed)
- **Maximum UDP Datagram Size**: 65,535 bytes (2¹⁶ - 1)
- **UDP Payload Calculation**: MTU - IP Header (20 bytes) - UDP Header (8 bytes) = Available payload
- **UDP Efficiency**: (Data Payload / Total Datagram Size) × 100%

## Key Points

- UDP provides a simple datagram delivery service with minimal protocol overhead
- The four-field UDP header contains: Source Port, Destination Port, Length, and Checksum
- UDP is preferred for real-time applications where speed matters more than reliability
- Common UDP applications include DNS, DHCP, VoIP, video streaming, and online gaming
- UDP checksum is optional in IPv4 but mandatory in IPv6
- Unlike TCP, UDP has no flow control, congestion control, or sequencing mechanisms
- Applications requiring reliability must implement their own error recovery on top of UDP

## Common Mistakes to Avoid

- Assuming UDP provides guaranteed delivery—it explicitly does not
- Confusing UDP's connectionless nature with having no addressing; ports provide the necessary multiplexing
- Forgetting that UDP checksum covers both header and data, not just the data
- Underestimating the need for application-layer reliability mechanisms when using UDP

## Revision Tips

- Memorize the 8-byte fixed UDP header structure with all four fields
- Practice comparing UDP and TCP characteristics as this appears frequently in exams
- Remember key port numbers: 53 (DNS), 67/68 (DHCP), 123 (NTP)
- Understand why certain applications choose UDP over TCP based on their requirements
- Review sample calculations for UDP efficiency and datagram length fields
