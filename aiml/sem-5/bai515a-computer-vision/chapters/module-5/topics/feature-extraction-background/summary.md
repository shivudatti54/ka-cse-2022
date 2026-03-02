# Feature Extraction: Background

### Overview

Feature extraction is a crucial step in computer vision that involves identifying and describing relevant information in an image.

### Key Concepts

- **Feature Extraction**: The process of identifying and describing relevant information in an image.
- **Descriptive Features**: Characteristics of an image that can be used for classification, recognition, or object detection (e.g., edges, corners, lines).
- **Intrinsic Features**: Internal properties of an object or scene that can be used for analysis (e.g., shape, color).
- **Extrinsic Features**: External properties of an object or scene that can be used for analysis (e.g., pose, orientation).

### Mathematical Formulas

- **Gradient**: $\nabla f(x,y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$
- **Sobel Operator**: $Sobel(x,y) = \frac{\partial f}{\partial x} \circ \sigma(x,y)$
- **Canny Edge Detection**: $E(x,y) = \sigma(x,y) \cdot \nabla f(x,y)$

### Important Definitions

- **Zero-Crossing**: The point where a gradient signal changes sign.
- **Zero-Crossing Distance**: The distance between two consecutive zero-crossings.
- **Edge**: A region where the intensity changes abruptly.

### Theorems

- **Canny Edge Detection Theorem**: A set of edge pixels can be obtained by applying the Canny edge detection algorithm to an image.
- **Hausdorff Distance**: A measure of the similarity between two sets of points.

### Key Algorithms

- **Sobel Operator**: A edge detection algorithm that uses gradient analysis.
- **Canny Edge Detection**: A multi-stage edge detection algorithm that uses gradient analysis and non-maximum suppression.
- **Non-Maximum Suppression**: A technique used to reduce the number of edge pixels.

### Important Terms

- **Open Set**: A set of pixels where the edge is oriented towards the interior.
- **Closed Set**: A set of pixels where the edge is oriented towards the exterior.
- **Boundary**: The region where the open and closed sets meet.
