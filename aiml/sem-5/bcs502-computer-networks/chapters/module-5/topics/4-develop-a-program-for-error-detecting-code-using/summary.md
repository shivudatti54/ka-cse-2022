# CRC-CCITT (16-bits) Error Detection Program

=============================================

### Introduction

- CRC-CCITT (16-bits) is a widely used error detection algorithm for detecting single-bit errors in digital data.
- It is based on the CCITT X.23 protocol.

### Key Concepts

- **CRC (Cyclic Redundancy Check)**: A mathematical function that takes a block of data as input and produces a digital signature, called the CRC value.
- **Polynomial**: A mathematical expression of the form `x^n + ax^(n-1) + ... + a_0`, used to generate the CRC value.
- **Hamming Weight**: The number of bits set to 1 in the CRC value.

### Important Formulas and Definitions

- **CRC-CCITT Polynomial**: `x^16 + x^12 + x^5 + 1`
- **CRC-CCITT Algorithm**:
  1.  Initialize the CRC value to `F`
  2.  XOR each bit of the data with the CRC value
  3.  Update the CRC value using the polynomial
  4.  Repeat steps 2-3 for each bit of the data
  5.  The final CRC value is the digital signature of the data

### Theorem

- The CRC-CCITT algorithm has a maximum Hamming distance of 8, meaning it can detect up to 8 single-bit errors.

### Important Theorems

- **Error Detection Capability**: The probability of detecting a single-bit error is `1 - (1 - p)^(8)`, where `p` is the probability of a single-bit error.
- **Error Correction Capability**: The probability of correcting a single-bit error is `p^8`.

### Program Implementation

- The CRC-CCITT algorithm can be implemented using a simple loop that updates the CRC value for each bit of the data.
- The final CRC value can be used to detect errors in the data.

### Example Use Case

- The CRC-CCITT algorithm can be used to detect errors in digital data transmitted over a network.
- For example, when sending a file over a network, the CRC-CCITT algorithm can be used to detect any single-bit errors that may occur during transmission.
