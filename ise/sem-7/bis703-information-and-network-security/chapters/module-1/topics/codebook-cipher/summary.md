# **Codebook Cipher Revision Notes**

## **Definition and Overview**

- A substitution cipher where each plaintext symbol is replaced by a corresponding symbol from a predefined codebook.
- Also known as a table cipher or transposition cipher.

## **Key Points**

- **Codebook Creation**:
  - A codebook is a table of pairs of plaintext and ciphertext symbols.
  - Each plaintext symbol is replaced by a corresponding ciphertext symbol.
- **Encryption Process**:
  - Read the plaintext message.
  - Look up each plaintext symbol in the codebook to find the corresponding ciphertext symbol.
  - Write the ciphertext symbol next to the plaintext symbol.
- **Decryption Process**:
  - Read the ciphertext message.
  - Look up each ciphertext symbol in the codebook to find the corresponding plaintext symbol.
  - Write the plaintext symbol next to the ciphertext symbol.

## **Theoretical Background**

- **Substitution Cipher**:

```math
P = C
```

where P is the plaintext, C is the ciphertext, and S is the substitution table.

- **Transposition Cipher**:

```math
C = S(P)
```

where C is the ciphertext, S is the substitution table, and P is the plaintext.

## **Security Considerations**

- **Weaknesses**:
  - Codebooks can be compromised if they are shared among multiple parties.
  - If an attacker has access to the codebook, they can decrypt the message.
- **Limitations**:
  - Codebook ciphers are vulnerable to frequency analysis attacks.

## **Important Formulas and Definitions**

- **Vigenère Square**:
  | | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | A | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
- **Fourier Transform**:

```math
F = \sum_{k=0}^{n-1} f(k)e^{-i2\pi k/n}
```

where F is the discrete Fourier transform, n is the length of the sequence, and f(k) is the sequence value at position k.

## **Important Theorems**

- **Caesar Cipher Theorem**:
  If a Caesar cipher is encrypted with a shift of m, then the decryption key is m.
- **Frequency Analysis Theorem**:
  If a ciphertext is encrypted with a frequency analysis attack, then the decryption key can be calculated.
