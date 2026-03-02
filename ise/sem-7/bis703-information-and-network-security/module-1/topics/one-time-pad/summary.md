# One-Time Pad

=====================================

### Overview

The One-Time Pad (OTP), also known as the Vernam Cipher, is a symmetric encryption technique that is theoretically unbreakable when used correctly. Invented by Gilbert Vernam in 1917 and proven secure by Claude Shannon in 1949, it encrypts each plaintext character with a corresponding character from a truly random key of equal length.

### Key Points

- **Encryption Formula:** Ciphertext = Plaintext XOR Key.
- **Decryption Formula:** Plaintext = Ciphertext XOR Key.
- **Perfect Secrecy:** Proven by Shannon's theorem; without the key, any plaintext of the same length is equally likely.
- **Key Must Be Truly Random:** Not pseudorandom; must come from an unpredictable source.
- **Key Length:** Must be at least as long as the plaintext message.
- **Single Use:** The key must never be reused; reuse destroys perfect secrecy.
- **Key Distribution Problem:** Securely exchanging keys as long as messages is the main practical limitation.
- **Theoretically Unbreakable:** The only cipher proven to offer perfect secrecy.

### Important Concepts

- XOR Properties: Commutative (A XOR B = B XOR A), Self-inverse (A XOR A = 0), Identity (A XOR 0 = A).
- Shannon's four requirements for perfect secrecy: truly random key, key length >= plaintext length, key kept secret, key used only once.
- OTP is impractical for most applications due to key management, generation, storage, and synchronization challenges.
- Despite theoretical perfection, OTP is rarely used in practice except in extremely high-security contexts.

### Notes

- Exam questions often ask the three/four conditions for OTP perfect secrecy; memorize all four.
- Be able to perform XOR-based encryption/decryption calculations.
- Understand why OTP is "theoretically perfect but practically impractical."
