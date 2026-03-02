

## Table of Contents

- [Module 1: Classical Encryption Techniques](#module-1-classical-encryption-techniques)
- [Topic: Hill Cipher](#topic-hill-cipher)
  - [1. Introduction](#1-introduction)
  - [2. Core Concepts](#2-core-concepts)
  - [3. Worked Example (2x2 Hill Cipher)](#3-worked-example-2x2-hill-cipher)
  - [4. Key Points & Summary](#4-key-points--summary)

Of course. Here is a comprehensive educational module on the Hill Cipher for Engineering students.

# Module 1: Classical Encryption Techniques

## Topic: Hill Cipher

### 1. Introduction

The Hill Cipher, invented by Lester S. Hill in 1929, is a classic polygraphic substitution cipher based on linear algebra. Unlike simple substitution ciphers that encrypt one character at a time (monographic), the Hill Cipher encrypts blocks of `m` characters simultaneously. This makes it significantly more secure against frequency analysis attacks, as it obscures the frequency distributions of single letters. Its security relies heavily on the use of a key matrix and operations in modular arithmetic.

### 2. Core Concepts

The Hill Cipher operates through three main steps: key generation, encryption, and decryption. The entire process works modulo 26, corresponding to the 26 letters of the English alphabet.

#### **2.1 Key Generation**

The key is an `m x m` invertible matrix **K**, where `m` is the size of the block to be encrypted. For the matrix to be invertible modulo 26, its determinant must be coprime to 26 (i.e., `gcd(det(K), 26) = 1`). This ensures a multiplicative inverse for the determinant exists modulo 26, which is crucial for decryption.

_Example:_ For `m=2`, a valid key could be:
**K** = `[ [3, 3] , [2, 5] ]`
Let's check: `det(K) = (3*5 - 3*2) = 15 - 6 = 9`. `gcd(9, 26) = 1`. ✅ Valid key.

#### **2.2 Encryption**

Encryption involves converting plaintext into numerical vectors and then multiplying them by the key matrix.

1.  **Convert plaintext to numbers:** Assign each letter a number (A=0, B=1, ..., Z=25).
2.  **Form plaintext vectors:** Group the numbers into column vectors **P** of size `m`.
3.  **Multiply by key matrix:** Compute the ciphertext vector **C** = **K** \* **P** mod 26.
4.  **Convert to letters:** Convert the resulting numbers back into letters.

#### **2.3 Decryption**

Decryption is the reverse process, using the inverse of the key matrix.

1.  **Find the inverse matrix:** Compute the modular inverse of the key matrix, **K⁻¹** mod 26.
2.  **Convert ciphertext to numbers.**
3.  **Form ciphertext vectors:** Group into vectors **C** of size `m`.
4.  **Multiply by inverse key:** Recover the plaintext vector **P** = **K⁻¹** \* **C** mod 26.
5.  **Convert to letters.**

**Finding K⁻¹ mod 26:**

1.  Calculate the determinant `d = det(K) mod 26`.
2.  Find `d⁻¹ mod 26`, the multiplicative inverse of `d`. This is a number such that `d * d⁻¹ ≡ 1 mod 26`.
3.  Compute the adjugate matrix of **K**, `adj(K)`.
4.  The inverse is: **K⁻¹ = (d⁻¹ \* adj(K)) mod 26**.

### 3. Worked Example (2x2 Hill Cipher)

Let's encrypt the word "" using the key **K** = `[ [3, 3], [2, 5] ]`.

- **Plaintext:** ``
- **Numerical Representation:** V=21, T=19, U=20.
  We need an even number of characters. Let's add a dummy letter 'X' (23) to make ` X` -> `[21, 19]` and `[20, 23]`.

**Encrypt first block (VI):**

1.  Plaintext vector **P₁** = `[21, 19]ᵀ`
2.  **C₁ = K \* P₁** = `[ [3, 3], [2, 5] ] * [21, 19]ᵀ` = `[ (3*21 + 3*19), (2*21 + 5*19) ]` = `[ (63+57), (42+95) ]` = `[120, 137]`
3.  `[120 mod 26, 137 mod 26]` = `[120 - 4*26, 137 - 5*26]` = `[120-104, 137-130]` = `[16, 7]`
4.  `16 = Q`, `7 = H`. So, `VI -> QH`

**Encrypt second block (UX):**

1.  Plaintext vector **P₂** = `[20, 23]ᵀ`
2.  **C₂ = K \* P₂** = `[ [3, 3], [2, 5] ] * [20, 23]ᵀ` = `[ (3*20 + 3*23), (2*20 + 5*23) ]` = `[ (60+69), (40+115) ]` = `[129, 155]`
3.  `[129 mod 26, 155 mod 26]` = `[129-4*26, 155-5*26]` = `[129-104, 155-130]` = `[25, 25]`
4.  `25 = Z`. So, `UX -> ZZ`

- **Final Ciphertext:** `QH ZZ`

**Decryption (Verification):**
We need **K⁻¹**. From earlier, `d = det(K) = 9`, `d⁻¹ mod 26` is the number that satisfies `9 * d⁻¹ ≡ 1 mod 26`. Testing multiples: `9*3=27≡1 mod 26`. So `d⁻¹ = 3`.
Adjugate of **K** is `adj(K) = [ [5, -3], [-2, 3] ]` = `[ [5, 23], [24, 3] ] mod 26`.
**K⁻¹ = 3 \* [ [5, 23], [24, 3] ]** = `[ [15, 69], [72, 9] ] mod 26` = `[ [15, 17], [20, 9] ]`.

Decrypt `QH (16,7)`:
**P = K⁻¹ \* C** = `[ [15, 17], [20, 9] ] * [16, 7]ᵀ` = `[ (15*16 + 17*7), (20*16 + 9*7) ]` = `[ (240 + 119), (320 + 63) ]` = `[359, 383] mod 26` = `[359-13*26, 383-14*26]` = `[359-338, 383-364]` = `[21, 19]` -> `V, T`. ✅

### 4. Key Points & Summary

- **Polygraphic Cipher:** Encrypts `m` letters at a time, making it resistant to simple frequency analysis.
- **Linear Algebra Foundation:** The core operation is matrix multiplication modulo 26.
- **Key is a Matrix:** The key is an `m x m` invertible matrix **K** with `gcd(det(K), 26) = 1`.
- **Strength:**
  - Hides letter frequency better than monoalphabetic ciphers.
  - The number of possible keys is large for bigger `m`.
- **Weaknesses:**
  - **Known Plaintext Attack:** It is highly vulnerable. If an attacker knows both plaintext (`P`) and ciphertext (`C`) for one block, they can easily solve for **K** (`C = K * P`).
  - **Fully Linear:** This linearity is its biggest weakness, as it does not provide diffusion and confusion as modern ciphers do.
- **Not Used in Modern Practice:** The Hill Cipher is academically important but is not used for modern security purposes due to its vulnerabilities. It serves as a great introduction to the application of algebra in cryptography.
