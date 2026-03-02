# Wireless Communication Fundamentals - Summary

## Key Definitions and Concepts

- **Wireless Communication:** Transfer of information between points without physical conductors using electromagnetic waves
- **Electromagnetic Spectrum:** Complete range of electromagnetic wave frequencies, divided into LF, MF, HF, VHF, UHF, SHF, and EHF bands
- **Propagation Modes:** Ground wave (low frequencies, long distance), Sky wave (HF, ionospheric reflection), Line-of-sight (VHF and above, straight path)
- **Modulation:** Process of encoding information onto carrier waves; includes AM, FM (analog) and ASK, FSK, PSK, QAM (digital)
- **Antenna Gain:** Measure of directional concentration of radiated power, measured in dBi

## Important Formulas and Theorems

- **Wavelength:** λ = c/f (c = 3 × 10⁸ m/s)
- **Free Space Path Loss:** PL(dB) = 20log₁₀(d) + 20log₁₀(f) + 20log₁₀(4π/c)
- **Shannon's Capacity Theorem:** C = B × log₂(1 + SNR) bps

## Key Points

- Wireless frequencies range from 3 kHz to 300 GHz; higher frequencies offer more bandwidth but shorter ranges
- Wi-Fi standards (802.11b/g/n/ac/ax) operate at 2.4/5/6 GHz with data rates up to 9.6 Gbps
- Bluetooth (802.15.1) is a WPAN technology with range up to 240m (version 5.0)
- Line-of-sight propagation requires antennas to be visible to each other without obstacles
- Multipath fading occurs when signals reach receivers via multiple paths, causing constructive/destructive interference
- Multiple access techniques (FDMA, TDMA, CDMA, OFDMA) enable spectrum sharing among multiple users
- Signal attenuation increases with distance and frequency due to free space path loss and environmental absorption

## Common Mistakes to Avoid

1. Confusing wavelength with frequency - remember they are inversely proportional (λ = c/f)
2. Converting frequency to GHz incorrectly in calculations - always use Hz in formulas
3. Using linear SNR instead of converting from dB when applying Shannon's theorem
4. Mixing up propagation modes - sky wave uses ionospheric reflection at HF frequencies only
5. Forgetting that higher frequencies have shorter ranges despite higher bandwidth capacity

## Revision Tips

1. Create a table comparing frequency bands with their characteristics and applications
2. Practice numerical problems on path loss and channel capacity calculations
3. Memorize the wireless network categories (WPAN, WLAN, WMAN, WWAN) with examples
4. Review the evolution of Wi-Fi standards (802.11b through 802.11ax) for comparison
5. Focus on understanding conceptual relationships rather than rote memorization
