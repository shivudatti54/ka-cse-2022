# Pyramids and Wavelets

## Overview

Image pyramids and wavelet transforms provide multi-resolution representations of images, enabling efficient processing at multiple scales. Pyramids use successive downsampling while wavelets decompose images into frequency subbands, both crucial for modern image processing and computer vision.

## Key Points

- **Gaussian Pyramid**: Successive smoothing and downsampling creating progressively smaller/blurred images
- **Laplacian Pyramid**: Difference between levels in Gaussian pyramid, captures details at each scale
- **Image Blending**: Laplacian pyramids enable seamless blending by combining different scales separately
- **Wavelet Transform**: Decomposes image into approximation (low-freq) and detail coefficients (high-freq horizontal, vertical, diagonal)
- **DWT Properties**: Provides both spatial and frequency localization unlike Fourier Transform
- **Multi-resolution Analysis**: Represents images at multiple scales for coarse-to-fine processing

## Important Concepts

- Gaussian pyramid loses information (low-pass filtering), Laplacian pyramid is invertible (lossless)
- Wavelets overcome Fourier Transform limitation of no spatial localization
- Applications include image compression (JPEG2000), feature detection at multiple scales, image fusion
- Common wavelets: Haar (simplest), Daubechies, Symlets, Coiflets

## Notes

- Understand Gaussian pyramid construction: smooth with Gaussian, downsample by 2
- Laplacian pyramid = difference of Gaussian levels, reconstructible without loss
- Wavelets provide time-frequency representation unlike pure frequency (Fourier)
- JPEG2000 uses wavelet transform instead of DCT for better compression
