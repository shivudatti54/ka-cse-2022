# **12.1 - 12.2: Data Link Layer - Error Detection and Correction**

## **Introduction**

- The data link layer is responsible for error detection and correction in computer networks.
- It ensures reliable data transfer between devices.

## **Block Coding**

- A method of error detection and correction that converts data into blocks.
- Each block is assigned a unique code word.
- Key concepts:
  - Hamming code
  - Reed-Solomon code
  - CRC (Cyclic Redundancy Check)

## **Cyclic Codes**

- A type of block code that uses a cyclic shift to generate code words.
- Key concepts:
  - Generator polynomial
  - Cyclic redundancy check (CRC)
  - Examples: BCH codes, Convolutional codes

## **Important Formulas and Definitions**

- **CRC (Cyclic Redundancy Check) formula**:
  - CRC = ∑[c(i) \* g(i)] mod M
  - where c(i) = data bit i, g(i) = generator polynomial, and M = code length
- **Generator polynomial**:
  - a polynomial used to generate code words
  - used in cyclic codes
- **Block code**:
  - a method of error detection and correction that converts data into blocks

## **Theorems**

- **Shannon-Hartley theorem**:
  - establishes the relationship between signal-to-noise ratio (SNR) and data transmission rate
- **Hamming bound**:
  - establishes the minimum distance between a code and its minimum distance

## **Key Points for Revision**

- Block coding and cyclic codes are used for error detection and correction.
- CRC is a common method used in cyclic codes.
- Generator polynomials are used to generate code words.
- Shannon-Hartley theorem and Hamming bound are important theorems in coding theory.
