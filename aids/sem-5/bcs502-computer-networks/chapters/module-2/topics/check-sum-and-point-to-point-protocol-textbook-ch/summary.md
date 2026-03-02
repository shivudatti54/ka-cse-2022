# **Check Sum and Point to Point Protocol**

**Important Definitions:**

- **Checksum:** A digital signature that detects errors in data transmission.
- **Point-to-Point Protocol (PTP):** A protocol used in data transmission where each device is connected to a single destination.

**Key Concepts:**

- **Checksum Formula:**
  - For bit-level checksum: `C = ∑i=0^n-1 d_i`
  - For byte-level checksum: `C = ∑i=0^n-1 s_i`
- **Parity Check:**
  - Odd parity: `C = mod(n, 2)`
  - Even parity: `C = mod(n, 2) + 1`
- **Block Coding:**
  - Definition: Encoding data into a block of bits to detect errors
  - Types: Hamming codes, Reed-Solomon codes, etc.
- **Cyclic Codes:**
  - Definition: A type of block code that can be divided by a generator polynomial
  - Types: BCH codes, Golay codes, etc.

**Important Formulas and Theorems:**

- **Hamming Code Formula:**
  - `C = [d_0 d_1 ... d_n]`
  - where `d_i` is the parity bit
- **Reed-Solomon Code Formula:**
  - `C = [d_0 d_1 ... d_n]`
  - where `d_i` is the encoded bit

**Key Points for Revision:**

- Check sum is used for single device data transmission
- Point-to-point protocol is used for error-free data transmission
- Block coding and cyclic codes are used for detecting and correcting errors
- Hamming codes and Reed-Solomon codes are examples of cyclic codes
