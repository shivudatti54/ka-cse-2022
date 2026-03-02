# **CRC-CCITT (16-bits) Error Detecting Code**

### Key Points

- **Definition:** CRC-CCITT is a cyclic redundancy check algorithm used for error detection in digital communication systems.
- **Purpose:** To detect single-bit errors in digital data.
- **Formula:**

```c
CRC = x^23 + x^22 + x^20 + x^18 + x^17 + x^16 + x^15 + x^13 + x^12 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x^1 + x^0
```

- **Algorithm:**
  1. Initialize the CRC value to 0.
  2. Iterate through each bit of the data:
  3. XOR the current bit with the CRC value.
  4. Shift the bits of the CRC value one position to the left.
  5. Add the new bit to the CRC value.
  6. The final CRC value is the error-detecting code.

### Important Formulas and Definitions

- **Polynomial:** The polynomial used to generate the CRC-CCITT code: x^23 + x^22 + x^20 + x^18 + x^17 + x^16 + x^15 + x^13 + x^12 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x^1 + x^0
- **Galois Field:** A finite field used in the CRC-CCITT algorithm.
- **Parity Bit:** A single-bit checksum used to detect even-numbered errors.

### Theorems

- **Error-Detecting Capability:** The CRC-CCITT algorithm can detect single-bit errors but not multi-bit errors.
- **Sensitivity:** The sensitivity of the CRC-CCITT algorithm is 4 bits, meaning it can detect errors up to 4 bits long.

### Quick Revision Tips

- Focus on the polynomial and the algorithm.
- Practice calculating the CRC value for different data inputs.
- Understand the limitations of the CRC-CCITT algorithm (single-bit error detection).
