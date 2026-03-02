# Error Detection and Correction Protocols

## Introduction

Error detection and correction protocols are fundamental mechanisms in computer networks that ensure reliable data transmission over unreliable communication channels. According to the Delhi University BSc (Physical Science) CS syllabus under NEP 2024, these protocols operate primarily at the Data Link Layer and are essential for maintaining data integrity in network communications.

## Key Concepts

### Types of Errors
- **Single-bit errors**: One bit altered during transmission (rare in serial communication)
- **Burst errors**: Multiple consecutive bits corrupted (more common in real-world scenarios)

### Error Detection Techniques

- **Parity Check**
  - Simple method using even or odd parity bits
  - Can detect only odd number of bit errors
  - Limited effectiveness

- **Checksum**
  - Data divided into segments, summed, and complemented
  - Used in IPv4 header and UDP/TCP
  - Better detection capability than parity

- **Cyclic Redundancy Check (CRC)**
  - Most powerful error detection method
  - Uses polynomial division
  - Detects burst errors up to length of generator polynomial
  - Widely used in Ethernet, Wi-Fi, and storage devices

### Error Correction Techniques

- **Hamming Code**
  - Adds redundant bits (parity bits) at specific positions
  - Can correct single-bit errors and detect double-bit errors
  - Formula: 2^r ≥ m + r + 1 (where m = data bits, r = parity bits)

- **Binary Convolution Codes**
  - More complex coding for higher error correction capability
  - Used in wireless communications

### Error Control Protocols (ARQ - Automatic Repeat reQuest)

- **Stop-and-Wait ARQ**
  - Sender waits for acknowledgment before sending next frame
  - Simple but inefficient for high-latency networks
  - Uses sequence numbers and timers

- **Go-Back-N ARQ**
  - Sender can send multiple frames without waiting for ACKs
  - Retransmits all frames from error point
  - Efficient for moderate error rates

- **Selective Repeat ARQ**
  - Only retransmits corrupted frames
  - Most efficient but complex implementation
  - Requires buffer at sender and receiver

### Flow Control Mechanisms
- **Sliding Window Protocol**: Allows multiple frames in transit
- **Receiver feedback**: ACK/NAK signals regulate data flow

## Conclusion

Error detection and correction protocols are essential for reliable network communication. Understanding CRC, Hamming codes, and ARQ protocols is crucial for exam success. These mechanisms form the backbone of data integrity in modern networking, with applications spanning from local area networks to wireless communications.

---

*Based on Delhi University BSc Physical Science (CS) NEP 2024 Syllabus - Data Link Layer Protocols*