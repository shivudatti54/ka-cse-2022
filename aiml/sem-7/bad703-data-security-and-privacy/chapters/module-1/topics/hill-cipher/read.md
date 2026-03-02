Of course. Here is a comprehensive educational module on the Hill Cipher for  engineering students.

# Module 1: Classical Encryption Techniques - Hill Cipher

## 1. Introduction

The Hill cipher, invented by Lester S. Hill in 1929, is a classic polygraphic substitution cipher based on linear algebra. Unlike simpler ciphers like Caesar or Shift cipher that encrypt one letter at a time (monoalphabetic), the Hill cipher encrypts blocks of letters simultaneously. This makes it more secure against frequency analysis attacks, as it obscures the frequencies of individual letters. Its core operation relies on matrix multiplication modulo 26, making it a foundational example of applying mathematics to cryptography.

## 2. Core Concepts

### 2.1 The Key Matrix
The heart of the Hill cipher is a square, invertible matrix `K` modulo 26, known as the key matrix. For a cipher that encrypts `m` letters at a time, the key is an `m x m` matrix. The elements of this matrix are integers from 0 to 25 (corresponding to A=0, B=1, ..., Z=25).

**Crucial Requirement:** The key matrix must be *invertible modulo 26*. This means its determinant must be non-zero and, most importantly, must have a multiplicative inverse modulo 26. In other words, `gcd(det(K), 26) = 1`.

### 2.2 Encryption Process
The encryption process involves converting plaintext into column vectors and multiplying them by the key matrix.

1.  **Choose Group Size (m):** Decide on the size of the block, `m` (e.g., m=2 for digraphic, m=3 for trigraphic).
2.  **Form Numeral Vectors:** Convert `m` letters of plaintext into their numerical equivalents (A=0, B=1, ..., Z=25) to form a column vector `P`.
3.  **Matrix Multiplication:** Multiply the key matrix `K` by the plaintext vector `P`.
    `C = K * P mod 26`
    where `C` is the resulting ciphertext vector.
4.  **Convert to Text:** Convert the numerical values of the ciphertext vector `C` back into letters.

### 2.3 Decryption Process
Decryption uses the inverse of the key matrix, denoted `K⁻¹`.

1.  **Find the Inverse Matrix:** Calculate the modular inverse of the key matrix, `K⁻¹ mod 26`.
2.  **Form Numeral Vectors:** Convert the ciphertext block into a numerical vector `C`.
3.  **Apply Inverse Matrix:** Multiply the inverse key matrix by the ciphertext vector.
    `P = K⁻¹ * C mod 26`
4.  **Convert to Text:** Convert the resulting numerical vector `P` back to plaintext letters.

**Calculating `K⁻¹ mod n`:**
The formula for the inverse of a matrix `K` is:
`K⁻¹ = (det(K))⁻¹ * adj(K) mod 26`
Where `(det(K))⁻¹` is the **modular multiplicative inverse** of the determinant modulo 26.

## 3. Example (2x2 Hill Cipher)

Let's encrypt the message "" using a 2x2 key matrix. (Note: We'll pad the message if its length isn't a multiple of `m`).

**Key Matrix (K):**
`K = [[3, 3], [2, 5]]`

**Step 1: Verify the Key is Valid**
First, check if the key is invertible modulo 26.
`det(K) = (3*5) - (3*2) = 15 - 6 = 9`
Now, check if `gcd(9, 26) = 1`. Since it is, 9 has a multiplicative inverse mod 26. The inverse of 9 mod 26 is 3, because `(9 * 3) mod 26 = 27 mod 26 = 1`.

**Step 2: Encrypt the Message**
Plaintext: "". We'll break it into blocks of 2: "VT", and "U" needs padding. We add a common letter (e.g., 'X') to make "UX".

*   **Block 1: "VT"**
    *   V = 21, T = 19. So vector `P1 = [[21], [19]]`
    *   `C1 = K * P1 = [[3, 3], [2, 5]] * [[21], [19]] = [[(3*21 + 3*19)], [(2*21 + 5*19)]] = [[(63 + 57)], [(42 + 95)]] = [[120], [137]]`
    *   Now, `mod 26`: `120 mod 26 = 16 (Q)`, `137 mod 26 = 7 (H)`
    *   Ciphertext for "VT" is "QH"

*   **Block 2: "UX"**
    *   U = 20, X = 23. So vector `P2 = [[20], [23]]`
    *   `C2 = K * P2 = [[3, 3], [2, 5]] * [[20], [23]] = [[(3*20 + 3*23)], [(2*20 + 5*23)]] = [[(60 + 69)], [(40 + 115)]] = [[129], [155]]`
    *   `mod 26`: `129 mod 26 = 25 (Z)`, `155 mod 26 = 25 (Z)`
    *   Ciphertext for "UX" is "ZZ"

**Final Ciphertext:** "QH ZZ"

**Step 3: Decrypt the Ciphertext "QHZZ"**
First, find `K⁻¹`.
We have `det(K) = 9` and `adj(K) = [[5, -3], [-2, 3]] = [[5, 23], [24, 3]]` (after converting negative numbers mod 26).
`K⁻¹ = (9⁻¹ mod 26) * adj(K) = 3 * [[5, 23], [24, 3]] = [[15, 69], [72, 9]]`
Now, `mod 26`: `K⁻¹ = [[15, 17], [20, 9]]` (since `69 mod 26 = 17`, `72 mod 26 = 20`).

Now, decrypt the first block "QH" (16, 7):
`P1 = K⁻¹ * C1 = [[15, 17], [20, 9]] * [[16], [7]] = [[(15*16 + 17*7)], [(20*16 + 9*7)]] = [[(240 + 119)], [(320 + 63)]] = [[359], [383]]`
`mod 26`: `359 mod 26 = 21 (V)`, `383 mod 26 = 19 (T)`. We get back "VT".

## 4. Key Points & Summary

*   **Polygraphic Cipher:** Encrypts multiple letters (`m`-grams) at once, making it resistant to simple frequency analysis.
*   **Linear Algebra Foundation:** The encryption and decryption processes are simple matrix multiplications modulo 26.
*   **Key is a Matrix:** The secret key is an `m x m` matrix that must be invertible modulo 26. This means its determinant and 26 must be coprime (`gcd(det(K), 26) = 1`).
*   **Strength:** The larger the size `m` of the key matrix, the stronger the cipher becomes. It was a significant advance over previous ciphers.
*   **Weakness:** It is vulnerable to known-plaintext attacks. If an attacker has access to both a plaintext block `P` and its corresponding ciphertext block `C`, they can set up the equation `C = K * P` and potentially solve for the key matrix `K`.
*   **Not Used in Modern Cryptography:** While historically important, the Hill cipher is not used today due to its vulnerabilities and inefficiency compared to modern algorithms like AES and RSA. However, it remains a brilliant teaching tool for understanding the application of linear algebra in cryptography.