# Feature Extraction

## Overview

Feature extraction transforms raw image data into compact representations capturing essential characteristics for recognition, classification, and matching. Features can be low-level (edges, corners), mid-level (textures, shapes), or high-level (object parts), forming the bridge between images and understanding.

## Key Points

- **Feature Types**: Edges, corners, blobs, ridges, textures, shapes, color histograms
- **Edge Features**: Canny, Sobel edges capture boundary information, directional gradients
- **Corner Features**: Harris, FAST detect points with high localization, good for matching
- **Blob Features**: SIFT, SURF, ORB provide scale and rotation invariant keypoints with descriptors
- **Texture Features**: LBP (Local Binary Patterns), Gabor filters, co-occurrence matrices characterize surface patterns
- **Shape Features**: Moments, Fourier descriptors, shape context capture object geometry
- **Descriptor**: Numerical representation of feature (SIFT: 128-dim vector, HOG: histogram of gradients)

## Important Concepts

- Good features: distinctive, repeatable, local, efficient, invariant to transformations
- Keypoint + descriptor: location/scale/orientation + appearance representation
- Feature matching: compare descriptors using distance metrics (Euclidean, Hamming)
- Applications include object recognition, image retrieval, 3D reconstruction, panorama stitching

## Notes

- SIFT: scale-space extrema detection, keypoint localization, orientation assignment, descriptor computation
- Harris corner: high gradients in multiple directions, eigenvalue analysis of structure tensor
- HOG: histogram of oriented gradients in cells, useful for pedestrian detection
- LBP: compare center pixel with neighbors, create binary code, texture classification
