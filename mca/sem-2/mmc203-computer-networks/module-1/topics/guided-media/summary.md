# Guided Media in Computer Networks - Summary

## Key Definitions and Concepts

- **Guided Media:** Physical communication channels that direct signals along a specific path from sender to receiver; includes twisted pair, coaxial, and fiber optic cables.

- **Twisted Pair Cable:** Two copper wires twisted together to reduce electromagnetic interference and crosstalk; most common LAN cable.

- **UTP (Unshielded Twisted Pair):** Twisted pair without additional shielding; susceptible to EMI but cost-effective.

- **STP (Shielded Twisted Pair):** Twisted pair with additional shielding; better EMI protection but more expensive.

- **Coaxial Cable:** Cable with central conductor, insulation, braided shield, and outer jacket; excellent shielding against EMI.

- **Fiber Optic Cable:** Transmits data as light pulses through glass/plastic fibers; highest bandwidth and longest distances.

- **Single-Mode Fiber:** Small core (8-10 μm) allowing one light path; used for long-distance (100+ km) communication.

- **Multi-Mode Fiber:** Larger core (50-62.5 μm) allowing multiple light paths; used for short distances (up to 2 km).

## Important Formulas and Theorems

- **Twisted Pair Categories:** Cat3 (16 MHz), Cat5 (100 MHz), Cat6 (250 MHz), Cat6a (500 MHz), Cat7 (600 MHz), Cat8 (2000 MHz)

- **Maximum Ethernet Distances:** Twisted Pair: 100m; 10Base2 (Coaxial): 185m; 10Base5 (Coaxial): 500m; Fiber MMF: 2km; Fiber SMF: 100+ km

- **Fiber Attenuation:** Typical single-mode = 0.25 dB/km; Multi-mode (850 nm) = 3 dB/km

- **Power Budget:** Received Power (dBm) = Transmitted Power (dBm) - Total Loss (dB)

## Key Points

- Twisted pair cables use RJ-45 connectors and are categorized by performance levels (Cat5e, Cat6, Cat6a, etc.)

- Coaxial cables (RG-58 for Thin Ethernet, RG-8 for Thick Ethernet) offer better shielding than twisted pair but are rarely used in modern LANs

- Fiber optic cables provide immunity to EMI, better security, and much longer transmission distances compared to copper cables

- Single-mode fiber requires laser light source and is more expensive but supports longer distances than multi-mode fiber

- For most modern LAN installations, Cat6 or Cat6a UTP is the recommended choice balancing cost, performance, and ease of installation

- Fiber optic technology is preferred for backbone networks, inter-building connections, and long-distance telecommunications

- The choice of guided media depends on bandwidth requirements, transmission distance, EMI environment, budget, and installation complexity

## Common Mistakes to Avoid

- Confusing UTP and STP: Remember UTP has no metallic shielding while STP has additional foil/braid shielding

- Mixing up single-mode and multi-mode fiber characteristics: Single-mode has smaller core but longer reach

- Forgetting maximum distance limitations: Exceeding 100m for twisted pair causes signal degradation

- Using inappropriate cable categories: Cat5e cannot support 10 Gbps over 55m; need Cat6a or better

- Ignoring EMI considerations: Industrial environments require shielded cables (STP or coaxial)

## Revision Tips

1. Create a comparison table of all three cable types covering bandwidth, distance, cost, advantages, and disadvantages

2. Memorize the Ethernet standards (10Base-T, 100Base-TX, 1000Base-T) and their cable requirements

3. Remember that fiber uses light (not electricity), making it immune to EMI and suitable for long distances

4. Practice with example scenarios: determine appropriate cable type given bandwidth, distance, and environmental constraints

5. Focus on understanding why certain cables are chosen for specific applications rather than just memorizing facts
