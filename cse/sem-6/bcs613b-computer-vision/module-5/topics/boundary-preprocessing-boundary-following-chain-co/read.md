# Boundary Preprocessing in Morphological Image Processing

## 1. Introduction

Boundary preprocessing constitutes a fundamental preprocessing step in morphological image processing and computer vision applications. It encompasses the extraction, representation, and characterization of object boundaries within digital images to produce binary representations where boundaries are distinctly delineated. This study material presents a comprehensive examination of boundary preprocessing techniques, with particular emphasis on boundary following algorithms and chain code representation schemes.

The significance of boundary preprocessing extends across numerous computer vision applications, including object detection, image segmentation, feature extraction, and shape analysis. Accurate boundary detection forms the foundation for higher-level image understanding tasks and enables precise quantification of object geometries.

## 2. Theoretical Background

### 2.1 Definitions

**Definition 2.1 (Boundary Point)**: Let I(x,y) represent a binary image where foreground pixels are denoted by value 1 (or 255) and background pixels by value 0. A pixel P(x,y) is classified as a boundary point (edge pixel) if P(x,y) = 1 and at least one of its 8-connected neighbors possesses value 0.

**Definition 2.2 (Digital Boundary)**: The digital boundary B of an object O in image I is defined as the set of all boundary points such that B = {p ∈ O | N₈(p) ∩ Oᶜ ≠ ∅}, where N₈(p) denotes the 8-neighborhood of p and Oᶜ represents the complement of O.

**Definition 2.3 (Chain Code)**: A chain code is a compact procedural representation that encodes the boundary of a connected region as a sequence of directional codes. Each code in the sequence corresponds to the direction of movement from one boundary pixel to its successive boundary pixel.

### 2.2 Boundary Extraction Principles

The extraction of boundaries from binary images relies on the fundamental principle of identifying foreground pixels that are adjacent to background pixels. Mathematically, for a binary image I with structuring element S, the boundary ∂O of object O can be defined as:

∂O = O − (O ⊖ S)

where ⊖ denotes the morphological erosion operation. Alternatively, the boundary can be defined using the gradient operator:

∂O(x,y) = |I(x+1,y) - I(x-1,y)| + |I(x,y+1) - I(x,y-1)|

## 3. Boundary Following Algorithms

### 3.1 Moore Neighbor Tracing Algorithm

The Moore neighbor tracing algorithm represents the most widely adopted method for boundary following. It systematically traverses the boundary by examining the 8-connected neighbors of each boundary pixel.

**Algorithm 3.1 (Moore Boundary Tracing)**:

```
Input: Binary image I, starting boundary pixel s
Output: Ordered list of boundary pixels B

1. Initialize B = [s]
2. Set current pixel p = s
3. Define search order for Moore neighbors starting from the
 neighbor of the entry point
4. Repeat:
 a. Examine the 8 neighbors of p in counterclockwise order
 b. Let q be the first neighbor with value 1 (foreground)
 c. If q exists:
 - Append q to B
 - Set p = q
 - Update search starting position
 d. Until q == s (returned to starting point)
5. Return B
```

The algorithm terminates when it returns to the initial starting pixel, ensuring a complete traversal of the closed boundary.

### 3.2 Algorithm Analysis

**Theorem 3.1 (Termination)**: The Moore neighbor tracing algorithm terminates after visiting each boundary pixel exactly once for a closed, connected boundary.

_Proof_: Since the boundary forms a closed curve in the 8-connected sense, the algorithm follows a deterministic path along this curve. The search always finds the next boundary pixel because every boundary pixel has at least one foreground neighbor. The algorithm terminates when it encounters the starting pixel again, which occurs after at most N iterations where N equals the number of boundary pixels. ∎

**Complexity Analysis**: The time complexity of the Moore boundary tracing algorithm is O(N), where N represents the total number of boundary pixels. The space complexity is O(N) for storing the boundary coordinates.

### 3.3 Choice of Starting Point

The selection of an appropriate starting point significantly impacts the boundary following process. Common approaches include:

1. **Scanning Method**: Traverse the image row by row until the first foreground pixel is encountered.
2. **Top-Leftmost Point**: Select the boundary pixel with minimum y-coordinate, breaking ties by minimum x-coordinate.
3. **Centroid-Based**: Use the object's centroid as a reference for initiating the search.

## 4. Chain Code Representation

### 4.1 Fundamentals

Chain codes provide a compact, computationally efficient representation of boundary geometry. They encode the relative positions of consecutive boundary pixels using a predetermined set of direction codes.

**Table 4.1: Direction Codes**

| Code | 4-Direction | 8-Direction |
| ---- | ----------- | ----------- |
| 0    | East        | East        |
| 1    | -           | Southeast   |
| 2    | South       | South       |
| 3    | -           | Southwest   |
| 4    | West        | West        |
| 5    | -           | Northwest   |
| 6    | North       | North       |
| 7    | -           | Northeast   |

### 4.2 Chain Code Generation Process

**Algorithm 4.1 (Chain Code Generation)**:

```
Input: Ordered boundary pixel sequence B = [p₀, p₁, ..., pₙ₋₁]
Output: Chain code sequence C = [c₀, c₁, ..., cₙ₋₁]

For i = 0 to n-1:
 Calculate displacement: Δx = xᵢ₊₁ - xᵢ, Δy = yᵢ₊₁ - yᵢ
 Determine direction code cᵢ based on displacement
 Append cᵢ to chain code sequence C
Return C
```

### 4.3 Normalization

Chain codes require normalization to achieve rotation invariance, as different starting points along the same boundary produce different but equivalent sequences.

**First Difference Normalization**: The first difference of a chain code converts relative direction changes into an absolute representation. For a chain code C = [c₀, c₁, ..., cₙ₋₁], the first difference ΔC is computed as:

Δcᵢ = (cᵢ₊₁ - cᵢ) mod N

where N = 4 for 4-directional chain codes and N = 8 for 8-directional chain codes.

**Starting Point Normalization**: To ensure translation invariance, the circular sequence is rotated to begin with the smallest integer representation.

### 4.4 Properties and Applications

Chain codes offer several advantageous properties:

1. **Compact Representation**: A boundary requiring N² pixels can be represented by N direction codes.
2. **Easy Computation**: Boundary length and shape descriptors can be directly computed from the chain code.
3. **Feature Extraction**: Curvature and corner detection can be performed by analyzing code transitions.

**Limitations**:

- Sensitivity to noise, which causes spurious boundary pixels
- Resolution dependence - same object at different scales yields different codes
- Boundary starting point affects the raw sequence

## 5. Implementation Considerations

### 5.1 Practical Implementation in Python

```python
import numpy as np
from collections import deque

def moore_boundary_tracing(binary_image):
 """
 Implements Moore neighbor boundary tracing algorithm.

 Parameters:
 binary_image: numpy array (binary, 0/255)

 Returns:
 boundary_pixels: list of (row, col) tuples
 """
 rows, cols = binary_image.shape

 # Find starting point (first foreground pixel)
 start = None
 for i in range(rows):
 for j in range(cols):
 if binary_image[i, j] == 255:
 start = (i, j)
 break
 if start:
 break

 if start is None:
 return []

 # 8-directional neighbors (clockwise from east)
 directions = [(0, 1), (1, 1), (1, 0), (1, -1),
 (0, -1), (-1, -1), (-1, 0), (-1, 1)]

 boundary = [start]
 current = start

 # Track direction for next search (start from direction 4 = West)
 search_dir = 4

 while True:
 found = False
 # Search 8 neighbors starting from search_dir
 for k in range(8):
 dir_idx = (search_dir + k) % 8
 dr, dc = directions[dir_idx]
 nr, nc = current[0] + dr, current[1] + dc

 # Check bounds and foreground pixel
 if 0 <= nr < rows and 0 <= nc < cols:
 if binary_image[nr, nc] == 255:
 boundary.append((nr, nc))
 current = (nr, nc)
 # Next search starts from direction (dir_idx + 5) % 8
 search_dir = (dir_idx + 5) % 8
 found = True
 break

 # Terminate if we return to start or no neighbor found
 if not found or current == start:
 break

 return boundary[:-1] if len(boundary) > 1 else boundary


def boundary_to_chain_code(boundary_pixels):
 """
 Converts boundary pixels to 8-directional chain code.
 """
 if len(boundary_pixels) < 2:
 return []

 directions = [(0, 1), (1, 1), (1, 0), (1, -1),
 (0, -1), (-1, -1), (-1, 0), (-1, 1)]

 chain_code = []
 for i in range(len(boundary_pixels) - 1):
 dr = boundary_pixels[i+1][0] - boundary_pixels[i][0]
 dc = boundary_pixels[i+1][1] - boundary_pixels[i][1]

 try:
 code = directions.index((dr, dc))
 chain_code.append(code)
 except ValueError:
 # Handle non-adjacent pixels
 chain_code.append(-1)

 return chain_code
```

### 5.2 Common Pitfalls

1. **Boundary Gaps**: Disconnected boundaries require separate tracing for each component.
2. **Diagonal Connectivity**: 8-directional chain codes may produce ambiguous results for diagonal segments.
3. **Noise Sensitivity**: Preprocessing with morphological operations (opening/closing) may be necessary.

## 6. Conclusion

Boundary preprocessing through boundary following and chain code representation provides foundational techniques for digital image analysis. The Moore neighbor tracing algorithm offers a systematic approach to boundary extraction, while chain codes enable compact representation suitable for subsequent processing stages. Understanding these methodologies is essential for applications in object recognition, medical imaging, document analysis, and autonomous navigation systems. The principles discussed herein also establish connections to advanced topics such as active contour models, level-set methods, and deep learning-based segmentation approaches.
