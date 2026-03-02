# **Patterns and Classes**

### Definition

- A pattern is a region of an image that has a specific shape or structure.
- A class is a group of pixels that share similar characteristics.

### Key Concepts

- **Connectivity**: The way pixels are connected to each other, used to define patterns.
- **Structural Element**: A small region of the image that is used to define a pattern.
- **Kernel**: A square or rectangular region that is used as a structural element.

### Important Formulas

- **Erosion**: Erode an image by applying a structuring element.
- **Dilation**: Dilate an image by applying a structuring element.
- **Opening**: Apply erosion followed by dilation to remove small objects.
- **Closing**: Apply dilation followed by erosion to fill small holes.

### Theorems

- **Theorem of Morphological Operations**: The result of a morphological operation is independent of the order of the operations.
- **Theorem of Dissimilarity**: The dissimilarity between two images is preserved under morphological operations.

### Important Definitions

- **Pixel**: A single unit of an image.
- **Neighbor**: A pixel that shares a border with another pixel.
- **Support**: The region of pixels that are connected to a pixel.

### Important Classes

- **Connected Component**: A group of pixels that are connected to each other.
- **Contrast Limited**: A region of an image that has a high contrast between pixels.
- **Closed Region**: A region of an image that has no holes or gaps.
