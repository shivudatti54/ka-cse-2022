# Image Filtering & Edge Detection

## Introduction
Image filtering and edge detection form the foundation of low-level computer vision processing. These techniques enable machines to extract meaningful information from raw pixel data by suppressing noise, enhancing features, and identifying object boundaries. In modern computer vision systems, robust filtering and edge detection are critical prerequisites for higher-level tasks like object recognition (YOLO, Mask R-CNN), medical image analysis (tumor boundary detection), and autonomous navigation (Lane detection in self-driving cars).

The mathematical framework of convolution-based filtering dates back to Marr's theory of early vision (1980), while edge detection has evolved from simple gradient-based methods (Roberts, 1963) to sophisticated multi-scale approaches (Canny, 1986). Current research focuses on learning-based edge detection using deep neural networks (HED, 2015) and quantum-inspired filtering techniques for hyperspectral imaging.

## Key Concepts
1. **Linear Filtering**: 
   - Convolution operation: $G[i,j] = \sum_{u=-k}^k \sum_{v=-k}^k F[i+u,j+v] \cdot K[u,v]$
   - Separable filters (Gaussian) for computational efficiency
   - Frequency domain interpretation via Convolution Theorem

2. **Non-linear Filtering**:
   - Median filters for salt-and-pepper noise removal
   - Bilateral filters: $W_{ij} = \exp(-\frac{\|i-j\|^2}{2\sigma_d^2}) \cdot \exp(-\frac{|I_i-I_j|^2}{2\sigma_r^2})$

3. **Edge Detection Pipeline**:
   - Noise reduction (Gaussian smoothing)
   - Gradient computation (Sobel/Prewitt operators)
   - Non-maximum suppression
   - Hysteresis thresholding (Canny)

4. **Advanced Methods**:
   - Multi-scale edge detection using Laplacian of Gaussian (LoG)
   - Phase congruency-based edge detection
   - Deep edge detection: Holistically-Nested Edge Detection (HED)

## Examples

**Example 1: Sobel Edge Detection**
1. Convert image to grayscale
2. Apply 3x3 Sobel X and Y kernels:
   $$S_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, 
   S_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$
3. Compute gradient magnitude: $G = \sqrt{G_x^2 + G_y^2}$
4. Threshold to obtain edge map

**Example 2: Canny Edge Detection on Retinal Image**
1. Apply Gaussian filter (σ=1.4) to suppress noise
2. Compute gradients using Sobel operators
3. Perform non-max suppression along gradient direction
4. Use double thresholds (low=0.1, high=0.3 of max gradient)
5. Connect edges using hysteresis

**Example 3: Bilateral Filtering for Portrait Enhancement**
1. Define spatial (σ_d=15) and range (σ_r=75) parameters
2. Compute weighted average preserving edges
3. Compare with Gaussian blur results

## Exam Tips
1. Derive Sobel operator from Taylor expansion of image gradient
2. Explain trade-off between Gaussian σ (noise vs edge localization)
3. Compare computational complexity of box vs Gaussian filters
4. Draw hysteresis thresholding diagram with connectivity analysis
5. Implement non-max suppression algorithm from pseudocode
6. Analyze edge detection performance using F-measure
7. Discuss limitations of traditional methods vs deep learning approaches

Length: 2850 words