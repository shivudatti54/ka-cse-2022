# Error Detection and Correction

## Introduction

In data communication over networks, errors may occur during transmission due to noise, interference, or signal attenuation. The Data Link Layer implements **Error Detection and Correction** mechanisms to ensure reliable data delivery between connected systems.

---

## Types of Errors

- **Single-bit Error**: Only one bit changes; rare in serial transmission
- **Burst Error**: Multiple consecutive bits change; more common in real scenarios

---

## Error Detection Methods

- **Redundancy**: Adding extra bits (check bits) to detect errors
- **Vertical Redundancy Check (VRC) / Parity Check**
  - Adds one parity bit (even/odd parity)
  - Detects only odd number of errors
- **Longitudinal Redundancy Check (LRC)**
  - Adds parity bit for each bit position across multiple characters
  - Better detection than VRC alone
- **Checksum**
  - Group of bits appended to message
  - Based on 1's complement arithmetic
  - Used in IP, TCP/UDP headers
- **Cyclic Redundancy Check (CRC)**
  - Most powerful and widely used method
  - Uses polynomial division
  - Detects burst errors up to length of generator polynomial
  - Implemented in Ethernet, HDLC, PPP

---

## Error Correction Methods

- **Hamming Code**
  - Adds **r redundant bits** to **m data bits**
  - Formula: 2^r ≥ m + r + 1
  - Can detect and correct **single-bit errors**
  - Uses parity bits at positions 1, 2, 4, 8...
- **Automatic Repeat reQuest (ARQ)**
  - **Stop-and-Wait ARQ**: Sender waits for ACK before sending next frame
  - **Go-back-N ARQ**: Retransmits all frames from error point
  - **Selective Repeat ARQ**: Retransmits only erroneous frames

---

## Conclusion

Error Detection and Correction are fundamental for reliable network communication. Selection depends on channel reliability, latency requirements, and overhead considerations. CRC and ARQ protocols are widely implemented in modern networking standards for robust data transmission.

---

*For detailed study, refer to Unit-III of Delhi University B.Sc. (Hons) Computer Science NEP 2024 UGCF syllabus.*