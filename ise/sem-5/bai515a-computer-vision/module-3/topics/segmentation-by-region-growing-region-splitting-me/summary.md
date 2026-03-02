# Segmentation by Region Growing and Splitting

## Overview

Region-based segmentation groups pixels into homogeneous regions by either growing from seed points (bottom-up) or recursively splitting non-uniform regions (top-down). Split-and-merge combines both approaches for robust segmentation.

## Key Points

- **Region Growing**: Start with seed pixels, iteratively add similar neighbors based on homogeneity predicate
- **Homogeneity Predicate P(R)**: Criterion determining if region uniform (intensity range, variance, texture)
- **Region Splitting**: Recursively subdivide image into quadrants until each region satisfies P(R)
- **Region Merging**: Combine adjacent regions with similar properties
- **Split-and-Merge**: Quadtree-based approach splitting then merging adjacent similar regions
- **Watershed Segmentation**: Treats image as topographic surface, floods from local minima

## Important Concepts

- Region growing sensitive to seed point selection and similarity criterion
- Splitting creates regions too small, merging often necessary to combine over-segmented areas
- Split-and-merge uses quadtree data structure for efficient hierarchical representation
- Watershed often produces over-segmentation, requires marker-based control or post-processing

## Notes

- Region growing algorithm: (1) select seeds (2) add similar neighbors (3) repeat until no pixels added
- Homogeneity examples: |max_intensity - min_intensity| < T, variance < T, texture similarity
- Split-and-merge: split if not P(R), merge adjacent regions if P(R1∪R2)
- Watershed analogy: rain falling on terrain, water flows to catchment basins (segments)
