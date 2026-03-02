# **Textbook-1: Chap- 3 (3.3 - 3.6) - Image Processing**

### Key Points

- **Neighborhood Operators**
  - Definition: A neighborhood operator is a function that assigns a value to a pixel based on the values of neighboring pixels.
  - Examples: Average, Median, Gradient
- **Fourier Transforms**
  - Definition: A mathematical operation that decomposes a function or a sequence of values into its constituent frequencies.
  - Formula: $F(\omega) = \sum_{n=-\infty}^{\infty} f(n) e^{-i\omega n}$
- **Pyramids**
  - Definition: A hierarchical representation of an image, with multiple scales of representation.
  - Formula: $L_i = \sigma \left( L_{i-1} \ast G_i \right)$, where $L_i$ is the scaled image, $L_{i-1}$ is the previous scale, $G_i$ is the Gaussian filter, and $\sigma$ is the scale factor.
- **Wavelets**
  - Definition: A mathematical function that represents a signal or image in a time-frequency domain.
  - Formula: $\psi(x) = \phi(x) - \sum_{k=1}^{K} a_k \phi(2x-k)$, where $\psi(x)$ is the wavelet function, $\phi(x)$ is the scaling function, and $a_k$ are the coefficients.

### Important Formulas and Definitions

- **Mean Squared Error (MSE)**: $MSE = \frac{1}{N} \sum_{i=1}^{N} (f_i - g_i)^2$
- **Peak Signal-to-Noise Ratio (PSNR)**: $PSNR = 20 \log_{10} \left( \frac{max_{i} f_i}{\sqrt{MSE}} \right)$
- **Frequency Domain Representation**: $Image = F \ast G$, where $Image$ is the input image, $F$ is the Fourier transform, and $G$ is the filter.

### Important Theorems

- **Shannon Sampling Theorem**: If the sampling rate is greater than twice the Nyquist frequency, the signal can be perfectly reconstructed.
- **Fourier Transform Theorem**: If $f(x) \leftrightarrow F(\omega)$, then $f(-x) \leftrightarrow F(-\omega)$ and $f(ax) \leftrightarrow \frac{1}{|a|} F\left( \frac{\omega}{a} \right)$
