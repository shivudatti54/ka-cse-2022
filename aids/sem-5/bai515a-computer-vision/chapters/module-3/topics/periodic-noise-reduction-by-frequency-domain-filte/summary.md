# Periodic Noise Reduction by Frequency Domain Filtering

### Definition and Background

- Periodic noise is a type of noise that has a regular, periodic pattern.
- Frequency domain filtering is a technique used to reduce noise by filtering out specific frequency components.

### Key Concepts

- **Fourier Transform**: A mathematical tool used to decompose a signal into its frequency components.
- **Discrete Fourier Transform (DFT)**: A specific type of Fourier Transform used for discrete-time signals.
- **Frequency Domain Filtering**: A technique used to remove noise by filtering out specific frequency components.
- **Periodic Noise Model**: A mathematical model used to describe periodic noise.

### Theoretical Background

- **Nyquist-Shannon Sampling Theorem**: States that a continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the highest frequency component.
- **Bessel Inequality**: A mathematical inequality used to determine the minimum number of samples required to reconstruct a continuous-time signal.

### Formulas and Equations

- **Discrete Fourier Transform (DFT)**:
  \[X[k] = \sum\_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}nk}\]
- **Inverse Discrete Fourier Transform (IDFT)**:
  \[x[n] = \frac{1}{N} \sum\_{k=0}^{N-1} X[k] e^{j\frac{2\pi}{N}nk}\]
- **Frequency Domain Filtering**:
  \[y[k] = \sum\_{m=0}^{M-1} h[m] X[m]\]

### Theorem

- **Bessel Inequality**:
  \[ \sum*{k=-\infty}^{\infty} |X[k]|^2 \geq \sum*{k=0}^{N-1} |x[n]|^2 \]

### Key Points for Revision

- Fourier Transform and DFT are used for frequency domain filtering.
- Periodic noise can be modeled using the periodic noise model.
- Frequency domain filtering is a technique used to remove noise by filtering out specific frequency components.
- The Bessel inequality is used to determine the minimum number of samples required to reconstruct a continuous-time signal.
