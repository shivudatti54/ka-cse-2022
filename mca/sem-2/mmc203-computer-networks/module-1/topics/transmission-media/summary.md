# Transmission Media - Summary

## Key Definitions and Concepts

- **Transmission Media**: The physical pathway for data communication, classified as guided (bounded) or unguided (unbounded)
- **Guided Media**: Physical cables that direct signals (twisted pair, coaxial, optical fiber)
- **Unguided Media**: Wireless transmission through air/space (radio waves, microwaves, infrared)
- **Attenuation**: Signal strength loss over distance, measured in decibels
- **Crosstalk**: Unwanted signal coupling between adjacent channels
- **Bandwidth**: Frequency range a medium can carry, determining data transfer capacity

## Important Formulas and Theorems

- **Maximum UTP Length**: 100 meters (standard for Ethernet)
- **Coaxial Cable Limits**: 185m (10Base2/thinnet), 500m (10Base5/thicknet)
- **Optical Fiber Distances**: Multi-mode up to 2 km, Single-mode up to 100 km
- **Attenuation Formula**: Total Loss = Transmitter Output - Minimum Required Signal
- **Frequency Ranges**: Radio (3 kHz-300 GHz), Microwave (1-300 GHz), Infrared (300 GHz-400 THz)

## Key Points

1. Twisted pair cables (UTP/STP) are most common for LANs, with Cat6 supporting up to 10 Gbps
2. Coaxial cables offer better shielding than twisted pair, used for cable TV and some networks
3. Optical fiber provides highest bandwidth, lowest attenuation, and immunity to EMI
4. Single-mode fiber has smaller core (8-10 μm) for long-distance; multi-mode (50-62.5 μm) for shorter runs
5. Radio waves are omnidirectional, microwaves require line-of-sight, infrared needs direct path
6. UTP uses RJ-45 connectors; fiber uses SC, ST, or LC connectors
7. Transmission types: Simplex (one-way), Half-Duplex (two-way, not simultaneous), Full-Duplex (simultaneous)
8. Repeaters amplify signals to overcome attenuation over long distances
9. Cost ranking (low to high): UTP → Coaxial → STP → Multi-mode Fiber → Single-mode Fiber

## Common Mistakes to Avoid

1. Confusing single-mode and multi-mode fiber characteristics - remember SMF is for long distances
2. Thinking optical fiber is always better - consider cost and actual distance requirements
3. Forgetting maximum cable length limits for different media in network design
4. Misunderstanding that all wireless media penetrate walls - infrared cannot
5. Confusing attenuation with amplification - attenuation is signal loss, amplification boosts signal

## Revision Tips

1. Create a comparison table of all transmission media with columns for type, bandwidth, max distance, cost, and applications
2. Memorize the frequency ranges for unguided media as this is frequently tested
3. Practice identifying appropriate media for different scenarios (LAN vs WAN, short vs long distance)
4. Remember the standard cable lengths: 100m for UTP, 185m/500m for coaxial
5. Focus on advantages and disadvantages of each medium - this helps in selection questions
