# Raster Scan Line Algorithms

## Introduction

Raster scan line algorithms form the backbone of computer graphics rendering, particularly in the context of understanding how geometric primitives are converted into their pixel representations on a display screen. In a raster display system, the screen is composed of a grid of pixels arranged in rows and columns, and every图形 element (line, circle, polygon) must be approximated using these discrete picture elements. This conversion process is fundamental to all graphics rendering pipelines, from simple drawing applications to complex 3D game engines.

The study of raster scan line algorithms is crucial for students of computer science because these algorithms demonstrate how continuous mathematical concepts are transformed into discrete computational procedures. Understanding these algorithms provides deep insights into the working of modern graphics systems, including those used in GUIs, computer-aided design (CAD) software, and video games. For students preparing for DU semester examinations, this topic frequently appears in both theoretical and practical components, making it essential to master not just the conceptual understanding but also the implementation details of each algorithm.

This module covers four fundamental raster scan line algorithms: the Digital Differential Analyzer (DDA) algorithm for line drawing, Bresenham's line algorithm (an optimized version of DDA), the Midpoint Circle Algorithm for circle generation, and the Scan-line Polygon Fill algorithm for area filling. Each algorithm has its own strengths, trade-offs, and appropriate use cases in real-world applications.

## Key Concepts

### 1. Understanding Raster Graphics and Pixel Representation

In a raster (or bitmap) display, the entire screen is divided into a two-dimensional array of pixels. Each pixel is identified by its (x, y) coordinates where x represents the column number and y represents the row number. When drawing geometric shapes like lines, circles, or polygons, we must determine which pixels to illuminate to create the visual impression of these shapes. The quality of the rendered image depends heavily on the algorithm used to select these pixels.

The resolution of a display is defined by the total number of pixels (width × height). Common resolutions include 1920×1080 (Full HD), 2560×1440 (2K), and 3840×2160 (4K). Higher resolution means more pixels are available to represent shapes, resulting in smoother and more accurate visual representations.

### 2. Line Drawing Algorithms

#### Digital Differential Analyzer (DDA) Algorithm

The DDA algorithm is a fundamental line drawing method that uses the parametric form of a line equation. The algorithm works by calculating the difference in x and y coordinates between the start and end points, then incrementally plotting points along the line path.

The algorithm follows these steps:
- Calculate Δx = x₂ - x₁ and Δy = y₂ - y₁
- Determine the number of steps: steps = max(|Δx|, |Δy|)
- Calculate x-increment: x-increment = Δx / steps
- Calculate y-increment: y-increment = Δy / steps
- Start from (x₁, y₁), and for each step, add the increments to the current position
- Round each calculated position to the nearest integer to get pixel coordinates

The DDA algorithm is conceptually simple and easy to understand, making it an excellent starting point for learning line drawing. However, it involves floating-point arithmetic (addition and division operations), which makes it computationally expensive compared to integer-only algorithms.

#### Bresenham's Line Algorithm

Bresenham's line algorithm is an optimization over DDA that uses only integer arithmetic, making it significantly faster and more suitable for hardware implementation. The algorithm was developed by Jack Bresenham in 1962 and remains one of the most widely used line drawing algorithms in computer graphics.

The core idea behind Bresenham's algorithm is to minimize the error between the ideal line and the selected pixels. At each step, the algorithm decides whether to move horizontally or diagonally based on the decision parameter. For lines with slope between 0 and 1 (shallow lines), the algorithm decides between plotting a pixel at (x+1, y) or (x+1, y+1).

The decision parameter P is updated using the formula:
- P₁ = 2Δy - Δx (for the first iteration)
- If P ≥ 0: Pₖ₊₁ = Pₖ + 2Δy - 2Δx, and move diagonally (x+1, y+1)
- If P < 0: Pₖ₊₁ = Pₖ + 2Δy, and move horizontally (x+1, y)

Bresenham's algorithm achieves efficiency by eliminating floating-point operations entirely, using only additions, subtractions, and bit shifting (multiplication by 2). This makes it ideal for implementation in graphics hardware and embedded systems.

### 3. Circle Drawing Algorithm: Midpoint Circle Algorithm

Drawing circles presents unique challenges compared to lines because the curvature requires continuous adjustment in both x and y directions. The Midpoint Circle Algorithm (also known as Bresenham's Circle Algorithm) is an efficient method that extends the principles of line drawing to circular arcs.

The algorithm exploits the eight-way symmetry of a circle. By drawing only one-eighth of the circle (the first octant from (0, R) to (R/√2, R/√2)), we can reflect these points to generate the complete circle using symmetry transformations.

The algorithm uses a decision parameter P to determine whether the next pixel should be at the horizontal or diagonal position:
- Initial decision parameter: P₀ = 1 - R (for circle centered at origin)
- If P < 0: Choose the horizontal pixel (x+1, y), update Pₖ₊₁ = Pₖ + 2x + 3
- If P ≥ 0: Choose the diagonal pixel (x+1, y-1), update Pₖ₊₁ = Pₖ + 2x - 2y + 5

The algorithm proceeds from the top of the circle (y = R, x = 0) and generates points in the clockwise direction through the first octant.

### 4. Scan-line Polygon Fill Algorithm

The scan-line fill algorithm is used to fill the interior of a polygon with a specified color. The algorithm works by drawing horizontal lines (scan lines) across the polygon and identifying where each scan line intersects the polygon's edges.

The key steps are:
- For each scan line y, find all intersections with polygon edges
- Sort the intersections from left to right
- Fill the pixels between pairs of intersections (inside/outside toggle)
- Handle special cases like vertices where edges meet

The algorithm must handle edge cases carefully:
- When a scan line passes through a vertex that connects two edges on the same side, it should count as only one intersection
- When a vertex connects edges on opposite sides of the scan line, it counts as two intersections
- Horizontal edges are typically ignored to avoid double-counting

The performance of the scan-line algorithm can be improved by using edge tables (ET) and active edge lists (AEL), which pre-sort edges and process only relevant edges for each scan line.

## Examples

### Example 1: DDA Algorithm for Line Drawing

**Problem:** Draw a line from point (2, 3) to point (10, 7) using the DDA algorithm.

**Solution:**

Given: x₁ = 2, y₁ = 3, x₂ = 10, y₂ = 7

Step 1: Calculate differences
- Δx = 10 - 2 = 8
- Δy = 7 - 3 = 4

Step 2: Determine number of steps
- steps = max(|8|, |4|) = 8

Step 3: Calculate increments
- x-increment = Δx / steps = 8 / 8 = 1
- y-increment = Δy / steps = 4 / 8 = 0.5

Step 4: Generate points

| Step | x | y (calculated) | Pixel (rounded) |
|------|---|-----------------|-----------------|
| 0 | 2 | 3.0 | (2, 3) |
| 1 | 3 | 3.5 | (3, 4) |
| 2 | 4 | 4.0 | (4, 4) |
| 3 | 5 | 4.5 | (5, 5) |
| 4 | 6 | 5.0 | (6, 5) |
| 5 | 7 | 5.5 | (8, 6) |
| 6 | 8 | 6.0 | (8, 6) |
| 7 | 9 | 6.5 | (9, 7) |
| 8 | 10 | 7.0 | (10, 7) |

The pixels to be illuminated are: (2,3), (3,4), (4,4), (5,5), (6,5), (8,6), (9,7), (10,7)

### Example 2: Bresenham's Line Algorithm

**Problem:** Draw a line from (2, 3) to (10, 7) using Bresenham's algorithm.

**Solution:**

Given: x₁ = 2, y₁ = 3, x₂ = 10, y₂ = 7
- Δx = 8, Δy = 4

Step 1: Since Δx > Δy, we move in x-direction with step size 1
- Initial decision parameter: P₀ = 2Δy - Δx = 2(4) - 8 = 0

Step 2: Iterate through each x-position

| k | Pₖ | Pixel (x, y) | Action | Next P |
|---|-----|--------------|--------|--------|
| 0 | 0 | (2, 3) | P < 0: horizontal | P₁ = 0 + 2(4) = 8 |
| 1 | 8 | (3, 3) | P ≥ 0: diagonal | P₂ = 8 + 2(4) - 2(8) = 8 + 8 - 16 = 0 |
| 2 | 0 | (4, 4) | P < 0: horizontal | P₃ = 0 + 8 = 8 |
| 3 | 8 | (5, 4) | P ≥ 0: diagonal | P₄ = 8 + 8 - 16 = 0 |
| 4 | 0 | (6, 5) | P < 0: horizontal | P₅ = 8 |
| 5 | 8 | (7, 5) | P ≥ 0: diagonal | P₆ = 0 |
| 6 | 0 | (8, 6) | P < 0: horizontal | P₇ = 8 |
| 7 | 8 | (9, 6) | P ≥ 0: diagonal | P₈ = 0 |
| 8 | 0 | (10, 7) | End | - |

Pixels: (2,3), (3,3), (4,4), (5,4), (6,5), (7,5), (8,6), (9,6), (10,7)

### Example 3: Midpoint Circle Algorithm

**Problem:** Generate points for a circle with radius R = 6 using the Midpoint Circle Algorithm.

**Solution:**

Given: R = 6, center at (0, 0)

Step 1: Initial values
- Start at (0, R) = (0, 6)
- Initial decision parameter: P₀ = 1 - R = 1 - 6 = -5

Step 2: Generate points in the first octant

| k | Pₖ | Point (x, y) | Action | Next P |
|---|-----|--------------|--------|--------|
| 0 | -5 | (0, 6) | P < 0: horizontal | P₁ = -5 + 2(0) + 3 = -2 |
| 1 | -2 | (1, 6) | P < 0: horizontal | P₂ = -2 + 2(1) + 3 = 3 |
| 2 | 3 | (2, 6) | P ≥ 0: diagonal | P₃ = 3 + 2(2) - 2(6) + 5 = 3 + 4 - 12 + 5 = 0 |
| 3 | 0 | (3, 5) | P ≥ 0: diagonal | P₄ = 0 + 2(3) - 2(5) + 5 = 6 - 10 + 5 = 1 |
| 4 | 1 | (4, 5) | P ≥ 0: diagonal | P₅ = 1 + 8 - 10 + 5 = 4 |
| 5 | 4 | (5, 4) | P ≥ 0: diagonal | P₆ = 4 + 10 - 8 + 5 = 11 |
| 6 | 11 | (6, 3) | P ≥ 0: diagonal | P₇ = 11 + 12 - 6 + 5 = 22 |

Stop when x ≥ y in the first octant.

Using eight-way symmetry, the complete circle points can be generated by reflecting these points across all octants.

## Exam Tips

1. **Know when to use which algorithm**: For DU exams, remember that DDA is conceptually simpler and uses floating-point arithmetic, while Bresenham's uses only integer operations and is more efficient. Bresenham's algorithm is the preferred method in practice.

2. **Decision parameter initialization**: For Bresenham's line algorithm, the initial decision parameter is P₀ = 2Δy - Δx. For the Midpoint Circle Algorithm, it's P₀ = 1 - R (for radius R). These are frequently tested in exams.

3. **Understanding the decision logic**: In Bresenham's algorithm, if P ≥ 0, move diagonally (increment both x and y); if P < 0, move horizontally (increment only x). This logic is essential for both line and circle algorithms.

4. **Handle all octants**: Remember that line drawing algorithms typically handle lines with slope between 0 and 1. For other slopes, you may need to swap roles of x and y, or reflect the line.

5. **Symmetry in circles**: The Midpoint Circle Algorithm uses the eight-way symmetry of circles. This means you draw only one-eighth and mirror the results to get the complete circle.

6. **Polygon fill edge cases**: For scan-line fill, remember that horizontal edges are ignored, and special handling is needed for vertices where edges meet on the same side versus opposite sides of the scan line.

7. **Time complexity awareness**: Bresenham's algorithm has O(|Δx|) or O(|Δy|) complexity, while the basic scan-line polygon fill has O(n × y-range) complexity where n is the number of edges.

8. **Practical implementations**: Modern graphics systems use antialiasing techniques and hardware acceleration, but understanding these fundamental algorithms remains crucial for comprehension of graphics pipelines.