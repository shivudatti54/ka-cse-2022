**Revisions Notes for Chap-10 (10.1 to 10.3.2) - Computer Vision**

### Image Degradation and Restoration Process

- **Definition:** Image degradation refers to the process of reducing image quality, while image restoration aims to recover the original image from the degraded one.
- **Model of Image Degradation:** Can be represented as a forward and inverse process, where:
  - Forward process: A degrading function (e.g. Gaussian blur) is applied to the original image to produce the degraded image.
  - Inverse process: A restoring function (e.g. deblurring) is applied to the degraded image to recover the original image.

### Image Models

- **Additive Model:**
  - Image intensity is a sum of the original intensity and noise.
  - Mathematical representation: $I(x) = f(x) + n(x)$, where $I(x)$ is the image intensity, $f(x)$ is the original intensity, and $n(x)$ is the noise.
- **Multiplicative Model:**
  - Image intensity is a product of the original intensity and a degradation factor.
  - Mathematical representation: $I(x) = f(x) \cdot h(x)$, where $I(x)$ is the image intensity, $f(x)$ is the original intensity, and $h(x)$ is the degradation factor.

### Deblurring and Denoising Techniques

- **Deblurring:**
  - Goal is to recover the original image from a blurred image.
  - Techniques include:
    - Blind deconvolution
    - Maximum likelihood estimation
- **Denoising:**
  - Goal is to remove noise from an image.
  - Techniques include:
    - Thresholding
    - Wavelet denoising

### Mathematical Formulas

- **The Fourier Transform:**
  - Representing the spatial domain image as a sum of frequency components.
  - Formula: $F(\omega) = \int_{-\infty}^{\infty} f(x) e^{-i\omega x} dx$
- **The Convolution Theorem:**
  - Representing the spatial domain image as a convolution of two functions.
  - Formula: $F(\omega) = F_s(\omega) \cdot F_d(\omega)$, where $F(\omega)$ is the Fourier Transform of the image, and $F_s(\omega)$ and $F_d(\omega)$ are the Fourier Transforms of the spatial and degrading functions, respectively.

### Important Definitions

- **Point Spread Function (PSF):** The degradation function that transforms the original image into the blurred image.
- **Weighted Least Squares (WLS):** A technique used in image restoration to find the optimal solution.

### Important Theorems

- **Cramer-Rao Lower Bound (CRLB):** A lower bound on the variance of the estimator in image restoration.
- **Maximum Likelihood Estimation (MLE):** A technique used in image restoration to find the optimal solution.
