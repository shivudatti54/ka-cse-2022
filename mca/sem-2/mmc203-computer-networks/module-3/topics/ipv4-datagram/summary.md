# IPv4 Datagram Header and Fragmentation - Summary

## Key Definitions and Concepts

- **IPv4 Datagram:** The fundamental unit of data transmission at the network layer, consisting of a 20-60 byte header and payload data.
- **Fragmentation:** The process of breaking large IP datagrams into smaller pieces to accommodate networks with smaller MTUs.
- **MTU (Maximum Transmission Unit):** The maximum packet size a network link can handle.
- **TTL (Time to Live):** A hop counter that prevents packets from circulating indefinitely in the network.

## Important Formulas and Theorems

- **Maximum datagram size:** 65,535 bytes (2¹⁶ - 1)
- **Header length range:** 20-60 bytes (IHL values 5-15, multiplied by 4)
- **Maximum fragment data per packet:** MTU - 20 bytes (minimum header)
- **Fragment offset calculation:** Offset = (Starting byte position) / 8
- **Number of fragments:** ceil(Total data size / Maximum fragment data)
- **IP Address classes:** Class A (1-126), Class B (128-191), Class C (192-223), Class D (224-239), Class E (240-255)

## Key Points

- IPv4 header contains 14 fields in the fixed portion plus optional fields
- All fragments of a datagram share the same Identification value
- The More Fragments (MF) flag is 1 for all fragments except the last
- Reassembly occurs only at the destination host, not at routers
- Header checksum covers only the IP header, not the data
- Each router decrements TTL and recalculates the header checksum
- The Protocol field identifies the upper-layer protocol (6=TCP, 17=UDP, 1=ICMP)
- Fragment offset is measured in 8-byte units to represent offsets up to 65,528 bytes with 13 bits

## Common Mistakes to Avoid

1. **Confusing TTL with time:** TTL is actually a hop count, not seconds. Each router decrements it, regardless of processing time.
2. **Forgetting fragment offset units:** Students often calculate offsets in bytes instead of 8-byte blocks.
3. **Assuming routers reassemble fragments:** Reassembly happens only at the destination, a common misconception.
4. **Not checking the DF flag:** If Don't Fragment is set and MTU is too small, the packet is simply discarded.

## Revision Tips

1. Draw the IPv4 header diagram from memory and label all fields with their bit sizes
2. Practice numerical problems on fragmentation with different MTU values
3. Memorize the Protocol field values for common protocols (TCP=6, UDP=17, ICMP=1)
4. Remember that 127.x.x.x is reserved for loopback testing
5. Understand the incremental checksum update method for quick calculations during exams
