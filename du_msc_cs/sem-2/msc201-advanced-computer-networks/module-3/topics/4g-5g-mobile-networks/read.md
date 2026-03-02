# 4G-5G Mobile Networks

## Introduction
Fourth-generation (4G) and fifth-generation (5G) mobile networks represent revolutionary advancements in wireless communication. 4G, standardized as LTE-Advanced, introduced all-IP networks with peak speeds of 1 Gbps, enabling HD video streaming and mobile broadband. 5G (IMT-2020) achieves 20 Gbps speeds, <1ms latency, and supports 1 million devices/km² through advanced technologies like millimeter wave (mmWave), massive MIMO, and network slicing.

The transition from 4G to 5G addresses emerging requirements of IoT, autonomous vehicles, and Industry 4.0. While 4G focused on human-centric services, 5G enables mission-critical communications and ultra-reliable low-latency applications. Current research focuses on dynamic spectrum sharing, AI-driven network optimization, and integration with satellite networks (3GPP Release 17/18).

## Key Concepts
1. **OFDMA vs FBMC**: 4G uses Orthogonal Frequency Division Multiple Access with cyclic prefix. 5G employs Filter Bank Multi-Carrier for better spectral efficiency.
2. **Massive MIMO**: 5G base stations use 64-256 antennas vs 4G's 2-8, enabling 3D beamforming.
3. **Network Slicing**: Creates virtual networks on shared infrastructure (eMMB, URLLC, mMTC slices).
4. **Edge Computing**: 5G moves computation to network edge (Multi-access Edge Computing) reducing latency.
5. **D2D Communication**: 5G enables direct device-to-device links bypassing base stations.
6. **Security Architecture**: 5G introduces SUPI encryption and enhanced authentication (5G-AKA vs 4G's EPS-AKA).

## Examples
**Example 1: Calculating 5G Throughput**
Given: 100 MHz channel, 256-QAM, 4x4 MIMO
Solution:
- Subcarriers = 1200 (30 kHz spacing)
- Symbols/slot = 14
- Throughput = 1200 × 14 × 6 (256-QAM) × 4 (MIMO) × 1000 slots/sec ≈ 3.36 Gbps

**Example 2: Network Slicing Configuration**
A smart city requires:
1. eMBB slice: 50 Mbps/user, 100ms latency (public WiFi)
2. URLLC slice: 1ms latency, 99.999% reliability (traffic control)
Implementation: Separate QoS Class Identifiers (QCIs) with dedicated resource blocks.

**Example 3: Handover Optimization**
4G uses X2-based handovers (40-60ms). 5G employs Dual Connectivity (EN-DC) with 4G anchor and 5G booster cells, reducing handover time to <10ms.

## Exam Tips
1. Memorize 3GPP release numbers: 4G (Release 8-14), 5G (Release 15+)
2. Understand protocol stack differences: 5G's Service-Based Architecture vs 4G's point-to-point
3. Compare key parameters: 4G (20 MHz BW, 2x2 MIMO) vs 5G (400 MHz BW, 64x64 MIMO)
4. Study network slicing use cases: Factory automation vs enhanced mobile broadband
5. Know security enhancements: 5G's permanent identifier protection (SUPI)
6. Practice latency calculations including processing delays
7. Review 5G NR frame structure (flexible numerology with μ=0-4)

Length: 2500 words, MSc CS (research-oriented) postgraduate level