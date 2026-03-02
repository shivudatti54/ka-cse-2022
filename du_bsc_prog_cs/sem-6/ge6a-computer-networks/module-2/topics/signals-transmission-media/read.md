# Signals and Transmission Media

## Comprehensive Study Material for Ge6A Computer Networks

---

## 1. Introduction and Real-World Relevance

### 1.1 What are Signals and Transmission Media?

In the context of computer networks, **signals** are electrical, electromagnetic, or optical representations of data that travel across **transmission media** from one device to another. The study of signals and transmission media forms the foundation of all communication systems, including the internet, mobile networks, and local area networks (LANs).

### 1.2 Real-World Applications

Consider the following everyday scenarios:

- **Video Streaming**: When you watch a YouTube video, the data travels through fiber optic cables (guided media) and wireless signals (unguided media) from servers to your device.
- **Video Calls**: During a Zoom or Google Meet call, your voice and video are converted into digital signals, transmitted through various media, and reconstructed at the destination.
- **Online Gaming**: Gaming requires real-time data transmission with minimal latency, achieved through carefully designed transmission media and signal processing.

Understanding signals and transmission media is essential for network engineers, system administrators, and anyone pursuing a career in telecommunications or cybersecurity.

---

## 2. Types of Signals

### 2.1 Analog Signals

**Analog signals** are continuous signals that vary smoothly over time. They can take any value within a given range and are represented by sine waves.

**Key Characteristics:**
- Continuous in both time and amplitude
- Described by three parameters: **amplitude**, **frequency**, and **phase**
- Vulnerable to noise and distortion

**Example**: Human voice, radio waves, analog television signals

### 2.2 Digital Signals

**Digital signals** are discrete signals that represent data using binary values (0s and 1s). They are typically represented as square waves with two distinct voltage levels.

**Key Characteristics:**
- Discrete in time and amplitude
- More resistant to noise than analog signals
- Easier to regenerate and process

**Example**: Computer data, digital audio, fiber optic signals

### 2.3 Comparison: Analog vs Digital Signals

| Feature | Analog Signal | Digital Signal |
|---------|---------------|----------------|
| Representation | Continuous wave | Discrete binary values |
| Bandwidth | Lower efficiency | Higher efficiency |
| Noise Resistance | Low | High |
| Equipment Complexity | Lower | Higher |
| Data Security | Lower | Higher (easier to encrypt) |

---

## 3. Key Signal Properties

### 3.1 Amplitude

**Amplitude** is the maximum displacement or strength of a signal from its average value (often measured in volts). In a sine wave, it represents the height of the peak from the center line.

- **Higher amplitude** = stronger signal = can travel longer distances
- **Lower amplitude** = weaker signal = more susceptible to noise

### 3.2 Frequency

**Frequency** is the number of complete cycles a signal completes per second, measured in **Hertz (Hz)**.

- **High frequency** signals can carry more data but have shorter wavelengths
- **Low frequency** signals travel longer distances but carry less data
- **Relationship**: Frequency (f) = 1/Period (T)

### 3.3 Phase

**Phase** describes the position of a point in time on a waveform cycle, measured in degrees (°) or radians. Phase is crucial because it allows multiple signals to be combined and later separated through modulation techniques.

**Key Points:**
- A complete cycle is 360° or 2π radians
- Phase shift occurs when the waveform is shifted in time
- Phase changes are used in PSK (Phase Shift Keying) for digital modulation

```
Phase Shift Example (Python):
import numpy as np
import matplotlib.pyplot as plt

# Generate time array
t = np.linspace(0, 1, 1000)

# Original signal (phase = 0)
f = 5  # frequency in Hz
signal_original = np.sin(2 * np.pi * f * t)

# Phase shifted signal (phase = 90 degrees = π/2)
phase_shift = np.pi / 2
signal_shifted = np.sin(2 * np.pi * f * t + phase_shift)

# Plotting
plt.figure(figsize=(12, 4))
plt.plot(t, signal_original, label='Original (Phase = 0°)', linewidth=2)
plt.plot(t, signal_shifted, label='Phase Shifted (Phase = 90°)', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Phase Shift Demonstration')
plt.legend()
plt.grid(True)
plt.savefig('phase_shift.png', dpi=150)
plt.show()
```

### 3.4 Bandwidth

**Bandwidth** is the range of frequencies that a transmission medium can carry effectively. It is measured in Hertz (Hz) and represents the difference between the highest and lowest frequencies.

**Important Relationships:**
- **Data Rate (bit rate)**: Maximum amount of data transmitted per second
- **Bandwidth**: Capacity of the channel

According to **Nyquist Theorem**:
```
Maximum Data Rate = 2 × Bandwidth × log₂(M)
```
Where M = number of signal levels

According to **Shannon's Capacity**:
```
Channel Capacity = Bandwidth × log₂(1 + SNR)
```
Where SNR = Signal-to-Noise Ratio

**Example**: A telephone line with 3000 Hz bandwidth and SNR of 30 dB:
```
SNR = 10^(30/10) = 1000
Capacity = 3000 × log₂(1001) ≈ 3000 × 9.97 ≈ 29,910 bps
```

---

## 4. Transmission Media: Guided

Guided transmission media provide a physical pathway for signals to travel. They include:

### 4.1 Twisted Pair Cable

**Description**: Consists of pairs of copper wires twisted together to reduce electromagnetic interference (EMI). This is the most common cabling for LANs.

**Types:**
- **UTP (Unshielded Twisted Pair)**: No shielding, susceptible to interference, used in Ethernet networks
- **STP (Shielded Twisted Pair)**: Has metallic shielding, better interference resistance

**Categories (TIA/EIA standards):**
| Category | Max Data Rate | Typical Use |
|----------|---------------|-------------|
| Cat 3 | 10 Mbps | Voice, legacy Ethernet |
| Cat 5 | 100 Mbps | Fast Ethernet |
| Cat 5e | 1 Gbps | Gigabit Ethernet |
| Cat 6 | 1 Gbps / 10 Gbps | Modern networks |
| Cat 6a | 10 Gbps | Data centers |
| Cat 7/8 | 25-40 Gbps | High-speed applications |

**Advantages**: Inexpensive, easy to install, adequate for short distances
**Disadvantages**: Limited bandwidth, susceptible to interference, limited distance (~100m)

### 4.2 Coaxial Cable

**Description**: Has a central copper conductor surrounded by insulation, a braided metal shield, and an outer jacket. Provides better shielding than twisted pair.

**Types:**
- **Thinnet (10Base2)**: Thin coaxial cable, up to 185m, used in early Ethernet
- **Thicknet (10Base5)**: Thick coaxial cable, up to 500m, used in early backbone networks

**Applications**: Cable television (CATV), cable internet, older Ethernet networks (10Base2/10Base5)

**Advantages**: Better shielding, longer distances than twisted pair, higher bandwidth
**Disadvantages**: More expensive, harder to install, heavier

### 4.3 Fiber Optic Cable

**Description**: Uses light signals to transmit data through thin strands of glass or plastic. Data is converted to light pulses and transmitted through total internal reflection.

**Types:**
- **Single-Mode Fiber (SMF)**: Core diameter 8-10 μm, carries one mode of light, used for long distances (up to 100km+)
- **Multi-Mode Fiber (MMF)**: Core diameter 50-62.5 μm, carries multiple modes of light, used for shorter distances (up to 2km)

**Advantages**:
- Extremely high bandwidth (100 Gbps+)
- Low signal attenuation (0.2 dB/km)
- Immune to electromagnetic interference
- Better security (difficult to tap)
- Longer transmission distances

**Disadvantages**:
- Expensive (cabling and equipment)
- Requires specialized installation skills
- Fragile compared to copper

**Code Example: Signal Attenuation Calculation**

```python
import math

def calculate_signal_strength(initial_power_dbm, distance_km, attenuation_db_per_km):
    """
    Calculate signal strength after attenuation
    
    Parameters:
    - initial_power_dbm: Initial signal power in dBm
    - distance_km: Distance in kilometers
    - attenuation_db_per_km: Attenuation factor in dB/km
    
    Returns:
    - Final signal power in dBm
    """
    total_attenuation = distance_km * attenuation_db_per_km
    final_power = initial_power_dbm - total_attenuation
    return final_power

# Example calculations for different media
media_attenuation = {
    "Single-mode Fiber": 0.2,  # dB/km
    "Multi-mode Fiber": 3.0,   # dB/km
    "Coaxial Cable": 7.0,      # dB/100m -> 70 dB/km
    "UTP Cat6": 20.0           # dB/100m -> 200 dB/km
}

initial_power = 0  # dBm (typical laser output)

print("Signal Strength After 1 km Transmission")
print("=" * 50)
for media, atten in media_attenuation.items():
    final = calculate_signal_strength(initial_power, 1, atten)
    print(f"{media:20s}: {final:6.1f} dBm")
    
# Calculate maximum distance for typical receiver sensitivity
receiver_sensitivity = -30  # dBm (minimum detectable signal)

print("\nMaximum Transmission Distance")
print("=" * 50)
for media, atten in media_attenuation.items():
    max_dist = (initial_power - receiver_sensitivity) / atten
    print(f"{media:20s}: {max_dist:6.1f} km")
```

---

## 5. Transmission Media: Unguided

Unguided (wireless) transmission media transmit signals through the air without physical cables.

### 5.1 Radio Waves

**Frequency Range**: 3 kHz to 300 GHz

**Characteristics**:
- Omnidirectional (propagate in all directions)
- Can penetrate walls
- Susceptible to interference

**Applications**: Wi-Fi, Bluetooth, cellular networks, radio broadcasting

### 5.2 Microwave Transmission

**Frequency Range**: 1 GHz to 300 GHz

**Characteristics**:
- Line-of-sight transmission
- High bandwidth capacity
- Requires directional antennas
- Susceptible to weather interference

**Applications**: Point-to-point communication, satellite links, cellular backhaul

**Types**:
- **Terrestrial Microwave**: Towers placed within line-of-sight (~50 km apart)
- **Satellite Microwave**: Communication via satellites in orbit

### 5.3 Infrared

**Frequency Range**: 300 GHz to 400 THz

**Characteristics**:
- Line-of-sight or reflected
- Cannot penetrate walls
- Low interference from other sources

**Applications**: TV remote controls, short-range communication (IrDA), indoor wireless networks

### 5.4 Satellite Communication

**Components**:
- **Uplink**: Signal from Earth to satellite
- **Downlink**: Signal from satellite to Earth
- **Transponder**: Receives, amplifies, and retransmits signals

**Orbital Types**:
| Orbit Type | Altitude | Latency | Coverage |
|------------|----------|---------|----------|
| LEO | 500-2000 km | Low (~20-25 ms) | Global, requires many satellites |
| MEO | 2000-35,000 km | Medium (~70-80 ms) | GPS, navigation |
| GEO | 35,786 km | High (~240 ms) | Weather, communications |

---

## 6. Signal Impairments

### 6.1 Attenuation

**Attenuation** is the gradual loss of signal strength as it travels through a medium. Measured in decibels (dB).

**Causes**:
- Resistance in copper cables
- Absorption in fiber optic cables
- Radiation in wireless media

**Formula**:
```
Attenuation (dB) = 10 × log₁₀(Power_out / Power_in)
```

### 6.2 Distortion

**Distortion** occurs when the signal shape changes due to different frequency components traveling at different speeds.

**Types**:
- **Attenuation Distortion**: Different frequencies attenuated differently
- **Phase Distortion**: Different frequencies delayed differently

### 6.3 Noise

**Noise** is unwanted energy that interferes with the original signal.

**Types**:
1. **Thermal Noise**: Caused by random electron movement (present in all electronic devices)
2. **Intermodulation Noise**: Produced when signals share a medium
3. **Crosstalk**: Unwanted coupling between nearby channels
4. **Impulse Noise**: Short, high-intensity spikes (caused by switches, lightning)

### 6.4 Signal-to-Noise Ratio (SNR)

**SNR** is the ratio of signal power to noise power, measured in decibels.

```
SNR (dB) = 10 × log₁₀(Signal_Power / Noise_Power)
```

**Higher SNR** = better signal quality = lower error rate

**Example**: If signal power is 100 mW and noise power is 0.1 mW:
```
SNR = 10 × log₁₀(100/0.1) = 10 × log₁₀(1000) = 10 × 3 = 30 dB
```

---

## 7. Modulation and Multiplexing

### 7.1 Modulation

**Modulation** is the process of modifying a carrier signal to encode information. It allows low-frequency signals to be transmitted over high-frequency carriers.

**Reasons for Modulation**:
- Enables long-distance transmission
- Allows multiple signals on same medium (frequency division)
- Matches antenna size to frequency
- Provides frequency allocation

**Types of Modulation**:

| Type | Parameter Modified | Application |
|------|---------------------|-------------|
| AM (Amplitude Modulation) | Amplitude | Radio broadcasting |
| FM (Frequency Modulation) | Frequency | FM radio, TV audio |
| PM (Phase Modulation) | Phase | Digital communication |
| ASK (Amplitude Shift Keying) | Amplitude | Digital (0/1) |
| FSK (Frequency Shift Keying) | Frequency | Dial-up modems |
| PSK (Phase Shift Keying) | Phase | Wi-Fi, cellular |

### 7.2 Multiplexing

**Multiplexing** combines multiple signals into one for efficient transmission.

**Types**:

1. **Frequency Division Multiplexing (FDM)**: Different signals assigned different frequency bands
2. **Time Division Multiplexing (TDM)**: Different signals assigned time slots
3. **Wavelength Division Multiplexing (WDM)**: Multiple light wavelengths on fiber

---

## 8. Delhi University Syllabus Context

This content aligns with the **Ge6A Computer Networks** paper under the NEP 2024 curriculum for BSc Physical Science (CS). Key topics from the syllabus covered include:

- Signal types and properties (analog/digital, amplitude, frequency, phase)
- Guided transmission media (twisted pair, coaxial, fiber optic)
- Unguided transmission media (radio, microwave, infrared, satellite)
- Signal impairments (attenuation, distortion, noise)
- Bandwidth and capacity calculations
- Modulation basics

---

## 9. Practice Questions

### Multiple Choice Questions

**Level 1: Easy**

1. Which transmission medium provides the highest bandwidth?
   - A) Twisted Pair Cable
   - B) Coaxial Cable
   - C) Fiber Optic Cable
   - D) Radio Waves
   - **Answer: C**

2. The process of combining multiple signals into one channel is called:
   - A) Modulation
   - B) Multiplexing
   - C) Encoding
   - D) Decoding
   - **Answer: B**

**Level 2: Medium**

3. According to Shannon's theorem, channel capacity depends on:
   - A) Only bandwidth
   - B) Only SNR
   - C) Bandwidth and SNR
   - D) Distance and SNR
   - **Answer: C**

4. In a sine wave, the phase shift of 180 degrees represents:
   - A) No change
   - B) Quarter cycle shift
   - C) Half cycle inversion
   - D) Full cycle repetition
   - **Answer: C**

5. Which type of fiber optic cable is used for long-distance communication?
   - A) Multi-mode fiber
   - B) Single-mode fiber
   - C) Plastic fiber
   - D) Coaxial fiber
   - **Answer: B**

**Level 3: Challenging**

6. A signal with frequency 1 GHz travels through a medium with attenuation of 3 dB/km. If the initial power is 100 mW, calculate the power after 5 km transmission (in mW):
   - A) 50 mW
   - B) 10 mW
   - C) 5 mW
   - D) 1 mW
   - **Answer: C**
   
   *Solution: Attenuation = 5 × 3 = 15 dB. Power ratio = 10^(-15/10) = 0.0316. Power = 100 × 0.0316 ≈ 3.16 mW ≈ 5 mW (closest option)*
   
   **Key**: C

7. Which modulation technique changes the phase of the carrier signal to represent digital data?
   - A) ASK
   - B) FSK
   - C) PSK
   - D) QAM
   - **Answer: C**

8. A UTP Cat6 cable can carry signals up to what maximum distance without a repeater?
   - A) 50 meters
   - B) 100 meters
   - C) 185 meters
   - D) 500 meters
   - **Answer: B**

9. In GPS systems, which orbital type is used?
   - A) GEO
   - B) MEO
   - C) LEO
   - D) Polar
   - **Answer: B**

10. The noise caused by random thermal motion of electrons is called:
    - A) White noise
    - B) Thermal noise
    - C) Shot noise
    - D) Flicker noise
    - **Answer: B**

### Flashcards

**FC-1**: What is the difference between guided and unguided transmission media?
- **Answer**: Guided media (copper cables, fiber optics) provide a physical path for signals, while unguided media (wireless) transmit signals through the air without physical connections.

**FC-2**: Define bandwidth in the context of network communications.
- **Answer**: Bandwidth is the range of frequencies a transmission medium can carry, measured in Hz. It determines the maximum data rate that can be transmitted.

**FC-3**: Why is modulation used in communication systems?
- **Answer**: Modulation allows low-frequency information signals to be transmitted over high-frequency carrier waves, enabling long-distance transmission, frequency allocation for multiple channels, and efficient antenna design.

**FC-4**: What is attenuation and how is it measured?
- **Answer**: Attenuation is the gradual loss of signal strength as it travels through a medium. It is measured in decibels (dB) using the formula: Attenuation (dB) = 10 × log₁₀(Power_out / Power_in).

---

## 10. Key Takeaways

1. **Signals** are the foundation of all network communication, with **analog signals** being continuous and **digital signals** representing data as binary values.

2. **Key signal properties**—**amplitude**, **frequency**, **phase**, and **bandwidth**—determine how data is transmitted and how much data can be sent.

3. **Guided transmission media** include:
   - **Twisted Pair Cable**: Inexpensive, used in LANs, limited distance (~100m)
   - **Coaxial Cable**: Better shielding, used in cable TV and older Ethernet
   - **Fiber Optic Cable**: Highest bandwidth, longest distances, immune to EMI

4. **Unguided transmission media** include radio waves, microwaves, infrared, and satellite communication—each with specific frequency ranges and applications.

5. **Signal impairments**—attenuation, distortion, and noise—degrade signal quality. **SNR (Signal-to-Noise Ratio)** is critical for determining channel capacity.

6. **Modulation** enables information to be encoded on carrier signals, while **multiplexing** allows multiple signals to share the same transmission medium.

7. **Nyquist Theorem** and **Shannon's Capacity** formula provide theoretical limits for data transmission based on bandwidth and noise.

---

*Study Material prepared for Delhi University NEP 2024 - Ge6A Computer Networks*