# IP Addressing & Subnetting - Summary

## Key Definitions and Concepts
- **IPv4**: 32-bit address with dotted-decimal notation
- **Subnet Mask**: Identifies network/host portions of IP
- **CIDR**: Classless addressing using prefix length (e.g., /24)
- **VLSM**: Variable subnet sizes within same network
- **IPv6**: 128-bit address with hexadecimal notation

## Important Formulas and Theorems
- Hosts per subnet = 2^(32 - prefix) - 2
- Subnets possible = 2^(subnet bits)
- IPv6 abbreviation rules: 
  - Remove leading zeros in hextet
  - Replace longest zero sequence with ::

## Key Points
- Class A: 1-126, B: 128-191, C: 192-223
- Private IP ranges cannot be routed on public internet
- /31 subnet allows 2 hosts (special case for point-to-point)
- IPv6 link-local addresses start with fe80::
- ARIN manages IP allocation in North America
- NAT translates private IPs to public IPs
- Subnetting reduces broadcast domains

## Common Mistakes to Avoid
- Forgetting to exclude network/broadcast addresses
- Incorrect CIDR to dotted-decimal conversion
- Double-compressing IPv6 addresses (only one :: allowed)
- Mixing classful concepts with CIDR/VLSM

## Revision Tips
1. Practice subnetting with random IPs using the "powers of 2" method
2. Create cheat sheet for /24 to /30 subnet masks
3. Use online tools like IP Calculator to verify answers
4. Memorize RFC 1918 private IP ranges
5. Solve DU's previous year questions on network design