# IPv4 Address - Summary

## Key Definitions and Concepts

- **IPv4 Address**: A 32-bit logical address expressed in dotted decimal notation (e.g., 192.168.1.1), uniquely identifying a device on a network.

- **Network ID**: The portion of an IP address that identifies the specific network on which a device resides.

- **Host ID**: The portion of an IP address that identifies a specific device within a network.

- **Subnet Mask**: A 32-bit number that separates network and host portions of an IP address, using 1s for network bits and 0s for host bits.

- **CIDR (Classless Inter-Domain Routing)**: A notation system (e.g., /24) that represents the number of network bits in an IP address.

## Important Formulas and Theorems

- **Usable Hosts Formula**: Usable hosts = 2^n - 2, where n = number of host bits (subtracting network and broadcast addresses)

- **Number of Subnets Formula**: Number of subnets = 2^n, where n = number of bits borrowed for subnetting

- **Block Size Calculation**: Block size = 256 - (value of last non-zero octet in subnet mask)

- **Default Subnet Masks**: Class A: 255.0.0.0 (/8), Class B: 255.255.0.0 (/16), Class C: 255.255.255.0 (/24)

## Key Points

- IPv4 addresses are 32-bit addresses with approximately 4.3 billion unique addresses available.

- Class A (1-126): /8 mask, 16M+ hosts per network; Class B (128-191): /16 mask, 65K+ hosts; Class C (192-223): /24 mask, 254 hosts.

- The address 127.0.0.1 is reserved for loopback testing.

- Private IP ranges: 10.0.0.0-10.255.255.255, 172.16.0.0-172.31.255.255, 192.168.0.0-192.168.255.255.

- Subnetting allows division of large networks into smaller, manageable segments.

- CIDR notation provides flexible allocation beyond traditional class boundaries.

- Network address has all host bits as 0; broadcast address has all host bits as 1.

## Common Mistakes to Avoid

1. **Forgetting to subtract 2**: Always remember to subtract network and broadcast addresses when calculating usable hosts.

2. **Classful thinking**: Avoid assuming default classes for all addresses; use CIDR and subnet masks for proper network division.

3. **Incorrect binary conversion**: Practice decimal-to-binary conversion thoroughly; each octet must be 0-255.

4. **Broadcast address confusion**: Remember broadcast address is the highest address in a subnet, not the network address.

## Revision Tips

1. Practice binary conversions daily - memorize powers of 2 from 2^0 to 2^8.

2. Draw the bit allocation for different classes to visualize network and host portions.

3. Work through at least 5 subnetting problems daily to build speed and accuracy.

4. Create a reference table of common subnet masks and their CIDR equivalents.

5. Remember the special addresses (loopback, private, broadcast) as they frequently appear in exams.
