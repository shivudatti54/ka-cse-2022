# Error Detection and Correction

## Introduction
Error detection and correction form the backbone of reliable data communication in computer networks. As digital signals traverse physical media, they're susceptible to interference from electromagnetic noise, crosstalk, and signal attenuation. These errors can corrupt critical data in financial transactions, medical systems, and network protocols. Modern networks achieve error rates as low as 1 in 10^12 bits through sophisticated detection mechanisms.

The importance of these techniques spans multiple layers of the OSI model. At the physical layer, they combat transmission errors. At data link layer, they enable reliable frame delivery. TCP/IP implementations use checksums for packet integrity. With 5G networks achieving 1ms latency, efficient error handling becomes crucial for real-time applications like autonomous vehicles and industrial IoT.

## Key Concepts
1. **Parity Checking**
   - Single Parity Check: Adds 1 bit to make total 1s even/odd
   - Two-Dimensional Parity: Matrix arrangement detects burst errors
   - Limitations: Detects only odd-numbered bit errors

2. **Cyclic Redundancy Check (CRC)**
   - Polynomial division using generator polynomial
   - 32-bit CRC used in Ethernet (IEEE 802.3)
   - Mathematical foundation: GF(2) polynomial arithmetic

3. **Hamming Codes**
   - (n,k) codes where n = k + r
   - Hamming distance: Minimum bits differing between codewords
   - Can detect 2-bit errors and correct 1-bit errors

4. **Checksums**
   - Internet checksum (used in IP/TCP/UDP)
   - One's complement addition
   - Vulnerable to certain error patterns

5. **Automatic Repeat Request (ARQ)**
   - Stop-and-Wait ARQ
   - Go-Back-N ARQ
   - Selective Repeat ARQ

## Examples

**Example 1: CRC Calculation**
Data: 1101011011
Generator: x^4 + x + 1 (10011)

Steps:
1. Append 4 zeros: 11010110110000
2. Perform XOR division:
   11010110110000 ÷ 10011
3. Remainder = 1110 → CRC code
4. Transmitted frame: 11010110111110

**Example 2: Hamming Code Correction**
Received 7-bit Hamming code: 1011011

1. Calculate parity bits:
   p1: bits 1,3,5,7 → 1+1+0+1 = 1 (odd)
   p2: bits 2,3,6,7 → 0+1+1+1 = 1
   p4: bits 4,5,6,7 → 1+0+1+1 = 1
2. Error position: p4p2p1 = 111 (7th bit)
3. Corrected code: 1011010

**Example 3: Internet Checksum**
Data words: 0x4500, 0x003C, 0x8A11

1. Sum = 4500 + 003C + 8A11 = CE4D
2. Add carry: CE4D + 0001 = CE4E
3. One's complement: 31B1

## Exam Tips
1. Practice polynomial long division for CRC (common 8-mark question)
2. Memorize Hamming code parity bit positions: 2^(n-1)
3. Understand difference between error detection (CRC) vs correction (Hamming)
4. ARQ protocols often appear as comparison tables (6 marks)
5. Checksum calculations require hexadecimal addition skills
6. Burst error detection capabilities vary: CRC > Checksum > Parity
7. Numerical on Hamming distance for code capability analysis