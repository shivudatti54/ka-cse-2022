# Keypoint Detection & Matching - Summary

## Key Definitions and Concepts
- **Keypoint**: Distinctive image location invariant to transformations
- **Descriptor**: Numerical representation of keypoint neighborhood
- **Repeatability**: Detector's ability to find same features under transformations
- **Matching**: Establishing correspondences between features in different images

## Important Formulas and Theorems
- **Harris Corner Response**:  
  \( R = \det(M) - k(\text{trace}(M))^2 \)  
  where \( M = \begin{bmatrix} I_x^2 & I_xI_y \\ I_xI_y & I_y^2 \end{bmatrix} \)
  
- **SIFT DoG**:  
  \( D(x,y,\sigma) = (G(x,y,k\sigma) - G(x,y,\sigma)) * I(x,y) \)
  
- **RANSAC Probability**:  
  \( P = 1 - (1 - w^n)^k \)  
  where w=inlier ratio, n=sample size, k=iterations

## Key Points
- SIFT uses DoG pyramid for scale invariance
- ORB combines FAST detector with BRIEF descriptor + orientation
- Binary descriptors (BRIEF, ORB) enable real-time performance
- Ratio test removes ambiguous matches
- RANSAC is crucial for robust geometric verification
- Modern learning-based methods outperform classical in complex scenes
- HPatches benchmark standard for evaluation

## Common Mistakes to Avoid
- Confusing detector and descriptor roles
- Ignoring scale-space processing in SIFT
- Using L2 distance for binary descriptors
- Forgetting to normalize descriptors
- Not considering computational constraints in algorithm selection

## Revision Tips
1. Make flashcards for detector/descriptor properties
2. Practice deriving Harris response function
3. Implement mini versions of SIFT/ORB from scratch
4. Study recent papers on LoFTR (CVPR 2021) and DISK (NeurIPS 2020)
5. Use OpenCV's evaluation module to compare real images