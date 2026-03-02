# Multiplexing: FDM, TDM, and WDM

## Comprehensive Study Material for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction to Multiplexing](#introduction-to-multiplexing)
2. [Frequency Division Multiplexing (FDM)](#frequency-division-multiplexing-fdm)
3. [Time Division Multiplexing (TDM)](#time-division-multiplexing-tdm)
4. [Wavelength Division Multiplexing (WDM)](#wavelength-division-multiplexing-wdm)
5. [Comparative Analysis: FDM vs TDM vs WDM](#comparative-analysis-fdm-vs-tdm-vs-wdm)
6. [Real-World Applications](#real-world-applications)
7. [Code Examples](#code-examples)
8. [Multiple Choice Questions (MCQs)](#multiple-choice-questions-mcqs)
9. [Flashcards for Quick Revision](#flashcards-for-quick-revision)
10. [Key Takeaways](#key-takeaways)

---

## Introduction to Multiplexing

### What is Multiplexing?

**Multiplexing** is a fundamental technique in computer networks and telecommunications that allows multiple signals or data streams to be combined into a single transmission medium or channel. The primary goal is to maximize the efficient use of bandwidth and reduce infrastructure costs by sharing a single communication path among multiple users or signals.

### Why is Multiplexing Important?

In the modern digital world, the demand for communication bandwidth continues to grow exponentially. Without multiplexing, each communication channel would require its own dedicated physical medium, which would be:

- **Economically inefficient**: Requires more cables, fiber optics, or wireless frequencies
- **Practically impossible**: Limited availability of electromagnetic spectrum
- **Wasteful**: Most channels remain underutilized for much of the time

Multiplexing solves these problems by enabling:
- Simultaneous transmission of multiple signals over one medium
- Optimal utilization of available bandwidth
- Cost-effective infrastructure deployment
- Scalability for growing network demands

### Real-World Relevance

Consider a typical telephone exchange: thousands of voice calls must be transmitted over a limited number of fiber optic cables connecting different cities. Without multiplexing, each call would require a dedicated physical line. Multiplexing makes it possible to bundle hundreds or thousands of calls into a single high-capacity link.

Similarly, when you stream a video while downloading a file and browsing the internet on your home Wi-Fi, multiple data streams share the same network bandwidth through multiplexing techniques implemented in network routers and switches.

---

## Frequency Division Multiplexing (FDM)

### Definition and Concept

**Frequency Division Multiplexing (FDM)** is an analog multiplexing technique that divides the total available bandwidth of a communication channel into multiple non-overlapping frequency bands. Each signal is assigned a unique frequency band within the shared medium, and all signals are transmitted simultaneously without interfering with each other.

### How FDM Works

In FDM, each signal is modulated onto a different carrier frequency. These modulated signals are then combined using a device called a **multiplexer (MUX)** at the transmitter end. At the receiver end, a **demultiplexer (DEMUX)** separates the combined signal back into individual signals based on their frequency bands.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     FDM TRANSMISSION SYSTEM                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Signal 1 ──► Modulator ──►    ┌─────────┐    ──► Demodulator ──► Signal 1
│  (f1 Hz)      (Carrier 1)      │         │        (Filter 1)         │
│                               │         │                          │
│  Signal 2 ──► Modulator ──►   │  MUX    │   ──► Demodulator ──► Signal 2
│  (f2 Hz)      (Carrier 2)      │ Channel │        (Filter 2)         │
│                               │         │                          │
│  Signal 3 ──► Modulator ──►   │         │   ──► Demodulator ──► Signal 3
│  (f3 Hz)      (Carrier 3)      └─────────┘        (Filter 3)         │
│                                                                     │
│  Frequency ─►  f1    f2    f3    f4    f5    f6    f7    f8   ─►    │
│  Spectrum    ├──┬───┴──┬───┴──┬───┴──┬───┴──┬───┴──┬───┴────      │
│              │Band 1│Band 2│Band 3│Band 4│Band 5│Band 6│Band 7│   │
│              └───────┴───────┴───────┴───────┴───────┴─────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Components of FDM

1. **Modulator**: Converts baseband signals to passband signals using different carrier frequencies
2. **Multiplexer (MUX)**: Combines multiple modulated signals into a single composite signal
3. **Transmission Medium**: Carries the combined signal (coaxial cable, microwave link, satellite)
4. **Demultiplexer (DEMUX)**: Separates the composite signal into individual signals
5. **Bandpass Filters**: Extract specific frequency bands at the receiver

### Guard Bands

To prevent interference between adjacent channels, **guard bands** (unused frequency gaps) are introduced between frequency channels. This ensures that even if there's slight frequency drift or non-ideal filter characteristics, signals remain isolated.

### Advantages of FDM

- **Simultaneous transmission**: All signals transmit at once without waiting
- **Analog-friendly**: Works well with analog signals
- **No synchronization required**: Each channel operates independently
- **Low latency**: No time-sharing delays

### Disadvantages of FDM

- **Inefficient bandwidth usage**: Guard bands waste spectrum
- **Complex hardware**: Requires precise filters and modulators
- **Limited scalability**: Number of channels fixed by available bandwidth
- **Intermodulation distortion**: Non-linearities can create interference

### Example of FDM

**Radio Broadcasting**: AM and FM radio stations each broadcast on different frequencies within the allocated spectrum. Your radio tuner (demultiplexer) selects the specific frequency (channel) you want to listen to.

**Television Broadcasting**: Multiple TV channels are transmitted simultaneously on different frequency bands through cable or satellite.

---

## Time Division Multiplexing (TDM)

### Definition and Concept

**Time Division Multiplexing (TDM)** is a digital multiplexing technique that divides the transmission time into discrete time slots. Each signal is assigned a specific time slot during which it can transmit its data. The signals take turns using the full bandwidth of the channel, but only one at a time.

### How TDM Works

In TDM, each input signal is sampled at regular intervals, and these samples are arranged in a sequential order. The multiplexer allocates fixed time slots to each signal in a repeating pattern. At the receiver, the demultiplexer uses synchronization to extract the correct samples for each channel.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     TDM TRANSMISSION SYSTEM                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Channel 1:  [D1]    [D1]    [D1]    [D1]    [D1]                  │
│                 │       │       │       │       │                   │
│  Channel 2:     [D2]    [D2]    [D2]    [D2]    [D2]                │
│                 │       │       │       │       │                   │
│  Channel 3:       [D3]    [D3]    [D3]    [D3]    [D3]              │
│                 │       │       │       │       │                   │
│                 ▼       ▼       ▼       ▼       ▼                   │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  T1   │  T2   │  T3   │  T1   │  T2   │  T3   │  T1   │ T2 ...│   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  Frame 1      Frame 2      Frame 3      Frame 4                     │
│                                                                     │
│  After DEMUX:                                                        │
│  Channel 1:  [D1]    [D1]    [D1]    [D1]    [D1]                  │
│  Channel 2:  [D2]    [D2]    [D2]    [D2]    [D2]                  │
│  Channel 3:  [D3]    [D3]    [D3]    [D3]    [D3]                  │
└─────────────────────────────────────────────────────────────────────┘
```

### Types of TDM

#### 1. Synchronous TDM

In **Synchronous TDM**, time slots are pre-assigned to each channel regardless of whether they have data to send or not. If a channel has no data, its time slot remains empty, leading to inefficient bandwidth utilization.

#### 2. Asynchronous TDM (Statistical TDM)

**Asynchronous TDM** (also called Statistical TDM) dynamically allocates time slots based on actual data traffic. Only channels with data to send receive time slots, making more efficient use of available bandwidth. This requires additional overhead for addressing information.

#### 3. Pulse Code Modulation (PCM)

PCM is a standard format for digital audio in TDM systems. It involves:
- **Sampling**: Measuring analog signal at regular intervals
- **Quantization**: Assigning discrete amplitude values
- **Encoding**: Converting values to binary representation

### Frame Structure

A TDM frame consists of one time slot from each channel:

```
┌─────────────────────────────────────────────────────────────┐
│                    TDM FRAME STRUCTURE                      │
├─────────────────────────────────────────────────────────────┤
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐   │
│  │ CH1│ CH2│ CH3│ CH4│ CH1│ CH2│ CH3│ CH4│ CH1│ CH2│ ...│   │
│  └──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┘   │
│     │    │    │    │    │    │    │    │    │    │        │
│     └────┴────┴────┴────┴────┴────┴────┴────┴────┘        │
│     <──────────────── Frame Period ─────────────────>       │
│                                                             │
│  Frame = n time slots (n = number of channels)            │
│  Frame Time = Sum of all time slot durations               │
└─────────────────────────────────────────────────────────────┘
```

### Advantages of TDM

- **Efficient digital transmission**: Optimized for digital signals
- **Flexible**: Easy to add or remove channels
- **No guard bands**: Unlike FDM, no wasted frequency spectrum
- **Better signal quality**: Regenerative repeaters can restore signal

### Disadvantages of TDM

- **Requires synchronization**: Precise timing is critical
- **Latency**: Higher than FDM due to time-slot waiting
- **Complex circuitry**: Needs accurate clocks and buffers
- **Fixed capacity**: Each channel gets equal time regardless of need

### Example of TDM

**Digital Telephone Systems**: Traditional digital telephone switching uses TDM. Multiple voice channels are sampled, encoded, and multiplexed into a single digital stream (e.g., T1/E1 lines).

---

## Wavelength Division Multiplexing (WDM)

### Definition and Concept

**Wavelength Division Multiplexing (WDM)** is a multiplexing technique specifically designed for fiber optic communications. It combines multiple optical signals (each at a different wavelength/colour of light) onto a single fiber optic cable. WDM is essentially the optical equivalent of FDM but operates at much higher frequencies (visible and near-infrared light).

### How WDM Works

In WDM, multiple laser beams, each generating light at a different wavelength, are combined using an **optical multiplexer**. These wavelengths travel together through the fiber optic cable without interfering with each other. At the receiving end, an **optical demultiplexer** separates the wavelengths using prisms or diffraction gratings.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     WDM TRANSMISSION SYSTEM                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  λ1 (1510nm) ──►                                                         │
│                 │                                                      │
│  λ2 (1515nm) ──► │  ┌─────────────────┐   ┌─────────────────┐       │
│                 ├─►│                 │   │                 │       │
│  λ3 (1520nm) ──► │  │  Optical MUX    │──►│  Fiber Optic    │       │
│                 │  │                 │   │      Cable      │       │
│  λ4 (1525nm) ──► │  └─────────────────┘   └────────┬────────┘       │
│                                                   │                  │
│                                                   ▼                  │
│                              ┌─────────────────────────────┐         │
│                              │      Optical DEMUX          │         │
│                              └──────────────┬──────────────┘         │
│                                             │                         │
│                    ┌────────┬────────┬──────┴──────┬──────┐         │
│                    │        │        │             │      │         │
│                    ▼        ▼        ▼             ▼      ▼         │
│                  (λ1)    (λ2)    (λ3)           (λ4)   (λn)          │
│                  1510nm  1515nm  1520nm         1525nm  1530nm       │
│                                                                     │
│  Spectrum:  ◄─── 40nm ───►                                         │
│            1510nm ───────────────────────────────────► 1550nm       │
│             │   │   │   │   │   │   │   │   │   │                   │
│             └───┴───┴───┴───┴───┴───┴───┴───┴───┴─┘               │
│              λ1  λ2  λ3  λ4  λ5  λ6  λ7  λ8  λ9  λ10                │
└─────────────────────────────────────────────────────────────────────┘
```

### Types of WDM

#### 1. Coarse WDM (CWDM)

**CWDM** uses wider wavelength spacing (typically 20nm apart) and supports fewer channels (up to 18 channels) over shorter distances. It's less expensive and simpler to implement.

#### 2. Dense WDM (DWDM)

**DWDM** uses very narrow wavelength spacing (0.8nm or less) and can support 40, 80, 160, or more channels in the C-band (1530-1565nm) and L-band (1570-1610nm). It's used for long-haul, high-capacity telecommunications.

### Key Components

1. **Laser Diodes**: Generate light at specific wavelengths
2. **Optical Multiplexer**: Combines multiple wavelengths using prisms or waveguide gratings
3. **Fiber Optic Cable**: Low-loss transmission medium
4. **Optical Amplifiers**: Amplify optical signals (EDFAs - Erbium-Doped Fiber Amplifiers)
5. **Optical Demultiplexer**: Separates wavelengths using diffraction gratings

### Advantages of WDM

- **Massive bandwidth**: Each wavelength can carry multiple TDM channels
- **Protocol transparent**: Works with any digital protocol (IP, ATM, SONET/SDH)
- **Low attenuation**: Fiber optic losses are minimal
- **Future-proof**: Easy to add more wavelengths as needed

### Disadvantages of WDM

- **Expensive equipment**: Lasers, multiplexers, and demultiplexers are costly
- **Complex installation**: Requires precise alignment and tuning
- **Optical nonlinearities**: At high power, fiber nonlinear effects can cause interference

### Example of WDM

**Long-Haul Telecommunications**: A single fiber optic cable using DWDM can carry 96 wavelengths × 40 Gbps = 3.84 Tbps of data - enough for millions of phone calls simultaneously.

**Data Center Interconnects**: WDM connects different buildings or data centers within a city at very high speeds.

---

## Comparative Analysis: FDM vs TDM vs WDM

| Feature | FDM | TDM | WDM |
|---------|-----|-----|-----|
| **Type** | Analog | Digital | Optical/Analog |
| **Division Method** | Frequency | Time | Wavelength |
| **Bandwidth Efficiency** | Low (guard bands) | High | Very High |
| **Complexity** | Moderate | High (sync needed) | Very High |
| **Applications** | Radio, TV broadcasting | Telephone, digital comm | Fiber optics |
| **Latency** | Very Low | Moderate to High | Very Low |
| **Equipment Cost** | Moderate | Low to Moderate | Very High |
| **Synchronization** | Not required | Required | Not required |
| **Channel Capacity** | Fixed | Dynamic (Statistical) | Very High |
| **Interference** | Adjacent channel | Timing errors | Crosstalk |

---

## Real-World Applications

### 1. FM Radio Broadcasting
Multiple radio stations transmit simultaneously on different carrier frequencies (FDM). Your radio receiver selects the desired station.

### 2. Digital Telephone Networks
TDM is used in T1 (24 channels) and E1 (30 channels) systems to multiplex voice calls into digital streams.

### 3. Television Cable Systems
Both FDM (different channels on different frequencies) and sometimes TDM (digital cable) are used.

### 4. Internet Backbone
WDM (especially DWDM) forms the backbone of global internet infrastructure, connecting continents via undersea fiber optic cables.

### 5. Satellite Communications
FDM separates multiple uplink/downlink signals to/from satellites.

---

## Code Examples

### Example 1: Simple FDM Simulation in Python

```python
"""
FDM (Frequency Division Multiplexing) Simulation
Demonstrates how multiple signals are combined using frequency bands
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_signal(frequency, duration, sample_rate, amplitude=1.0):
    """Generate a sinusoidal signal"""
    t = np.linspace(0, duration, int(sample_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def fd multiplex_signals(signals, frequencies, sample_rate):
    """
    Combine multiple signals using FDM technique
    Each signal is modulated to a different frequency band
    """
    combined = np.zeros(len(signals[0]))
    
    for signal, freq in zip(signals, frequencies):
        # In real FDM, signals would be modulated to different carrier frequencies
        # Here we simply add them to represent the combined signal
        combined += signal
    
    return combined

# Parameters
sample_rate = 10000  # 10 kHz
duration = 0.01     # 10 ms

# Generate three different signals (representing voice/data channels)
# These would be baseband signals
t1, signal1 = generate_signal(100, duration, sample_rate, amplitude=0.5)  # 100 Hz
t2, signal2 = generate_signal(200, duration, sample_rate, amplitude=0.5)  # 200 Hz
t3, signal3 = generate_signal(300, duration, sample_rate, amplitude=0.5)  # 300 Hz

# In FDM, we would modulate each to different carrier frequencies
# For demonstration, let's simulate modulation to higher frequencies
carrier_frequencies = [1000, 2000, 3000]  # 1kHz, 2kHz, 3kHz carriers

def modulate_to_carrier(signal, carrier_freq, t):
    """Modulate baseband signal to carrier frequency"""
    carrier = np.sin(2 * np.pi * carrier_freq * t)
    return signal * carrier

# Modulate signals to their assigned frequency bands
modulated1 = modulate_to_carrier(signal1, carrier_frequencies[0], t1)
modulated2 = modulate_to_carrier(signal2, carrier_frequencies[1], t2)
modulated3 = modulate_to_carrier(signal3, carrier_frequencies[2], t3)

# Combine all modulated signals
fdm_signal = modulated1 + modulated2 + modulated3

# Visualization
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t1 * 1000, modulated1, 'b-', linewidth=0.8)
plt.title('Signal 1 - Modulated to 1 kHz')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t1 * 1000, modulated2, 'g-', linewidth=0.8)
plt.title('Signal 2 - Modulated to 2 kHz')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t1 * 1000, fdm_signal, 'r-', linewidth=0.8)
plt.title('FDM Combined Signal (All Channels)')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.savefig('fdm_simulation.png', dpi=150)
plt.show()

print("FDM Simulation Complete!")
print(f"Total bandwidth used: {carrier_frequencies[-1] - carrier_frequencies[0] + 200} Hz")
print(f"Number of channels: 3")
```

### Example 2: Simple TDM Simulation in Python

```python
"""
TDM (Time Division Multiplexing) Simulation
Demonstrates time-slot based multiplexing
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_digital_signal(bits, bit_rate, sample_rate):
    """Generate digital signal from bit sequence"""
    duration = len(bits) / bit_rate
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    samples_per_bit = int(sample_rate / bit_rate)
    signal = np.array([])
    
    for bit in bits:
        if bit == 1:
            wave = np.ones(samples_per_bit)
        else:
            wave = np.zeros(samples_per_bit)
        signal = np.concatenate([signal, wave])
    
    return t, signal

def td_multiplex(channels, samples_per_slot):
    """
    Combine multiple digital signals using TDM
    Each channel gets one time slot per frame
    """
    multiplexed = np.array([])
    
    # Number of complete frames we can form
    min_frames = min(len(ch) for ch in channels) // samples_per_slot
    
    for frame in range(min_frames):
        for channel_data in channels:
            start_idx = frame * samples_per_slot
            slot = channel_data[start_idx:start_idx + samples_per_slot]
            multiplexed = np.concatenate([multiplexed, slot])
    
    return multiplexed

def td_demultiplex(multiplexed, num_channels, samples_per_slot):
    """
    Extract individual channels from TDM signal
    """
    channels = [[] for _ in range(num_channels)]
    
    total_slots_per_frame = num_channels * samples_per_slot
    num_frames = len(multiplexed) // total_slots_per_frame
    
    for frame in range(num_frames):
        for ch in range(num_channels):
            frame_start = frame * total_slots_per_frame
            slot_start = frame_start + ch * samples_per_slot
            slot = multiplexed[slot_start:slot_start + samples_per_slot]
            channels[ch].extend(slot)
    
    return [np.array(ch) for ch in channels]

# Parameters
bit_rate = 1000  # 1 kbps
sample_rate = 10000  # 10 kHz
samples_per_bit = int(sample_rate / bit_rate)
samples_per_slot = samples_per_bit * 2  # 2 bits per time slot per channel

# Create different data patterns for 4 channels
channel1_data = [1, 0, 1, 1, 0, 0, 1, 1]  # 10110011
channel2_data = [0, 1, 0, 0, 1, 1, 0, 0]  # 01001100
channel3_data = [1, 1, 0, 1, 1, 0, 0, 1]  # 11011001
channel4_data = [0, 0, 1, 0, 0, 1, 1, 0]  # 00100110

# Generate signals for each channel
t1, ch1 = generate_digital_signal(channel1_data, bit_rate, sample_rate)
t2, ch2 = generate_digital_signal(channel2_data, bit_rate, sample_rate)
t3, ch3 = generate_digital_signal(channel3_data, bit_rate, sample_rate)
t4, ch4 = generate_digital_signal(channel4_data, bit_rate, sample_rate)

channels = [ch1, ch2, ch3, ch4]

# Perform TDM
tdm_signal = td_multiplex(channels, samples_per_slot)

# Perform TDM Demultiplexing
demux_channels = td_demultiplex(tdm_signal, 4, samples_per_slot)

# Time axis for multiplexed signal
duration = len(tdm_signal) / sample_rate
t_mux = np.linspace(0, duration, len(tdm_signal))

# Visualization
fig, axes = plt.subplots(5, 1, figsize=(14, 10))

colors = ['blue', 'green', 'orange', 'purple']

# Plot original channels
for i, (ch, color) in enumerate(zip(channels, colors)):
    t_ch = np.linspace(0, len(ch)/sample_rate, len(ch))
    axes[i].plot(t_ch * 1000, ch, color=color, linewidth=0.8)
    axes[i].set_title(f'Channel {i+1} Data: {"".join(map(str, channel1_data if i==0 else channel2_data if i==1 else channel3_data if i==2 else channel4_data))}')
    axes[i].set_xlabel('Time (ms)')
    axes[i].set_ylabel('Amplitude')
    axes[i].set_ylim(-0.2, 1.2)
    axes[i].grid(True)

# Plot multiplexed signal
axes[4].plot(t_mux * 1000, tdm_signal, 'r-', linewidth=0.8)
axes[4].set_title('TDM Multiplexed Signal (4 Channels Combined)')
axes[4].set_xlabel('Time (ms)')
axes[4].set_ylabel('Amplitude')
axes[4].set_ylim(-0.2, 1.2)
axes[4].grid(True)

# Add time slot markers
for i in range(1, 4):
    axes[4].axvline(x=i * samples_per_slot * 1000 / sample_rate, 
                     color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('tdm_simulation.png', dpi=150)
plt.show()

# Verify demultiplexed data
print("\nTDM Simulation Complete!")
print(f"Number of channels: 4")
print(f"Time slots per frame: 4")
print(f"Frame duration: {samples_per_slot * 4 / sample_rate * 1000:.2f} ms")
print(f"\nDemultiplexed Data Verification:")
for i, (orig, demod) in enumerate(zip(channels, demux_channels)):
    orig_bits = ''.join(map(str, (orig[:len(demod)] > 0.5).astype(int)))
    demod_bits = ''.join(map(str, (demod > 0.5).astype(int)))
    print(f"Channel {i+1}: Original = {orig_bits[:8]}, Demultiplexed = {demod_bits[:8]}")
```

---

## Multiple Choice Questions (MCQs)

### FDM (Frequency Division Multiplexing)

**Question 1:** What is the primary method by which FDM separates multiple signals?
- (a) Time slots
- (b) **Frequency bands** ✓
- (c) Wavelengths
- (d) IP addresses

**Question 2:** In FDM, the unused frequency gaps between channels are called:
- (a) Dead zones
- (b) **Guard bands** ✓
- (c) Safety margins
- (d) Isolation bands

**Question 3:** Which device combines multiple signals in FDM?
- (a) Modem
- (b) **Multiplexer (MUX)** ✓
- (c) Router
- (d) Switch

**Question 4:** FDM is primarily used for:
- (a) Digital signals only
- (b) **Analog signals** ✓
- (c) Only video signals
- (d) Only data signals

**Question 5:** A radio receiver selecting a particular station is an example of:
- (a) Modulation
- (b) Multiplexing
- (c) **Demultiplexing** ✓
- (d) Encoding

### TDM (Time Division Multiplexing)

**Question 6:** TDM divides the transmission medium based on:
- (a) **Time slots** ✓
- (b) Frequency
- (c) Wavelength
- (d) Voltage levels

**Question 7:** Which type of TDM allocates time slots dynamically?
- (a) Synchronous TDM
- (b) **Statistical TDM (Asynchronous)** ✓
- (c) Frequency TDM
- (d) Analog TDM

**Question 8:** In TDM, a complete cycle of time slots is called a:
- (a) Frame ✓
- (b) Packet
- (c) Block
- (d) Cycle

**Question 9:** The main disadvantage of Synchronous TDM is:
- (a) High cost
- (b) Complex hardware
- (c) **Wasted bandwidth when channels are idle** ✓
- (d) Signal interference

**Question 10:** TDM primarily works with:
- (a) Analog signals only
- (b) **Digital signals** ✓
- (c) Optical signals
- (d) Radio signals

### WDM (Wavelength Division Multiplexing)

**Question 11:** WDM is primarily used in:
- (a) Copper wire transmissions
- (b) **Fiber optic communications** ✓
- (c) Radio broadcasting
- (d) Satellite communications

**Question 12:** What is the optical equivalent of WDM?
- (a) TDM
- (b) **FDM** ✓
- (c) CDM
- (d) SDM

**Question 13:** CWDM stands for:
- (a) Central Wavelength Multiplexing
- (b) Compact Wavelength Division
- (c) **Coarse Wavelength Division Multiplexing** ✓
- (d) Combined WDM

**Question 14:** DWDM uses:
- (a) Wide wavelength spacing
- (b) **Dense wavelength spacing** ✓
- (c) No wavelength spacing
- (d) Variable spacing

**Question 15:** Which device separates wavelengths in WDM?
- (a) Optical splitter
- (b) Optical Combiner
- (c) **Optical Demultiplexer** ✓
- (d) Fiber Coupler

### Comparative Questions

**Question 16:** Which multiplexing technique has the highest bandwidth efficiency?
- (a) FDM
- (b) TDM
- (c) **WDM** ✓
- (d) All equal

**Question 17:** Which technique requires precise synchronization?
- (a) FDM
- (b) **TDM** ✓
- (c) WDM
- (d) None

**Question 18:** The telephone system traditionally uses:
- (a) FDM
- (b) **TDM** ✓
- (c) WDM
- (d) FDM and TDM

**Question 19:** For undersea fiber optic cables, which technique is used?
- (a) FDM only
- (b) TDM only
- (c) **WDM (DWDM)** ✓
- (d) FDM and TDM

**Question 20:** Guard bands are required in:
- (a) **FDM** ✓
- (b) TDM
- (c) WDM
- (d) Statistical TDM

---

## Flashcards for Quick Revision

### Flashcard Set 1: FDM

| Term | Definition |
|------|------------|
| **FDM** | Frequency Division Multiplexing - divides bandwidth into frequency bands |
| **MUX** | Multiplexer - combines multiple signals into one channel |
| **DEMUX** | Demultiplexer - separates combined signal back to individual signals |
| **Guard Band** | Unused frequency gap between channels to prevent interference |
| **Carrier Frequency** | The central frequency on which a signal is modulated |

### Flashcard Set 2: TDM

| Term | Definition |
|------|------------|
| **TDM** | Time Division Multiplexing - divides time into slots for different signals |
| **Frame** | One complete cycle containing one time slot from each channel |
| **Time Slot** | Fixed time interval allocated to each channel in TDM frame |
| **Synchronous TDM** | Fixed time slots assigned regardless of data availability |
| **Statistical TDM** | Dynamic time slot allocation based on actual data (Asynchronous TDM) |

### Flashcard Set 3: WDM

| Term | Definition |
|------|------------|
| **WDM** | Wavelength Division Multiplexing - combines multiple optical signals |
| **CWDM** | Coarse WDM - wider spacing (~20nm), fewer channels, shorter distances |
| **DWDM** | Dense WDM - narrow spacing (<1nm), many channels (40-160+), long-haul |
| **Optical Multiplexer** | Device that combines multiple wavelengths onto one fiber |
| **C-band** | Wavelength range 1530-1565nm used in DWDM systems |

### Flashcard Set 4: Key Differences

| Feature | FDM | TDM | WDM |
|---------|-----|-----|-----|
| Domain | Analog | Digital | Optical |
| Separation by | Frequency | Time | Wavelength |
| Typical Use | Radio/TV | Telephone | Fiber Optics |
| Synchronization | Not needed | Required | Not needed |

---

## Key Takeaways

1. **Multiplexing** is essential for efficient bandwidth utilization in communication networks, allowing multiple signals to share a single transmission medium.

2. **FDM (Frequency Division Multiplexing)**:
   - Divides available bandwidth into non-overlapping frequency bands
   - Each signal gets its own frequency "lane"
   - Requires guard bands to prevent interference
   - Used in analog applications: radio, TV broadcasting
   - Simple concept but inefficient spectrum use

3. **TDM (Time Division Multiplexing)**:
   - Shares time among multiple signals in fixed time slots
   - Digital technique requiring precise synchronization
   - Synchronous TDM wastes bandwidth when channels are idle
   - Statistical (Asynchronous) TDM dynamically allocates slots
   - Foundation of digital telephone systems (T1/E1)

4. **WDM (Wavelength Division Multiplexing)**:
   - Optical version of FDM using different light wavelengths
   - CWDM: Fewer channels, wider spacing, shorter distances
   - DWDM: Many channels, dense spacing, long-haul telecommunications
   - Enables massive bandwidth (terabits per second)
   - Powers global internet backbone

5. **Comparative Insights**:
   - FDM: Low latency, analog-friendly, spectrum inefficient
   - TDM: Digital-optimized, flexible, requires sync
   - WDM: Highest capacity, expensive, protocol-transparent

6. **Real-World Impact**: These technologies work together in modern networks. Your voice call might be digitized (TDM), combined with others (more TDM), then carried across continents on a single fiber using dozens of wavelengths (WDM).

---

*Prepared for BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)*  
*Subject: Computer Networks - Unit: Multiplexing Techniques*