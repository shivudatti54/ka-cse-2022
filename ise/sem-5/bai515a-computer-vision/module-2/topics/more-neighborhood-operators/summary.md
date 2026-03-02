# More Neighborhood Operators

## Overview

Beyond basic linear filtering, advanced neighborhood operators include nonlinear filters, adaptive filters, and specialized operators for edge-preserving smoothing, texture analysis, and robust noise reduction. These operators consider local image statistics and structure for superior performance in specific scenarios.

## Key Points

- **Median Filter**: Nonlinear filter replacing pixel with neighborhood median, excellent for salt-and-pepper noise
- **Bilateral Filter**: Edge-preserving smoothing using both spatial and intensity similarity weights
- **Non-local Means**: Denoising by averaging similar patches across entire image, not just local neighborhood
- **Morphological Filters**: Erosion, dilation, opening, closing using structuring elements for shape-based processing
- **Adaptive Filters**: Adjust behavior based on local image statistics (variance, edge presence)
- **Rank-Order Filters**: Min, max, median, percentile filters for various noise types

## Important Concepts

- Median filter better than linear filters for impulse noise but computationally more expensive
- Bilateral filter weights = spatial distance × intensity similarity, preserves edges while smoothing
- Morphological operations useful for binary images, shape analysis, feature extraction
- Adaptive filters change parameters based on local content (smooth in uniform areas, preserve edges)

## Notes

- Understand when to use nonlinear over linear filters: impulse noise → median, edge preservation → bilateral
- Median filter: sort neighborhood values, take middle value, cannot be implemented via convolution
- Bilateral filter has two kernels: spatial (Gaussian) and range (intensity difference)
- Morphological operations require structuring element defining neighborhood shape
