# Restoration in the Presence of Noise Only

### Overview

Restoration of degraded images in the presence of noise is a crucial problem in computer vision. This summary covers the key concepts, techniques, and formulas relevant to this topic.

### Definitions and Theorems

- **Noise**: Random fluctuations in the image intensity that can be additive, multiplicative, or spatially correlated.
- **Noise Model**: A statistical model that describes the distribution of noise in an image.
- **Blind Deconvolution**: The process of estimating the original image from the degraded image without knowing the blurring kernel.

### Key Concepts

- **Wiener Filter**: A linear filter that estimates the original image by minimizing the mean squared error between the degraded image and the original image.
  - Formula: `W = H^* (H H^*)^-1`, where `H` is the Fourier transform of the blurring kernel, and `W` is the Wiener filter.
- **Regularized Least Squares (RLS)**: A method that regularizes the least squares solution to minimize the noise variance.
- **Expectation-Maximization (EM) Algorithm**: A method that iteratively estimates the noise model parameters to minimize the expected log-likelihood.

### Restoration Techniques

- **Filtering**: Techniques such as the Wiener filter and RLS to remove noise from the image.
- **Deconvolution**: Techniques such as blind deconvolution and maximum likelihood deconvolution to estimate the original image.

### Important Formulas

- **Wiener Filter Formula**: `W = H^* (H H^*)^-1`
- **Regularized Least Squares Formula**: `x = (H^T H + λ I)^-1 H^T y`, where `x` is the restored image, `H` is the Fourier transform of the blurring kernel, `y` is the degraded image, and `λ` is the regularization parameter.

### Quick Revision Points

- Wiener filter: `W = H^* (H H^*)^-1`
- RLS: `x = (H^T H + λ I)^-1 H^T y`
- Blind deconvolution: estimate original image from degraded image without knowing blurring kernel
- EM algorithm: estimate noise model parameters to minimize expected log-likelihood
