# Error Control in Data Communication

## Introduction

Error control is a fundamental aspect of data communication that ensures reliable delivery of data across unreliable communication channels. In any real-world communication system, data transmitted from sender to receiver is susceptible to various types of errors caused by noise, interference, attenuation, and other channel impairments. Without proper error control mechanisms, the integrity of transmitted data would be compromised, leading to corrupted information, failed transactions, and system failures.

Error control encompasses two primary strategies: error detection and error correction. Error detection identifies when data has been corrupted during transmission, while error correction goes a step further by reconstructing the original data without requiring retransmission. The choice between these approaches depends on channel characteristics, latency requirements, and the application domain. For instance, real-time applications like video streaming may tolerate some errors, while financial transactions demand perfect data integrity.

This topic covers the essential techniques for detecting and correcting errors, including checksum, cyclic redundancy check (CRC), Hamming code, and various ARQ (Automatic Repeat reQuest) protocols. Understanding these mechanisms is crucial for designing robust network protocols and ensuring reliable data communication in computer networks.

## Key Concepts

### Types of Errors

**Single-Bit Error**: Occurs when only one bit in the data unit changes from 1 to 0 or 0 to 1. This type of error is less common in serial transmission but can occur in parallel communication channels.

**Burst Error**: More prevalent in real-world scenarios, a burst error affects multiple consecutive bits. The length of the burst is measured from the first corrupted bit to the last corrupted bit. Burst errors are typically caused by impulse noise or fading in communication channels.

### Error Detection Techniques

**Parity Check**: The simplest form of error detection using a single parity bit. In even parity, the parity bit is set to make the total number of 1s even. In odd parity, the total number of 1s is made odd. While simple to implement, parity check can only detect odd-numbered bit errors and cannot correct errors.

**Two-Dimensional Parity Check**: Extends simple parity by organizing data into a matrix and adding parity bits for each row and column. This method can detect burst errors and some specific patterns that single parity would miss.

**Checksum**: A group of check digits computed from the data bits. The sender divides data into equal segments, adds them together using one's complement arithmetic, and appends the complement of the sum as the checksum. The receiver performs the same calculation and compares the result. Any discrepancy indicates an error.

**Cyclic Redundancy Check (CRC)**: The most powerful and widely used error detection method. CRC treats the data as a binary polynomial, divides it by a predetermined generator polynomial, and appends the remainder (CRC bits) to the data. The receiver performs the same division and checks if the remainder is zero. CRC can detect all single-bit errors, burst errors shorter than the divisor, and has a very high probability of detecting random errors.

### Error Correction Techniques

**Hamming Code**: A linear block code that can both detect and correct single-bit errors. It uses redundant bits (parity bits) placed at specific positions in the data word. For a data word of length m bits, r redundant bits are added where 2^r ≥ m + r + 1. The positions of parity bits are powers of 2 (1, 2, 4, 8, 16...), and each parity bit covers specific bit positions.

**Convolutional Codes**: Encode data by combining current and previous data bits using shift registers and modulo-2 adders. The encoded output depends on the entire stream of input bits, making these codes suitable for sequential data transmission.

### Automatic Repeat Request (ARQ)

**Stop-and-Wait ARQ**: The sender transmits a single frame and waits for acknowledgment (ACK) before sending the next frame. If no ACK arrives within a timeout period, or if a NACK (negative acknowledgment) is received, the sender retransmits the frame. This protocol is simple but inefficient for high-latency channels.

**Go-Back-N ARQ**: Allows the sender to transmit multiple frames before receiving acknowledgments. If an error is detected in frame i, the sender retransmits frame i and all subsequent frames (i+1, i+2, ...). This protocol is efficient for channels with moderate error rates.

**Selective Repeat ARQ**: The most efficient ARQ protocol where only the erroneous frames are retransmitted. The receiver buffers correctly received out-of-order frames and reorders them before delivery. This requires more complex receiver logic and buffer management.

## Examples

### Example 1: Parity Check Detection

**Problem**: Data "1011001" is transmitted using even parity. Determine the parity bit to be added and check if the received data "1011101" is correct.

**Solution**:

**Step 1**: Count 1s in original data: 1011001 contains four 1s (positions 1, 3, 4, 5).

**Step 2**: Since even parity is used and we already have four 1s (even), the parity bit = 0.

**Step 3**: Transmitted data = 10110010

**Step 4**: Received data = 1011101 (7 bits), so we check if parity matches. Count 1s: five 1s.

**Step 5**: Five 1s is odd, indicating an error in transmission.

### Example 2: CRC Error Detection

**Problem**: Data = 110101, Generator = 1011 (degree 3). Calculate the CRC bits and verify if received data 110101011 is error-free.

**Step 1**: Append zeros equal to generator degree: 110101000

**Step 2**: Perform binary division:

```
110101000 ÷ 1011
```

**Step 3**: Using modulo-2 division:

- 1011 goes into 1101 → quotient bit 1, XOR: 1101 ⊕ 1011 = 0110
- Bring down next bit: 0110 (with next bit 1) = 01101
- 1011 goes into 01101 → quotient bit 1, XOR: 01101 ⊕ 01011 = 00110
- Bring down 0: 001100
- 1011 goes into 001100 → quotient bit 0, XOR: 001100 ⊕ 00000 = 001100
- Continue: 001100 → 00110, bring down 0: 001100
- 1011 goes into 001100 → quotient bit 0, XOR remains 001100
- Final remainder after processing all bits: 011

**Step 4**: CRC bits = 011 (3 bits)

**Step 5**: Transmitted data = 110101011

**Step 6**: Verify at receiver: Divide 110101011 by 1011. If remainder = 0, no error. In this case, remainder = 0, so data is error-free.

### Example 3: Hamming Code Correction

**Problem**: The 7-bit Hamming code word 1001110 is received. Check if there are any errors and correct if necessary. Assume even parity.

**Solution**:

**Step 1**: Identify bit positions (from right, position 1 is LSB):
Position: 7 6 5 4 3 2 1
Data: 1 0 0 1 1 1 0

**Step 2**: Identify parity bits at positions 1, 2, 4 (powers of 2):

- P1 (pos 1): bit 0
- P2 (pos 2): bit 1
- P4 (pos 4): bit 1

**Step 3**: Calculate parity for each group:

- Group 1 (P1 covers positions 1,3,5,7): bits at 1,3,5,7 = 0,1,0,1 → sum = 2 (even), P1 should be 0 ✓
- Group 2 (P2 covers positions 2,3,6,7): bits at 2,3,6,7 = 1,1,0,1 → sum = 3 (odd), P2 should be 0 but is 1 ✗
- Group 4 (P4 covers positions 4,5,6,7): bits at 4,5,6,7 = 1,0,0,1 → sum = 2 (even), P4 should be 0 ✓

**Step 4**: Error position = position with wrong parity in groups where P2 failed = position 2

**Step 5**: Flip bit at position 2: 1 → 0

**Step 6**: Corrected data: 1001010

## Exam Tips

1. **Remember the CRC relationship**: For a data word of n bits and generator of degree r, the transmitted code word has n+r bits.

2. **Hamming Code Formula**: Always remember 2^r ≥ m + r + 1, where m is data bits and r is parity bits. This is frequently asked in exams.

3. **Parity bit positions**: In Hamming code, parity bits occupy positions 1, 2, 4, 8, 16... (powers of 2).

4. **CRC vs Checksum**: CRC is stronger for burst error detection; checksum is simpler but less reliable. CRC can detect all burst errors of length ≤ degree of generator polynomial.

5. **ARQ Efficiency Formula**: For Stop-and-Wait ARQ, efficiency = 1/(1+2a) where a = propagation delay/transmission time.

6. **Error Correction vs Detection**: Hamming distance determines error detection/correction capability. For detecting d errors, minimum distance must be ≥ d+1. For correcting d errors, minimum distance must be ≥ 2d+1.

7. **Burst Error Detection**: CRC can detect burst errors of length greater than the generator if the error pattern is not divisible by the generator polynomial.

8. **Channel Characteristics**: For noisy channels, use ARQ with error correction. For clean channels, simple error detection with retransmission is sufficient.
