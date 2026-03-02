# 3D Vision: Point Clouds - Summary

## Key Definitions and Concepts
- **Point Cloud**: Unstructured set of {x,y,z} coordinates ± additional attributes
- **Voxelization**: 3D grid quantization for CNN processing
- **FPFH**: 33-bin histogram capturing local geometry around a point
- **T-Net**: Spatial transformer subnetwork in PointNet

## Important Formulas and Theorems
- **ICP Energy Function**: min_{R,t} Σ ||Rp_i + t - q_j||²
- **Surface Normal via PCA**: Eigenvector of smallest eigenvalue of covariance matrix C = 1/k Σ(p_i - μ)(p_i - μ)^T
- **RANSAC Probability**: P = 1 - (1 - w^n)^k (w=inlier ratio, n=sample size)
- **PointNet Global Feature**: h = MAX{MLP(p_i)} over all points

## Key Points
- LiDAR point density decreases with distance (sparsity challenge)
- ICP requires good initialization (use FPFH for coarse alignment)
- PointNet processes raw points without voxelization (permutation invariant)
- RandLA-Net uses random sampling for efficient large-scale processing
- Dynamic graphs in DGCNN adapt to non-uniform point densities
- Attention in Point Transformer improves long-range dependencies
- Open3D/PCL are standard libraries for point cloud processing

## Common Mistakes to Avoid
- Applying 2D CNNs directly to unordered point clouds
- Ignoring normals' orientation consistency in reconstruction
- Using ICP without outlier rejection (divergence risk)
- Confusing RANSAC inliers with ground truth annotations

## Revision Tips
1. Implement ICP from scratch using NumPy SVD
2. Visualize FPFH descriptors using Open3D's visualization tools
3. Compare PointNet vs. PointNet++ on ModelNet40 classification
4. Practice with KITTI dataset for real-world LiDAR processing

Length: 400-800 words