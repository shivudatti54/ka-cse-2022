# Polygon Filling Algorithms

## Introduction
Polygon filling is a fundamental operation in raster graphics that converts polygon outlines into filled regions. It is essential for rendering solid objects, shading, and creating filled shapes in computer-generated images. Various algorithms exist to efficiently fill polygons based on their edges and interior points.

## Key Concepts

### 1. Basic Definitions
- **Polygon**: A closed plane figure bounded by line segments
- **Scan-line**: A horizontal line used to fill the polygon
- **Active Edge Table (AET)**: Data structure containing edges intersecting the current scan-line

### 2. Scan-Line Algorithm (Most Important)
- Processes polygon scan-line by scan-line from top to bottom
- **Steps**:
  1. Find intersection points of scan-line with polygon edges
  2. Sort intersections from left to right
  3. Fill pixels between pairs of intersections (odd-even rule)
  4. Handle special cases (vertices, horizontal edges)
- **Advantage**: Efficient, processes one scan-line at a time

### 3. Active Edge Table (AET) Method
- Stores only edges active for current scan-line
- **Edge structure**: x-coordinate, Δx (inverse slope), ymax
- Updated as scan-line moves from one row to next
- Used with scan-line algorithm for optimization

### 4. Flood Fill Algorithm
- Starts from an interior point and fills outward
- **Types**:
  - **4-connected**: Fills up, down, left, right
  - **8-connected**: Fills in all 8 directions
- **Application**: Paint programs, region filling
- **Limitation**: Cannot fill non-seed points

### 5. Boundary Fill Algorithm
- Similar to flood fill but stops at boundary color
- Fills until specified boundary color is encountered
- Used for filling irregular shapes with defined borders

### 6. Edge Fill Algorithm
- Uses parity concept for each scan-line
- Fills based on edge intersection parity
- Processes each edge independently

### 7. YX Algorithm
- Sorts edges by y-coordinate, then by x-coordinate
- More efficient for certain polygon types
- Reduces sorting overhead

### 8. Filling Rules
- **Odd-Even Rule (Even-Odd Rule)**: Fill if odd number of intersections to the left
- **Non-Zero Winding Rule**: Fill based on edge direction (clockwise vs counter-clockwise)

## Special Considerations
- **Vertex Handling**: Proper handling of shared vertices to avoid over/under filling
- **Horizontal Edges**: Typically ignored or handled specially
- **Anti-aliasing**: Reduces jagged edges (optional advanced topic)

## Conclusion
Polygon filling algorithms are essential for raster graphics rendering. The scan-line algorithm with active edge table is the most efficient for real-time applications, while flood fill and boundary fill are simpler for interactive applications. Understanding these algorithms is crucial for implementing graphics primitives and forms a significant part of the Delhi University computer graphics syllabus (DCG).

---
*For detailed implementation, refer to Delhi University B.Sc. (H) Computer Graphics Unit III*