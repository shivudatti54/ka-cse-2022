# Stereo Vision Depth Estimation - Summary

## Key Definitions and Concepts
- **Disparity**: Horizontal pixel difference between corresponding points
- **Epipolar Plane**: Geometric plane containing camera centers and 3D point
- **Rectification**: Image transformation making epipolar lines parallel
- **Cost Volume**: 3D/4D tensor storing matching costs across disparities

## Important Formulas and Theorems
- Depth Formula: Z = fB/d
- Disparity Error Impact: δZ/Z = δd/d
- Essential Matrix: E = [t]×R
- Photometric Constraint: I₁(x,y) ≈ I₂(x+d,y)

## Key Points
- Depth accuracy improves with larger baseline but reduces maximum measurable depth
- Textureless regions cause matching ambiguities
- Deep methods learn feature representations instead of hand-crafted similarity metrics
- Semi-global matching optimizes disparity with smoothness constraints
- Temporal stereo combines multiple frames for dynamic scenes
- Active stereo systems use projected patterns for texture enhancement
- Evaluation metrics: EPE (End-Point Error), D1-all (KITTI metric)

## Common Mistakes to Avoid
- Confusing essential vs fundamental matrices
- Neglecting rectification in disparity computation
- Assuming constant disparity error across depth ranges
- Overlooking occlusion handling in matching algorithms

## Revision Tips
1. Practice deriving Z = fB/d from similar triangles
2. Use OpenCV's StereoBM/StereoSGBM for hands-on experience
3. Study KITTI leaderboard methods for current trends
4. Implement a simple block matcher with different window sizes
5. Analyze depth error surfaces for various baselines

Length: 650 words