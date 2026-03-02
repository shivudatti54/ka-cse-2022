# Steganography

=====================================

### Overview

Steganography is the practice of concealing information within other non-secret data, hiding the very existence of a message rather than just its content. Unlike cryptography which makes data unreadable, steganography makes data invisible. Modern techniques embed messages in images, audio, video, and text files.

### Key Points

- **Definition:** From Greek "steganos" (covered) + "graphein" (writing); the art of hiding messages within ordinary-looking data.
- **Image Steganography (LSB):** Least Significant Bit modification changes the rightmost bits of pixel values to encode message bits.
- **Audio Steganography:** Techniques include echo hiding, phase coding, and spread spectrum methods.
- **Text Steganography:** Uses whitespace manipulation, syntax modification, and semantic methods.
- **Video Steganography:** Frame-based hiding and motion vector modification.
- **Steganalysis:** The science of detecting hidden messages through statistical analysis, pattern detection, and machine learning.
- **Crypto-Steganography:** Combining encryption and steganography provides both content protection and existence concealment.

### Important Concepts

- Cryptography protects message content; steganography hides message existence.
- Steganography output looks normal (an image, audio file); cryptography output looks obviously encrypted.
- LSB technique is the most common image steganography method and a frequent exam topic.
- Combined approach: Plaintext -> Encryption -> Ciphertext -> Steganography -> Carrier File.
- Applications: digital watermarking, covert communication, data integrity verification.

### Notes

- Always differentiate between cryptography (protects content) and steganography (hides existence) in exam answers.
- LSB modification is the most commonly asked steganography technique; know how pixel bits are altered.
- Combined crypto-steganography provides the strongest security and is the recommended modern approach.
