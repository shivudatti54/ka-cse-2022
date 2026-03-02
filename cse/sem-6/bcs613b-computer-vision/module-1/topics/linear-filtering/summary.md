# Linear Filtering

## Overview

Linear filtering modifies pixel values based on weighted combinations of neighboring pixels through convolution operations. This fundamental technique enables noise reduction, edge detection, image enhancement, and feature extraction by applying mathematical kernels to images.

## Key Points

- **Convolution**: Output(x,y) = ΣΣ I(x-i, y-j) × K(i,j) combines image with kernel through multiply-and-sum operation
- **Smoothing Filters**: Box filter (simple average), Gaussian filter (weighted average), reduce noise and detail (low-pass)
- **Sharpening Filters**: Laplacian, unsharp masking enhance edges and fine details (high-pass)
- **Edge Detection**: Sobel, Prewitt operators detect horizontal and vertical edges through gradient computation
- **Padding Strategies**: Zero padding, replicate padding, mirror padding, wrap padding handle image boundaries
- **Separable Filters**: Decompose 2D convolution into two 1D operations reducing complexity from O(n²) to O(2n)
- **Convolution Theorem**: Spatial convolution equivalent to frequency domain multiplication

## Important Concepts

- Box filter creates boxy artifacts while Gaussian provides more natural blur
- Sobel operator weights center pixels more heavily than Prewitt for better noise immunity
- Larger kernels produce more smoothing but may blur important details
- Frequency domain interpretation: low-pass filters preserve low frequencies, high-pass filters preserve high frequencies
- Nonlinear filters (median, bilateral) often perform better for specific tasks like impulse noise removal

## Notes

- Practice computing convolution output values for small examples manually
- Know common kernel types and their purposes (3×3 patterns for each filter type)
- Understand difference between correlation (slides kernel as-is) and convolution (rotates 180°)
- Be able to demonstrate separability for Gaussian filter showing computational savings
- Remember boundary handling strategies and their trade-offs
- Link filter types to applications: Gaussian for preprocessing, Sobel for edge detection, Laplacian for sharpening
