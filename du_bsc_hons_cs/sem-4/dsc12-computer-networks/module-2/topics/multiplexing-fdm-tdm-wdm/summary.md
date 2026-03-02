# Multiplexing: FDM, TDM, WDM
**Unit 3: Data Communication & Networking** | BSc (H) CS - Delhi University (NEP 2024 UGCF)

## Introduction
Multiplexing is a fundamental concept in data communication that allows multiple signals to share a single transmission medium, maximizing bandwidth utilization. This summary covers the three primary multiplexing techniques: FDM, TDM, and WDM.

---

## Key Concepts

### What is Multiplexing?
- **Definition**: Technique of combining multiple signals into a single transmission channel
- **Purpose**: Efficient utilization of bandwidth; cost-effective communication
- **Key Components**: Multiplexer (combines signals) → Transmission Channel → Demultiplexer (separates signals)

### Frequency Division Multiplexing (FDM)
- **Principle**: Signals are allocated non-overlapping frequency bands
- **Working**: Each signal modulates a different carrier frequency; combined signals travel simultaneously
- **Applications**: AM/FM radio broadcasting, television transmission, telephone systems
- **Advantages**: Simultaneous transmission; suitable for analog signals
- **Limitations**: Requires bandpass filters; susceptible to intermodulation noise; inefficient if channels are idle

### Time Division Multiplexing (TDM)
- **Principle**: Signals share the same frequency but occupy different time slots
- **Types**:
  - **Synchronous TDM**: Fixed time slots assigned to each channel (even if idle)
  - **Statistical/Asynchronous TDM**: Dynamic allocation based on demand
- **Working**: Sample each input signal sequentially; transmit samples in time slots
- **Applications**: Digital telephone networks, PCM systems, digital audio broadcasting
- **Advantages**: Suitable for digital signals; flexible; better bandwidth utilization (statistical)
- **Limitations**: Requires precise synchronization; buffering delays

### Wavelength Division Multiplexing (WDM)
- **Principle**: Multiple optical signals transmitted simultaneously on different wavelengths (colors) of light
- **Working**: Combines multiple light signals using prisms/gratings; separates at receiver
- **Types**:
  - **Coarse WDM (CWDM)**: Fewer channels, wider spacing
  - **Dense WDM (DWDM)**: Many channels, narrow spacing (up to 80+ channels)
- **Applications**: High-capacity fiber optic networks, telecommunications backbone
- **Advantages**: Extremely high capacity; low signal degradation; cost-effective for long distances
- **Limitations**: Requires expensive optical equipment; crosstalk issues

---

## Comparison Table

| Feature | FDM | TDM | WDM |
|---------|-----|-----|-----|
| Domain | Frequency | Time | Wavelength |
| Signal Type | Analog | Digital | Light/Optical |
| Capacity | Low-Medium | Medium | Very High |
| Complexity | Moderate | High | Very High |

---

## Conclusion
Multiplexing techniques are essential for efficient network resource utilization. FDM suits analog applications, TDM is ideal for digital transmission, and WDM enables ultra-high-capacity optical networks. Understanding these techniques is crucial for designing modern communication systems and performing well in Delhi University examinations.