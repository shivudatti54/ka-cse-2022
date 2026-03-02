# Image Processing Basics


## Table of Contents

- [Image Processing Basics](#image-processing-basics)
- [What is Image Processing?](#what-is-image-processing)
- [Types of Image Processing Operations](#types-of-image-processing-operations)
  - [1. Point Operations (Pixel-wise)](#1-point-operations-pixel-wise)
  - [2. Neighborhood Operations](#2-neighborhood-operations)
  - [3. Global Operations](#3-global-operations)
- [Convolution and Filtering](#convolution-and-filtering)
  - [Common Kernels](#common-kernels)
- [Types of Filters](#types-of-filters)
  - [Smoothing Filters (Low-pass)](#smoothing-filters-low-pass)
  - [Sharpening Filters (High-pass)](#sharpening-filters-high-pass)
- [Morphological Operations](#morphological-operations)
- [Histogram Operations](#histogram-operations)
  - [Histogram](#histogram)
  - [Histogram Equalization](#histogram-equalization)
- [Geometric Transformations](#geometric-transformations)
- [Image Arithmetic](#image-arithmetic)
- [Summary](#summary)

## What is Image Processing?

Image processing involves manipulating digital images using mathematical operations. It transforms images to enhance quality, extract information, or prepare them for further analysis.

## Types of Image Processing Operations

### 1. Point Operations (Pixel-wise)

Operate on individual pixels independently.

| Operation    | Formula                 | Effect                              |
| ------------ | ----------------------- | ----------------------------------- |
| Brightness   | O = I + c               | Add constant to increase brightness |
| Contrast     | O = a \* I              | Multiply to increase contrast       |
| Inversion    | O = 255 - I             | Create negative image               |
| Thresholding | O = 255 if I > T else 0 | Convert to binary                   |

### 2. Neighborhood Operations

Operate on a pixel using its neighbors (convolution/filtering).

### 3. Global Operations

Use entire image information (histogram equalization).

## Convolution and Filtering

**Convolution** applies a small matrix (kernel) across the image:

```
Output[i,j] = Sum(Image[i+m,j+n] * Kernel[m,n])
```

### Common Kernels

**Identity (no change):**

```
[0 0 0]
[0 1 0]
[0 0 0]
```

**Box Blur (averaging):**

```
1/9 * [1 1 1]
      [1 1 1]
      [1 1 1]
```

**Gaussian Blur:**

```
1/16 * [1 2 1]
       [2 4 2]
       [1 2 1]
```

**Sharpen:**

```
[ 0 -1  0]
[-1  5 -1]
[ 0 -1  0]
```

## Types of Filters

### Smoothing Filters (Low-pass)

Reduce noise by averaging neighboring pixels.

| Filter    | Properties       | Use Case                      |
| --------- | ---------------- | ----------------------------- |
| Box/Mean  | Simple average   | Fast blur, reduces noise      |
| Gaussian  | Weighted average | Natural blur, pre-processing  |
| Median    | Middle value     | Removes salt-and-pepper noise |
| Bilateral | Edge-preserving  | Denoise while keeping edges   |

### Sharpening Filters (High-pass)

Enhance edges and fine details.

## Morphological Operations

Used primarily on binary images.

| Operation | Effect                | Application                  |
| --------- | --------------------- | ---------------------------- |
| Erosion   | Shrinks white regions | Remove small noise           |
| Dilation  | Expands white regions | Fill small holes             |
| Opening   | Erosion then Dilation | Remove noise, preserve shape |
| Closing   | Dilation then Erosion | Fill holes, preserve shape   |

**Structuring Element:** Small matrix (typically 3x3 or 5x5) defining the neighborhood shape.

## Histogram Operations

### Histogram

A graph showing frequency of each intensity level (0-255).

### Histogram Equalization

Redistributes pixel intensities to use full range, improving contrast.

**Steps:**

1. Compute histogram
2. Calculate cumulative distribution function (CDF)
3. Map intensities using CDF

## Geometric Transformations

| Transform   | Description                                       |
| ----------- | ------------------------------------------------- |
| Translation | Shift image position                              |
| Rotation    | Rotate by angle                                   |
| Scaling     | Resize image                                      |
| Affine      | Combines translation, rotation, scaling, shearing |
| Perspective | 3D projection onto 2D                             |

## Image Arithmetic

| Operation      | Formula           | Application                              |
| -------------- | ----------------- | ---------------------------------------- |
| Addition       | C = A + B         | Blend images, add watermark              |
| Subtraction    | C = A - B         | Background subtraction, change detection |
| Blending       | C = a*A + (1-a)*B | Weighted combination                     |
| Bitwise AND/OR | Masking           | Apply masks, combine regions             |

## Summary

- Point operations modify individual pixels (brightness, contrast)
- Convolution applies kernels for filtering effects
- Smoothing reduces noise; sharpening enhances edges
- Morphological operations work on binary images
- Histogram equalization improves contrast
- Geometric transformations change image position/size/orientation
