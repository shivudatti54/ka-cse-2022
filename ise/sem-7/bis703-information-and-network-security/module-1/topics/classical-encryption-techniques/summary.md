# Classical Encryption Techniques

=====================================

### Overview

Classical encryption techniques are the historical foundation of modern cryptography, predating computer-based systems. They introduce core concepts like confusion, diffusion, cryptanalysis, and the role of the key. These ciphers fall into two broad categories: substitution ciphers and transposition ciphers.

### Key Points

- **Substitution Ciphers:** Replace plaintext letters with other letters or symbols using a fixed rule or key.
- **Caesar Cipher:** Shifts each letter by a fixed number of positions; only 25 possible keys, easily broken by brute force.
- **Monoalphabetic Cipher:** Uses an arbitrary random mapping of 26 letters; key space is 26! but vulnerable to frequency analysis.
- **Playfair Cipher:** Encrypts digraphs (letter pairs) using a 5x5 matrix, hiding single-letter frequency distributions.
- **Vigenere Cipher:** Polyalphabetic cipher using a keyword for multiple Caesar shifts; resists simple frequency analysis.
- **Transposition Ciphers:** Rearrange the order of plaintext letters rather than replacing them (e.g., Rail Fence Cipher).
- **Kerckhoffs's Principle:** Security must depend only on the secrecy of the key, not the algorithm.

### Important Concepts

- **Confusion:** Hiding the relationship between ciphertext and key (provided by substitution).
- **Diffusion:** Spreading plaintext statistics across the ciphertext (provided by transposition).
- **Frequency Analysis:** Exploiting predictable letter frequencies in a language to break substitution ciphers.
- **Kasiski Examination:** Finding repeated patterns in ciphertext to determine the keyword length of the Vigenere cipher.
- **Modern ciphers (AES)** combine both substitution (confusion) and transposition (diffusion).

### Notes

- Caesar cipher has only 25 keys; always mention brute-force vulnerability in exams.
- Large key space (e.g., 26! for monoalphabetic) does not guarantee security if frequency patterns are preserved.
- Vigenere was called the "unbreakable cipher" but is defeated by Kasiski examination once keyword length is found.
