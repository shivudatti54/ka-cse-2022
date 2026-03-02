# IPv6 Datagram - Summary

## Key Definitions and Concepts

- **IPv6 Datagram**: The fundamental packet format in IPv6, consisting of a fixed 40-byte base header followed by optional extension headers and payload data.

- **Flow Label**: A 20-bit field in IPv6 header used to identify packets belonging to the same flow for special routing or QoS treatment by routers.

- **Extension Headers**: Optional headers in IPv6 that provide additional functionality such as routing, fragmentation, authentication, and encryption.

- **Next Header**: An 8-bit field indicating the type of header following the IPv6 base header (either an extension header or an upper-layer protocol).

- **Hop Limit**: An 8-bit field in IPv6 (replacing TTL in IPv4) that limits the number of hops a packet can traverse before being discarded.

## Important Formulas and Theorems

- **IPv6 Address Space**: 2¹²⁸ addresses (approximately 3.4 × 10³⁸ unique addresses)
- **IPv6 Base Header Size**: Fixed at 40 bytes (320 bits)
- **Maximum Payload Length**: 65,535 bytes (using 16-bit Payload Length field); larger payloads require Jumbo Payload option
- **Extension Header Processing Order**: Hop-by-Hop → Destination Options (routing) → Routing → Fragment → AH → ESP → Destination Options (upper-layer)

## Key Points

- IPv6 uses 128-bit source and destination addresses compared to 32-bit in IPv4, solving the address depletion problem.
- The IPv6 header has only 8 fields compared to 12+ in IPv4, resulting in simpler and faster packet processing.
- IPv6 eliminates the header checksum, reducing processing overhead at each router.
- Only the source node can fragment IPv6 packets; routers cannot fragment, unlike in IPv4.
- The Flow Label field enables efficient handling of real-time traffic and quality of service implementations.
- IPv6 has mandatory IPsec support through Authentication Header (AH) and Encapsulating Security Payload (ESP) extension headers.
- Common Next Header values: TCP (6), UDP (17), ICMPv6 (58), IPv6 (41), ESP (50), AH (51).
- IPv6 addresses use hexadecimal notation with colon separators, with compression rules to simplify representation.

## Common Mistakes to Avoid

1. **Confusing TTL with Hop Limit**: Remember IPv6 uses "Hop Limit" not "Time to Live" - both serve similar purposes but have different names.

2. **Incorrect Extension Header Order**: Always remember the correct processing order of extension headers; incorrect ordering can cause packet processing errors.

3. **Using Multiple Double Colons**: When compressing IPv6 addresses, only ONE double colon (::) is allowed in an address.

4. **Assuming Routers Can Fragment**: Unlike IPv4, IPv6 routers cannot fragment packets; only the source can perform fragmentation.

5. **Forgetting Next Header Types**: Students often confuse Next Header values - remember TCP is 6, UDP is 17, and ICMPv6 is 58.

## Revision Tips

1. Practice writing out the 8 IPv6 header fields with their bit sizes until you can do it from memory.

2. Create a table of common Next Header values and their meanings for quick reference.

3. Work through multiple IPv6 address compression examples to master the simplification rules.

4. Draw the extension header order diagram and recite it before exams.

5. Focus on the differences between IPv4 and IPv6 headers as this is a frequently tested concept.
