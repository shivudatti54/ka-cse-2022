# **Restoration in the Presence of Noise Only**

## **Definition**

- Restoration is the process of recovering the original image from corrupted or degraded image data.

## **Types of Noise**

- **Additive Noise**: the signal is increased by an additive term
- **Multiplicative Noise**: the signal is multiplied by a random term

## **Mathematical Models**

- **Gaussian Noise**:
  - $y = x + \epsilon$
  - $\epsilon \sim \mathcal{N}(0, \sigma^2)$
- **Salt and Pepper Noise**:
  - $y = x + \epsilon$
  - $\epsilon \in \{0, 1\}$

## **Restoration Techniques**

- **Filtering**:
  - Linear filters (e.g., mean filter, median filter)
  - Non-linear filters (e.g., Wiener filter, Bayesian filter)
- **Deconvolution**:
  - Recovering the original image by reversing the degradation process
- **Image Denoising**:
  - Removing noise from the image while preserving its content

## **Important Formulas and Theorems**

- **Wiener Filter**:
  - $H(\omega) = \frac{S_{xx}(\omega)}{S_{xx}(\omega) + S_{yy}(\omega)}$
  - where $H(\omega)$ is the transfer function of the filter
- **Bayesian Filter**:
  - $\hat{x} = E[x | y] = \int x \pi(x | y) dx$
  - where $\hat{x}$ is the estimate of the original image, and $\pi(x | y)$ is the posterior probability density function

## **Key Concepts**

- **Noise Models**: Gaussian, salt and pepper, etc.
- **Filtering**: Linear, non-linear, deconvolution, image denoising
- **Image Degradation**: Additive, multiplicative, etc.

## **Revision Tips**

- Review the different types of noise and their mathematical models.
- Understand the various restoration techniques, including filtering, deconvolution, and image denoising.
- Familiarize yourself with the Wiener filter and Bayesian filter formulas.
