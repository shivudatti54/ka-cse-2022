# DNS, DHCP, and BOOTP

## Introduction
Domain Name System (DNS), Dynamic Host Configuration Protocol (DHCP), and Bootstrap Protocol (BOOTP) form the backbone of modern network infrastructure. DNS acts as the internet's phonebook, translating human-readable domain names to machine-readable IP addresses. DHCP automates IP address allocation, while BOOTP enables diskless workstations to boot from the network. 

These protocols are critical for maintaining seamless internet operations. For DU students, understanding their hierarchical architectures and packet exchange processes is essential for network administration and cybersecurity roles. With the growing adoption of IPv6 and IoT devices, these protocols are evolving to meet modern scalability and security challenges.

## Key Concepts

**DNS Architecture**
- Hierarchical structure with root, TLD, and authoritative servers
- Resource Records: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail exchange), NS (name server)
- Query types: Recursive vs Iterative resolution
- DNSSEC for authentication and data integrity

**DHCP Operation**
- DORA process: Discover, Offer, Request, Acknowledgement
- Lease time management and address pools
- DHCP options (subnet mask, router, DNS server)
- DHCPv6 for IPv6 networks

**BOOTP Fundamentals**
- MAC address-based IP assignment
- Limited to static IP allocation
- TFTP for bootstrap image transfer
- BOOTP Relay Agents

**Protocol Comparison**
- BOOTP vs DHCP: Dynamic vs static allocation, lease management
- DNS vs DHCP: Name resolution vs address configuration

## Examples

**Example 1: DNS Resolution for www.du.ac.in**
1. Client queries local DNS resolver
2. Resolver contacts root server → .in TLD → .ac.in server → du.ac.in authoritative server
3. Authoritative server returns A record (103.25.195.50)
4. Resolver caches response for TTL duration

**Example 2: DHCP Lease Process**
1. Client broadcasts DHCPDISCOVER
2. Server responds with DHCPOFFER (IP: 192.168.1.100)
3. Client sends DHCPREQUEST to confirm
4. Server acknowledges with DHCPACK
5. Client configures IP and starts lease timer

**Example 3: BOOTP in Diskless Workstation**
1. Workstation broadcasts BOOTP request with MAC
2. BOOTP server responds with IP and boot file location
3. Workstation downloads OS image via TFTP
4. System boots from network image

## Exam Tips
1. Always mention RFC numbers: DNS (1034/1035), DHCP (2131), BOOTP (951)
2. For 6-mark questions, compare DHCPv4 vs DHCPv6 operations
3. Draw packet diagrams for DORA process in DHCP
4. Remember DNS uses both UDP (queries) and TCP (zone transfers)
5. BOOTP limitations: No dynamic allocation, manual IP-MAC binding
6. DNSSEC uses digital signatures (RRSIG records) for authentication
7. Practice Wireshark captures of DNS/DHCP packets

Length: 2200 words, BSc (Hons) level