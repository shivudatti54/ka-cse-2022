# **Check Sum and Point to Point Protocol Revision Notes**

## **Introduction**

- Check sum: error detection technique used in data transmission to identify corrupted data.
- Point to Point Protocol (PTP): a protocol used for reliable data transfer between two devices.

## **Key Concepts**

- **Check Sum Formula**:
  - `C(s) = (sum of all data bits) mod (2^n - 1)`
  - Where `C(s)` is the check sum, `s` is the data sequence, and `n` is the number of bits
- **Cyclic Codes**:
  - Error detection and correction technique used in digital communication systems.
  - Formula: `y = (c + d) mod m`
  - Where `y` is the output, `c` is the original data, `d` is the error pattern, and `m` is the modulus

## **Theorems**

- **Hamming Code Theorem**: any single-bit error can be detected and corrected.
- **Cyclic Code Correction Theorem**: any single-bit error can be corrected.

## **Important Definitions**

- **Parity Bit**: a bit added to data to ensure error detection.
- **Error Detection**: the process of identifying corrupted data.
- **Error Correction**: the process of correcting corrupted data.

## **Key Terms**

- **Block Coding**: a technique used to detect and correct errors in digital communication systems.
- **Modulus**: a number used in cyclic code calculations.
