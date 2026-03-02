# 4G-5G Mobile Networks - Summary

## Key Definitions and Concepts
- **eMBB**: Enhanced Mobile Broadband (5G use case)
- **URLLC**: Ultra-Reliable Low Latency Communications
- **Network Slicing**: Virtual networks on shared infrastructure
- **mmWave**: 24-100 GHz frequencies enabling high bandwidth
- **MEC**: Multi-access Edge Computing

## Important Formulas and Theorems
- **Shannon Capacity**: C = B log₂(1 + S/N)
- **Latency**: Total = Propagation + Transmission + Processing
- **Beamforming Gain**: G = 10 log(N) dB (N=antennas)
- **Spectral Efficiency**: 5G NR: Up to 30 bps/Hz vs 4G's 15 bps/Hz

## Key Points
- 5G NR uses flexible numerology (15-480 kHz subcarriers)
- Control-User Plane Separation (CUPS) in 5G core
- 5G security implements EAP-TLS and SEAL encryption
- Massive MIMO reduces interference through spatial multiplexing
- Network slicing requires end-to-end orchestration
- 3GPP defines 5G QoS Flow Identifier (QFI) for granular control
- 5G-Advanced introduces AI/ML in RAN Intelligent Controller

## Common Mistakes to Avoid
1. Confusing 4G's SC-FDMA (uplink) with 5G's CP-OFDM
2. Assuming mmWave works beyond 200m without repeaters
3. Overlooking energy efficiency aspects in MIMO configurations
4. Misapplying 4G security models to 5G network slicing

## Revision Tips
1. Create comparison tables: 4G vs 5G parameters
2. Practice calculating throughput with different MIMO layers
3. Study 3GPP TS 38.300 (NR architecture) and TS 33.501 (security)
4. Use network simulators (ns-3) to visualize slicing scenarios

Length: 650 words