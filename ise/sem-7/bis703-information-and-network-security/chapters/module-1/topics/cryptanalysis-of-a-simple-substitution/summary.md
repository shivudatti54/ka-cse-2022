# Cryptanalysis of a Simple Substitution

### Overview

Cryptanalysis is the process of analyzing and breaking encryption algorithms. A simple substitution cipher is a basic encryption technique where each plaintext character is replaced by a different ciphertext character.

### Terminology

- **Substitution Cipher**: A type of encryption where each plaintext character is replaced by a different ciphertext character.
- **Key**: The mapping between plaintext and ciphertext characters.
- **Frequency Analysis**: A method for breaking substitution ciphers by analyzing the frequency of characters in the plaintext and ciphertext.

### Key Points

- **Vigenère Cipher**: A polyalphabetic substitution cipher that uses a keyword to determine the substitution for each character.
- **Caesar Cipher**: A simple substitution cipher where each character is shifted by a fixed number of positions in the alphabet.
- **Frequency of Letters**: In the English language, the frequency of letters is approximately:
  - E: 12.7%
  - T: 9.1%
  - A: 8.2%
  - O: 7.5%
  - I: 6.9%
- **Formula for Frequency Analysis**:
  - $P(x) = \frac{C(x)}{L}$
  - Where:
    - $P(x)$ is the probability of character $x$ in the plaintext
    - $C(x)$ is the probability of character $x$ in the ciphertext
    - $L$ is the length of the plaintext
- **Square and Cube Method**:
  - Brute-force attack using a square or cube table to find the key.
  - Used for small alphabets (e.g., A-Z or A-26)

### Important Formulas and Definitions

- **Frequency of Letters Formula**
- **Square and Cube Method Formula**

### Theorem

- **Kaplan and Wilcox Theorem**: States that if a substitution cipher is broken using frequency analysis, the resulting key is unique.

### Revision Tips

- Understand the basics of substitution ciphers and frequency analysis.
- Practice solving simple substitution ciphers using frequency analysis.
- Use the Square and Cube Method for brute-force attacks.
- Review the Kaplan and Wilcox Theorem for uniqueness of the resulting key.
