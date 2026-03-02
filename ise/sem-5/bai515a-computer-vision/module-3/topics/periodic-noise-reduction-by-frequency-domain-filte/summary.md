# Periodic Noise Reduction by Frequency Domain Filtering

===========================================================

## Introduction

---

Frequency domain filtering is a technique used to reduce periodic noise in images by separating the signal into different frequency components.

## Key Concepts

---

- **Fourier Transform (FT)**: a mathematical tool used to decompose a signal into its constituent frequencies.
- **Low-Pass Filter (LPF)**: a frequency filter that allows low frequencies to pass through while attenuating high frequencies.
- **High-Pass Filter (HPF)**: a frequency filter that attenuates low frequencies while allowing high frequencies to pass through.
- **Frequency Domain Filtering (FDF)**: a technique that uses FT to filter an image in the frequency domain.

## Mathematical Formulas

---

- **Discrete Fourier Transform (DFT)**: used to decompose a discrete-time signal into its frequency components: $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}nk}$
- **Fourier Transform (FT)**: used to decompose a continuous-time signal into its frequency components: $X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt$
- **Frequency Domain Filtering (FDF) Equation**: used to filter an image in the frequency domain: $Y(\omega) = H(\omega) X(\omega)$, where $Y(\omega)$ is the filtered image, $H(\omega)$ is the frequency response of the filter, and $X(\omega)$ is the original image.

## Important Theorems and Definitions

---

- **Nyquist-Shannon Sampling Theorem**: states that a continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the highest frequency component.

## Applications

---

- **Periodic Noise Reduction**: frequency domain filtering can be used to remove periodic noise from images, such as stripes or grid patterns.
- **Image Denoising**: frequency domain filtering can be used to reduce noise in images by removing high-frequency components that represent noise.

## Revision Tips

---

- Review the Fourier Transform and its applications.
- Understand the concept of frequency domain filtering and its applications.
- Practice solving problems involving frequency domain filtering.
