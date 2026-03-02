# SIFT, SURF, ORB Features - Summary

## Key Definitions and Concepts
- **DoG (Difference of Gaussian):** Scale-space representation for SIFT
- **Integral Image:** Precomputed sums for fast SURF computations
- **oFAST:** Oriented FAST detector with intensity centroid
- **rBRIEF:** Rotation-aware BRIEF descriptor
- **Hessian Matrix:** Used for keypoint localization and edge rejection

## Important Formulas and Theorems
- **Scale-space:** L(x,y,σ) = G(x,y,σ) * I(x,y)
- **DoG:** D(x,y,σ) = L(x,y,kσ) - L(x,y,σ)
- **Hessian (SIFT):** H = [D_xx D_xy; D_xy D_yy], reject if (Tr(H)²/Det(H)) > (r+1)²/r
- **SURF Hessian:** det(H) = D_xxD_yy - (0.9D_xy)²
- **ORB Orientation:** θ = arctan(m01/m10) where m_ij are intensity moments

## Key Points
- SIFT: Most robust but computationally intensive (128D float)
- SURF: 3x faster than SIFT using integral images (64D float)
- ORB: Fastest with binary descriptors (256 bits), suitable for mobile
- All are invariant to rotation and partially to illumination
- Matching requires different strategies: L2 for SIFT/SURF, Hamming for ORB
- Modern alternatives: Learned features (SuperPoint, LF-Net) but less interpretable
- Essential for SLAM, image registration, and 3D reconstruction

## Common Mistakes to Avoid
- Confusing scale-space construction methods (Gaussian vs Box filters)
- Ignoring descriptor normalization steps (L2 for SIFT, L1 for SURF)
- Using incorrect distance metrics (e.g., Hamming for SIFT)
- Overlooking orientation assignment in ORB
- Not applying ratio test in feature matching

## Revision Tips
1. Implement all three algorithms in OpenCV with different hyperparameters
2. Create comparison tables: detector type, descriptor size, invariance properties
3. Practice deriving orientation histograms from sample image patches
4. Study RANSAC integration for outlier rejection
5. Explore recent papers on hybrid feature systems (e.g., SIFT+CNN)