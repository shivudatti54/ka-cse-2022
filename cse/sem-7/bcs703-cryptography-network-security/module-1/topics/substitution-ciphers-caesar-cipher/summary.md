# Substitution Ciphers: Caesar Cipher

=====================================

### Overview

The Caesar Cipher is one of the simplest and oldest substitution ciphers, named after Julius Caesar. It shifts each letter in the plaintext by a fixed number of positions in the alphabet. The Monoalphabetic Cipher generalizes this by using any random permutation of the 26 letters. Both are monoalphabetic ciphers that use a single fixed substitution alphabet.

### Key Points

- **Caesar Cipher Encryption:** C = (P + K) mod 26, where K is the shift value (1-25).
- **Caesar Cipher Decryption:** P = (C - K) mod 26.
- **Caesar Key Space:** Only 25 possible keys; trivially broken by brute force.
- **Monoalphabetic Cipher:** Uses a random permutation of the alphabet; key space is 26! (approximately 4 x 10^26).
- **Frequency Analysis:** Both ciphers preserve letter frequency distributions, making them vulnerable.
- **English Letter Frequencies:** E (12.02%), T (9.10%), A (8.12%), O (7.68%), I (7.31%) are the most common.
- **Brute-Force vs. Frequency Analysis:** Caesar is broken by brute force (25 keys); Monoalphabetic requires frequency analysis.

### Important Concepts

- Both Caesar and Monoalphabetic are monoalphabetic (single substitution alphabet for entire message).
- Frequency analysis: most common ciphertext letter likely corresponds to 'E'.
- A large key space (26!) does not guarantee security when frequency patterns are preserved.
- Common digraphs (TH, HE, IN, ER) and trigraphs (THE, ING, AND) aid in breaking monoalphabetic ciphers.
- These weaknesses led to the development of polyalphabetic ciphers (Vigenere).

### Notes

- Memorize the Caesar formulas: C = (P + K) mod 26 and P = (C - K) mod 26.
- Show work in tables for exam encryption/decryption problems to avoid calculation errors.
- Be prepared to compare Caesar (25 keys, shift) vs. Monoalphabetic (26! keys, random mapping) in essay questions.
