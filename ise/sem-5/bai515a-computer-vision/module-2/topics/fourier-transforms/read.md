# Fourier Transforms in Image Processing


## Table of Contents

- [Fourier Transforms in Image Processing](#fourier-transforms-in-image-processing)
- [Introduction to Fourier Transforms](#introduction-to-fourier-transforms)
- [Mathematical Foundation](#mathematical-foundation)
  - [1D Fourier Transform](#1d-fourier-transform)
  - [2D Fourier Transform for Images](#2d-fourier-transform-for-images)
- [Key Concepts in Fourier Image Processing](#key-concepts-in-fourier-image-processing)
  - [Frequency Domain Representation](#frequency-domain-representation)
  - [Visualization of Fourier Transforms](#visualization-of-fourier-transforms)
  - [Important Properties](#important-properties)
- [Discrete Fourier Transform (DFT) Implementation](#discrete-fourier-transform-dft-implementation)
  - [DFT Computation Steps](#dft-computation-steps)
- [Applications in Image Processing](#applications-in-image-processing)
  - [Filtering in Frequency Domain](#filtering-in-frequency-domain)
  - [Comparison of Filtering Approaches](#comparison-of-filtering-approaches)
  - [Image Analysis and Enhancement](#image-analysis-and-enhancement)
- [Practical Implementation Considerations](#practical-implementation-considerations)
  - [Padding for Convolution](#padding-for-convolution)
  - [MATLAB/Python Implementation Example](#matlabpython-implementation-example)
- [Read image](#read-image)
- [Apply Fourier Transform](#apply-fourier-transform)
- [Create low-pass filter mask](#create-low-pass-filter-mask)
- [Apply mask and inverse DFT](#apply-mask-and-inverse-dft)
- [Exam Tips](#exam-tips)

## Introduction to Fourier Transforms

The Fourier Transform is a fundamental mathematical tool in image processing that allows us to decompose an image from its spatial domain (pixel intensities across x and y coordinates) into its frequency domain representation. This transformation reveals the frequency components that make up the image, providing powerful capabilities for analyzing and manipulating visual information.

In computer vision, Fourier Transforms help us understand how much of each frequency component exists in an image. Low frequencies correspond to gradual changes in intensity (smooth areas), while high frequencies correspond to rapid changes (edges, noise, fine details).

## Mathematical Foundation

### 1D Fourier Transform

For a continuous function f(x), the Fourier Transform F(ω) is defined as:

```
F(ω) = ∫ f(x)e^(-jωx) dx
```

And the inverse Fourier Transform is:

```
f(x) = (1/2π) ∫ F(ω)e^(jωx) dω
```

### 2D Fourier Transform for Images

For images, we use the 2D Fourier Transform. For an image f(x,y) of size M×N:

**Forward Transform:**

```
F(u,v) = (1/MN) ∑∑ f(x,y)e^(-j2π(ux/M + vy/N))
```

**Inverse Transform:**

```
f(x,y) = ∑∑ F(u,v)e^(j2π(ux/M + vy/N))
```

Where:

- (x,y) = spatial coordinates
- (u,v) = frequency coordinates
- F(u,v) = frequency domain representation

## Key Concepts in Fourier Image Processing

### Frequency Domain Representation

When we apply Fourier Transform to an image, we get a complex-valued function represented as:

```
F(u,v) = R(u,v) + jI(u,v)
```

We typically work with the magnitude spectrum:

```
|F(u,v)| = √[R²(u,v) + I²(u,v)]
```

And the phase spectrum:

```
φ(u,v) = tan⁻¹[I(u,v)/R(u,v)]
```

### Visualization of Fourier Transforms

```
Original Image (Spatial Domain)      Fourier Transform (Frequency Domain)
    [Image Matrix]                       [Frequency Spectrum]

    +---------------+                    +-------------------+
    |               |    FT Forward     |                   |
    |   Pixel       |   ------------>   |   Frequency       |
    |   Intensities |                    |   Components      |
    |               |    FT Inverse     |                   |
    +---------------+   <------------   +-------------------+
```

The frequency domain is typically centered such that low frequencies are at the center and high frequencies are at the edges.

### Important Properties

1. **Linearity**: FT(af(x,y) + bg(x,y)) = aF(u,v) + bG(u,v)
2. **Translation**: f(x-x₀, y-y₀) ⇔ F(u,v)e^(-j2π(ux₀/M + vy₀/N))
3. **Convolution Theorem**: f(x,y)\*g(x,y) ⇔ F(u,v)G(u,v)
4. **Correlation Theorem**: f(x,y)∘g(x,y) ⇔ F(u,v)G\*(u,v)
5. **Separability**: The 2D FT can be computed as successive 1D transforms

## Discrete Fourier Transform (DFT) Implementation

For digital images, we use the Discrete Fourier Transform (DFT). The 2D DFT for an M×N image is:

```
F(u,v) = (1/MN) ∑∑ f(x,y)e^(-j2π(ux/M + vy/N))
```

The Fast Fourier Transform (FFT) is an efficient algorithm that reduces the computation from O(N²) to O(N log N).

### DFT Computation Steps

1. Apply 1D DFT to each row of the image
2. Apply 1D DFT to each column of the result
3. Normalize the output

```
Image Matrix          Row-wise DFT        Column-wise DFT
+---+---+---+        +---+---+---+        +---+---+---+
| a | b | c |        | A | B | C |        | P | Q | R |
+---+---+---+        +---+---+---+        +---+---+---+
| d | e | f |  --->  | D | E | F |  --->  | S | T | U |
+---+---+---+        +---+---+---+        +---+---+---+
| g | h | i |        | G | H | I |        | V | W | X |
+---+---+---+        +---+---+---+        +---+---+---+
```

## Applications in Image Processing

### Filtering in Frequency Domain

Fourier transforms enable powerful filtering operations:

**Low-pass Filtering**: Blurs image by removing high frequencies

```
G(u,v) = F(u,v)H(u,v)
where H(u,v) = { 1 if D(u,v) ≤ D₀, 0 otherwise }
```

**High-pass Filtering**: Sharpens image by removing low frequencies

```
H(u,v) = { 0 if D(u,v) ≤ D₀, 1 otherwise }
```

**Band-pass Filtering**: Keeps specific frequency ranges

```
H(u,v) = { 1 if D₁ ≤ D(u,v) ≤ D₂, 0 otherwise }
```

### Comparison of Filtering Approaches

| Method                 | Spatial Domain           | Frequency Domain                    |
| ---------------------- | ------------------------ | ----------------------------------- |
| **Implementation**     | Convolution with kernel  | Multiplication with filter function |
| **Computational Cost** | O(N²k²) for k×k kernel   | O(N² log N) with FFT                |
| **Flexibility**        | Limited to small kernels | Any filter shape possible           |
| **Understanding**      | Local operations         | Global frequency analysis           |

### Image Analysis and Enhancement

1. **Periodic Noise Removal**: Isolate and remove periodic patterns
2. **Texture Analysis**: Analyze repetitive patterns through frequency content
3. **Image Compression**: JPEG uses DCT (related to Fourier Transform)
4. **Template Matching**: Using correlation theorem for pattern recognition

## Practical Implementation Considerations

### Padding for Convolution

When filtering, we need to avoid wrap-around errors by padding the image:

```
Original Image: M×N
Padding size: P = 2M, Q = 2N (typically)
```

### MATLAB/Python Implementation Example

```python
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('image.jpg', 0)

# Apply Fourier Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Create low-pass filter mask
rows, cols = img.shape
crow, ccol = rows//2, cols//2
mask = np.zeros((rows, cols), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# Apply mask and inverse DFT
fshift = fshift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
```

## Exam Tips

1. **Remember the Convolution Theorem**: It's frequently tested and crucial for understanding filtering operations
2. **Understand Phase vs Magnitude**: Phase information often contains more structural information than magnitude
3. **Visualize Frequency Domain**: Practice interpreting Fourier spectra of simple images (stripes, circles, etc.)
4. **Know the Computational Advantage**: FFT reduces O(N²) to O(N log N) - this is often an exam question
5. **Practice Padding Calculations**: Be able to determine proper padding sizes for convolution operations
6. **Compare Spatial vs Frequency Domain**: Understand when each approach is more appropriate
7. **Memorize Key Properties**: Linearity, translation, convolution theorem are commonly tested
