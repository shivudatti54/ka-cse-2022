# 11.1 - 11.4: Data Link Layer - Error Detection and Correction

===========================================================

## Introduction

---

The Data Link Layer is the second layer of the OSI model and is responsible for providing error-free transfer of data frames between two devices on the same network. It does this by detecting and correcting errors that may occur during data transmission.

## Block Coding

---

Block coding is a method of error detection and correction that involves dividing data into fixed-length blocks and adding redundancy to each block. This redundancy is used to detect and correct errors that may occur during transmission.

### Advantages of Block Coding

- Provides high error detection and correction capabilities
- Can be used with any type of data transmission
- Can be used with any type of channel

### Disadvantages of Block Coding

- Can be complex to implement
- Requires more bandwidth than other error detection and correction methods
- Requires more processing power than other error detection and correction methods

### Types of Block Codes

- **Cyclic Codes**: Cyclic codes are a type of block code that uses a cyclic shift to detect and correct errors. They are widely used in digital communication systems.
- **Non-Cyclic Codes**: Non-cyclic codes are a type of block code that uses a non-cyclic shift to detect and correct errors. They are less widely used than cyclic codes.

### Example of Block Coding

Suppose we have a data block of 8 bits that we want to transmit over a channel. We can add redundancy to each bit to provide higher error detection and correction capabilities. For example, we can use a (7,1) code, which adds 1 parity bit to each data bit.

| Bit | Parity Bit |
| --- | ---------- |
| 0   | 0          |
| 1   | 1          |
| 0   | 0          |
| 1   | 1          |
| 0   | 0          |
| 1   | 1          |
| 0   | 0          |
| 1   | 1          |

## Cyclic Codes

---

Cyclic codes are a type of block code that uses a cyclic shift to detect and correct errors. They are widely used in digital communication systems.

### Properties of Cyclic Codes

- **Periodicity**: Cyclic codes have a period of 2^t, where t is the number of parity bits.
- **Minimum Distance**: Cyclic codes have a minimum distance of 2^t - 1, which is the minimum number of bits that must be changed to detect an error.
- **Check Polynomial**: Cyclic codes use a check polynomial to detect and correct errors. The check polynomial is a polynomial that is used to calculate the parity bits.

### Example of a Cyclic Code

Suppose we have a data block of 8 bits that we want to transmit over a channel. We can use a (7,1) cyclic code to add redundancy to each bit. The check polynomial for this code is:

G(x) = x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1

We can calculate the parity bits using the check polynomial:

| Bit | Parity Bit |
| --- | ---------- |
| 0   | 0          |
| 1   | 0          |
| 0   | 0          |
| 1   | 1          |
| 0   | 1          |
| 1   | 0          |
| 0   | 0          |
| 1   | 1          |

## Non-Cyclic Codes

---

Non-cyclic codes are a type of block code that uses a non-cyclic shift to detect and correct errors. They are less widely used than cyclic codes.

### Properties of Non-Cyclic Codes

- **Minimum Distance**: Non-cyclic codes have a minimum distance of 2^t - 1, where t is the number of parity bits.
- **Check Polynomial**: Non-cyclic codes use a check polynomial to detect and correct errors. The check polynomial is a polynomial that is used to calculate the parity bits.

### Example of a Non-Cyclic Code

Suppose we have a data block of 8 bits that we want to transmit over a channel. We can use a (7,1) non-cyclic code to add redundancy to each bit. The check polynomial for this code is:

G(x) = x^7 + x^6 + x^4 + x^3 + x^2 + x + 1

We can calculate the parity bits using the check polynomial:

| Bit | Parity Bit |
| --- | ---------- |
| 0   | 0          |
| 1   | 1          |
| 0   | 0          |
| 1   | 0          |
| 0   | 1          |
| 1   | 1          |
| 0   | 1          |
| 1   | 0          |

## Conclusion

---

In this study material, we have covered the topics of block coding, cyclic codes, and non-cyclic codes. We have discussed the advantages and disadvantages of each type of code, as well as the properties and examples of each type of code. We have also provided a detailed explanation of how block codes, cyclic codes, and non-cyclic codes are used to detect and correct errors in digital communication systems.
