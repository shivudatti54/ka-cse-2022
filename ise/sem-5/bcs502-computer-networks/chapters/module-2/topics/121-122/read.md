# 12.1 - 12.2: Error Detection and Correction

=====================================================

## 12.1 Introduction to Error Detection and Correction

---

Error detection and correction are crucial aspects of data communication in computer networks. Errors can occur due to various reasons such as electromagnetic interference, physical damage to the communication media, or transmission errors. If errors are not detected and corrected in a timely manner, they can lead to data corruption, loss, or misinterpretation.

### Error Detection

Error detection is the process of identifying errors that occur during data transmission. It involves checking the received data against a redundant copy of the original data to detect any discrepancies.

#### Types of Errors

- **Bit Flip Errors**: A single bit is flipped from 0 to 1 or vice versa.
- **Bit Insertion Errors**: One or more bits are inserted into the data stream.
- **Bit Deletion Errors**: One or more bits are deleted from the data stream.
- **Bit Erasure Errors**: One or more bits are completely erased from the data stream.

### Error Correction

Error correction is the process of correcting the errors detected during data transmission. It involves using error-correcting codes to rebuild the original data from the received data.

### Block Codes

Block codes are a type of error-correcting code that divides the data into fixed-length blocks and adds redundancy to each block. The redundancy is used to detect and correct errors.

#### Types of Block Codes

- **Single-Error Correcting (SEC) Codes**: Can correct one bit error.
- **Dual-Error Correcting (DEC) Codes**: Can correct two bit errors.
- **Triple-Error Correcting (TEC) Codes**: Can correct three bit errors.

## 12.2 Cyclic Codes

---

Cyclic codes are a type of block code that is used for error correction. They are called cyclic because they are cyclically shifted during the encoding process.

### Properties of Cyclic Codes

- **Periodicity**: Cyclic codes have a periodicity of `n`, where `n` is the length of the data block.
- **Cyclic Shift Invariance**: Cyclic codes remain the same after a cyclic shift.

### Construction of Cyclic Codes

Cyclic codes are constructed using the following steps:

1.  **Divide the data block into non-overlapping blocks**: Divide the data block into non-overlapping blocks of length `n`.
2.  **Compute the parity bits**: Compute the parity bits for each block using the following equations:
    - `p_i = ∑_{j=1}^{n/2} c_{(2i+j-1) mod n}`
    - `p_i = ∑_{j=n/2+1}^{n} c_{(2i+j-1) mod n}`
3.  **Concatenate the blocks and parity bits**: Concatenate the blocks and parity bits to form the codeword.

### Example of Cyclic Code Construction

Suppose we have a data block of length 5: `10101`. We divide this block into two non-overlapping blocks of length 3: `101` and `01`.

We compute the parity bits for each block:

- `p_1 = ∑_{j=1}^{3/2} c_{(2i+j-1) mod 3} = 1 + 0 + 1 = 2`
- `p_2 = ∑_{j=3/2+1}^{3} c_{(2i+j-1) mod 3} = 0 + 1 + 1 = 2`

We concatenate the blocks and parity bits to form the codeword: `010122`.
