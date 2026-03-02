# Fourier Transforms

## Overview

Fourier Transforms decompose images from spatial domain (pixel intensities) to frequency domain (frequency components), revealing how much of each frequency exists in an image. This transformation enables powerful frequency-based filtering and analysis impossible in spatial domain.

## Key Points

- **2D Fourier Transform**: F(u,v) = (1/MN) ΣΣ f(x,y)e^(-j2π(ux/M + vy/N)) converts spatial to frequency domain
- **Magnitude Spectrum**: |F(u,v)| = √[R²(u,v) + I²(u,v)] shows frequency component strengths
- **Phase Spectrum**: φ(u,v) = tan⁻¹[I(u,v)/R(u,v)] contains structural information
- **Convolution Theorem**: Spatial domain convolution equivalent to frequency domain multiplication (f\*g ⇔ F×G)
- **FFT Algorithm**: Reduces computation from O(N²) to O(N log N) for efficient processing
- **Frequency Filtering**: Low-pass (blur), high-pass (sharpen), band-pass (specific frequencies) applied via multiplication
- **Separability**: 2D FT computed as successive 1D transforms (rows then columns)

## Important Concepts

- Low frequencies correspond to smooth areas, high frequencies to edges and fine details
- Frequency domain filtering computationally cheaper than large spatial kernels
- Phase information often contains more structural information than magnitude
- Padding required to avoid wrap-around errors during convolution

## Notes

- Memorize Convolution Theorem - frequently tested and crucial for filtering understanding
- Practice interpreting Fourier spectra of simple patterns (stripes, circles, etc.)
- Understand FFT's O(N log N) computational advantage over direct O(N²) computation
- Know when frequency domain is more appropriate than spatial domain filtering
- Applications include periodic noise removal, texture analysis, JPEG compression (DCT)
