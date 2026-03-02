# Random Access Protocols (Multiple Access) - Summary

## Key Definitions and Concepts

- **Multiple Access Protocol**: A set of rules that govern how multiple devices share a common communication channel without excessive collisions
- **Random Access (Contention-based) Protocols**: MAC protocols where stations compete for channel access, handling collisions when they occur
- **Vulnerable Time**: The time period during which a frame is susceptible to collision if another station transmits
- **Carrier Sense**: The mechanism of checking if the channel is idle before attempting transmission
- **Binary Exponential Backoff**: An algorithm where the random wait time doubles after each collision

## Important Formulas and Theorems

| Protocol | Maximum Throughput | Vulnerable Time |
|----------|-------------------|-----------------|
| Pure ALOHA | S = G × e^(-2G), Smax = 0.184 | 2T |
| Slotted ALOHA | S = G × e^(-G), Smax = 0.368 | T |
| CSMA/CD | ~98.6% (under ideal conditions) | N/A |

- **Minimum Frame Size for CSMA/CD**: ≥ 2 × propagation delay × bandwidth
- **CSMA/CD Efficiency**: 1 / (1 + 5a), where a = propagation delay / transmission time

## Key Points

1. ALOHA was the first random access protocol, developed at University of Hawaii for satellite communication
2. Slotted ALOHA doubles the maximum throughput compared to Pure ALOHA by reducing vulnerable time
3. CSMA improves over ALOHA by implementing carrier sense before transmission
4. 1-persistent CSMA has lowest delay but highest collision probability; non-persistent has lowest collisions but highest delay
5. CSMA/CD (Ethernet) allows collision detection during transmission; minimum frame size ensures this works
6. CSMA/CA (WiFi) cannot detect collisions reliably, so it avoids them through IFS, backoff, and RTS/CTS
7. Hidden terminal problem is solved in WiFi using RTS/CTS exchange
8. Network Allocation Vector (NAV) provides virtual carrier sensing in wireless networks
9. Binary exponential backoff in Ethernet ranges from 0 to 2¹⁰-1 slot times after collisions
10. Modern switched Ethernet operates in full-duplex, eliminating collision domains entirely

## Common Mistakes to Avoid

1. **Confusing CSMA/CD and CSMA/CA**: CSMA/CD is for wired Ethernet (detects collisions), CSMA/CA is for wireless WiFi (avoids collisions)
2. **Forgetting vulnerable time difference**: Pure ALOHA has 2T, Slotted ALOHA has T - this is a common exam trick
3. **Incorrect frame size calculation**: Remember minimum frame size ensures round-trip propagation can be detected
4. **Missing IFS values**: In CSMA/CA, different IFS (SIFS, DIFS, EIFS) create priority levels - don't confuse them
5. **Ignoring hidden terminal problem**: This is specifically why WiFi uses RTS/CTS, which Ethernet doesn't need

## Revision Tips

1. **Practice numerical problems**: Focus on throughput calculations for ALOHA and minimum frame size for CSMA/CD
2. **Create comparison tables**: Make a table comparing all protocols (ALOHA variants, CSMA variants, CSMA/CD, CSMA/CA)
3. **Understand the "why"**: For each protocol, ask - what problem does it solve? What limitation does it address?
4. **Remember real-world associations**: Ethernet = CSMA/CD, WiFi = CSMA/CA
5. **Draw timing diagrams**: Visualize the carrier sense, backoff, and transmission sequences for each protocol