# Boundary Preprocessing (Boundary Following & Chain Codes)

## **Key Points**

- **Boundary Following**
  - Algorithm to track and analyze image boundaries
  - Used to identify and specify the region of interest
  - Implemented using a line buffer or a stack data structure
- **Chain Codes**
  - Numerical representation of slope and orientation of edges
  - Used to describe the orientation of the boundary
  - 8-chain codes (0-7) are used to represent 8 different directions

## **Definitions**

- **Boundary**: The set of pixels that form the outermost edge of an image
- **Edge**: A point on the boundary where the intensity changes
- **Chain Code**: A numerical representation of the slope and orientation of an edge

## **Formulas**

- **Chain Code Formula**: `c = (y2 - y1) * (x2 - x1)` where `(x1, y1)` and `(x2, y2)` are two consecutive points on the boundary
- **8-chain codes**:
  - 0: no change in slope
  - 1: horizontal edge
  - 2: vertical edge
  - 3: diagonal edge (top-left)
  - 4: diagonal edge (top-right)
  - 5: diagonal edge (bottom-left)
  - 6: diagonal edge (bottom-right)
  - 7: no change in slope

## **Theorems**

- **Chain Code Theorem**: The chain code of a boundary can be used to reconstruct the original boundary.

## **Important Concepts**

- **Boundary Following**: An algorithm that tracks and analyzes image boundaries to identify the region of interest.
- **Chain Codes**: A numerical representation of the slope and orientation of edges on an image boundary.

This summary should provide a concise overview of the key points, definitions, formulas, and theorems related to boundary preprocessing in computer vision.
