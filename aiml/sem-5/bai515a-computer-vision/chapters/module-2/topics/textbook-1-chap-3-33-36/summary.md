# Textbook-1: Chap- 3 (3.3 - 3.6) Revision Notes

=====================================================

### Neighborhood Operators

- **Definition:** A neighborhood operator is a mathematical function that takes an image as input and produces an output based on a small region of the image.
- **Types of Neighborhood Operators:**
  - **Mean Filter:** Replaces each pixel with the mean of the neighboring pixels.
  - **Gaussian Filter:** Replaces each pixel with the weighted average of the neighboring pixels using a Gaussian distribution.
  - **Median Filter:** Replaces each pixel with the median of the neighboring pixels.
- **Importance:** Used for image smoothing and noise removal.

### Fourier Transforms

- **Definition:** A mathematical operation that decomposes an image into its constituent frequencies.
- **Types of Fourier Transforms:**
  - **Discrete Fourier Transform (DFT):** Suitable for discrete images.
  - **Fast Fourier Transform (FFT):** Efficient algorithm for DFT.
- **Importance:** Used for image filtering, feature extraction, and compression.

### Pyramids

- **Definition:** A hierarchical representation of an image, where each level represents a downsampling of the previous level.
- **Types of Pyramids:**
  - **Multiresolution Pyramid:** Combines low-pass and high-pass filters to produce multiple scales.
  - **Scale Space Pyramid:** Uses the Laplacian operator to produce a pyramid of images at different scales.
- **Importance:** Used for image segmentation, feature extraction, and object recognition.

### Wavelets

- **Definition:** A mathematical function that represents the frequency content of an image.
- **Types of Wavelets:**
  - **Discrete Wavelet Transform (DWT):** Suitable for discrete images.
  - **Continuous Wavelet Transform (CWT):** Suitable for continuous images.
- **Importance:** Used for image compression, feature extraction, and denoising.

### Important Formulas and Theorems

- **Discrete Fourier Transform (DFT):**
  - $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}nk}$
- **Fast Fourier Transform (FFT):**
  - Uses the DFT and the Cooley-Tukey algorithm to reduce computational complexity.
- **Laplacian Operator:**
  - $\nabla^2f(x,y) = \frac{\partial^2f}{\partial x^2} + \frac{\partial^2f}{\partial y^2}$
