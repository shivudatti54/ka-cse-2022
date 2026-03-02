# Periodic Noise Reduction by Frequency Domain Filtering

### Overview

Periodic noise reduction is an essential technique in image restoration to remove unwanted patterns or noise from images. Frequency domain filtering is a widely used method to achieve this.

### Key Points

- **Definition:** Periodic noise is a type of noise that has a periodic or repetitive pattern, such as grid noise or filter artifacts.
- **Frequency Domain Filtering:** This technique involves filtering an image in the frequency domain to remove periodic noise.
- **Types of Frequency Domain Filters:**
  - **Low-Pass Filter (LPF):** Removes high-frequency components, including periodic noise.
  - **High-Pass Filter (HPF):** Removes low-frequency components, including periodic noise.
  - **Band-Pass Filter (BPF):** Removes both low- and high-frequency components, including periodic noise.
- **Important Formulas and Theorems:**
  - **Fourier Transform:** A mathematical operation that decomposes a function or sequence of values into its constituent frequencies.
  - **Discrete Fourier Transform (DFT):** A mathematical operation that decomposes a discrete-time signal into its constituent frequencies.
  - **Fast Fourier Transform (FFT):** An efficient algorithm for calculating the DFT of a sequence.
  - **Wiener Filter:** A type of frequency domain filter that uses the Wiener-Hopf equation to remove noise from an image.

- **Wiener-Hopf Equation:**
  - $H(\omega) = \frac{S_{xy}(\omega)}{S_{xx}(\omega) + S_{yy}(\omega)}$

  where $H(\omega)$ is the frequency domain filter, $S_{xy}(\omega)$ is the cross-spectral density, and $S_{xx}(\omega)$ and $S_{yy}(\omega)$ are the auto-spectral densities.

### Important Concepts

- **Periodicity:** A function or sequence has a periodic pattern if it repeats itself at regular intervals.
- **Spectral Density:** The spectral density of an image is a measure of the power or energy contained in each frequency component.

### Quick Revision Tips

- Understand the concept of periodic noise and its removal using frequency domain filtering.
- Familiarize yourself with the different types of frequency domain filters and their applications.
- Review the Wiener-Hopf equation and its use in designing frequency domain filters.
- Practice applying the FFT and Wiener filter to remove periodic noise from images.
