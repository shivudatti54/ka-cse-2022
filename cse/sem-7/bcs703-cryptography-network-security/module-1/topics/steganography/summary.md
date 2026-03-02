# Steganography - Summary

## Key Definitions

- **Steganography:** The practice of hiding information within other non-secret data so that the existence of the hidden information is imperceptible.
- **Cover Object (Carrier):** The original media file (image, audio, video, or text) used to hide secret data.
- **Stego-Object:** The modified cover object containing hidden information.
- **Stego-Key:** A secret key used to control the embedding process, providing additional security.
- **Steganalysis:** The technique of detecting the presence of hidden information in digital media.
- **Least Significant Bit (LSB):** The bit in a binary representation that has the smallest value and can be modified without significantly affecting the original data.

## Important Formulas

- **LSB Capacity:** For an image with n pixels and b bits per pixel, the maximum data that can be hidden is n × b bits (or n × b/8 bytes) when using all bit planes.
- **Visual Distortion:** Modifying the LSB causes a maximum change of ±1 in pixel value for grayscale images, resulting in less than 0.4% change in intensity.

## Key Points

1. Steganography conceals the existence of communication, unlike cryptography which makes the message unintelligible but visible.

2. The most common technique is LSB replacement, where the least significant bits of pixel values are replaced with secret data bits.

3. Digital images, audio files, and video files serve as primary carriers due to their redundant data and large size.

4. The effectiveness of steganography depends on the imperceptibility of modifications to the carrier media.

5. Steganography and cryptography can be combined: encrypt the message first, then hide it for enhanced security.

6. Steganalysis is the counter-discipline that aims to detect hidden messages through statistical and visual analysis.

7. Applications include digital watermarking for copyright protection, covert military communication, and secure data transfer.

## Common Mistakes

1. **Confusing steganography with cryptography:** Remember that steganography hides the message's existence, while cryptography hides the message's content.

2. **Ignoring the stego-key:** The stego-key is essential for security; without it, even if the stego-object is detected, the message cannot be extracted.

3. **Overlooking compression effects:** Hidden data in compressed images (like JPEG) must be embedded after compression to survive, as compression destroys LSB data.