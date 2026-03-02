# Polyalphabetic Ciphers

=====================================

### Overview

Polyalphabetic ciphers use multiple substitution alphabets to encrypt a message, overcoming the frequency analysis vulnerability of monoalphabetic ciphers. The most famous example is the Vigenere Cipher, which uses a repeating keyword to apply different Caesar shifts to successive plaintext letters. The One-Time Pad represents the theoretically perfect form of polyalphabetic substitution.

### Key Points

- **Multiple Alphabets:** A single plaintext letter can map to different ciphertext letters at different positions.
- **Vigenere Cipher:** Uses a keyword repeated over the plaintext; each keyword letter specifies a Caesar shift.
- **Vigenere Encryption:** C*i = (P_i + K*(i mod m)) mod 26, where m is keyword length.
- **Vigenere Decryption:** P*i = (C_i - K*(i mod m) + 26) mod 26.
- **Tabula Recta:** The Vigenere table with 26 shifted alphabets used for lookup-based encryption.
- **One-Time Pad:** A polyalphabetic cipher with a truly random key as long as the message; theoretically unbreakable.
- **Kasiski Examination:** Finds repeated ciphertext sequences to determine keyword length, enabling per-group frequency analysis.
- **Improvement Over Monoalphabetic:** Obscures single-letter frequency distributions.

### Important Concepts

- Once keyword length m is known via Kasiski examination, the ciphertext splits into m groups, each a simple Caesar cipher.
- Vigenere was called the "unbreakable cipher" for centuries before Kasiski's method was published.
- OTP requires: truly random key, key >= message length, key never reused, key kept secret.
- Security of polyalphabetic ciphers depends on keyword length and randomness.

### Notes

- Practice Vigenere encryption/decryption with modular arithmetic for exam calculations.
- For theory questions, explain why polyalphabetic ciphers improve over monoalphabetic (multiple alphabets defeat simple frequency analysis).
- Remember: OTP is theoretically secure but impractical; Vigenere is practical but breakable.
