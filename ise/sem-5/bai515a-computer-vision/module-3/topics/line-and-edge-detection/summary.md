# Line and Edge Detection

## Overview

Edge detection identifies significant local intensity changes corresponding to object boundaries, surface orientation discontinuities, or material property changes. Line detection finds thin elongated structures. Both are fundamental for feature extraction, segmentation, and object recognition.

## Key Points

- **Edge Definition**: Significant local intensity change, characterized by magnitude (strength) and direction
- **Gradient-Based Detection**: Sobel, Prewitt, Roberts operators compute first derivatives approximating ∇f = [∂f/∂x, ∂f/∂y]
- **Canny Edge Detector**: Optimal multi-stage algorithm - Gaussian smoothing → gradient computation → non-maximum suppression → hysteresis thresholding
- **Laplacian (Second Derivative)**: ∇²f detects zero-crossings, sensitive to noise, often combined with Gaussian (LoG)
- **Hough Transform**: Detects lines by transforming to parameter space, robust to gaps and noise
- **Line Detection Masks**: Specialized kernels for horizontal, vertical, diagonal lines

## Important Concepts

- Edge magnitude: M = √(Gx² + Gy²), direction: θ = tan⁻¹(Gy/Gx)
- Canny advantages: good detection, good localization, single response per edge
- Non-maximum suppression thins edges to single-pixel width by suppressing non-peak gradient magnitudes
- Hysteresis thresholding uses two thresholds (high, low) to link edge pixels reducing false edges

## Notes

- Sobel weights center pixels more than Prewitt for better noise performance
- Canny's three criteria: good detection, good localization, minimal false response
- Hough transform maps (x,y) edge points to (ρ,θ) parameter space, intersections indicate lines
- First derivative detects edges, second derivative detects zero-crossings (edge centers)
