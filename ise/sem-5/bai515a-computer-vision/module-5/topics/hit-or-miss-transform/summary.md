# Hit-or-Miss Transform

## Overview

The Hit-or-Miss Transform is a morphological operation for shape detection and pattern matching in binary images. It matches both foreground (hit) and background (miss) patterns simultaneously, enabling precise shape localization and feature extraction.

## Key Points

- **Definition**: A⊛B = (A⊖B1) ∩ (A^c⊖B2), where B1=foreground SE, B2=background SE
- **Dual SEs**: B1 matches object pattern (hit), B2 matches background pattern (miss)
- **Shape Detection**: Locates exact shape and orientation of template defined by B1 and B2
- **Corner Detection**: Specialized SEs detect corners by matching L-shaped foreground and diagonal background patterns
- **Thinning and Thickening**: Iterative hit-or-miss with rotation-invariant SEs extracts skeletons

## Important Concepts

- Hit-or-miss more selective than erosion alone by constraining both foreground and background
- SE pair (B1, B2) must be disjoint and their union covers neighborhood
- Result indicates positions where pattern exactly matches
- Applications include shape matching, corner detection, skeleton extraction, defect detection

## Notes

- Hit pattern (B1) specifies required foreground pixels
- Miss pattern (B2) specifies required background pixels
- Output 1 only where B1 fits in foreground AND B2 fits in background
- Thinning: subtract hit-or-miss result from image iteratively until convergence
