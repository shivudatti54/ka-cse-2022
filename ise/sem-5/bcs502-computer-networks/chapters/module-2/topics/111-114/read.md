# 11.1 - 11.4: Data Link Layer Error Detection and Correction

===========================================================

## 11.1 Introduction

---

The Data Link Layer is responsible for framing, error detection, and error correction. Error detection is the process of identifying errors that may have occurred during data transmission, while error correction is the process of correcting these errors.

### Key Concepts:

- **Error Detection**: The process of identifying errors that may have occurred during data transmission.
- **Error Correction**: The process of correcting errors that have been detected.
- **Frame**: A sequence of bits that is transmitted between two devices.

## 11.2 Block Coding

---

Block coding is a technique used to detect errors in data transmission. It works by dividing the data into blocks, encoding each block with error-checking information, and transmitting the encoded blocks.

### Key Concepts:

- **Block Size**: The number of bits in a block of data.
- **Parity Bit**: A single bit added to a block of data to detect errors.
- **Error-Correcting Code (ECC)**: A code that can correct single-bit errors.

## 11.3 Cyclic Codes

---

Cyclic codes are a type of block code that is used to detect and correct errors in data transmission. They work by adding error-checking information to each block of data.

### Key Concepts:

- **Cyclic Code**: A code that is used to detect and correct errors in data transmission.
- **Generator Polynomial**: A polynomial used to generate the cyclic code.
- **Cyclic Redundancy Check (CRC)**: A checksum calculated using the generator polynomial.

## 11.4 Data Link Layer Error Detection and Correction

---

### Error Detection

- **Parity Check**: A simple error detection technique that uses parity bits to detect errors.
- **Cyclic Redundancy Check (CRC)**: A more complex error detection technique that uses a generator polynomial to calculate a checksum.

### Error Correction

- **Single-Error Correction (SEC)**: A single-bit error correction technique that uses ECC codes to correct errors.
- **Double-Error Correction (DEC)**: A two-bit error correction technique that uses ECC codes to correct errors.
