# Hill Cipher

=====================================

### Overview

The Hill Cipher, invented by Lester S. Hill in 1929, is a polygraphic substitution cipher based on linear algebra. It encrypts blocks of m characters simultaneously using matrix multiplication modulo 26, making it more resistant to frequency analysis than monoalphabetic ciphers.

### Key Points

- **Polygraphic Cipher:** Encrypts m letters at a time as a block, not one letter at a time.
- **Key Matrix:** The key is an m x m invertible matrix K; gcd(det(K), 26) must equal 1.
- **Encryption:** C = (K \* P) mod 26, where P is the plaintext vector and C is the ciphertext vector.
- **Decryption:** P = (K^-1 \* C) mod 26, using the modular inverse of the key matrix.
- **Modular Inverse:** K^-1 = (det(K))^-1 \* adj(K) mod 26.
- **Strength:** Hides single-letter frequency patterns; large key space for bigger block sizes.
- **Known Plaintext Attack:** Highly vulnerable; knowing one plaintext-ciphertext pair of m letters can reveal the key.
- **Academically Important:** Not used in modern practice due to its linear nature but foundational for understanding algebra in cryptography.

### Important Concepts

- det(K) mod 26 must be coprime with 26 (i.e., gcd(det(K), 26) = 1) for decryption to work.
- Multiplicative inverse: find d^-1 such that d \* d^-1 = 1 mod 26.
- For 2x2 matrix [[a,b],[c,d]]: det = ad - bc; adj = [[d,-b],[-c,a]] mod 26.
- Padding with a dummy letter (e.g., X) is needed if plaintext length is not a multiple of m.

### Notes

- Practice 2x2 matrix encryption/decryption with small numbers for exam calculations.
- Always verify the key matrix is invertible mod 26 before proceeding.
- The Hill cipher is fully linear, which is its biggest weakness; it lacks confusion and diffusion of modern ciphers.
