# Error Control in Data Communication

## Introduction

Error control is a fundamental concept in data communication that ensures reliable transmission of data from sender to receiver. In any communication system, data traveling through a transmission medium is susceptible to various types of errors caused by noise, interference, signal attenuation, or equipment malfunction. These errors can corrupt data bits, leading to incorrect information being received. Error control mechanisms are designed to detect these errors and, when possible, correct them automatically.

In the context of 's Computer Science and Engineering curriculum, understanding error control is essential for designing robust network protocols and communication systems. The OSI model explicitly defines a Data Link Layer that is responsible for error control between adjacent nodes. Modern networking relies heavily on these techniques to ensure data integrity in applications ranging from simple file transfers to complex distributed systems. Without effective error control, the reliability of digital communication would be severely compromised, making accurate data exchange impossible.

This module covers the essential error detection and error correction techniques that form the backbone of reliable data communication. We will examine parity checking, checksum, cyclic redundancy check (CRC), and Hamming code - each with its unique approach to identifying and rectifying transmission errors. Understanding these techniques is crucial for both theoretical examinations and practical implementation of communication protocols.

## Key Concepts

### Types of Errors

Errors in data transmission are primarily categorized into two types: single-bit errors and burst errors. A single-bit error occurs when only one bit in the data unit changes from 1 to 0 or from 0 to 1. This type of error is relatively uncommon in serial transmission but can occur in parallel communication channels where multiple lines are involved. Single-bit errors are easier to detect and correct compared to burst errors.

A burst error, on the other hand, involves multiple consecutive bits being corrupted. The length of the burst is measured from the first corrupted bit to the last corrupted bit. Burst errors are more common in communication systems and are often caused by impulse noise or fading in wireless communications. The probability of burst errors is generally higher than single-bit errors, making error detection and correction more challenging.

### Error Detection Techniques

**Parity Checking**

Parity checking is the simplest form of error detection. In this technique, a single parity bit is added to the data unit to make the total number of 1s either even (even parity) or odd (odd parity). For even parity, if the data contains an even number of 1s, the parity bit is 0; if odd, the parity bit is 1. The receiver counts the 1s in the received data and compares it with the expected parity.

The major limitation of simple parity checking is that it can only detect odd-numbered errors. If two bits are flipped during transmission, the parity remains unchanged, and the error goes undetected. To improve upon this, two-dimensional parity checking can be used, where data is organized in a matrix and parity bits are added both row-wise and column-wise. This method can detect and correct single-bit errors in the matrix.

**Checksum**

Checksum is an error detection technique that treats the data as a sequence of words (typically 16-bit words) and computes their arithmetic sum. The sender calculates the sum of all data words and sends both the data and the checksum value. The receiver performs the same calculation on the received data and compares it with the received checksum.

There are two common approaches to checksum: ones complement addition and modular addition. In the Internet checksum (RFC 1071), the sender adds all 16-bit words using ones complement arithmetic, takes the ones complement of the result to get the checksum, and sends it along with the data. The receiver adds all received words including the checksum; if the result is all 1s (in ones complement), the data is considered error-free. Checksum can detect all single-bit errors and most multiple-bit errors, but it is not as powerful as CRC.

**Cyclic Redundancy Check (CRC)**

CRC is one of the most powerful and widely used error detection techniques. It is based on polynomial division and treats the data as a binary polynomial. The sender and receiver agree on a generator polynomial (divisor). The sender divides the data (appended with zeros equal to degree of generator) by the generator polynomial using binary division and obtains the remainder. This remainder is appended to the data as the CRC bits.

At the receiver, the data with CRC bits is divided by the same generator polynomial. If the remainder is zero, the data is assumed to be error-free; otherwise, an error is detected. CRC can detect all single-bit errors, all odd number of bit errors, and most burst errors with length less than or equal to the degree of the generator polynomial. Commonly used CRC polynomials include CRC-8, CRC-12, CRC-16, and CRC-32 (used in Ethernet, ZIP files, and PNG images).

### Error Correction Techniques

**Hamming Code**

Hamming code is a linear block code that can both detect and correct single-bit errors. It uses redundant bits (called parity bits) strategically placed at specific positions in the data word. For a data word of length m bits, the number of redundant bits r required is determined by the inequality 2^r ≥ m + r + 1.

The parity bits are placed at positions that are powers of 2 (1, 2, 4, 8, 16, etc.). Each parity bit covers specific bit positions based on their binary representation. To calculate the parity for a particular position, we consider all bit positions that have a 1 in that position's binary representation. For example, parity bit at position 1 checks all odd-numbered positions, parity bit at position 2 checks positions 2, 3, 6, 7, 10, 11, and so on.

At the receiver, each parity bit is checked, and the bit positions where parity fails are noted. The binary number formed by these positions (called syndrome) indicates the position of the erroneous bit. If the syndrome is zero, no error occurred. The erroneous bit is then flipped to correct the error. Hamming code can correct single-bit errors and detect double-bit errors when an overall parity bit is added, creating what is known as Hamming SECDED (Single Error Correction, Double Error Detection).

## Examples

### Example 1: Single Parity Check

**Problem**: Data "1011001" is to be transmitted using even parity. Find the parity bit to be added.

**Solution**:

Step 1: Count the number of 1s in the data.
Data: 1 0 1 1 0 0 1
Number of 1s = 4

Step 2: Since we are using even parity and the count is already even (4), the parity bit should be 0.

Step 3: Transmitted data = 10110010

**Verification at receiver**: If received data is "10110011" (last bit changed from 0 to 1):
Number of 1s = 5 (odd)
Even parity expected but odd number detected → Error detected!

### Example 2: CRC Calculation

**Problem**: Data = 110101 and generator polynomial G(x) = 1011 (degree 3). Find the CRC bits to be appended.

**Solution**:

Step 1: Append zeros equal to degree of generator (3 zeros) to data.
Data after appending: 110101000

Step 2: Perform binary division.

```
110101000 ÷ 1011
```

Using long division:

- 1011 goes into 1101 once → quotient bit 1, subtract to get 0110
- Bring down 0 → 01100, 1011 goes once → quotient 1, remainder 0101
- Bring down 0 → 01010, 1011 goes zero times → quotient 0, remainder 01010
- Bring down 0 → 010100, 1011 goes once → quotient 1, remainder 00110
- Bring down (nothing left but we need 3 more bits) → continue
  Actually, let's do standard division properly:
  110101000
  1011
  00111010 (remainder after first division)
  Continue until we have performed divisions equal to original data length
  Final remainder = 100 (3 bits as required)

Step 3: CRC = 100
Transmitted data = 110101100

### Example 3: Hamming Code

**Problem**: Data bits "101" are to be encoded using Hamming code. Find the codeword.

**Solution**:

Step 1: Number of data bits m = 3
Find r such that 2^r ≥ m + r + 1
2^2 = 4, 3 + 2 + 1 = 6, 4 < 6 ❌
2^3 = 8, 3 + 3 + 1 = 7, 8 ≥ 7 ✓
So r = 3 parity bits required

Step 2: Total codeword length = m + r = 6 bits
Positions: p1 p2 d1 p3 d2 d3
Data bits: d1=1, d2=0, d3=1

Step 3: Calculate parity bits:

- p1 (position 1): checks positions 1,3,5 → p1, d1, d2 → p1,1,0
  1 + 0 + p1 should be even → p1 = 1 (for even parity)
- p2 (position 2): checks positions 2,3,6 → p2, d1, d3 → p2,1,1
  1 + 1 + p2 should be even → p2 = 0
- p3 (position 4): checks positions 4,5,6 → p3, d2, d3 → p3,0,1
  0 + 1 + p3 should be even → p3 = 1

Step 4: Codeword = p1 p2 d1 p3 d2 d3 = 1 0 1 1 0 1 = 101101

## Exam Tips

1. **Remember the CRC generator polynomial properties**: A good generator polynomial must have at least two terms, and the first and last bits must be 1. The divisor should not divide x^n + 1 for any n less than the data length.

2. **Hamming code formula**: For m data bits and r redundant bits, always remember the relationship 2^r ≥ m + r + 1. This is frequently asked in exams.

3. **Parity bit positions in Hamming code**: Remember that parity bits are placed at positions 1, 2, 4, 8, 16 (powers of 2). This pattern is essential for syndrome calculation.

4. **Syndrome calculation**: The syndrome in Hamming code directly indicates the position of the erroneous bit. A syndrome of 0 means no error, while a non-zero syndrome gives the bit position to flip.

5. **CRC vs Checksum**: CRC is stronger than checksum for burst error detection. CRC can detect all burst errors with length less than or equal to the degree of the generator polynomial.

6. **Error detection vs correction capability**: Simple parity can only detect odd number of errors. Two-dimensional parity can detect and correct single-bit errors. Hamming code can correct single-bit errors with SECDED capability.

7. **Understand polynomial representation**: Know how to represent data as polynomials and perform binary division for CRC calculations. This is crucial for solving numerical problems.

8. **Applications of CRC**: Remember that CRC-32 is used in Ethernet, ZIP files, and PNG; CRC-16 is used in USB and Bluetooth; CRC-8 is used in ATM header error correction.
