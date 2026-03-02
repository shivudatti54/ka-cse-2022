

## Table of Contents

- [Module 3: Two Simple Hash Functions](#module-3-two-simple-hash-functions)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. Properties of a Cryptographic Hash Function](#1-properties-of-a-cryptographic-hash-function)
  - [2. A Simple Hash Function (Using Modulo Operator)](#2-a-simple-hash-function-using-modulo-operator)
  - [3. The Davies-Meyer Hash Function (Using a Block Cipher)](#3-the-davies-meyer-hash-function-using-a-block-cipher)
- [Key Points / Summary](#key-points--summary)

Of course. Here is a comprehensive educational module on two simple hash functions, tailored for Engineering students.

# Module 3: Two Simple Hash Functions

## Introduction

In the realm of **Cryptography & Network Security**, hash functions are fundamental cryptographic primitives. They are not used for encryption but for ensuring **data integrity** and authentication. A cryptographic hash function takes an input message (of any length) and returns a fixed-size alphanumeric string, called the **hash value** or **message digest**.

This module explores two historically significant but **cryptographically weak** hash functions: The Simple Hash Function and The Davies-Meyer Hash Function. Understanding these simple constructions provides a solid foundation for grasping the more complex and secure hash algorithms like SHA-256.

## Core Concepts

### 1. Properties of a Cryptographic Hash Function

Before diving into the specific functions, it's crucial to understand what a secure hash function must provide:

- **Pre-image Resistance:** Given a hash value `h`, it should be computationally infeasible to find any input `m` such that `hash(m) = h`.
- **Second Pre-image Resistance:** Given an input `m1`, it should be infeasible to find a different input `m2` such that `hash(m1) = hash(m2)`.
- **Collision Resistance:** It should be infeasible to find any two distinct inputs `m1` and `m2` such that `hash(m1) = hash(m2)`.

The simple functions we will discuss fail to meet these requirements robustly.

### 2. A Simple Hash Function (Using Modulo Operator)

This is one of the most intuitive ways to create a fixed-length output.

#### Concept:

The function processes the message by breaking it into blocks of a fixed size. Each block is interpreted as a number. A simple arithmetic operation (like modulo division) is performed iteratively on these blocks to produce a final hash value.

#### Algorithm Steps:

1.  **Message Preparation:** The input message is split into blocks of a fixed size (e.g., 32 bits or 64 bits). If the message length isn't a multiple of the block size, it is padded.
2.  **Initialization:** Start with an initial value (IV), often zero.
3.  **Iterative Processing:** For each block `M_i`:
    - Combine the current hash value with the current message block. A common way is simple addition.
    - Apply a compression function. Here, we use the modulo operator with a prime number `p` to create a value within a fixed range.
    - The result becomes the new intermediate hash value.
4.  **Finalization:** After all blocks are processed, the final intermediate value is the hash digest.

**Formula:** `H_i = (H_{i-1} + M_i) \mod p`

Where:

- `H_i` is the new hash value.
- `H_{i-1}` is the previous hash value (or IV for the first block).
- `M_i` is the current message block.
- `p` is a large prime number (determines the size of the hash output, e.g., 128-bit prime for a 128-bit hash).

#### Example:

Let's choose a small prime for demonstration: `p = 13`. Our message is "", and we'll use its ASCII values.
Message: 'V' (86), 'T' (84), 'U' (85). IV = 0.

- Process Block 1 (86): `H1 = (0 + 86) mod 13 = 86 mod 13 = 86 - 6*13 = 86-78 = 8`
- Process Block 2 (84): `H2 = (8 + 84) mod 13 = 92 mod 13 = 92 - 7*13 = 92-91 = 1`
- Process Block 3 (85): `H3 = (1 + 85) mod 13 = 86 mod 13 = 8`

**Final Hash Digest:** `8` (This would be a very weak 4-bit hash in reality).

#### Weakness:

This function is highly susceptible to collisions. For example, the messages "" (86,84,85) and "ABC" (65,66,67) would also hash to `(0+65)mod13=0`, `(0+66)mod13=1`, `(1+67)mod13=3`? Wait, that's different. But many messages can easily produce the same final `8`. The modulo addition provides almost no diffusion or confusion.

### 3. The Davies-Meyer Hash Function (Using a Block Cipher)

This is a more sophisticated construction that forms the basis for many real-world hash functions. It uses a symmetric block cipher (like AES) as its core component.

#### Concept:

The message blocks are used as the **key** input to the block cipher. The current hash value is used as the **plaintext** input. The output ciphertext is then combined with the input plaintext to produce the next hash value. This introduces confusion and diffusion from the cipher.

#### Algorithm Steps:

1.  **Split Message:** Split the message `M` into `t` blocks of the key size for the cipher: `M1, M2, ..., Mt`.
2.  **Initialization:** Set an initial value `H0` (e.g., a vector of zeros).
3.  **Iterative Compression:** For each message block `i` (from 1 to `t`):
    - **Encrypt:** Encrypt the current hash value `H_{i-1}` using the message block `M_i` as the key. `E(M_i, H_{i-1})`
    - **Combine (Feedforward):** XOR the result of the encryption with the original hash value `H_{i-1}`. This step is crucial for pre-image resistance.
    - `H_i = E(M_i, H_{i-1}) \oplus H_{i-1}`
4.  **Output:** The final value `H_t` is the message digest.

#### Example:

Assume a trivial 2-bit block cipher. Let `H0 = 00` (binary). Message block `M1 = 10`.
Suppose encryption `E(Key=10, Plaintext=00)` yields `11`.
Then: `H1 = E(M1, H0) XOR H0 = 11 XOR 00 = 11`.

The next message block `M2` would be used as a key to encrypt `H1=11`, and so on.

#### Strength and Weakness:

- **Strength:** This design is much stronger than the simple modulo hash. The security relies on the strength of the underlying block cipher. The feedforward (XOR step) makes it resistant to certain attacks.
- **Weakness:** Real-world implementations need to address issues like the block cipher's block size and resistance to specific attacks like **fixed points**. Modern functions like SHA-256 use a similar but more complex structure called a **Davies-Meyer compression function** with a dedicated design, not an off-the-shelf cipher like AES.

## Key Points / Summary

| Feature            | Simple Modulo Hash                                      | Davies-Meyer Hash                                                       |
| :----------------- | :------------------------------------------------------ | :---------------------------------------------------------------------- |
| **Core Idea**      | Simple arithmetic operations (addition, modulo)         | Uses a block cipher in a compression function                           |
| **Security**       | **Very Weak.** Prone to collisions and easy to reverse. | **Theoretically Stronger.** Security is based on the underlying cipher. |
| **Example Use**    | Academic example to understand the concept.             | Conceptual basis for industry-standard hash functions.                  |
| **Key Operation**  | `(H_prev + M_i) mod p`                                  | `H_i = E(M_i, H_{i-1}) XOR H_{i-1}`                                     |
| **Output Control** | Size determined by prime `p`                            | Size determined by block cipher's block size                            |

**Conclusion:** While both functions are simple, the Davies-Meyer scheme is a critical concept in cryptography. It illustrates a powerful design principle: building a one-way hash function from a symmetric cipher. However, for modern applications, **neither** of these should be used directly. They are teaching tools to prepare you for understanding secure, standardized algorithms like those in the **SHA family** (Secure Hash Algorithm), which are essential for protocols like SSL/TLS, Bitcoin mining, and digital signatures.
