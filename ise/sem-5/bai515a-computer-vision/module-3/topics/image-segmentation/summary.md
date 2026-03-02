# Image Segmentation

## Overview

Image segmentation partitions images into meaningful regions or objects by grouping pixels with similar characteristics. This fundamental CV task bridges low-level processing and high-level understanding, enabling object recognition, scene analysis, and image understanding.

## Key Points

- **Segmentation Goal**: Partition image into regions R1, R2, ..., Rn where union=image, regions disjoint, each region homogeneous
- **Thresholding**: Simplest method using intensity values, global or adaptive, Otsu's method finds optimal threshold
- **Edge-Based**: Detect discontinuities using edge operators (Sobel, Canny), link edges to form region boundaries
- **Region-Based**: Region growing (merge similar neighbors), region splitting (divide non-uniform regions), split-and-merge
- **Clustering**: K-means, mean-shift group pixels in feature space (intensity, color, texture)
- **Watershed**: Treats image as topographic surface, finds catchment basins, often over-segments

## Important Concepts

- No single best segmentation method - depends on application and image characteristics
- Thresholding fast but limited to images with distinct intensity modes
- Edge-based finds boundaries but must link edges to form closed regions
- Region-based methods produce connected regions but sensitive to initialization
- Applications include medical image analysis, object detection, autonomous driving, image editing

## Notes

- Understand trade-offs: thresholding (fast/simple/limited), edges (boundaries/gaps), regions (connected/initialization-sensitive)
- Otsu's method automatically finds threshold maximizing between-class variance
- Canny edge detector: smooth→gradient→non-max suppression→hysteresis thresholding
- Region growing requires seed points and homogeneity criterion
