# Two Simple Hash Functions

=====================================

### Overview

This topic covers two foundational hash function constructions: the Simple Modulo Hash Function and the Davies-Meyer Hash Function. Both are cryptographically weak and meant as teaching tools to understand the design principles behind secure hash algorithms like SHA-256. They illustrate how fixed-size digests are produced from variable-length inputs.

### Key Points

- **Simple Modulo Hash:** Uses arithmetic addition and modulo operation to compress message blocks into a fixed-size digest
- **Simple Modulo Formula:** H*i = (H*{i-1} + M_i) mod p, where p is a large prime
- **Davies-Meyer Hash:** Uses a block cipher as the core compression function, with message blocks as keys
- **Davies-Meyer Formula:** H*i = E(M_i, H*{i-1}) XOR H\_{i-1} (feedforward XOR is crucial)
- **Feedforward Step:** XOR of cipher output with previous hash value provides pre-image resistance
- **Simple Modulo Weakness:** Highly susceptible to collisions; provides almost no diffusion or confusion
- **Davies-Meyer Strength:** Security relies on the strength of the underlying block cipher
- **Both Are Insecure:** Neither should be used in practice; they are conceptual foundations only

### Important Concepts

- Hash function requirements: pre-image resistance, second pre-image resistance, collision resistance
- Simple Hash steps: split message into blocks -> initialize IV -> iteratively apply (H + M) mod p -> output final hash
- Davies-Meyer steps: split message into key-sized blocks -> initialize H0 -> encrypt H*{i-1} with M_i as key -> XOR with H*{i-1}
- SHA-256 uses a Davies-Meyer-like compression function with a dedicated internal design
- The modulo hash is trivially reversible; the Davies-Meyer construction achieves one-wayness through cipher properties

### Notes

- Know both formulas and be able to work through small numerical examples
- Emphasize the feedforward XOR step as the critical difference making Davies-Meyer stronger
- For exams, clearly state that neither function is secure for real-world use -- they are educational tools
- Understand how these simple constructions lead to understanding SHA family algorithms
