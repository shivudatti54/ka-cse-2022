# Physical Layer Transmission Media

## Introduction
Transmission media form the physical path between transmitter and receiver in communication systems. As the foundational layer in computer networks (OSI Layer 1), their characteristics directly impact network performance, reliability, and cost. 

Modern networks use two broad categories: guided (wired) media like twisted pair and fiber optics, and unguided (wireless) media including radio waves and microwaves. Selection depends on bandwidth requirements, transmission distance, environmental factors, and installation costs. With 5G networks achieving 20 Gbps speeds and submarine cables handling 250 Tbps, understanding transmission media is crucial for network design.

The physical layer's efficiency determines maximum data rates through Shannon's Theorem: C = B log₂(1 + S/N). This makes media choice critical for applications ranging from IoT sensors (low bandwidth) to data centers (high-speed fiber links).

## Key Concepts
1. **Twisted Pair Cables**
   - **UTP (Unshielded Twisted Pair)**: Category 6A supports 10 Gbps up to 100m. Used in Ethernet (IEEE 802.3). Susceptible to EMI
   - **STP (Shielded)**: Foil shielding reduces interference. Used in industrial environments

2. **Coaxial Cable**
   - RG-6 used for cable TV (550 MHz bandwidth)
   - Impedance matching (50Ω vs 75Ω) crucial for signal integrity

3. **Fiber Optics**
   - Single-mode fiber: 9µm core, 1310/1550 nm lasers, <0.4 dB/km loss
   - Multi-mode: 50-62.5µm core, LED sources. OM5 supports SWDM
   - DWDM systems carry 80+ channels @ 100 GHz spacing

4. **Wireless Media**
   - Radio Waves: IEEE 802.11ax (Wi-Fi 6) uses 2.4/5 GHz bands
   - Microwaves: Point-to-point links (5G NR FR2: 24-52 GHz)
   - Infrared: Short-range (TV remotes, IrDA)
   - Satellite: GEO (35,786 km), LEO constellations (Starlink: 550 km)

5. **Transmission Characteristics**
   - Attenuation: α = 10 log₁₀(P₁/P₂) dB
   - Dispersion: Modal (MMF), Chromatic (SMF)
   - Shannon-Hartley Capacity: C = B log₂(1 + SNR)

## Examples

**Example 1: Enterprise Network Design**
*Requirement*: Connect 3 buildings (200m apart) with 10 Gbps links
*Solution*:
1. For intra-building: Cat 6A UTP (100m limit)
2. Inter-building: Single-mode fiber (1310 nm)
3. Calculate power budget: 
   - Transmitter: -3 dBm
   - Receiver sensitivity: -28 dBm
   - Allowable loss: 25 dB
   - Fiber loss: 0.4 dB/km × 0.2 km = 0.08 dB
   - Connectors: 4 × 0.3 dB = 1.2 dB
   - Total: 1.28 dB < 25 dB → Feasible

**Example 2: Wireless Link Budget**
*Scenario*: 5 GHz microwave link (20 km)
*Calculations*:
1. Free Space Path Loss: 
   FSPL = 20 log₁₀(d) + 20 log₁₀(f) + 92.45
   = 20 log(20) + 20 log(5) + 92.45 = 26.02 + 13.98 + 92.45 = 132.45 dB
2. System Gain: 
   Tx Power (30 dBm) + Antenna Gain (24 dBi ×2) - FSPL
   = 30 + 48 - 132.45 = -54.45 dBm
3. Margin: Rx sensitivity (-70 dBm) - (-54.45) = 15.55 dB

## Exam Tips
1. Always mention both technical specs and application scenarios
2. Memorize frequency bands: Wi-Fi (2.4/5 GHz), 5G mmWave (24-52 GHz)
3. Fiber types: SMF vs MMF core diameters and light sources
4. Calculate link budgets using FSPL and dB arithmetic
5. Compare media using tables (bandwidth, distance, cost)
6. Recent trends: SDM (Space Division Multiplexing) in fiber
7. Draw diagrams for twisted pair shielding and fiber refraction