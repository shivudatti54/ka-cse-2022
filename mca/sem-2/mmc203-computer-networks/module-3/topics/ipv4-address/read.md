# IPv4 Address


## Table of Contents

- [IPv4 Address](#ipv4-address)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Structure of IPv4 Address](#structure-of-ipv4-address)
  - [Classes of IPv4 Addresses](#classes-of-ipv4-addresses)
  - [Special IPv4 Addresses](#special-ipv4-addresses)
  - [Subnet Mask](#subnet-mask)
  - [CIDR (Classless Inter-Domain Routing) Notation](#cidr-classless-inter-domain-routing-notation)
- [Examples](#examples)
  - [Example 1: Determining Network and Broadcast Addresses](#example-1-determining-network-and-broadcast-addresses)
  - [Example 2: Calculating Number of Hosts in a Subnet](#example-2-calculating-number-of-hosts-in-a-subnet)
  - [Example 3: Subnetting a Class C Network](#example-3-subnetting-a-class-c-network)
- [Exam Tips](#exam-tips)

## Introduction

IPv4 (Internet Protocol version 4) is the foundational addressing scheme used to identify devices on a computer network. Developed in 1981, IPv4 remains the most widely used protocol for network communication despite the introduction of IPv6. Every device connected to the internet or a local network requires a unique IP address to facilitate communication. The IPv4 address serves as the logical identifier that enables data packets to be routed from source to destination across interconnected networks.

Understanding IPv4 addressing is critical for network administrators, system engineers, and computer science professionals. It forms the backbone of network configuration, subnetting, and routing decisions. In the curriculum, this topic carries significant weight as it establishes the foundation for understanding higher-level networking concepts like subnetting, CIDR, and network security. The ability to calculate network addresses, broadcast addresses, and valid host ranges is essential for practical network implementation and troubleshooting.

## Key Concepts

### Structure of IPv4 Address

An IPv4 address is a 32-bit logical address that uniquely identifies a device on a network. This 32-bit address is divided into two parts: the **Network ID** (also called Network Address) and the **Host ID** (also called Host Address). The Network ID identifies the specific network on which a device resides, while the Host ID identifies the particular device within that network.

To make IPv4 addresses human-readable, they are represented in **dotted decimal notation**. The 32-bit address is divided into four 8-bit octets (or bytes), and each octet is converted to a decimal number ranging from 0 to 255. The octets are separated by periods (dots). For example, the binary address 11000000.10101000.00000001.00000001 is written as 192.168.1.1.

### Classes of IPv4 Addresses

IPv4 addresses are categorized into five classes based on the leading bits and the range of the first octet:

**Class A:** Uses the first octet for network identification and the remaining three octets for host identification. The first bit is always 0, making the first octet range from 1 to 126. Class A supports approximately 16 million hosts per network, but only 126 networks are available. The default subnet mask is 255.0.0.0 (/8).

**Class B:** Uses the first two octets for network identification and the last two octets for host identification. The first two bits are 10, so the first octet ranges from 128 to 191. Class B supports approximately 65,534 hosts per network and about 16,384 networks. The default subnet mask is 255.255.0.0 (/16).

**Class C:** Uses the first three octets for network identification and the last octet for host identification. The first three bits are 110, so the first octet ranges from 192 to 223. Class C supports 254 hosts per network but offers approximately 2 million networks. The default subnet mask is 255.255.255.0 (/24).

**Class D:** Used for multicast groups. The first four bits are 1110, so the first octet ranges from 224 to 239. These addresses do not have network and host portions.

**Class E:** Reserved for experimental or future use. The first four bits are 1111, so the first octet ranges from 240 to 255.

### Special IPv4 Addresses

Certain IPv4 addresses serve special purposes and cannot be assigned to individual devices:

**Loopback Address:** The address 127.0.0.1 is reserved for loopback testing. Any address in the 127.x.x.x range points to the local machine, enabling software to test network communication without physical network interface usage.

**Private IP Addresses:** These addresses are used within private networks and are not routable on the internet:

- 10.0.0.0 to 10.255.255.255 (Class A private range)
- 172.16.0.0 to 172.31.255.255 (Class B private range)
- 192.168.0.0 to 192.168.255.255 (Class C private range)

**Broadcast Address:** The highest address in a network range serves as the broadcast address. All data sent to this address is received by all devices on the network. For example, in the network 192.168.1.0/24, the broadcast address is 192.168.1.255.

**Network Address:** The lowest address in a network range represents the network itself and cannot be assigned to hosts. For example, 192.168.1.0 is the network address for 192.168.1.0/24.

**Default Route:** 0.0.0.0 is used to represent the default route or unknown destination.

**Limited Broadcast:** 255.255.255.255 is used for broadcasting to all hosts on the local network.

### Subnet Mask

A subnet mask is a 32-bit number that divides an IP address into network and host portions. It uses consecutive 1s to represent the network portion and consecutive 0s to represent the host portion. The subnet mask is combined with an IP address using bitwise AND operation to determine the network address.

Common subnet masks include:

- 255.0.0.0 (/8) - Class A default
- 255.255.0.0 (/16) - Class B default
- 255.255.255.0 (/24) - Class C default
- 255.255.255.128 (/25) - Subnet with 126 hosts
- 255.255.255.192 (/26) - Subnet with 62 hosts
- 255.255.255.224 (/27) - Subnet with 30 hosts
- 255.255.255.240 (/28) - Subnet with 14 hosts
- 255.255.255.248 (/29) - Subnet with 6 hosts
- 255.255.255.252 (/30) - Subnet with 2 hosts (point-to-point links)

### CIDR (Classless Inter-Domain Routing) Notation

CIDR notation represents IP addresses and their associated network prefix in the format A.B.C.D/n, where n is the number of bits in the network portion. For example, 192.168.1.0/24 indicates that the first 24 bits represent the network, and the remaining 8 bits represent hosts. CIDR notation provides more efficient IP address allocation compared to classful addressing.

## Examples

### Example 1: Determining Network and Broadcast Addresses

**Problem:** Given the IP address 192.168.45.130 with subnet mask 255.255.255.0, find the network address and broadcast address.

**Solution:**

Step 1: Write the IP address in binary:
192.168.45.130 = 11000000.10101000.00101101.10000010

Step 2: Write the subnet mask in binary:
255.255.255.0 = 11111111.11111111.11111111.00000000

Step 3: Perform bitwise AND to find network address:
11000000.10101000.00101101.10000010
AND
11111111.11111111.11111111.00000000
=
11000000.10101000.00101101.00000000
= 192.168.45.0

Step 4: To find broadcast address, change all host bits to 1:
Network bits: 11000000.10101000.00101101 (first 24 bits)
Host bits (8 bits): 00000000 → change to 11111111
Broadcast: 11000000.10101000.00101101.11111111
= 192.168.45.255

**Answer:** Network Address = 192.168.45.0, Broadcast Address = 192.168.45.255

### Example 2: Calculating Number of Hosts in a Subnet

**Problem:** A network administrator is given the network 172.16.0.0/20. How many usable host addresses are available, and what is the first and last usable IP address?

**Solution:**

Step 1: The prefix /20 means 20 bits for network and 12 bits for hosts.
Number of host bits = 32 - 20 = 12

Step 2: Total addresses in subnet = 2^12 = 4096 addresses
Usable host addresses = Total - 2 (Network address and Broadcast address)
Usable hosts = 4096 - 2 = 4094

Step 3: Network address: The first 20 bits are fixed.
172.16.0.0 in binary: 10101100.00010000.00000000.00000000
With /20 mask, the third octet has 4 bits for network (11110000 = 240)
Network: 172.16.0.0 to 172.16.15.255

Step 4: First usable IP = Network address + 1 = 172.16.0.1
Last usable IP = Broadcast address - 1 = 172.16.15.254

**Answer:** 4094 usable hosts, First usable: 172.16.0.1, Last usable: 172.16.15.254

### Example 3: Subnetting a Class C Network

**Problem:** A company needs to create 6 subnets from the network 210.44.56.0/24. Determine the subnet mask and list all subnet addresses.

**Solution:**

Step 1: Determine the number of bits needed for 6 subnets.
2^n >= 6, so n = 3 (since 2^3 = 8)
We need to borrow 3 bits from the host portion.

Step 2: New prefix length = 24 + 3 = /27
Subnet mask = 255.255.255.224 (since 224 = 11100000 in binary)

Step 3: Block size = 256 - 224 = 32
This means each subnet is 32 addresses apart.

Step 4: Subnet addresses:

- Subnet 1: 210.44.56.0/27
- Subnet 2: 210.44.56.32/27
- Subnet 3: 210.44.56.64/27
- Subnet 4: 210.44.56.96/27
- Subnet 5: 210.44.56.128/27
- Subnet 6: 210.44.56.160/27
- Subnet 7: 210.44.56.192/27
- Subnet 8: 210.44.56.224/27

**Answer:** Subnet mask: 255.255.255.224 (/27), Available subnets: 8 (6 needed subnets can be satisfied)

## Exam Tips

1. **Memorize the class ranges**: Remember that Class A is 1-126, Class B is 128-191, Class C is 192-223. Note that 127 is reserved for loopback.

2. **Default subnet masks**: Class A: 255.0.0.0 (/8), Class B: 255.255.0.0 (/16), Class C: 255.255.255.0 (/24)

3. **Calculate hosts efficiently**: Number of usable hosts = 2^n - 2, where n is the number of host bits. The minus 2 accounts for network and broadcast addresses.

4. **Understand binary conversion**: Practice converting between decimal and binary. Remember that each octet has 8 bits, and the place values are 128, 64, 32, 16, 8, 4, 2, 1.

5. **Private IP ranges**: Know the three private address ranges - 10.0.0.0-10.255.255.255, 172.16.0.0-172.31.255.255, and 192.168.0.0-192.168.255.255.

6. **CIDR to subnet mask conversion**: The number after the slash (/) represents the number of 1s in the subnet mask. Write that many 1s and fill the rest with 0s.

7. **Subnetting trick**: For subnetting calculations, always determine the block size by subtracting the last octet of the subnet mask from 256.

8. **Special addresses**: Remember that 127.x.x.x is loopback, 0.0.0.0 is default route, and 255.255.255.255 is limited broadcast.
