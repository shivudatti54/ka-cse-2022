# Boundary Preprocessing

### Overview

Boundary preprocessing is a crucial step in morphological image processing. It involves transforming the image into a binary representation to effectively analyze and process its boundaries.

### Key Concepts

- **Boundary Following**
  - Essentially a procedure to create a boundary representation of an image
  - Produces a binary image where connected objects are represented by 1's
  - Not a standard morphological operation

### Chain Codes

- **Definition**: A numerical description of the gradient of an image
- **Chain Code Formula**:
  - For a pixel with neighbors (u, v): (u, v)
  - For pixels at the image border, assume direction is "outside" the image
- **Chain Code Representation**: A 4-tuple (u, v, direction, difference)
  - u and v are the horizontal and vertical directions of the gradient
  - direction is 0 if the pixel is at the top-left corner, 1 at top-right, 2 at bottom-right, and 3 at bottom-left
  - difference is 0 if the pixel is at the top-left corner, 1 at top-right, -1 at bottom-right, and -1 at bottom-left
- **Chain Code Theorem**: When two pixels have the same chain code, they are in the same connected component

### Important Formulas and Definitions

- **Boundary Image**: A binary image where connected objects are represented by 1's

### Important Theorems

- **Chain Code Theorem**: When two pixels have the same chain code, they are in the same connected component
