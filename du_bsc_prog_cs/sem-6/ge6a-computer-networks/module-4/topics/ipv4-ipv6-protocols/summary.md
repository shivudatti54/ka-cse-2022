# IPv4 and IPv6 Protocols - Summary

## Key Definitions and Concepts

- **IPv4:** Internet Protocol version 4, using 32-bit addresses allowing approximately 4.3 billion unique addresses, with header sizes of 20-60 bytes.

- **IPv6:** Internet Protocol version 6, using 128-bit addresses allowing approximately 340 undecillion addresses, with fixed 40-byte headers.

- **CIDR (Classless Inter-Domain Routing):** Address allocation method using prefix lengths (e.g., /24) instead of classful boundaries, enabling efficient route aggregation.

- **Subnetting:** Dividing a network into smaller sub-networks by borrowing host bits for network bits.

- **NAT (Network Address Translation):** Technique allowing multiple devices to share a single public IPv4 address.

- **SLAAC (Stateless Address Autoconfiguration):** IPv6 mechanism allowing hosts to automatically configure addresses without DHCP.

- **IPv4-mapped IPv6 addresses:** Format (::ffff:x.x.x.x) enabling IPv6 clients to communicate with IPv4 servers.

## Important Formulas and Theorems

- **IPv4 usable hosts per subnet:** 2ⁿ - 2, where n = number of host bits (subtract 2 for network and broadcast addresses)

- **IPv6 address space:** 2¹²⁸ ≈ 3.4 × 10³⁸ addresses

- **IPv4 header minimum size:** 20 bytes (without options)

- **IPv6 header fixed size:** 40 bytes

- **IPv4 minimum MTU:** 68 bytes; IPv6 minimum MTU:** 1280 bytes

## Key Points

- IPv4 header contains 14 fields including Version, IHL, TOS, Total Length, Identification, Flags, Fragment Offset, TTL, Protocol, Header Checksum, Source Address, and Destination Address.

- IPv4 addresses are 32-bit (4 bytes), represented in dotted-decimal notation (e.g., 192.168.1.1).

- IPv6 addresses are 128-bit (16 bytes), represented in colon-hexadecimal notation (e.g., 2001:db8::1).

- IPv4 private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.

- IPv6 link-local addresses use FE80::/10 prefix.

- IPv6 eliminates broadcast; multicast replaces all broadcast functionality.

- IPv4 header includes checksum; IPv6 header does not (handled by lower layers).

- IPv6 implements IPsec natively; IPv4 requires additional implementation.

- IPv6 fragmentation is source-only; IPv4 allows router fragmentation.

## Common Mistakes to Avoid

1. **Confusing IPv4 and IPv6 loopback addresses:** IPv4 uses 127.0.0.1; IPv6 uses ::1

2. **Forgetting that IPv6 :: can be used only once per address** for compression

3. **Assuming broadcast exists in IPv6** — it has been replaced by multicast

4. **Ignoring that IPv6 minimum MTU is 1280 bytes** (vs IPv4's 68 bytes)

5. **Not understanding that IPv6 headers don't include fragmentation-related fields** since only sources can fragment

## Revision Tips

1. Create a comparison table between IPv4 and IPv6 covering address length, header size, security, QoS, fragmentation, auto-configuration, and broadcast handling.

2. Practice IPv6 address compression—convert between full and compressed forms repeatedly.

3. Memorize the IPv4 header field sequence in order; this is frequently tested in practical exams.

4. Remember the three IPv4 private ranges and the IPv6 link-local prefix (FE80::/10).

5. Understand why IPv6 was developed (address exhaustion) and how it solves each limitation of IPv4.