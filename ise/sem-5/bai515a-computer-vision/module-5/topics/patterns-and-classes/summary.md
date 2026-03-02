# Patterns and Classes

### Definitions

- **Pattern**: A regular arrangement of pixels or features in an image.
- **Class**: A set of similar patterns in an image.

### Theorems

- **Delaunay Triangulation Theorem**: Every pattern can be represented by a triangulated mesh.
- **Minkowski Theorem**: The sum of two sets is equal to the set of all points that are within a certain distance of at least one of the sets.

### Formulas

- **Erosion Formula**: Eroded image = (Image \∩ (Kernel \∩ Image))
- **Dilation Formula**: Dilated image = (Image \∪ (Kernel \∪ Image))
- **Minkowski Sum Formula**: Minkowski sum = Image \∪ (Kernel \∪ Image)

### Key Concepts

- **Structural Elements**: Used to describe patterns in an image.
- **Kernel**: A small structural element used for erosion and dilation.
- **Pattern Class**: A set of similar patterns in an image.

### Important Concepts in Morphological Image Processing

- ** hit-or-miss operation**: Tests if a pattern is present in an image.
- **Opening**: Removes small details from an image while preserving large features.
- **Closing**: Fills small holes in an image while preserving large features.
