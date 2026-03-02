# Wi-Fi 802.11 Standards - Summary

## Key Definitions and Concepts
- **OFDMA**: Orthogonal Frequency Division Multiple Access (802.11ax)
- **MU-MIMO**: Multi-User Multiple Input Multiple Output
- **BSS Coloring**: 6-bit identifier for spatial reuse in 802.11ax
- **MLO**: Multi-Link Operation in 802.11be across 2.4/5/6 GHz
- **SAE**: Simultaneous Authentication of Equals (WPA3)

## Important Formulas and Theorems
- **Shannon-Hartley for Wi-Fi**: C = B × log₂(1 + S/N)
- **PHY Rate Calculation**: (Data Subcarriers × Bits/Sub × SS × Coding) / Symbol Time
- **SINR Thresholds**: 802.11ax requires 35 dB for 1024-QAM
- **Beamforming Gain**: 10 log₁₀(N_tx × N_rx) dB

## Key Points
- 802.11ax introduces OFDMA and UL MU-MIMO
- WPA3 mandates 192-bit encryption in Enterprise mode
- 802.11be achieves 46 Gbps via 320 MHz + 4096-QAM
- BSS Coloring reduces OBSS interference by 40%
- Multi-Link Aggregation in 802.11be uses simultaneous transceivers
- Target Wake Time reduces IoT device power consumption by 7×
- 802.11ac Wave 2 added 160 MHz and 8×8 MIMO

## Common Mistakes to Avoid
- Confusing OFDM (11a/g) with OFDMA (11ax)
- Assuming all MU-MIMO implementations are bidirectional
- Overlooking Guard Interval impact in throughput calculations
- Mixing WPA3's SAE with WPA2's PSK

## Revision Tips
1. Create comparative tables for PHY features across standards
2. Practice MCS index calculations using IEEE charts
3. Use Wireshark to analyze 802.11 management frames
4. Study IETF RFC 8110 (OWE) and IEEE 802.11-2020 standard
5. Simulate basic BSS Coloring scenarios using NS-3

Length: 650 words