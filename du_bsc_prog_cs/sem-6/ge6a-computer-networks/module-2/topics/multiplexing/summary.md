# Multiplexing
**Ge6A Computer Networks - BSc Physical Science (CS), Delhi University**

## Introduction

Multiplexing is a fundamental technique in computer networks that allows multiple signals to be transmitted simultaneously over a single communication channel. It maximizes bandwidth utilization and reduces transmission costs by combining several low-speed signals into a single high-speed channel.

---

## Key Concepts

### What is Multiplexing?
- Technique of combining multiple signals into one transmission medium
- Solves bandwidth wastage problem in communication channels
- **Multiplexer (MUX)**: Combines multiple input signals into one output
- **Demultiplexer (DEMUX)**: Separates combined signals back to individual channels

### Types of Multiplexing

**1. Frequency Division Multiplexing (FDM)**
- Signals transmitted simultaneously using different frequency bands
- Each channel gets dedicated frequency bandwidth
- Used in radio and TV broadcasting, telephone systems
- Requires bandpass filters to separate frequencies

**2. Time Division Multiplexing (TDM)**
- Multiple signals share same frequency but occupy different time slots
- Data transmitted in predetermined time slots
- **Synchronous TDM**: Fixed time slots assigned to each channel (unused slots remain idle)
- **Asynchronous TDM**: Dynamically allocated time slots (more efficient)

**3. Wavelength Division Multiplexing (WDM)**
- Used in fiber optic communications
- Multiple optical signals transmitted using different wavelengths
- **Coarse WDM (CWDM)** and **Dense WDM (DWDM)** variants

**4. Code Division Multiplexing (CDM) / CDMA)**
- All channels transmit simultaneously using unique codes
- Each signal multiplied by unique spreading code
- Used in mobile communications (3G, GPS)
- Provides security and resistance to interference

### Advantages of Multiplexing
- Efficient bandwidth utilization
- Reduced infrastructure costs
- Enables simultaneous transmission of multiple data streams
- Simplifies network architecture

---

## Conclusion

Multiplexing is essential for modern network communication, enabling efficient data transmission over limited bandwidth. Understanding FDM, TDM, WDM, and CDMA is crucial for exam success, as these form the foundation of channel access techniques in computer networks.

*Reference: Delhi University NEP 2024 Syllabus - Ge6A Computer Networks*