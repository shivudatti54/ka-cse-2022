# HOG Features (Histogram of Oriented Gradients)

## What is HOG?

Histogram of Oriented Gradients (HOG) is a feature descriptor primarily used for object detection, especially pedestrian detection. Developed by Dalal and Triggs in 2005, it captures edge/gradient structure that characterizes local object appearance and shape.

## HOG Algorithm Steps

### 1. Preprocessing

- Resize image to fixed size (e.g., 64x128 for pedestrian detection)
- Optional: Gamma/color normalization

### 2. Compute Gradients

Calculate gradient magnitude and direction at each pixel:

```
Gx = I(x+1, y) - I(x-1, y)
Gy = I(x, y+1) - I(x, y-1)
Magnitude = sqrt(Gx^2 + Gy^2)
Direction = atan2(Gy, Gx)
```

### 3. Create Cell Histograms

- Divide image into cells (typically 8x8 pixels)
- For each cell, create histogram of gradient orientations
- Usually 9 bins (0-180 degrees, unsigned gradients)
- Weight by gradient magnitude

### 4. Block Normalization

- Group cells into blocks (typically 2x2 cells)
- Normalize histogram values within each block
- Overlapping blocks for robustness
- Common: L2-norm normalization

### 5. Concatenate to Form Descriptor

Combine all block histograms into single feature vector.

## HOG Descriptor Size Calculation

For 64x128 image with 8x8 cells, 2x2 blocks, 9 bins:

```
Cells: 64/8 x 128/8 = 8 x 16 = 128 cells
Blocks: (8-1) x (16-1) = 7 x 15 = 105 blocks (with stride 1)
Features per block: 2 x 2 x 9 = 36
Total: 105 x 36 = 3780 dimensions
```

## Key Design Choices

| Parameter     | Typical Value | Effect                                |
| ------------- | ------------- | ------------------------------------- |
| Cell size     | 8x8 pixels    | Larger = more invariance, less detail |
| Block size    | 2x2 cells     | Affects normalization context         |
| Bins          | 9 (unsigned)  | More bins = finer orientation         |
| Block stride  | 1 cell        | Overlap for robustness                |
| Normalization | L2-norm       | Handles illumination changes          |

## Block Normalization Methods

| Method  | Formula    |
| ------- | ---------- | --- | --- | --- | --------- |
| L2-norm | v / sqrt(  |     | v   |     | ^2 + e^2) |
| L1-norm | v / (      |     | v   |     | \_1 + e)  |
| L1-sqrt | sqrt(v / ( |     | v   |     | \_1 + e)) |

## Comparison with Other Descriptors

| Feature    | HOG                  | SIFT            | LBP                    |
| ---------- | -------------------- | --------------- | ---------------------- |
| Focus      | Shape/edges          | Keypoints       | Texture                |
| Invariance | Partial illumination | Scale, rotation | Illumination           |
| Detection  | Dense                | Sparse          | Dense                  |
| Use case   | Object detection     | Matching        | Texture classification |

## Applications

1. **Pedestrian Detection**: Original and most famous application
2. **Vehicle Detection**: In autonomous driving
3. **Face Detection**: Combined with SVM classifier
4. **Hand Gesture Recognition**: Shape-based features
5. **Object Recognition**: As part of sliding window detector

## Advantages

- Captures local shape well
- Robust to geometric and photometric transformations
- Works well with linear classifiers (SVM)
- Interpretable features

## Limitations

- Not scale invariant (requires multi-scale detection)
- Not rotation invariant (oriented objects)
- High-dimensional descriptor
- Slower than deep learning approaches

## Summary

- HOG captures gradient orientations in local regions
- Four stages: gradients, cell histograms, block normalization, concatenation
- Primarily used for object detection with sliding window
- 3780-D descriptor for 64x128 image (standard pedestrian)
- Combined with linear SVM for classification
