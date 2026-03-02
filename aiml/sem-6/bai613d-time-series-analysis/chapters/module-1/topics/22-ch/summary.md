# **2.2 Ch: Autocorrelation Function and Spectrum**

### Key Points

- **Autocorrelation Function (ACF)**:
  - Definition: Measure of similarity between a time series and a delayed version of itself
  - Formula: ACF(x) = $\frac{1}{N} \sum_{t=0}^{N-1} x(t) x(t+x)$
- **Spectral Density (SD)**:
  - Definition: Power spectral density of a stationary process, represents the distribution of power across different frequencies
  - Formula: SD(f) = $\frac{1}{N} |X(e^{i2\pi ft})|^2$
- **Autocorrelation Function and Spectrum Relationship**:
  - ACF and SD are Fourier transforms of each other
  - Theorem: ACF = Fourier Transform of Power Spectral Density (SD)
- **Importance of ACF and SD**:
  - ACF helps identify autocorrelation and correlation breaks
  - SD helps identify frequency components and power distribution

### Important Formulas

- Autocorrelation Function (ACF): ACF(x) = $\frac{1}{N} \sum_{t=0}^{N-1} x(t) x(t+x)$
- Spectral Density (SD): SD(f) = $\frac{1}{N} |X(e^{i2\pi ft})|^2$

### Important Definitions

- Stationary process: Time series with constant statistical properties (mean, variance, autocorrelation)
- Power spectral density (SD): Distribution of power across different frequencies

### Quick Revision Tips

- Understand the relationship between ACF and SD
- Identify the autocorrelation and correlation breaks using ACF
- Use SD to identify frequency components and power distribution
