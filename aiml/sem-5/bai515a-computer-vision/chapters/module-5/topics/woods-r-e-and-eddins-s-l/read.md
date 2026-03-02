# Module 5: Image Compression (Woods & Eddins)

## Introduction

In the realm of Computer Vision, the ability to acquire, process, and store vast amounts of image data is paramount. However, high-resolution images and video sequences consume significant storage space and bandwidth. This is where image compression becomes a critical technology. Module 5, based on the work of Woods and Eddins (often referencing their foundational textbook *Digital Image Processing*), delves into the principles and techniques used to reduce the size of image data without compromising its perceived quality to an unacceptable degree. The core objective is to represent an image with as few bits as possible—a process governed by the fundamental trade-off between compression ratio and image fidelity.

## Core Concepts

Image compression techniques are broadly classified into two categories:

1.  **Lossless Compression:** Algorithms that allow the exact original image to be reconstructed from the compressed data. They exploit statistical redundancies in the data (like repeating patterns) but offer relatively low compression ratios (typically 2:1 to 3:1 for natural images). Common methods include:
    *   **Run-Length Encoding (RLE):** Replaces sequences (runs) of identical pixels with a single value and a count. It is highly effective for simple images with large uniform areas (e.g., binary images like scanned documents).
    *   **Huffman Coding:** A variable-length coding technique that assigns shorter codes to more frequent symbols (pixel values) and longer codes to less frequent ones, minimizing the average code length.
    *   **LZW (Lempel-Ziv-Welch) Coding:** A dictionary-based algorithm that builds a table of strings of data encountered in the image. Repeated patterns are replaced with a shorter code pointing to the dictionary entry.

2.  **Lossy Compression:** Algorithms that achieve much higher compression ratios (e.g., 10:1 to 50:1 or more) by permanently discarding some information deemed psychologically or visually less important. The reconstructed image is an approximation of the original. The most prevalent standard, JPEG, is a prime example and is built upon the following steps, which are central to Woods and Eddins' explanation:
    *   **Transformation (Discrete Cosine Transform - DCT):** The image is divided into small 8x8 blocks. The 2D-DCT is applied to each block, transforming the data from the spatial domain (pixel values) into the frequency domain. This concentrates the most important visual information (low-frequency components) into a few coefficients and separates out less important fine details (high-frequency components).
    *   **Quantization:** This is the primary lossy step. The DCT coefficients are divided by a predefined quantization matrix and rounded to integers. This step drastically reduces the precision of the high-frequency coefficients (often to zero), which significantly compresses the data but also discards detail.
    *   **Entropy Encoding:** The quantized coefficients are then losslessly compressed using techniques like Huffman coding to produce the final compressed bitstream.

**Example:** Consider an 8x8 block of a grayscale image. After applying the DCT, the top-left coefficient (the DC coefficient) represents the average intensity of the block. The other (AC) coefficients represent increasingly finer details. During quantization, these AC coefficients are heavily quantized. A block from a smooth blue sky might have many high-frequency AC coefficients quantized to zero, making them highly compressible. A block from a detailed textured region would have more non-zero coefficients, resulting in a lower compression ratio for that block.

## Key Points & Summary

*   **Goal:** The primary goal of image compression is to reduce the number of bits required to represent an image, thereby saving storage and transmission bandwidth.
*   **Redundancy:** Compression exploits two main types of redundancy:
    *   **Coding Redundancy:** Using optimal code words (e.g., Huffman).
    *   **Interpixel Redundancy:** Correlations between neighboring pixels (e.g., RLE, LZW, DCT).
    *   **Psychovisual Redundancy:** Removing information the human eye is less sensitive to (e.g., quantization of high-frequency DCT coefficients).
*   **Lossless vs. Lossy:** Lossless methods (RLE, Huffman, LZW) preserve all information for perfect reconstruction but offer modest compression. Lossy methods (JPEG) achieve high compression by discarding selective information, trading off quality for size.
*   **JPEG Standard:** The JPEG pipeline (Color Space Transformation, DCT, Quantization, Entropy Coding) is a canonical example of a lossy compression technique that leverages both statistical and psychovisual redundancies.
*   **Trade-off:** The process is always a balance between the **compression ratio** (size of original / size of compressed) and the **fidelity** (quality) of the reconstructed image. The level of lossy compression can typically be controlled by adjusting the quantization parameters.