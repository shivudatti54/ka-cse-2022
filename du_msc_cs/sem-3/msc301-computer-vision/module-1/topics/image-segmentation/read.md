# Image Segmentation

## Introduction
Image segmentation is a fundamental task in computer vision that partitions digital images into meaningful regions or objects. This process enables higher-level tasks like object detection, medical diagnosis, and scene understanding by reducing complexity through pixel-level classification. 

With the advent of deep learning, segmentation has evolved from traditional threshold-based methods to sophisticated neural architectures like U-Net and Mask R-CNN. Current research focuses on real-time segmentation for autonomous systems, 3D medical image analysis, and weakly supervised learning to reduce annotation costs.

The importance of segmentation lies in its critical role across domains: from tumor detection in MRI scans (achieving 89% Dice coefficient in recent studies) to pedestrian detection in autonomous vehicles. Emerging applications include AR/VR content creation and satellite imagery analysis for climate change monitoring.

## Key Concepts
1. **Thresholding**: 
   - Otsu's Method: Automatically determines optimal threshold by maximizing inter-class variance
   - Adaptive Thresholding: Uses local intensity values (e.g., Gaussian-weighted sums)

2. **Edge-Based Methods**:
   - Canny Edge Detection: Multi-stage algorithm with gradient calculation and hysteresis thresholding
   - Active Contours: Energy-minimizing curves that evolve to object boundaries

3. **Region-Based Approaches**:
   - Region Growing: Aggregates pixels with similar properties (intensity, texture)
   - Watershed Algorithm: Treats image as topographic surface, flooding from markers

4. **Clustering Methods**:
   - K-Means: Groups pixels in feature space (RGB, HSV)
   - Mean Shift: Non-parametric clustering with variable bandwidth

5. **Deep Learning Architectures**:
   - Fully Convolutional Networks (FCNs): End-to-end pixel-wise classification
   - U-Net: Symmetric encoder-decoder with skip connections (standard in medical imaging)
   - Transformer-Based Models: Vision Transformers (ViTs) with self-attention mechanisms

## Examples

**Example 1: Otsu's Thresholding**
Problem: Segment blood cells from background in a microscopy image (histogram shows bimodal distribution)

Solution:
1. Compute normalized histogram (probability distribution)
2. Calculate between-class variance σ² = ω₀ω₁(μ₀-μ₁)²
3. Find threshold that maximizes σ²
4. Apply threshold: pixel > T → foreground

**Example 2: U-Net for Medical Segmentation**
Problem: Segment liver tumors in CT scans

Implementation Steps:
1. Preprocess: Normalize Hounsfield units (-100 to 400)
2. Architecture:
   - Encoder: 4 downsampling blocks (Conv+ReLU+MaxPool)
   - Bottleneck: Two 3x3 convolutions
   - Decoder: Transposed conv + skip connections
3. Loss: Dice Loss = 1 - (2|X∩Y|)/(|X|+|Y|)
4. Postprocess: Remove small false positives with connected components

**Example 3: Graph-Cut Segmentation**
Problem: Separate foreground object from background with user input

Algorithm:
1. User marks foreground/background seeds
2. Build graph where:
   - Nodes = pixels
   - Edges = similarity (color, spatial proximity)
3. Compute min-cut/max-flow using Boykov-Kolmogorov algorithm
4. Assign labels based on cut

## Exam Tips
1. Memorize Otsu's variance formula: σ² = ω₀ω₁(μ₀-μ₁)² (frequently asked derivations)
2. Understand tradeoffs: Watershed vs. Mean Shift (sensitivity to noise vs computational complexity)
3. Practice drawing U-Net architecture with exact channel dimensions
4. Know evaluation metrics: Dice Coefficient, IoU, Hausdorff Distance
5. Study recent advances: SAM (Segment Anything Model) foundation models
6. Remember edge detection steps: Noise reduction → Gradient → NMS → Thresholding
7. Compare FCNs vs CRF-RNN (conditional random fields as recurrent neural networks)