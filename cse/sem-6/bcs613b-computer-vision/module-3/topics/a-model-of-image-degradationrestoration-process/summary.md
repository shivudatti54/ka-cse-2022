# Model of Image Degradation/Restoration Process

## Overview

The degradation/restoration model provides mathematical framework for understanding how images become degraded and how to reverse the process. The model combines system degradation function with additive noise, enabling design of restoration algorithms.

## Key Points

- **Degradation Model**: g(x,y) = h(x,y)\*f(x,y) + η(x,y) in spatial domain, G=H×F+N in frequency domain
- **Degradation Function h**: Represents blur (motion, defocus, atmospheric), characterized by Point Spread Function (PSF)
- **Noise η**: Additive random component (Gaussian, salt-and-pepper, Poisson) degrading signal quality
- **Restoration Goal**: Estimate f^ from g given knowledge or estimate of h and statistical properties of η
- **Types of Degradation**: Motion blur, atmospheric turbulence, out-of-focus blur, sensor noise

## Important Concepts

- Convolution theorem enables frequency domain analysis: g=h\*f → G=H×F
- Different degradation types require different restoration approaches
- Complete restoration impossible with noise; trade-off between deblurring and noise amplification
- Prior knowledge of degradation improves restoration quality significantly

## Notes

- Spatial domain: convolution with h plus additive noise
- Frequency domain: multiplication with H plus noise spectrum
- PSF characterizes how single point spreads in degraded image
- Real-world degradations combine multiple effects requiring composite models
