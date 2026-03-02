# **10.1-10.4: Data Link Layer - Error Detection and Correction**

### 10.1: Error Detection and Correction

- **Error Detection:**
  - Error detection is the process of identifying when errors occur during data transmission.
  - Common error detection techniques:
    - Parity bits
    - Checksums
- **Error Correction:**
  - Error correction is the process of correcting errors detected during data transmission.
  - Common error correction techniques:
    - Block coding
    - Cyclic codes

### 10.2: Block Coding

- **Block Coding:**
  - A technique used to detect and correct errors by dividing data into fixed-length blocks.
  - Advantages:
    - Reduces error rate
    - Increases data reliability
- **Types of Block Codes:**
  - Hamming codes
  * Vitegen codes
  * Reed-Solomon codes

### 10.3: Cyclic Codes

- **Cyclic Codes:**
  - A type of block code that uses cyclic shifts to detect and correct errors.
  - Properties:
    - Periodicity
    - Division algorithm
- **Cyclic Code Properties:**
  - Generator polynomial
  - Minimum distance
  - Error-correcting capability

### 10.4: Introduction to Cyclic Codes

- **Definition:**
  - A cyclic code is a type of block code that satisfies certain properties.
- **Properties:**
  - Periodicity
  - Division algorithm
  - Error-correcting capability
- **Applications:**
  - Error detection and correction
  - Data transmission over noisy channels

### Important Formulas and Theorems

- **Hamming Code:**
  - p(k,n) = 2^k - 1 (number of codewords)
  - d = 2t + 1 (minimum distance)
- **Cyclic Code:**
  - g(x) = generator polynomial
  - h(x) = parity polynomial
  - d = 2t + 1 (minimum distance)
