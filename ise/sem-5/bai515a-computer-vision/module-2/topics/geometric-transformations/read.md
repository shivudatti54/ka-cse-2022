# Geometric Transformations in Image Processing


## Table of Contents

- [Geometric Transformations in Image Processing](#geometric-transformations-in-image-processing)
- [Introduction to Geometric Transformations](#introduction-to-geometric-transformations)
- [Fundamental Concepts](#fundamental-concepts)
  - [Coordinate Systems](#coordinate-systems)
  - [Forward vs. Inverse Mapping](#forward-vs-inverse-mapping)
- [Types of Geometric Transformations](#types-of-geometric-transformations)
  - [1. Linear Transformations](#1-linear-transformations)
  - [2. Projective Transformations (Homographies)](#2-projective-transformations-homographies)
  - [3. Nonlinear Transformations](#3-nonlinear-transformations)
- [Implementation Considerations](#implementation-considerations)
  - [Interpolation Methods](#interpolation-methods)
  - [Image Registration Process](#image-registration-process)
- [Applications of Geometric Transformations](#applications-of-geometric-transformations)
  - [1. Image Registration](#1-image-registration)
  - [2. Camera Calibration](#2-camera-calibration)
  - [3. Image Morphing](#3-image-morphing)
  - [4. Panoramic Image Stitching](#4-panoramic-image-stitching)
  - [5. Document Image Processing](#5-document-image-processing)
- [Comparison of Transformation Types](#comparison-of-transformation-types)
- [Implementation Example: Affine Transformation](#implementation-example-affine-transformation)
- [Apply transformation using inverse mapping](#apply-transformation-using-inverse-mapping)
- [Example: Rotate 30 degrees clockwise around center](#example-rotate-30-degrees-clockwise-around-center)
- [Challenges and Limitations](#challenges-and-limitations)
- [Exam Tips](#exam-tips)

## Introduction to Geometric Transformations

Geometric transformations are fundamental operations in image processing that alter the spatial relationships between pixels in an image. Unlike point operations that modify pixel values or neighborhood operations that change values based on surrounding pixels, geometric transformations change the positions of pixels while typically preserving their values.

These transformations are essential for various computer vision applications including:

- Image registration (aligning multiple images)
- Camera calibration and correction
- Image morphing and warping
- Perspective correction
- Image stitching for panoramas

## Fundamental Concepts

### Coordinate Systems

In digital image processing, we work with two coordinate systems:

1. **Spatial Domain (x,y)**: The original image coordinates
2. **Transformed Domain (u,v)**: The new coordinates after transformation

```
Original Image Coordinates      Transformed Image Coordinates
      (x,y)          →               (u,v)
```

The transformation is defined by mapping functions:

- u = f(x,y)
- v = g(x,y)

### Forward vs. Inverse Mapping

There are two approaches to implementing geometric transformations:

**Forward Mapping:**

- For each pixel in the source image (x,y), compute its new position (u,v) in the destination image
- Problem: May leave holes or cause overlaps in the output image

```
Source Image → Destination Image
(x,y) → (u,v)
```

**Inverse Mapping (More Common):**

- For each pixel in the destination image (u,v), find which pixel from the source image (x,y) should be placed there
- Avoids holes and overlaps in the output image

```
Destination Image → Source Image
(u,v) → (x,y)
```

## Types of Geometric Transformations

### 1. Linear Transformations

Linear transformations preserve the operations of vector addition and scalar multiplication. They can be represented using matrix multiplication.

#### Affine Transformations

Affine transformations preserve points, straight lines, and planes. They include:

**Translation:**
Moves every point by a fixed distance in a specified direction.

```
[ u ]   =   [ 1  0  tx ]   [ x ]
[ v ]       [ 0  1  ty ]   [ y ]
[ 1 ]       [ 0  0  1  ]   [ 1 ]
```

Where tx and ty are translation distances in x and y directions.

Example: Moving an image 50 pixels to the right and 30 pixels down.

**Rotation:**
Rotates points around the origin by a specified angle θ.

```
[ u ]   =   [ cosθ  -sinθ  0 ]   [ x ]
[ v ]       [ sinθ   cosθ  0 ]   [ y ]
[ 1 ]       [  0      0    1 ]   [ 1 ]
```

Example: Rotating an image by 30 degrees clockwise.

**Scaling:**
Changes the size of an image by scaling factors sx and sy.

```
[ u ]   =   [ sx  0   0 ]   [ x ]
[ v ]       [ 0   sy  0 ]   [ y ]
[ 1 ]       [ 0   0   1 ]   [ 1 ]
```

Example: Doubling the size of an image (sx = 2, sy = 2).

**Shearing:**
Slants the shape of an image by shearing factors shx and shy.

```
[ u ]   =   [ 1   shx  0 ]   [ x ]
[ v ]       [ shy 1    0 ]   [ y ]
[ 1 ]       [ 0   0    1 ]   [ 1 ]
```

Example: Creating an italic effect on text.

#### Composite Affine Transformations

Multiple transformations can be combined through matrix multiplication:

```
T = T₁ × T₂ × T₃ × ... × Tₙ
```

The order of multiplication matters - transformations are applied from right to left.

### 2. Projective Transformations (Homographies)

Projective transformations, also known as perspective transformations or homographies, map lines to lines but do not preserve parallelism. They are represented by a 3×3 matrix in homogeneous coordinates.

```
[ u' ]   =   [ h11  h12  h13 ]   [ x ]
[ v' ]       [ h21  h22  h23 ]   [ y ]
[ w' ]       [ h31  h32  h33 ]   [ 1 ]
```

Where u = u'/w' and v = v'/w'

Projective transformations are essential for:

- Correcting perspective distortion
- Image stitching
- Augmented reality applications

### 3. Nonlinear Transformations

Nonlinear transformations include more complex mappings that cannot be represented by a simple matrix multiplication.

**Polynomial Transformations:**
Use polynomial functions to map coordinates:

- u = a₀ + a₁x + a₂y + a₃x² + a₄xy + a₅y² + ...
- v = b₀ + b₁x + b₂y + b₃x² + b₄xy + b₅y² + ...

Used for lens distortion correction and complex warping operations.

## Implementation Considerations

### Interpolation Methods

When mapping from destination to source coordinates, the calculated source position often falls between pixels. We need interpolation to estimate the pixel value.

**Nearest Neighbor Interpolation:**

- Uses the value of the closest pixel
- Fastest but produces jagged edges
- Formula: I(u,v) = I(round(x), round(y))

```
Source:      Destination:
[1][2]       [?][?]
[3][4]       [?][?]

For position (0.3, 0.7) → uses pixel (0,1) = value 3
```

**Bilinear Interpolation:**

- Weighted average of the four nearest pixels
- Smoother results than nearest neighbor
- Formula: I(u,v) = (1-a)(1-b)I(i,j) + a(1-b)I(i+1,j) + (1-a)bI(i,j+1) + abI(i+1,j+1)
  Where a = fractional part of x, b = fractional part of y

```
Weights for point (i+a, j+b):
(i,j): (1-a)(1-b)
(i+1,j): a(1-b)
(i,j+1): (1-a)b
(i+1,j+1): ab
```

**Bicubic Interpolation:**

- Uses 16 neighboring pixels
- Produces smoother results than bilinear
- More computationally expensive
- Better for photographic images

### Image Registration Process

Image registration aligns two or more images of the same scene. The process typically involves:

1. **Feature Detection**: Identify distinctive points in images
2. **Feature Matching**: Find correspondences between features
3. **Transform Estimation**: Compute transformation parameters
4. **Image Resampling**: Apply transformation with interpolation

## Applications of Geometric Transformations

### 1. Image Registration

Aligning multiple images of the same scene taken at different times, from different viewpoints, or by different sensors.

### 2. Camera Calibration

Correcting lens distortion and accounting for camera perspective using techniques like the Tsai camera calibration method.

### 3. Image Morphing

Creating smooth transitions between two images by gradually warping one image into another.

### 4. Panoramic Image Stitching

Combining multiple overlapping images to create a wider field of view panorama.

### 5. Document Image Processing

Correcting perspective distortion in photographed documents and aligning scanned pages.

## Comparison of Transformation Types

| Transformation Type | Properties Preserved     | Matrix Form     | Degrees of Freedom |
| ------------------- | ------------------------ | --------------- | ------------------ |
| Translation         | Orientation, shape, size | 2×3 affine      | 2 (tx, ty)         |
| Rotation            | Shape, size              | 2×3 affine      | 1 (θ)              |
| Scaling             | Shape, orientation       | 2×3 affine      | 2 (sx, sy)         |
| Rigid (Euclidean)   | All distances            | 2×3 affine      | 3 (θ, tx, ty)      |
| Similarity          | Angles, ratios           | 2×3 affine      | 4 (s, θ, tx, ty)   |
| Affine              | Parallelism, lines       | 2×3 affine      | 6                  |
| Projective          | Lines                    | 3×3 homogeneous | 8                  |

## Implementation Example: Affine Transformation

```python
import numpy as np
import cv2

def apply_affine_transform(image, transformation_matrix):
    """
    Apply affine transformation to an image
    """
    height, width = image.shape[:2]

    # Apply transformation using inverse mapping
    transformed_image = cv2.warpAffine(
        image,
        transformation_matrix,
        (width, height),
        flags=cv2.INTER_LINEAR
    )

    return transformed_image

# Example: Rotate 30 degrees clockwise around center
center = (width//2, height//2)
rotation_matrix = cv2.getRotationMatrix2D(center, -30, 1.0)
rotated_image = apply_affine_transform(image, rotation_matrix)
```

## Challenges and Limitations

1. **Information Loss**: Some transformations may cause loss of image information
2. **Interpolation Artifacts**: Poor interpolation can introduce blurring or aliasing
3. **Computational Complexity**: Some transformations, especially nonlinear ones, are computationally expensive
4. **Parameter Estimation**: Finding the right transformation parameters can be challenging

## Exam Tips

1. **Understand Matrix Representations**: Be comfortable with homogeneous coordinates and transformation matrices
2. **Know the Differences**: Be able to distinguish between affine, projective, and nonlinear transformations
3. **Interpolation Trade-offs**: Understand the pros and cons of different interpolation methods
4. **Order of Operations**: Remember that transformation order matters in composite transformations
5. **Practical Applications**: Be prepared to discuss real-world applications of geometric transformations
6. **Forward vs Inverse Mapping**: Know when to use each approach and their respective advantages
7. **Common Pitfalls**: Be aware of issues like holes in forward mapping and interpolation artifacts
