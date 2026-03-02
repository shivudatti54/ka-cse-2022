# TCP/IP Protocol Suite - Summary

## Key Definitions and Concepts

- **TCP/IP Protocol Suite**: A set of network protocols used for interconnecting network devices on the Internet, consisting of four layers: Network Access, Internet, Transport, and Application.

- **Encapsulation**: The process of adding headers to data as it passes through each layer of the TCP/IP model, from application to network interface.

- **IP Address**: A unique logical address assigned to each device on a network. IPv4 uses 32-bit addresses; IPv6 uses 128-bit addresses.

- **Port Number**: A 16-bit identifier (0-65535) that specifies a particular application or service on a host.

- **Subnetting**: The process of dividing a network into smaller subnetworks (subnets) for better management and security.

## Important Formulas and Theorems

- **Number of usable hosts in a subnet**: 2^(32-n) - 2, where n is the CIDR prefix length (subtract 2 for network and broadcast addresses)

- **Three-way handshake**: SYN → SYN-ACK → ACK (for TCP connection establishment)

- **Well-known ports**: HTTP(80), HTTPS(443), FTP(21), SSH(22), SMTP(25), DNS(53)

- **Private IP ranges**: 10.0.0.0-10.255.255.255, 172.16.0.0-172.31.255.255, 192.168.0.0-192.168.255.255

## Key Points

1. TCP/IP has 4 layers (Application, Transport, Internet, Network Access) compared to OSI's 7 layers.

2. IP operates at the Internet Layer and provides best-effort, unreliable delivery.

3. TCP provides reliable, connection-oriented service with error recovery and flow control.

4. UDP provides unreliable, connectionless service suitable for real-time applications.

5. IPv4 addresses are 32-bit (4 octets), while IPv6 addresses are 128-bit (8 groups of hex digits).

6. Class A networks support ~16 million hosts; Class B supports ~65,000; Class C supports 254 hosts.

7. Subnetting with CIDR notation (e.g., /24) provides more efficient IP address allocation.

8. Port numbers identify specific applications; well-known ports are 0-1023.

## Common Mistakes to Avoid

1. Confusing TCP/IP layers with OSI layers - remember TCP/IP has only 4 layers.

2. Forgetting that network and broadcast addresses cannot be assigned to hosts in any subnet.

3. Using public IP addresses for private networks, which causes routing issues.

4. Believing TCP guarantees delivery instantly - it ensures reliability but may cause delays due to retransmission.

5. Misunderstanding port numbers - they identify applications, not devices (which is what IP addresses do).

## Revision Tips

1. Draw the TCP/IP model diagram with protocols at each layer and revise it daily.

2. Practice solving subnetting problems - this is the most scoring question type in exams.

3. Memorize well-known port numbers as they frequently appear in questions.

4. Create a comparison table between TCP and UDP to understand their differences clearly.

5. Remember that ping uses ICMP (not TCP/UDP) and operates at the Internet Layer.
