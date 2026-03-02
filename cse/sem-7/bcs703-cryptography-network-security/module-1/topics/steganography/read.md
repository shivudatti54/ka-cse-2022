# Steganography

## Introduction

Steganography is the art and science of concealing the existence of secret communication, distinct from cryptography which transforms the message content to make it unintelligible. While cryptography protects the content of a message, steganography protects the fact that communication is occurring at all. The term derives from the Greek words "steganos" (covered) and "graphia" (writing), literally meaning "covered writing." This technique has evolved from ancient methods such as invisible ink and concealed messages in wax tablets to sophisticated digital implementations that hide information within multimedia files. Within the context of classical encryption techniques, steganography represents the complementary approach of information hiding, historically used alongside encryption to provide multiple layers of security. The discipline gained renewed importance in the digital age where vast amounts of data traverse networks daily, creating opportunities for covert communication that blends seamlessly with legitimate traffic.

## Key Concepts

### Fundamental Model

Steganography can be formally modeled using Simmons' Prisoners' Problem, where two prisoners, Alice and Bob, wish to exchange secret messages without detection by the warden. The model consists of three components: the cover medium (C), the secret message (M), and the steganographic key (K). The embedding function E takes the cover, message, and key to produce the stego-object: S = E(C, M, K). The extraction function D recovers the message: M = D(S, K). For a secure system, the stego-object S must be statistically indistinguishable from the cover C to prevent detection by steganalysis.

### Classification of Techniques

Steganographic techniques are classified based on the cover medium and the domain of embedding. **Spatial domain methods** manipulate the pixel values directly, with Least Significant Bit (LSB) substitution being the most straightforward approach. In LSB steganography, the least significant bits of cover pixels are replaced with secret data bits. For an 8-bit grayscale image, modifying only the least significant bit results in minimal visual distortion (less than 1 dB degradation in peak signal-to-noise ratio). The embedding capacity for LSB in a 512×512 grayscale image is approximately 32 KB, calculated as (512 × 512 × 1)/8 bytes.

**Transform domain methods** embed information in the frequency coefficients of the cover medium. Discrete Cosine Transform (DCT) steganography modifies the DCT coefficients of JPEG images, while Discrete Wavelet Transform (DWT) methods operate on wavelet-decomposed images. These techniques offer greater robustness against compression and filtering attacks compared to spatial domain methods. The embedding capacity in DCT domain is typically 5-15% of the cover size, with minimal perceptual impact due to the masking properties of human visual perception.

**Statistical steganography** modifies statistical properties of the cover, while **spread spectrum steganography** distributes the secret information across multiple frequency bands. Modern techniques also include edge-based methods that exploit the human eye's reduced sensitivity to changes in edge regions, and model-based steganography that preserves statistical models of the cover.

### Steganalysis

Steganalysis is the countermeasure to steganography, focused on detecting the presence of hidden information. Statistical attacks analyze chi-square distributions, pair analysis, and higher-order statistics to identify modifications. Visual attacks attempt to reveal hidden data through image processing operations. Machine learning approaches, particularly deep neural networks, have become effective at detecting steganographic content by learning distinguishing features between cover and stego objects.

## Examples

**Example 1: LSB Embedding Capacity Calculation**
For a 1920×1080 RGB image (24 bits per pixel), calculate the maximum secret message size that can be embedded using 1-bit LSB steganography.
Solution: Total pixels = 1920 × 1080 = 2,073,600 pixels. Each pixel has 3 color channels, each with 1 LSB available. Total embeddable bits = 2,073,600 × 3 = 6,220,800 bits. Maximum message size = 6,220,800 / 8 = 777,600 bytes ≈ 759 KB.

**Example 2: DCT Coefficient Modification**
In JPEG DCT steganography, consider a 8×8 block with quantized DCT coefficients [16, -2, 1, 0, 0, 0, 0, 0]. To embed a binary '1', we might modify coefficient -2 to -3 (making it odd), while for binary '0', we ensure the coefficient remains even. The JPEG quantization table determines the maximum modification allowed while maintaining visual quality.

**Example 3: Comparison of Approaches**
For a security application requiring both confidentiality and invisibility, a common strategy combines cryptography with steganography: first encrypt the message using AES-256, then embed the ciphertext within cover images using LSB replacement. This provides defense-in-depth: even if the steganographic channel is detected, the encrypted content remains secure without the decryption key.

## Exam Tips

1. Remember the fundamental distinction: steganography hides the existence of communication, while cryptography hides the content.
2. LSB steganography offers highest capacity but lowest security; transform domain methods provide better robustness at the cost of reduced capacity.
3. The human visual system is less sensitive to changes in high-frequency components (edges and textures) than smooth regions.
4. For numerical problems, remember the formula: Capacity (bytes) = (Width × Height × Channels × LSB bits used) / 8.
5. Steganalysis effectiveness depends on the statistical distinguishability of stego objects from covers.
6. Common steganography tools include OpenStego, Steghide, and OutGuess; understanding their techniques helps in detection.
7. The "cover" is the original medium, while "stego" refers to the medium containing hidden information.
