# Periodic Noise Reduction by Frequency Domain Filtering

### Definition

- Frequency domain filtering is a technique used to reduce periodic noise in images by processing the image in the frequency domain.

### Key Concepts

- **Fourier Transform (FT)**: a mathematical operation that decomposes a function or sequence of values into its constituent frequencies.
- **Magnitude Spectrum**: the absolute value of the Fourier Transform, representing the amplitude of each frequency component.
- **Phase Spectrum**: the phase angle of the Fourier Transform, representing the phase information of each frequency component.

### Theorem

- **Nyquist-Shannon Sampling Theorem**: states that a continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the highest frequency component.

### Important Formulas

- **Discrete Fourier Transform (DFT)**: `X[k] = ∑[n=0 to N-1] x[n] * e^(-j * 2 * π * k * n / N)`
- **Fast Fourier Transform (FFT)**: an efficient algorithm for computing the DFT.

### Frequency Domain Filtering Techniques

- **Low-Pass Filtering (LPF)**: removes high-frequency components, reducing high-frequency noise.
- **High-Pass Filtering (HPF)**: removes low-frequency components, reducing low-frequency noise.

### Regularization Techniques

- **Wiener Filter**: a type of LPF that uses a regularization term to minimize the mean squared error between the original and filtered images.
- **Nonlinear Filtering**: uses a nonlinear function to reduce noise in the frequency domain.

### Applications

- **Image Deblurring**: removes blur caused by out-of-focus pixels or motion.
- **Image Denoising**: reduces noise in images, improving overall quality.
- **Image Compression**: reduces the number of pixels required to represent an image, while preserving important features.

### Important Terms

- **Artifact**: a noise component that is not part of the original signal.
- **Periodicity**: a property of a signal where it repeats itself over a fixed interval.
- **Stationarity**: a property of a signal where its statistical properties remain constant over time.
