# Computer Networks: Data Link Layer (10.1-10.4)

=====================================================

## Introduction

---

The Data Link Layer is the second layer of the OSI model, responsible for ensuring reliable transfer of data frames between two devices on the same network. This layer adds error detection and correction mechanisms to ensure data integrity.

### Key Concepts

- **Frame**: A block of data transmitted over a network, consisting of a header and payload.
- **Error Detection**: Methods used to identify errors in data transmission.
- **Error Correction**: Techniques used to correct errors detected in data transmission.

## Block Coding

---

Block coding is a method of error detection and correction used in the Data Link Layer. It involves dividing data into blocks and adding redundant information to each block.

### Key Concepts

- **Block Size**: The number of bits in a data frame.
- **Redundant Bits**: Additional bits added to each block to detect and correct errors.
- **Cyclic Redundancy Check (CRC)**: A method of error detection using a polynomial equation.

### How Block Coding Works

1.  Divide data into blocks of a fixed size (block size).
2.  Add redundant bits to each block (error detection and correction).
3.  Transmit the block with the added redundant bits.
4.  Receive the block and calculate the CRC.
5.  Compare the received CRC with the calculated CRC.

## Cyclic Codes

---

Cyclic codes are a type of block code used for error detection and correction. They use a polynomial equation to detect and correct errors.

### Key Concepts

- **Polynomial Equation**: A mathematical equation used to detect and correct errors.
- **Generator Polynomial**: A polynomial used to generate the cyclic code.
- **Parity-Check Matrix**: A matrix used to detect and correct errors.

### How Cyclic Codes Work

1.  Define a generator polynomial.
2.  Generate the cyclic code using the generator polynomial.
3.  Divide the data into blocks and add redundant bits using the cyclic code.
4.  Transmit the block with the added redundant bits.
5.  Receive the block and calculate the CRC using the parity-check matrix.

## Error Detection and Correction

---

Error detection and correction are critical functions of the Data Link Layer. They ensure reliable data transfer over networks.

### Error Detection Methods

- **Checksum**: A method of error detection using a sum of bits.
- **CRC**: A method of error detection using a polynomial equation.
- **Parity-Check**: A method of error detection using redundant bits.

### Error Correction Methods

- **Block Coding**: A method of error correction using redundant bits.
- **Cyclic Codes**: A type of block code used for error correction.
- **Forward Error Correction (FEC)**: A method of error correction using redundant bits.

## Key Terms

---

- **Frame Error Rate (FER)**: The probability of error in data transmission.
- **Bit Error Rate (BER)**: The probability of error in a single bit.
- **Packet Loss**: The loss of data packets during transmission.

### Summary

The Data Link Layer is responsible for ensuring reliable data transfer over networks. Block coding and cyclic codes are used for error detection and correction. Understanding these concepts is crucial for designing and implementing efficient network protocols.
