Of course. Here is a comprehensive educational module on the Hill Cipher, tailored for  engineering students.

# Module 1: Classical Cryptography - The Hill Cipher

## 1. Introduction

The Hill cipher, invented by Lester S. Hill in 1929, is a classic polygraphic substitution cipher based on linear algebra. Unlike monoalphabetic ciphers like Caesar or Shift cipher that encrypt one letter at a time, the Hill cipher encrypts blocks of `n` letters simultaneously, making it more secure against frequency analysis attacks. Its strength lies in its use of matrix operations for both encryption and decryption, making it a fascinating bridge between mathematics (linear algebra) and cryptography.

## 2. Core Concepts

### 2.1. The Basic Idea
The core idea is to treat a group of letters as a vector and transform it into another vector (the ciphertext) using a key matrix. The transformation is a linear operation: multiplication of the key matrix by the plaintext vector, modulo 26.

### 2.2. Key Components
1.  **Key Matrix (`K`)**: A randomly chosen `n x n` square matrix that serves as the secret key. For the cipher to be decryptable, this matrix must be **invertible modulo 26**. This means its determinant must have a multiplicative inverse modulo 26 (i.e., `gcd(det(K), 26) = 1`).

2.  **Plaintext (`P`)**: The original message. It is divided into blocks (or vectors) of size `n`. If the last block is incomplete, it is padded with a predetermined letter (like 'X').

3.  **Ciphertext (`C`)**: The encrypted message. Each block of ciphertext is derived from a corresponding block of plaintext.

4.  **Modulo 26**: Since we are working with the 26-letter English alphabet (A=0, B=1, ..., Z=25), all arithmetic operations are performed modulo 26.

### 2.3. Encryption Process
The encryption of a single block of plaintext is given by the linear equation:
`C = K * P mod 26`

Where:
*   `C` is a column vector representing the ciphertext block.
*   `K` is the `n x n` key matrix.
*   `P` is a column vector representing the plaintext block.

**Steps:**
1.  Choose a key matrix `K` of size `n x n`.
2.  Convert the plaintext message into a numerical sequence (A=0, B=1, ..., Z=25).
3.  Split this sequence into blocks of length `n`.
4.  For each block `P`, perform the matrix multiplication `K * P`.
5.  Take the result modulo 26 to get the ciphertext vector `C`.
6.  Convert the numbers back to letters.

### 2.4. Decryption Process
Decryption is the reverse operation, performed using the **modular inverse** of the key matrix (`K⁻¹`).
`P = K⁻¹ * C mod 26`

**Steps:**
1.  Find the inverse of the key matrix `K` modulo 26. This involves calculating the determinant, the modular inverse of the determinant, the matrix of minors, cofactors, and adjugate. The formula is:
    `K⁻¹ = (det(K))⁻¹ * adj(K) mod 26`
2.  Convert the ciphertext into numerical vectors of length `n`.
3.  For each ciphertext vector `C`, multiply it by `K⁻¹`.
4.  Take the result modulo 26 to recover the original plaintext vector `P`.

## 3. Example (2x2 Hill Cipher)

Let's encrypt the word "" using a 2x2 key matrix.

**Key Matrix (K):**
`K = [ [3, 3] `
`      [2, 5] ]`

**Step 1: Check if the key is valid.**
Determinant, `det(K) = (3*5) - (3*2) = 15 - 6 = 9`.
`gcd(9, 26) = 1`. Since 1 is the gcd, 9 has a multiplicative inverse modulo 26 (which is 3, because 9*3=27 ≡ 1 mod 26). The key is valid.

**Step 2: Convert "" to numbers.**
V -> 21, T -> 19, U -> 20.
We have two blocks: `P1 = [21, 19]^T` and `P2 = [20]`. Since our block size is 2, the second block is incomplete. We pad it with 'X' (23). So the second block becomes `P2 = [20, 23]^T`.

**Step 3: Encrypt the first block (`P1 = [21, 19]^T`)**
`C1 = K * P1 mod 26`
`C1 = [ [3, 3] * [21]   mod 26 = [ (3*21 + 3*19) ] mod 26 = [ (63 + 57) ] mod 26 = [120] mod 26 = [16] `
`      [2, 5]   [19] ]           [ (2*21 + 5*19) ]         [ (42 + 95) ]         [137]         [7]  `
So, `C1 = [16, 7]^T` -> Q, H.

**Step 4: Encrypt the second block (`P2 = [20, 23]^T`)**
`C2 = K * P2 mod 26`
`C2 = [ [3, 3] * [20]   mod 26 = [ (3*20 + 3*23) ] mod 26 = [ (60 + 69) ] mod 26 = [129] mod 26 = [25] `
`      [2, 5]   [23] ]           [ (2*20 + 5*23) ]         [ (40 + 115)]         [155]         [25] `
So, `C2 = [25, 25]^T` -> Z, Z.

**Step 5: Final Ciphertext**
The encrypted blocks are "QH" and "ZZ". Therefore, "" encrypted to **"QHZZ"**.

*Decryption would require finding `K⁻¹` and applying it to "QH" and "ZZ", which would yield back "VT" and "UX", confirming the original padded message.*

## 4. Key Points & Summary

*   **Polygraphic Cipher**: Encrypts multiple letters (`n`-grams) at a time, obscuring letter frequency patterns.
*   **Linear Algebra Foundation**: Relies entirely on matrix multiplication and modular arithmetic.
*   **Key is a Matrix**: The secret key is an `n x n` invertible matrix modulo 26.
*   **Strength**: The size of the key space grows with `n`, making brute-force attacks difficult for larger `n`. It was a significant advancement over simpler ciphers.
*   **Weakness**: It is **vulnerable to known-plaintext attacks**. If an attacker knows `n` pairs of plaintext and ciphertext vectors, they can often solve for the key matrix `K`. It is also linear and lacks diffusion, making it vulnerable to more modern cryptanalysis.
*   **Legacy**: While not used in modern cryptography due to its vulnerabilities, the Hill cipher is an important pedagogical tool for understanding the application of linear algebra in cryptography and the concepts of block ciphers.