# Cryptographic Hash Functions

## Introduction to Hash Functions

A cryptographic hash function is a fundamental building block in modern cryptography. It is a mathematical algorithm that takes an input (or 'message') of arbitrary length and returns a fixed-size string of bytes, typically a digest that appears random. The output is called the hash value, message digest, digital fingerprint, or simply hash.

Hash functions are used in various applications, including digital signatures, message authentication codes (MACs), password storage, and blockchain technology. Their primary purpose is to ensure data integrity—verifying that data has not been altered.

## Properties of Cryptographic Hash Functions

For a hash function to be considered cryptographically secure, it must possess the following properties:

### 1. Pre-image Resistance (One-Wayness)

Given a hash value `h`, it should be computationally infeasible to find any input `m` such that `hash(m) = h`. In simpler terms, it should be easy to compute the hash from the input, but virtually impossible to reverse the process.

```
Input: "Hello World"  --> Hash Function --> Output: a591a6d40bf420404a011733...
( Easy )

Input: ?              <-- Hash Function <-- Output: a591a6d40bf420404a011733...
( Computationally Infeasible )
```

### 2. Second Pre-image Resistance (Weak Collision Resistance)

Given an input `m1`, it should be computationally infeasible to find a different input `m2` (where `m1 ≠ m2`) such that `hash(m1) = hash(m2)`. This protects against an attacker finding an alternative message with the same fingerprint.

```
Given:
m1 = "Pay John $100"  --> Hash --> h1
Find:
m2 = "Pay Paul $999"  --> Hash --> h1
( Must be computationally infeasible )
```

### 3. Collision Resistance (Strong Collision Resistance)

It should be computationally infeasible to find any two distinct inputs `m1` and `m2` such that `hash(m1) = hash(m2)`. A collision is when two different inputs produce the same output hash.

```
Find ANY:
m1 = "Document A" --> Hash --> h
m2 = "Document B" --> Hash --> h
( Must be computationally infeasible )
```

### 4. Deterministic

The same input will always produce the same hash output.

### 5. Avalanche Effect

A small change in the input (even a single bit) should produce a drastic change in the output hash, making the new hash appear uncorrelated to the old hash.

```
Input: "Hello World"   --> Hash --> b10a8db164e0754105b7a99...
Input: "Hello World!"  --> Hash --> 7f83b1657ff1fc53b92dc18...
( Completely different outputs )
```

### 6. Speed

The computation of the hash value for any given message should be fast. This is crucial for efficiency in various applications.

## Structure of Hash Functions: The Merkle-Damgård Construction

Many famous hash functions (like MD5, SHA-1, and SHA-2) are built using the **Merkle-Damgård iterated structure**. This design processes the input message in fixed-size blocks.

```
+-----------------+   +-----------------+   +-----------------+
|  Initialization |   |  Compression   |   |  Compression   |
|     Vector (IV) +-->+    Function    +-->+    Function    +--> ... --> Final Hash
+-----------------+   +-------+-------+   +-------+-------+
                              ^                    ^
                              |                    |
                        +-----+------+       +-----+------+
                        | Message    |       | Message    |
                        | Block 1    |       | Block 2    |
                        +------------+       +------------+
```

1.  **Padding:** The message is padded so its length is a multiple of the block size. Padding includes the original message length.
2.  **Initialization:** A fixed initial value (IV), or initial hash value, is set.
3.  **Processing:** Each message block is processed sequentially with a **compression function**. The compression function takes the current hash value and the next message block and produces a new hash value.
    `H_i = f(H_{i-1}, M_i)`
4.  **Output:** The output after processing the last block is the final hash value.

## Common Hash Algorithms

| Algorithm | Output Size (bits) | Status     | Notes                                                             |
| :-------- | :----------------- | :--------- | :---------------------------------------------------------------- |
| **MD5**   | 128                | **Broken** | Vulnerable to collisions. Not suitable for security applications. |
| **SHA-1** | 160                | **Broken** | Theoretical collisions found. Being phased out.                   |
| **SHA-2** | 224, 256, 384, 512 | **Secure** | Family includes SHA-256 and SHA-512. Widely used.                 |
| **SHA-3** | 224, 256, 384, 512 | **Secure** | Uses Keccak sponge construction, not Merkle-Damgård.              |

## Applications of Hash Functions

### 1. Data Integrity Verification

The most straightforward application. The hash of a file is computed and stored. Later, the hash is recomputed and compared to the stored value. If they match, the file is unaltered.

```
Sender:
File --> Hash --> Digest
Send File + Digest

Receiver:
Received File --> Hash --> New Digest
Compare New Digest vs. Received Digest
```

### 2. Password Storage

Systems store the hash of a user's password instead of the plaintext password. During login, the hash of the entered password is compared to the stored hash. To defend against precomputed attacks (rainbow tables), a **salt** (a random value) is added to the password before hashing.

```
Storing Password:
User Password: "myp@ss123"
Generate Random Salt: "a1b2c3"
Combine: "myp@ss123a1b2c3"
Hash: SHA-256("myp@ss123a1b2c3") = h
Store: h + Salt

Verifying Login:
Entered Password: "myp@ss123"
Lookup Stored Salt: "a1b2c3"
Combine: "myp@ss123a1b2c3"
Hash: SHA-256("myp@ss123a1b2c3") = h_new
Compare h_new vs. Stored h
```

### 3. Digital Signatures

Digital signature schemes often sign the hash of a message rather than the message itself. This is more efficient for large messages and maintains the security properties needed for non-repudiation and authentication.

```
Signing:
Large Message M --> Hash --> Digest
Sign Digest with Private Key --> Signature

Verifying:
Receive M + Signature
M --> Hash --> Digest
Verify Signature on Digest using Public Key
```

### 4. Blockchain and Cryptocurrency

Hash functions are the core of blockchain technology. They are used to create block hashes, link blocks together (each block contains the hash of the previous block), and in the proof-of-work consensus algorithm (mining).

```
Block 1: Data + Previous Hash (0) + Nonce --> Hash --> Hash1
Block 2: Data + Previous Hash (Hash1) + Nonce --> Hash --> Hash2
Block 3: Data + Previous Hash (Hash2) + Nonce --> Hash --> Hash3
```

## Hash Functions vs. Encryption

It is critical to understand the difference:

- **Encryption (AES, RSA):** A two-way function. Data is encrypted into ciphertext and can be decrypted back to plaintext using a key.
- **Hashing (SHA-256, MD5):** A one-way function. Data is hashed into a digest, which cannot be reversed to retrieve the original data.

## Exam Tips

1.  **Memorize the Properties:** Be able to list and explain pre-image resistance, second pre-image resistance, and collision resistance. These are frequently tested.
2.  **Understand the Construction:** Knowing the steps of the Merkle-Damgård construction (Padding, IV, Compression Function) can be valuable for diagram-based questions.
3.  **Application Scenarios:** Be prepared to describe how hash functions are used in specific scenarios like password storage (mention salting!) and digital signatures.
4.  **Compare and Contrast:** You may be asked to differentiate between encryption and hashing. Remember: encryption is reversible with a key; hashing is not.
5.  **Algorithm Awareness:** Know that MD5 and SHA-1 are considered broken and that SHA-256 (part of SHA-2) is a current standard. Being aware of SHA-3 is a bonus.
