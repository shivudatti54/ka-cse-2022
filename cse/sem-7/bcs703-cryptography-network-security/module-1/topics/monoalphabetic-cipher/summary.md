# Monoalphabetic Cipher

=====================================

### Overview

The Monoalphabetic Cipher is a substitution cipher where each plaintext letter is mapped to a fixed, unique ciphertext letter for the entire message. It uses a single substitution alphabet, which is an arbitrary permutation of the 26 letters. Despite its massive key space, it is easily broken using frequency analysis.

### Key Points

- **Key:** A random permutation of the 26-letter alphabet defining the substitution mapping.
- **Key Space:** 26! (approximately 4 x 10^26) possible keys, making brute-force infeasible.
- **Encryption:** C = E(P), where E is the substitution mapping; each letter always maps to the same ciphertext letter.
- **Decryption:** P = D(C), using the inverse of the encryption mapping.
- **Fatal Weakness:** Preserves the frequency distribution of the original language, making it vulnerable to frequency analysis.
- **Frequency Analysis:** The most frequent ciphertext letter likely maps to 'E'; common digraphs (TH, HE, IN) and trigraphs (THE, ING) help crack the cipher.
- **Historical Significance:** Demonstrated that a large key space alone is insufficient for security.

### Important Concepts

- English letter frequencies: E (12.02%), T (9.10%), A (8.12%), O (7.68%), I (7.31%), N (6.95%).
- Common digraphs: TH, HE, AN, IN, ER; common trigraphs: THE, ING, AND.
- Monoalphabetic = single fixed substitution alphabet for the entire message.
- The weakness of monoalphabetic ciphers led to the development of polyalphabetic ciphers (e.g., Vigenere).

### Notes

- In exams, start frequency analysis by identifying the most common ciphertext letter as 'E'.
- A large key space does not guarantee security; pattern preservation is the real vulnerability.
- Be ready to compare Caesar cipher (25 keys, shift-based) vs. Monoalphabetic (26! keys, random mapping).
