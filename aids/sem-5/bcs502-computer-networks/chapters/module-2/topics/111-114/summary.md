# **11.1 - 11.4: Data Link Layer Error Detection and Correction**

### Introduction

- The Data Link Layer is responsible for error detection and correction in a network.
- Error detection and correction are essential for maintaining data integrity and reliability.

### Block Coding

- **Definition:** A method of error detection and correction that involves dividing data into fixed-length blocks.
- **Types:**
  - **Block Code:** A set of codes used for error detection and correction.
  - **Cyclic Code:** A type of block code that uses cyclic shift to encode data.
- **Key Concepts:**
  - **Block Code Equivalence:** Two block codes are equivalent if they produce the same parity check result.
  - **Cyclic Redundancy Check (CRC):** A method of error detection that uses a block code to check for errors.

### Cyclic Codes

- **Definition:** A type of block code that uses cyclic shift to encode data.
- **Types:**
  - **Binary Cyclic Codes:** Used for digital data transmission.
  - **Ternary Cyclic Codes:** Used for analog data transmission.
- **Key Concepts:**
  - **Generator Polynomial:** A polynomial used to generate cyclic codes.
  - **Primitive Polynomial:** A polynomial used to generate primitive cyclic codes.

### Important Formulas and Definitions

- **CRC Formula:** `CRC = P(x) = (g(x))^n + r(x)`
- **Generator Polynomial Formula:** `g(x) = (1 + x + x^2 + ... + x^(2^n-1))`
- **Primitive Polynomial Formula:** `p(x) = (1 + x + x^2 + ... + x^(2^n-1))`

### Theorems

- **Hamming Bound:** A bound on the minimum distance of a code.
- **Shannon-Hartley Theorem:** A theorem that relates the capacity of a communication channel to its bandwidth.

Note: This summary is a concise revision guide and is not intended to be a comprehensive introduction to the topic.
