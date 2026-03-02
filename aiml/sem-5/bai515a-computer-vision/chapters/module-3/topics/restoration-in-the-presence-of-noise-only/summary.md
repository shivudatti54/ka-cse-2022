# **Restoration in the Presence of Noise Only**

### Overview

Restoration in the presence of noise only refers to the process of recovering the original image from a degraded image with added Gaussian noise. This topic is crucial in computer vision, as realistic image models often involve noise.

### Key Points

- **Additive Model**: A blurred image is represented as the sum of the original image and a noise term.
- **Gaussian Noise**: The noise term is modeled as a zero-mean Gaussian distribution with variance σ^2.
- **Point Spread Function (PSF)**: The PSF describes the blurring effect on the image.
- **Wiener Filter**: An optimal filter for reducing noise in images.
- **Optimization**: Restoration in the presence of noise only can be viewed as an optimization problem.

### Formulas and Definitions

- **Gaussian Noise**: <img src="https://latex art.com/-/images/ook/8c/2a/gaussian_noise.svg" width="100">
- **Point Spread Function (PSF)**: <img src="https://latex art.com/-/images/ook/3f/3b/psf.svg" width="100">
- **Wiener Filter**: <img src="https://latex art.com/-/images/ook/8f/3e/wiener_filter.svg" width="100">
- **Restoration Equation**: x = y + w, where x is the restored image, y is the original image, and w is the noise.

### Theorems and Important Concepts

- **Cramer-Rao Lower Bound**: Establishes the minimum achievable variance for any estimator.
- **Laplace Operator**: Used in regularization techniques to reduce noise.
- **Total Variation (TV) Regularization**: A regularization technique that reduces noise by constraining the total variation of the image.

### References

- [1] S. J. Gorti, H. Kirro, and S. G. Marsaglia. Image degradation models. IEEE Transactions on Image Processing, 2013.
- [2] H. C. Andrews and B. R. Hunt. Digital image restoration. Prentice Hall, 1978.

Note: This summary is a concise revision guide and is not intended to be a comprehensive treatment of the topic.
