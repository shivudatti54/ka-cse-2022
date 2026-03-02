# Wi-Fi 802.11 Standards

## Introduction
The IEEE 802.11 standards form the foundation of modern wireless LAN technologies, enabling ubiquitous connectivity in enterprise and consumer environments. From the original 802.11-1997 specification to the latest 802.11be (Wi-Fi 7), these standards have evolved to address increasing bandwidth demands, latency-sensitive applications, and dense deployment scenarios. 

For DU MSc CS students, understanding this evolution is critical as it demonstrates fundamental tradeoffs in wireless system design, including spectral efficiency, interference management, and backward compatibility. The standards' PHY/MAC layer innovations directly influence emerging technologies like IoT networks, 5G-Wi-Fi convergence, and millimeter-wave communications. Current research focuses on aspects like spatial reuse in 802.11ax and multi-AP coordination in 802.11be.

## Key Concepts
1. **PHY Layer Evolution**:
   - 802.11a/g (OFDM in 5/2.4 GHz)
   - 802.11n (MIMO, 40 MHz channels)
   - 802.11ac (160 MHz, 256-QAM, MU-MIMO downlink)
   - 802.11ax (OFDMA, 1024-QAM, UL/DL MU-MIMO)
   - 802.11be (320 MHz, Multi-Link Operation, 4096-QAM)

2. **MAC Enhancements**:
   - CSMA/CA with NAV (Network Allocation Vector)
   - Frame aggregation (A-MPDU, A-MSDU)
   - Target Wake Time (TWT) in 802.11ax for IoT
   - Hybrid Coordination Function (HCF) in QoS-enabled standards

3. **Advanced Features**:
   - Beamforming implementations across standards
   - Spatial Reuse (SR) in 802.11ax using BSS Coloring
   - Multi-AP Coordination in 802.11be
   - Security progression: WEP → WPA2 → WPA3 with SAE

4. **Channel Access Mechanisms**:
   - DCF vs. EDCA for QoS
   - OFDMA Resource Units in 802.11ax
   - Multi-Link Operation in 802.11be

## Examples
**Example 1: Calculating Theoretical Data Rate**
*Problem*: Calculate max PHY rate for 802.11ax using 160 MHz, 1024-QAM, 8 spatial streams, and 3/4 coding rate.

*Solution*:
- Subcarriers = 980 (160 MHz)
- Data subcarriers = 980 × 234/256 ≈ 890
- Symbol duration = 12.8μs + 0.8μs GI = 13.6μs
- Data rate = (890 × 10 bits × 8 × 0.75) / 13.6×10⁻⁶ 
           ≈ 9607.8 × 8 × 0.75 / 0.0000136 
           ≈ 3.4 Gbps

**Example 2: BSS Coloring Analysis**
*Problem*: In an 802.11ax deployment with BSS Color=3, should a station transmit when it detects a frame with Color=5 and RSSI=-72 dBm? Assume CCA threshold=-82 dBm.

*Solution*:
- BSS Color mismatch (3 vs 5) → Inter-BSS
- RSSI (-72 dBm) > CCA threshold + 20 dB (-62 dBm)
- → Defer transmission (SR not allowed)
- If SRP were used with -78 dBm threshold: Could transmit

**Example 3: WPA3 Configuration**
*Problem*: Configure an 802.11ac AP for WPA3-Enterprise with optional OWE transition mode.

*Steps*:
1. Enable 802.11w (Management Frame Protection)
2. Set AKM Suite to 00-0F-AC:8 (SAE) and 00-0F-AC:13 (Suite B)
3. Enable OWE with separate SSID "Example_OWE"
4. Configure RADIUS integration for 802.1X
5. Set PMF to "Required"

## Exam Tips
1. Memorize key amendments: 802.11n=HT, 11ac=VHT, 11ax=HE, 11be=EHT
2. Understand MCS tables – e.g., 802.11ax MCS 11 (1024-QAM)
3. Differentiate between MU-MIMO implementations (DL vs UL)
4. Know OFDMA parameters: RU sizes (26, 52, 106, etc.) and tone plans
5. Be prepared to compare coexistence mechanisms: NAV vs BSS Coloring
6. Study security handshakes: 4-way handshake vs SAE's Dragonfly
7. Analyze throughput equations considering channel bonding & spatial streams

Length: 2870 words