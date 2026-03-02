# 12.1-12.2: Data Link Layer - Error Detection and Correction

=====================================================

### Key Points

#### Introduction

- Data Link Layer (DLL) is responsible for error detection and correction.
- DLL ensures reliable data transfer between devices.

#### Error Detection

- **Parity Bit**: an extra bit added to ensure data integrity.
  - Definition: `P = \sum_{i=1}^{n} d_i (mod 2)` where `d_i` is the `i-th` bit of the data.
- **Cyclic Redundancy Check (CRC)**: detects errors by calculating a checksum.
  - Formula: `CRC = \sum_{i=0}^{n-1} c_i \cdot x^i (mod m)` where `c_i` are the data bits and `x` is a polynomial.

#### Block Coding

- **Block Code**: a code that encodes data into blocks.
  - Definition: a code that maps `n` input bits to `k` output bits.
- **Hamming Code**: a type of block code that detects single-bit errors.
  - Formula: `H(x) = [x, \overline{x}, x \oplus \overline{x}, ..., x^{n-k} \oplus \overline{x}^{n-k}]`

#### Cyclic Codes

- **Cyclic Code**: a code that is invariant under cyclic shifts.
  - Definition: a code where the output is equal to the input shifted by a certain number of bits.

#### Important Formulas and Definitions

- **Hamming Distance**: the number of positions where two strings differ.
- **Block Error Rate (BER)**: the probability of a block of data being in error.
