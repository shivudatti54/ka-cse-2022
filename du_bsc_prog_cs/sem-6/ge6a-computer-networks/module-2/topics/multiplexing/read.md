# Comprehensive Study Material: Multiplexing

## Subject: Ge6A Computer Networks | BSc Physical Science (CS) - Delhi University, NEP 2024

---

## 1. Introduction

### What is Multiplexing?

**Multiplexing** is a fundamental networking concept that allows multiple signals or data streams to be combined and transmitted simultaneously over a single communication channel. At its core, multiplexing addresses a critical problem in communication systems: how to efficiently utilize limited bandwidth while serving multiple users or applications concurrently.

Think of a highway during rush hour—without lanes and traffic management systems, chaos would ensue. Similarly, without multiplexing, communication channels would become congested, inefficient, and costly. Multiplexing acts as the "traffic controller" of the networking world, enabling efficient bandwidth utilization by sharing a single transmission medium among multiple signals.

### Real-World Relevance

In today's hyper-connected world, multiplexing is everywhere:

- **Telecommunications**: When you make a phone call while browsing the internet on your smartphone, multiplexing allows both voice and data to travel simultaneously over the same cellular connection.
- **Television Broadcasting**: Hundreds of TV channels are transmitted through a single cable or satellite link using frequency division multiplexing.
- **Internet Connectivity**: When multiple devices in your home share a single Wi-Fi router, multiplexing techniques ensure each device gets its fair share of the bandwidth.
- **Fiber Optic Communications**: Modern internet backbones use wavelength division multiplexing to transmit terabits of data per second through a single optical fiber.
- **Radio Broadcasting**: Multiple radio stations broadcast simultaneously on different frequencies, all captured by your radio receiver through FDM.

---

## 2. Fundamentals of Multiplexing

### The Basic Principle

The fundamental concept behind multiplexing can be broken down into two key operations:

1. **Multiplexing (MUX)**: At the transmitter end, multiple independent signals are combined into a single composite signal for transmission over a shared medium.

2. **Demultiplexing (DEMUX)**: At the receiver end, the composite signal is separated back into its original individual signals.

```
[Signal 1] ──────┐
[Signal 2] ──────┼──→ [MUX] ──→ [Transmission Channel] ──→ [DEMUX] ──┬──→ [Signal 1]
[Signal 3] ──────┘                                              ├──→ [Signal 2]
                                                                   └──→ [Signal 3]
```

### Why Multiplexing Matters

- **Bandwidth Efficiency**: Maximizes the use of available bandwidth
- **Cost Reduction**: Reduces the number of physical channels required
- **Infrastructure Savings**: Minimizes wiring and infrastructure costs
- **Scalability**: Allows easy addition of more channels
- **Quality of Service**: Enables priority-based transmission

---

## 3. Types of Multiplexing

### 3.1 Frequency Division Multiplexing (FDM)

#### Concept

**Frequency Division Multiplexing** is an analog multiplexing technique that divides the total available bandwidth of a communication channel into multiple frequency bands. Each signal is assigned a unique, non-overlapping frequency band and all signals are transmitted simultaneously.

#### How It Works

1. Each input signal is modulated onto a different carrier frequency
2. Guard bands (unused frequency gaps) separate the channels to prevent interference
3. All modulated signals are combined and transmitted together
4. At the receiver, filters separate the frequency bands
5. Demodulation extracts the original signals

#### Mathematical Representation

If the total bandwidth is **B** Hz and we have **n** channels with **g** Hz guard bands:

```
Effective bandwidth per channel = (B - (n+1) × g) / n
```

#### Key Characteristics

| Property | Value |
|----------|-------|
| Type | Analog |
| Signal Separation | Filters |
| Guard Bands | Required |
| Synchronization | Not required |
| Complexity | Moderate |

#### Practical Example: FM Radio Broadcasting

FM radio is a classic example of FDM:

- FM radio frequencies range from 88 MHz to 108 MHz
- Each radio station occupies approximately 200 kHz
- Stations are separated by guard bands of 400 kHz
- Your radio tuner acts as a demultiplexer, selecting the desired frequency band

```python
# Python simulation of FDM concept
import numpy as np
import matplotlib.pyplot as plt

def fdm_simulation():
    """
    Simulating Frequency Division Multiplexing
    Each signal is modulated to a different frequency band
    """
    # Parameters
    duration = 0.01  # seconds
    sample_rate = 10000  # samples per second
    
    # Generate three different input signals (baseband)
    t = np.linspace(0, duration, int(sample_rate * duration))
    signal1 = np.sin(2 * np.pi * 100 * t)  # 100 Hz signal
    signal2 = np.sin(2 * np.pi * 200 * t)  # 200 Hz signal
    signal3 = np.sin(2 * np.pi * 300 * t)  # 300 Hz signal
    
    # Carrier frequencies for FDM
    carrier1 = 1000  # 1 kHz
    carrier2 = 2000  # 2 kHz
    carrier3 = 3000  # 3 kHz
    
    # Modulate signals to their frequency bands
    modulated1 = signal1 * np.cos(2 * np.pi * carrier1 * t)
    modulated2 = signal2 * np.cos(2 * np.pi * carrier2 * t)
    modulated3 = signal3 * np.cos(2 * np.pi * carrier3 * t)
    
    # Combine all signals (Multiplexing)
    multiplexed = modulated1 + modulated2 + modulated3
    
    return t, signal1, signal2, signal3, multiplexed

# Note: This is a conceptual demonstration
# In real systems, FDM requires bandpass filters and more complex modulation
```

---

### 3.2 Time Division Multiplexing (TDM)

#### Concept

**Time Division Multiplexing** is a digital multiplexing technique that divides the transmission channel into multiple time slots. Each signal is assigned a specific time slot and transmits its data in bursts during that allocated time. All signals share the same frequency band but at different times.

#### Types of TDM

1. **Synchronous TDM**: Fixed, pre-assigned time slots regardless of whether the source has data to send
2. **Asynchronous TDM**: Dynamic time slot allocation based on data availability
3. **Statistical TDM**: More efficient, slots allocated only when data is present

#### How It Works

1. Each input signal is sampled and converted to digital format
2. Time is divided into frames, and each frame into slots
3. Each input gets exactly one slot per frame
4. The multiplexer scans all inputs in sequence, sampling each during its slot
5. At the receiver, the demultiplexer extracts samples based on timing
6. Reconstructed signals are converted back to analog

#### Mathematical Representation

If the sample rate is **S** samples/second and we have **n** channels:

```
Frame duration = n / S seconds
Bits per frame = n × bits per sample
Effective bit rate per channel = Total bit rate / n
```

#### Key Characteristics

| Property | Value |
|----------|-------|
| Type | Digital |
| Signal Separation | Time slots |
| Guard Time | Required (timing overhead) |
| Synchronization | Required |
| Complexity | High (timing critical) |

#### Practical Example: Digital Telephone Systems

TDM is extensively used in digital telephone networks:

- **DS0**: 64 Kbps (single voice channel, 8-bit samples at 8 kHz)
- **T1 (North America)**: 24 DS0 channels = 1.544 Mbps
- **E1 (Europe)**: 30 voice channels + 2 signaling = 2.048 Mbps
- **T3**: 28 T1 channels = 44.736 Mbps

```python
# Python simulation of TDM
import numpy as np

def tdm_simulation():
    """
    Simulating Time Division Multiplexing
    Multiple digital signals share time slots
    """
    # Parameters
    num_channels = 4
    samples_per_slot = 8
    total_samples = num_channels * samples_per_slot
    
    # Generate different input signals as digital samples
    # Each channel gets a fixed number of samples per frame
    channel_data = []
    for i in range(num_channels):
        # Generate random 8-bit samples for each channel
        samples = np.random.randint(0, 256, samples_per_slot)
        channel_data.append(samples)
    
    # Multiplexing: Interleave samples from all channels
    multiplexed_frame = np.zeros(total_samples, dtype=int)
    for i in range(num_channels):
        multiplexed_frame[i::num_channels] = channel_data[i]
    
    # Demultiplexing: Extract samples back to each channel
    received_data = []
    for i in range(num_channels):
        channel_samples = multiplexed_frame[i::num_channels]
        received_data.append(channel_samples)
    
    return channel_data, multiplexed_frame, received_data

# Example usage
original, multiplexed, received = tdm_simulation()

print("Original Channel Data:")
for i, data in enumerate(original):
    print(f"  Channel {i+1}: {list(data)}")

print(f"\nMultiplexed Frame: {list(multiplexed)}")

print("\nReceived Channel Data:")
for i, data in enumerate(received):
    print(f"  Channel {i+1}: {list(data)}")
```

---

### 3.3 Wavelength Division Multiplexing (WDM)

#### Concept

**Wavelength Division Multiplexing** is specifically designed for fiber optic communications. It combines multiple optical signals (each carrying data) at different wavelengths (colors) of light onto a single optical fiber. Think of it as the fiber optic equivalent of FDM, but using light wavelengths instead of radio frequencies.

#### Types of WDM

1. **Coarse WDM (CWDM)**: 18 channels with 20 nm spacing (used for short distances)
2. **Dense WDM (DWDM)**: 80+ channels with 0.4 nm or less spacing (used for long-haul)
3. **Ultra-Dense WDM (UDWDM)**: Extremely close channel spacing for maximum capacity

#### How It Works

1. Multiple laser sources generate light at different wavelengths
2. An optical multiplexer combines these optical signals
3. The combined signal travels through a single fiber
4. An optical demultiplexer separates the wavelengths
5. Photodetectors convert each wavelength back to electrical signals

#### Mathematical Representation

If we have **n** wavelengths with channel spacing **Δλ** and bandwidth **B** per channel:

```
Total capacity = n × B
Minimum wavelength spacing = Δλ (to avoid crosstalk)
Operating wavelength range = λ_min to λ_max
```

#### Key Characteristics

| Property | Value |
|----------|-------|
| Type | Optical Analog |
| Signal Separation | Prisms/gratings |
| Guard Band | Wavelength guard band |
| Synchronization | Not required |
| Capacity | Extremely high (Terabits/s) |

#### Practical Example: Internet Backbone

Modern internet backbone cables use DWDM:

```
Example: 80-channel DWDM system
- Each wavelength carries 100 Gbps
- Total capacity: 80 × 100 Gbps = 8 Tbps
- Transmission distance: 80-100 km without regeneration
- Each fiber pair can carry multiple terabits per second
```

---

### 3.4 Code Division Multiplexing (CDM) / CDMA

#### Concept

**Code Division Multiplexing**, also known as **Code Division Multiple Access (CDMA)**, is a spread-spectrum technique where all users transmit simultaneously in the same frequency band. Each user is assigned a unique code (spreading code) that distinguishes their signal from others.

#### How It Works

1. Each user is assigned a unique orthogonal code sequence
2. The data signal is multiplied by the spreading code (spreading)
3. All users transmit on the same frequency simultaneously
4. At the receiver, the signal is multiplied by the same code (despreading)
5. Only the intended signal is recovered; others appear as noise

#### Mathematical Representation

**Spreading Process:**
```
Transmitted Signal S(t) = Σ [d_i(t) × c_i(t)]
```
Where:
- d_i(t) = data signal of user i
- c_i(t) = spreading code of user i

**Orthogonality Condition:**
```
∫ c_i(t) × c_j(t) dt = 0  (for i ≠ j)
∫ c_i(t) × c_i(t) dt = 1
```

**Processing Gain:**
```
PG = Chip Rate / Data Rate = B_transmitted / B_data
```

#### Key Characteristics

| Property | Value |
|----------|-------|
| Type | Digital/Spread Spectrum |
| Signal Separation | Code correlation |
| Frequency Band | Single shared band |
| Capacity | Limited by code orthogonality |
| Security | Inherently secure (noise-like) |

#### Practical Example: Cellular Networks (3G)

CDMA was the foundation of 3G cellular networks:

- **Qualcomm** developed the CDMA standard used worldwide
- Each user receives a unique 64-bit Walsh code
- Multiple users share the same 1.25 MHz channel
- Soft handoff capability (seamless switching between towers)

```python
# Python simulation of CDMA
import numpy as np

def cdma_simulation():
    """
    Simulating Code Division Multiple Access (CDMA)
    """
    # Parameters
    num_users = 4
    data_bits = 8
    chip_length = 8  # Spreading factor (processing gain)
    
    # Generate orthogonal spreading codes using Walsh-Hadamard matrix
    def hadamard(n):
        """Generate Walsh-Hadamard matrix of order n"""
        if n == 1:
            return np.array([[1]])
        else:
            H_n_1 = hadamard(n // 2)
            return np.vstack([
                np.hstack([H_n_1, H_n_1]),
                np.hstack([H_n_1, -H_n_1])
            ])
    
    # Get spreading codes (rows of Hadamard matrix)
    codes = hadamard(4)  # 4x4 matrix for 4 users
    
    # Generate random data for each user
    np.random.seed(42)
    user_data = []
    for i in range(num_users):
        data = np.random.randint(0, 2, data_bits)  # Random 0/1 data
        # Convert 0 to -1 for bipolar representation
        data = 2 * data - 1
        user_data.append(data)
    
    # Spread each user's data
    spread_signals = []
    for i in range(num_users):
        # Repeat each data bit 'chip_length' times
        spread = np.repeat(user_data[i], chip_length)
        # Multiply by spreading code (tile the code for the data length)
        code_repeated = np.tile(codes[i], data_bits)
        spread_signal = spread * code_repeated
        spread_signals.append(spread_signal)
    
    # Combine all spread signals (multiplexing)
    # All users transmit simultaneously in the same channel
    combined_signal = np.sum(spread_signals, axis=0)
    
    # Demodulate: Extract each user's signal using correlation
    received_data = []
    for i in range(num_users):
        code_repeated = np.tile(codes[i], data_bits)
        # Correlate with user's code and despread
        despread = combined_signal * code_repeated
        # Integrate over each bit period
        bit_values = np.sum(spread.reshape(data_bits, chip_length), axis=1)
        # Decision: positive = 1, negative = 0
        received_bit = (bit_values > 0).astype(int)
        received_data.append(received_bit)
    
    return user_data, codes, received_data

# Run simulation
original_data, codes, received = cdma_simulation()

print("Spreading Codes (Walsh-Hadamard):")
print(codes)

print("\nOriginal Data vs Received Data:")
for i in range(4):
    original = (original_data[i] + 1) // 2  # Convert back to 0/1
    received_bits = received[i]
    match = "✓" if np.array_equal(original, received_bits) else "✗"
    print(f"  User {i+1}: {list(original)} → {list(received_bits)} {match}")
```

---

## 4. Comparative Analysis

### Comparison Table

| Feature | FDM | TDM | WDM | CDMA |
|---------|-----|-----|-----|------|
| **Type** | Analog | Digital | Optical | Digital |
| **Domain** | Frequency | Time | Wavelength | Code |
| **Separation** | Filters | Time slots | Prisms/gratings | Correlation |
| **Guard** | Guard bands | Guard time | Wavelength gap | Processing gain |
| **Sync Required** | No | Yes | No | Yes |
| **Flexibility** | Low | Medium | Low | High |
| **Complexity** | Low | High | Medium | High |
| **Typical Application** | Radio/TV | Telephone | Fiber optics | Cellular |

### When to Use Each Technique

**Use FDM when:**
- Transmitting analog signals
- Operating in environments with fixed bandwidth
- Simplicity is prioritized over efficiency
- Broadcasting (radio, television)

**Use TDM when:**
- Working with digital signals
- Bandwidth is limited but high data rates needed
- Precise timing control is possible
- Digital telephone systems

**Use WDM when:**
- Maximizing fiber optic capacity
- Long-haul communication
- Very high bandwidth requirements
- Modern internet backbone

**Use CDMA when:**
- Security is important
- Variable number of users
- Soft handoff needed (cellular)
- Spread spectrum operation required

---

## 5. Mathematical Concepts and Formulas

### Bandwidth Calculations

#### FDM Bandwidth Efficiency

```
η_FDM = (n × B_c) / B_total

Where:
- n = number of channels
- B_c = bandwidth per channel
- B_total = total bandwidth including guard bands
```

**Example Problem:**
A communication system has a total bandwidth of 100 MHz and uses FDM to carry 10 voice channels. Each channel requires 3 MHz with 1 MHz guard bands. Calculate the bandwidth efficiency.

**Solution:**
```
Guard bands total = 11 × 1 MHz = 11 MHz
Used bandwidth = 10 × 3 MHz = 30 MHz
Total utilized = 30 + 11 = 41 MHz

Bandwidth efficiency = (10 × 3) / 100 = 30%
Or considering guard bands: (30) / 100 = 30%
```

#### TDM Frame Efficiency

```
η_TDM = (n × T_s) / T_frame

Where:
- n = number of channels
- T_s = time slot duration
- T_frame = total frame time
```

#### CDMA Processing Gain

```
PG = Chip Rate / Data Rate = B_wideband / B_baseband

Also expressed in dB:
PG(dB) = 10 × log10(B_wideband / B_baseband)
```

### Numerical Problems

#### Problem 1: TDM Frame Calculation

**Question:** A TDM system multiplexes 24 digital voice channels. Each voice sample is 8 bits and the sampling rate is 8 kHz. Calculate:
a) The bit rate of each voice channel
b) The total frame time
c) The data rate of the multiplexed output

**Solution:**
```
a) Bit rate per channel = 8 bits × 8 kHz = 64 Kbps

b) For each voice channel:
   Samples per second = 8,000
   Samples per frame (assuming 1 sample per frame) = 1
   Frame rate = 8,000 frames/second
   Frame time = 1/8000 = 0.125 ms = 125 μs

c) Total data rate = 24 × 64 Kbps = 1.536 Mbps
   (This is the T1 standard)
```

#### Problem 2: FDM Channel Capacity

**Question:** An FDM system has a total bandwidth of 12 MHz. It must carry 3 video channels, each requiring 3 MHz. Calculate:
a) The total bandwidth required with 0.5 MHz guard bands
b) The unused bandwidth

**Solution:**
```
a) With guard bands:
   Total bandwidth = (3 × 3) + (4 × 0.5)
                   = 9 + 2
                   = 11 MHz

b) Unused bandwidth = 12 - 11 = 1 MHz
```

#### Problem 3: CDMA Processing Gain

**Question:** A CDMA system uses a chip rate of 3.84 Mcps (megachips per second) and transmits data at 9.6 Kbps. Calculate:
a) The processing gain
b) The processing gain in dB

**Solution:**
```
a) Processing Gain = 3,840,000 / 9,600 = 400

b) PG(dB) = 10 × log10(400)
          = 10 × 2.602
          = 26.02 dB
```

---

## 6. Practical Applications

### 1. Television Cable Systems

Cable TV uses FDM to bundle hundreds of channels:

- **Bandwidth**: 50 MHz to 1000 MHz (typical cable spectrum)
- **Channel width**: 6 MHz per channel (NTSC)
- **Modulation**: QAM (quadrature amplitude modulation)
- **Example**: A cable system with 860 MHz bandwidth can carry approximately 143 channels

### 2. Digital Audio Broadcasting (DAB)

- Uses OFDM (Orthogonal FDM) variant
- Multiple audio streams multiplexed in frequency domain
- Error correction added for robust reception

### 3. Satellite Communication

- Multiple transponders (FDM) on different frequencies
- Each transponder handles multiple carriers
- Downlink to Earth covers vast geographic areas

### 4. GPON (Gigabit Passive Optical Network)

- Uses TDM for upstream (OLT to ONUs)
- WDM for bidirectional communication
- Single fiber serves 32-64 users

### 5. 4G/5G Cellular Networks

- Combines TDD (Time Division Duplex) and FDD (Frequency Division Duplex)
- OFDMA for multiple access
- Carrier aggregation (combining multiple frequency bands)

---

## 7. Multiple Choice Questions (MCQs)

### Level 1: Basic Understanding

**Question 1:** What is the primary purpose of multiplexing?
- A) To increase the speed of data transmission
- B) To combine multiple signals into one for efficient transmission
- C) To compress data for storage
- D) To encrypt data for security

**Answer:** B

---

**Question 2:** In Frequency Division Multiplexing, signals are separated using:
- A) Time slots
- B) Filters
- C) Codes
- D) Wavelengths

**Answer:** B

---

### Level 2: Intermediate

**Question 3:** In a TDM system with 8 channels, each transmitting 4 Kbps, what is the total data rate of the multiplexed signal?
- A) 4 Kbps
- B) 8 Kbps
- C) 32 Kbps
- D) 64 Kbps

**Answer:** C (8 × 4 = 32 Kbps)

---

**Question 4:** Which multiplexing technique uses orthogonal codes for signal separation?
- A) FDM
- B) TDM
- C) WDM
- D) CDMA

**Answer:** D

---

**Question 5:** In WDM, the signals are separated using:
- A) Bandpass filters
- B) Time slots
- C) Prisms or diffraction gratings
- D) Correlators

**Answer:** C

---

### Level 3: Advanced/Challenging

**Question 6:** A CDMA system has a chip rate of 3.84 Mcps and a data rate of 9600 bps. What is the processing gain?
- A) 40
- B) 400
- C) 4000
- D) 40000

**Answer:** B (Processing Gain = 3,840,000 / 9,600 = 400)

---

**Question 7:** In synchronous TDM, if a frame contains 10 time slots and each time slot is 8 bits, with a frame rate of 1000 frames/second, what is the total data rate?
- A) 8 Kbps
- B) 10 Kbps
- C) 80 Kbps
- D) 1000 Kbps

**Answer:** C (10 slots × 8 bits × 1000 frames = 80,000 bps = 80 Kbps)

---

**Question 8:** Which of the following is NOT an advantage of WDM in fiber optic communications?
- A) Extremely high capacity
- B) Low attenuation over long distances
- C) No need for optical-electrical-optical conversion at intermediate points
- D) Works with existing copper infrastructure

**Answer:** D (WDM specifically requires fiber optic cables)

---

**Question 9:** A telephone company wants to carry 30 voice channels using TDM. Each voice channel requires 64 Kbps. What is the minimum data rate needed?
- A) 30 × 64 Kbps = 1.92 Mbps
- B) 32 × 64 Kbps = 2.048 Mbps (E1 standard)
- C) 24 × 64 Kbps = 1.536 Mbps (T1 standard)
- D) 64 × 64 Kbps = 4.096 Mbps

**Answer:** B (The E1 standard uses 32 slots: 30 for voice, 2 for framing/synchronization)

---

**Question 10:** In FDM, guard bands are necessary to:
- A) Increase the bandwidth of each channel
- B) Prevent interference between adjacent channels
- C) Allow for frequency modulation
- D) Enable digital transmission

**Answer:** B

---

## 8. Key Takeaways

### Core Concepts

1. **Multiplexing** is the process of combining multiple signals into a single transmission medium, while demultiplexing separates them at the receiver.

2. **FDM (Frequency Division Multiplexing)** divides bandwidth into frequency bands—ideal for analog signals and broadcasting applications.

3. **TDM (Time Division Multiplexing)** allocates time slots to different signals—fundamental to digital telephone systems and digital communications.

4. **WDM (Wavelength Division Multiplexing)** is the optical equivalent of FDM, enabling terabit/s capacities in modern fiber optic networks.

5. **CDMA (Code Division Multiple Access)** uses unique codes for user separation—a spread-spectrum technique used in 3G cellular networks.

### Important Formulas to Remember

- **FDM Efficiency**: η = (n × B_c) / B_total
- **TDM Data Rate**: R_total = n × R_channel
- **CDMA Processing Gain**: PG = Chip Rate / Data Rate
- **WDM Capacity**: C_total = n × B_per_wavelength

### Practical Insights

- **Delhi University Syllabus**: This topic covers fundamental networking concepts essential for understanding data transmission, communication systems, and network design.
- **Career Applications**: Understanding multiplexing is crucial for careers in telecommunications, network engineering, and wireless communications.
- **Future Trends**: As data demands grow, WDM and its advanced variants (DWDM, UDWDM) will continue to power global internet infrastructure.

### Common Pitfalls to Avoid

- Don't confuse FDM with TDM—they operate in different domains (frequency vs. time)
- Remember that TDM requires strict synchronization while FDM does not
- Understand that guard bands in FDM and guard times in TDM serve the same purpose (prevent interference) but in different domains

---

## References for Further Study

1. **Textbook**: "Computer Networking: A Top-Down Approach" by Kurose & Ross
2. **Delhi University Syllabus**: Ge6A Computer Networks, NEP 2024
3. **Standards**: ITU-T recommendations for TDM (G.703, G.704), IEEE 802 for wireless
4. **Advanced Topics**: OFDM, SCPC, FDMA in satellite communications

---

*End of Study Material*