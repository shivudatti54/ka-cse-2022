# Image Processing Point Operators

## Overview

Image processing encompasses various mathematical operations to manipulate digital images for enhancement, analysis, or preparation for further processing. Operations are categorized as point operations (pixel-wise), neighborhood operations (convolution), and global operations (whole image).

## Key Points

- **Point Operations**: Brightness (O=I+c), Contrast (O=a×I), Inversion (O=255-I), Thresholding (binary conversion)
- **Convolution/Filtering**: Applies kernel across image: Output[i,j] = Σ(Image[i+m,j+n] × Kernel[m,n])
- **Common Kernels**: Identity (no change), Box blur (1/9 all ones), Gaussian (weighted center), Sharpen (negative neighbors, positive center)
- **Smoothing Filters**: Box/Mean (fast blur), Gaussian (natural blur), Median (salt-and-pepper noise), Bilateral (edge-preserving)
- **Morphological Operations**: Erosion (shrink), Dilation (expand), Opening (erosion+dilation), Closing (dilation+erosion) on binary images
- **Histogram Equalization**: Redistributes intensities using CDF to improve contrast across full range
- **Geometric Transformations**: Translation (shift), Rotation, Scaling (resize), Affine, Perspective projection

## Important Concepts

- Structuring element (small matrix) defines neighborhood shape for morphological operations
- Histogram shows frequency of intensity levels revealing image characteristics
- Image arithmetic: Addition (blending), Subtraction (background removal), Blending (weighted combination)
- Geometric transforms change position/size/orientation while preserving image content

## Notes

- Understand three operation categories: point (individual pixels), neighborhood (convolution), global (histogram)
- Know standard kernel patterns and their effects on images
- Practice applying morphological operations on binary images step-by-step
- Histogram equalization improves contrast by spreading intensity distribution
- Different filter types serve different purposes: smooth for noise, sharpen for edges, morphology for binary
