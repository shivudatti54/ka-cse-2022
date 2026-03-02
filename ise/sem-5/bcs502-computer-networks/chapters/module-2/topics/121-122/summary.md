# **12.1 - 12.2: Data Link Layer - Error Detection and Correction**

### Introduction

- Data Link Layer is a layer in the OSI model responsible for error detection and correction.
- It ensures that data is transmitted reliably between two devices on the same network.

### Key Concepts

- **Error Detection:**
  - Types of errors: bit errors, frame errors, and protocol errors
  - Error detection techniques: checksum, cyclic redundancy checks (CRCs)
- **Error Correction:**
  - Types of codes: block codes, convolutional codes
  - Block codes:
    - Block codes: replace a small block of bits with a single bit
    - Examples: Hamming (7,4), BCH (15,11)
  - Cyclic codes:
    - Cyclic codes: use cyclic shift to detect errors
    - Examples: cyclic redundancy checks (CRCs), cyclic codes (7,4)

### Important Formulas and Definitions

- **Checksum formula:** ∑x_i = r mod m = 0 (where x_i are the data bits, r is the result, and m is the modulus)
- **CRC formula:** (x*n + x*{n-1} + ... + x_0) mod (2^m - 1)
- **Hamming distance:** d = ∑(x_i \* y_i) (where x_i and y_i are the data bits)

### Key Theorems

- **Shannon-Hamming Bound:** ∑p(x_i) \* log_2(m/d) ≥ S (where p(x_i) are the probabilities of error, m is the code length, d is the minimum distance, and S is the entropy of the channel)
- **Cyclic Redundancy Check (CRC) theorem:** A CRC can detect errors with a minimum distance of t+1
