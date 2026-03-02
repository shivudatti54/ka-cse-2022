# Polyalphabetic Ciphers - Summary

## Key Definitions

- **Polyalphabetic Cipher**: A substitution cipher that uses multiple distinct substitution alphabets throughout the encryption process, changing the substitution rule according to a defined pattern or key.

- **Vigenère Cipher**: A polyalphabetic cipher that uses a keyword to determine the shift amount for each letter, with the formula C_i = (P_i + K_i) mod 26 for encryption.

- **Autokey Cipher**: A variant of Vigenère where the key after the initial priming value consists of the plaintext itself, creating a non-repeating key sequence.

- **One-Time Pad**: A special polyalphabetic cipher using a truly random key of the same length as the message, used only once, that achieves perfect secrecy.

- **Kasiski Examination**: A cryptanalytic technique that examines repeated sequences in ciphertext to determine the key length of polyalphabetic ciphers.

- **Index of Coincidence (IC)**: A statistical measure used to determine the likelihood that two randomly selected letters from a text are identical, useful for estimating key length.

## Important Formulas

- **Vigenère Encryption**: C_i = (P_i + K_i) mod 26
- **Vigenère Decryption**: P_i = (C_i - K_i) mod 26
- **Modular Arithmetic**: When C - K < 0, add 26: P = (C - K + 26) mod 26

## Key Points

1. Polyalphabetic ciphers use multiple substitution alphabets, making them resistant to simple frequency analysis that breaks monoalphabetic ciphers.

2. The Vigenère cipher with a short key is vulnerable to Kasiski examination and Friedman test for key length determination.

3. The autokey cipher provides a non-repeating key but is vulnerable to known-plaintext attacks due to its self-synchronizing property.

4. The one-time pad achieves perfect secrecy but requires impractical key distribution and management.

5. Longer key lengths provide better security by making statistical patterns less detectable in the ciphertext.

6. Despite their historical importance, polyalphabetic ciphers are not suitable for modern security due to their vulnerability to computational attacks.

7. The security of polyalphabetic ciphers depends on keeping the key secret, not on keeping the algorithm secret (Kerckhoffs's principle).

## Common Mistakes

1. Forgetting to convert letters to numerical values (A=0, B=1, ..., Z=25) before applying encryption or decryption formulas.

2. Not properly handling negative results in modular arithmetic during decryption; always add 26 when the result is negative.

3. Confusing the autokey cipher with the standard Vigenère cipher; remember that autokey uses plaintext as continuation after the priming key.

4. Believing that the one-time pad can be broken with sufficient computational power; its security is information-theoretic, not computational.

5. Using the same key for multiple messages in one-time pad, which completely breaks the security of the system.