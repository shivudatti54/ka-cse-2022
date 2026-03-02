# Image Processing - Summary

## Key Definitions and Concepts

- Image Processing: Manipulation of digital images using algorithms to enhance quality, restore degraded images, or extract information
- Pixel: Smallest unit of a digital image, containing intensity/color values
- Grayscale Image: Single-channel image where pixel values represent brightness (0=black to 255=white)
- Color Image: Multi-channel image, typically RGB with three channels (Red, Green, Blue)
- Convolution: Mathematical operation applying a kernel to each pixel considering its neighborhood
- Kernel/Mask: Small matrix used in convolution operations defining the transformation

## Important Formulas and Theorems

- Brightness Adjustment: O(x,y) = I(x,y) + b (b is constant)
- Contrast Enhancement: O(x,y) = a × (I(x,y) - μ) + μ (a is scaling factor, μ is mean)
- Convolution: O(x,y) = Σ Σ I(i,j) × K(x-i, y-j) summed over kernel dimensions
- Gradient Magnitude: G = √(Gx² + Gy²) or G ≈ |Gx| + |Gy| for Sobel
- Histogram Equalization: new_value = floor((cdf(current) - cdf_min) × (L-1) / (N - cdf_min))

## Key Points

- Three types of image processing: enhancement (subjective quality improvement), restoration (removing degradations), and analysis (extracting quantitative information)
- Point operations transform pixels independently based on their own values; neighborhood operations consider surrounding pixels
- Common kernels: averaging (blur), Gaussian (smooth blur), Laplacian (edge enhancement), Sobel (edge detection)
- Gaussian filter is separable, enabling efficient two-pass computation
- Color spaces: RGB (display), HSV (color segmentation), LAB (perceptual uniformity)
- Sampling determines spatial resolution; quantization determines intensity resolution
- Histogram equalization automatically adjusts contrast by redistributing intensity values

## Common Mistakes to Avoid

- Confusing point operations with neighborhood operations in examination answers
- Forgetting to handle boundary conditions when applying convolution (padding is required)
- Applying histogram equalization to all three RGB channels separately, which can distort colors; apply to intensity channel instead
- Mixing up the roles of different edge detection operators (Sobel for gradients, Laplacian for second derivatives)

## Revision Tips

- Practice manually computing convolution with small kernels on 3×3 or 5×5 image patches
- Memorize the standard 3×3 kernels for common operations (average, Gaussian, Sobel horizontal/vertical, Laplacian)
- Understand the relationship between kernel values and their effects: positive center with negative neighbors detects edges; uniform positive values smooth
- Review previous year question papers to identify frequently asked question patterns
- Implement basic image processing operations in Python or MATLAB to gain practical understanding