# 12.1 - 12.2: Data Link Layer - Error Detection and Correction

===========================================================

## 12.1 - Introduction to Error Detection and Correction

---

### Definition

Error detection and correction are essential functions in a computer network that ensure the reliable transfer of data between devices.

### Why is Error Detection and Correction Important?

- Prevents data corruption and loss
- Ensures data integrity
- Reduces the need for retransmission
- Improves network reliability

### Types of Errors

- **Bit errors**: Random fluctuations in the bits transmitted
- **Packet errors**: Loss or corruption of packets during transmission
- **Forward errors**: Errors introduced during transmission, such as signal attenuation

## 12.2 - Block Coding

---

### Definition

Block coding is a technique used to detect and correct errors in digital data transmission.

### How Block Coding Works

1. **Block formation**: Divide the data into fixed-length blocks
2. **Encoding**: Add error-checking codes to each block
3. **Transmission**: Send the coded blocks through the network
4. **Decoding**: Receive and decode the blocks at the receiving end

### Types of Block Codes

- **Single-error-correcting (SEC) codes**: Can correct single-bit errors
- **Double-error-correcting (DEC) codes**: Can correct double-bit errors
- **Triple-error-correcting (TEC) codes**: Can correct triple-bit errors

### Examples of Block Codes

- **Hamming codes**: Used for single-error correction
- **Cyclic Redundancy Check (CRC) codes**: Used for single-error detection and correction
- **Viterbi codes**: Used for multi-error correction

## Key Concepts

---

- **Block size**: The number of bits in a block of data
- **Error rate**: The probability of errors occurring during transmission
- **Hamming distance**: The minimum distance between two codewords
- **Cyclic redundancy check (CRC)**: A checksum used for error detection

### Example

Suppose we have a block of data `10101010` and we use a Hamming code with a block size of 7 bits. The encoded block would be `11010101`. If an error occurs during transmission, the receiver can detect the error by calculating the Hamming distance between the received and transmitted blocks.
