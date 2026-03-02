# Image Restoration and Reconstruction

## Overview

Image restoration aims to recover original images from degraded observations by modeling the degradation process and applying inverse operations. Unlike enhancement (subjective), restoration is objective using prior knowledge of degradation like blur, noise, or missing data.

## Key Points

- **Degradation Model**: g(x,y) = h(x,y) \* f(x,y) + n(x,y) where g=observed, h=blur, f=original, n=noise
- **Inverse Filtering**: G/H recovers F but amplifies noise at frequencies where H is small
- **Wiener Filtering**: Optimal restoration minimizing mean square error, balances deblurring and noise amplification
- **Constrained Least Squares**: Incorporates smoothness constraints for stable solutions
- **Blind Deconvolution**: Estimates both h and f from g when blur kernel unknown
- **Richardson-Lucy**: Iterative algorithm for restoration assuming Poisson noise

## Important Concepts

- Restoration requires degradation model knowledge, enhancement does not
- Inverse filtering unstable when H(u,v)≈0, needs regularization
- Wiener filter uses power spectra ratio: H\*/(|H|²+Sn/Sf) where Sn, Sf are noise and signal power
- Applications include motion blur removal, focus blur correction, atmospheric degradation removal

## Notes

- Degradation model h can represent various blur types: motion, out-of-focus, atmospheric
- Direct inverse G/H fails due to noise amplification and division by near-zero values
- Wiener filter optimal in minimum mean square error sense, requires noise statistics
- Blind deconvolution more challenging but necessary when degradation unknown
