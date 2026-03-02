# Point Detection

## Overview

Point detection identifies isolated pixels that differ significantly from their neighborhoods, useful for finding spots, noise, or features like interest points and corners. Point detectors are fundamental building blocks for feature-based matching and tracking.

## Key Points

- **Point Detection Principle**: Compare pixel with neighborhood using Laplacian or similar operators to find isolated significant responses
- **Laplacian Mask**: Isotropic second derivative operator detecting points where ∇²f has large magnitude
- **Corner Detection**: Harris corner detector finds points with large intensity variations in all directions using eigenvalues of structure tensor
- **Interest Points**: SIFT, SURF detect scale-invariant keypoints robust to transformations
- **Threshold Selection**: Points detected when |R| > T where R is response function

## Important Concepts

- Point detection uses second derivatives (Laplacian) or local structure analysis (Harris)
- Corners are points with high intensity variation in multiple directions, useful for matching
- Harris detector: λ1 and λ2 both large indicates corner, R = λ1×λ2 - k×(λ1+λ2)²
- Applications include feature matching, image registration, object tracking, 3D reconstruction

## Notes

- Laplacian point detection: convolve with Laplacian mask, threshold large absolute responses
- Harris corner detector computes structure matrix M from gradients, analyzes eigenvalues
- SIFT keypoints are scale and rotation invariant, enable robust matching across viewpoints
- Point detection precedes feature description and matching in many CV pipelines
