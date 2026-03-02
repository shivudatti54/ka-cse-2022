# **10.1-10.4: Data Link Layer - Error Detection and Correction**

## **10.1: Introduction**

- Definition: A subset of the protocol layer that provides error-free transfer of data frames between two devices on the same network.
- Error Detection and Correction: Critical functions of the Data Link Layer.
- Types of Errors: Bit Flip Errors, Bit Position Errors, Frame Errors.

## **10.2: Block Coding**

- Definition: A technique used to detect and correct errors by adding redundant bits to the data.
- Types of Block Codes:
  - Even-Odd Check Codes
  - Cyclic Redundancy Check (CRC) Codes
  - Hamming Codes
- Codes and Their Properties:
  - Hamming (7,4) Code: Error Correction Capability = 1 Error, Error Detection Capability = 3 Errors
  - Hamming (8,4) Code: Error Correction Capability = 1 Error, Error Detection Capability = 3 Errors

## **10.3: Cyclic Codes**

- Definition: A type of block code that uses a cyclic shift to detect and correct errors.
- Cyclic Code Properties:
  - Error Correction Capability: n-k
  - Error Detection Capability: n-k
- Cyclic Code Formula:
  - g(x) = gcd(c(x), x^n - 1)
  - c(x) = f(x) mod (x^n - 1)
- Important Theorems:
  - Berlekamp-Massey Algorithm: Algorithm for finding the maximum weight of a linear code

## **10.4: Error Correcting Codes**

- Definition: A code that can correct errors in data transmission.
- Examples of Error Correcting Codes:
  - Reed-Solomon Codes
  - Viterbi Codes
- Important Formulas:
  - Hamming Bound: Minimum Distance of a Code ≥ (d-1)/2
