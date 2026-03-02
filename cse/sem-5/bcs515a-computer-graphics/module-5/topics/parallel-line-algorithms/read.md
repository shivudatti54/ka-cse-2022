# Parallel Line Algorithms

## Introduction

Parallel line algorithms are fundamental techniques in computer graphics used to draw straight lines between two points on a raster display. When we view any digital image on our screens, we see pixels arranged in a grid pattern. Drawing a perfect straight line connecting two points requires determining which pixels should be illuminated to approximate that line as closely as possible. This is where line drawing algorithms become essential.

The importance of efficient line drawing algorithms cannot be overstated in computer graphics applications. From simple drawing programs to complex CAD systems, from video games to medical imaging, lines form the backbone of visual representation. The quality and performance of these algorithms directly impact the visual fidelity and responsiveness of graphical applications. 's curriculum includes this topic to ensure students understand both the theoretical foundations and practical implementations of line drawing techniques.

This module covers three major parallel line algorithms: the Digital Differential Analyzer (DDA) algorithm, Bresenham's line algorithm, and the Midpoint line algorithm. Each approach has its own advantages and trade-offs in terms of computational efficiency, accuracy, and implementation complexity. Understanding these algorithms provides a strong foundation for more advanced topics in computer graphics like polygon filling, curve generation, and anti-aliasing techniques.

## Key Concepts

### Understanding the Problem

Before diving into specific algorithms, it's crucial to understand the fundamental problem we need to solve. Given two endpoints (x₁, y₁) and (x₂, y₂) on a raster grid, we must determine which grid positions (pixels) best represent the straight line connecting these points. The challenge arises because pixel positions are discrete integer coordinates, while the mathematical line passes through continuous real-valued positions.

The slope of the line plays a critical role in determining our approach. Lines can be categorized based on their slope: lines with slope between 0 and 1 (shallow lines), lines with slope greater than 1 (steep lines), and lines with negative slopes. Different algorithms handle these cases differently, and many implementations include special cases for vertical lines (undefined slope) and horizontal lines.

### DDA (Digital Differential Analyzer) Algorithm

The DDA algorithm is an incremental algorithm that uses the concept of sampling the line at regular intervals. The name "Digital Differential Analyzer" comes from its method of computing intermediate points by adding small increments. The algorithm works by calculating the slope of the line and then stepping through the major axis (the axis with the greater change) one pixel at a time.

The algorithm begins by calculating the differences in x and y coordinates: dx = x₂ - x₁ and dy = y₂ - y₁. The number of steps is determined by the maximum of the absolute values of dx and dy. If |dx| > |dy|, we step through x coordinates and compute corresponding y values; otherwise, we step through y coordinates and compute corresponding x values.

The step sizes are calculated as xStep = dx / steps and yStep = dy / steps. Starting from the initial point, we add these step values to get intermediate points, rounding each to the nearest integer to determine pixel positions. This process continues until we reach the endpoint.

One important characteristic of DDA is that it uses floating-point arithmetic throughout the computation, which can be computationally expensive on systems without hardware floating-point support. However, the algorithm is conceptually straightforward and easy to understand, making it an excellent starting point for learning line drawing techniques.

### Bresenham's Line Algorithm

Bresenham's line algorithm, developed by Jack Bresenham in 1962, is the most widely used line drawing algorithm in computer graphics. Its remarkable efficiency stems from its use of only integer arithmetic, making it extremely fast and suitable for implementation in hardware and embedded systems.

The algorithm works by making decisions at each step about which pixel is closer to the ideal line. It maintains an error term or decision parameter that indicates the cumulative displacement from the ideal line. At each step, we choose between two possible pixel positions based on this error term.

For lines with slope between 0 and 1, the algorithm proceeds as follows: we start at the initial point and calculate the initial decision parameter P = 2*dy - dx. At each x coordinate, if P < 0, we plot the pixel at (x+1, y) and update P = P + 2*dy; otherwise, we plot the pixel at (x+1, y+1) and update P = P + 2*dy - 2*dx. This process continues until we reach the endpoint.

The key insight behind Bresenham's algorithm is that it compares the vertical distances from the two candidate pixels to the ideal line, rather than computing actual distances. This comparison can be performed using only integer arithmetic, resulting in superior performance compared to algorithms requiring floating-point calculations.

### Midpoint Line Algorithm

The Midpoint line algorithm is another efficient integer arithmetic-based algorithm that uses the implicit equation of a line to make pixel selection decisions. It was developed as an improvement and alternative to Bresenham's algorithm, though both achieve similar performance.

The algorithm defines the line using the implicit equation F(x, y) = Ax + By + C = 0, where for a line from (x₁, y₁) to (x₂, y₂), we have A = y₁ - y₂, B = x₂ - x₁, and C = x₁y₂ - x₂y₁. This form allows us to determine on which side of the line any point lies by evaluating F(x, y).

At each step, we consider the midpoint between two candidate pixels. If the midpoint lies above the line, we choose the lower pixel; if it lies below, we choose the upper pixel. The decision is made by evaluating F at the midpoint: if F(midpoint) < 0, the midpoint is on one side; if F(midpoint) > 0, it's on the other side.

The initial decision parameter for the midpoint algorithm is d = A + 0.5\*B, where A and B are as defined above. The update formulas depend on the current value of d and differ slightly from Bresenham's approach, though the final result produces the same set of pixels.

### Handling Different Line Orientations

All three algorithms need to handle various line orientations beyond the basic case. This includes lines with negative slopes, lines where x₂ < x₁ (drawing from right to left), and lines where |dy| > |dx| (steep lines with slope > 1 or < -1).

The standard approach is to handle the basic case (0 ≤ slope ≤ 1 with x₂ > x₁) first, then apply transformations or swaps to handle other cases. Common techniques include swapping endpoints if necessary to ensure we always draw in a consistent direction, using absolute values to handle negative slopes, and interchanging the role of x and y for steep lines.

## Examples

### Example 1: DDA Algorithm

**Problem:** Draw a line from (2, 3) to (8, 7) using the DDA algorithm.

**Solution:**

Step 1: Calculate differences
dx = 8 - 2 = 6
dy = 7 - 3 = 4

Step 2: Determine number of steps
steps = max(|6|, |4|) = 6

Step 3: Calculate step sizes
xStep = 6/6 = 1
yStep = 4/6 = 0.667

Step 4: Generate points (starting from (2, 3))

| Step | x   | y (actual) | y (rounded) | Pixel |
| ---- | --- | ---------- | ----------- | ----- |
| 0    | 2   | 3.0        | 3           | (2,3) |
| 1    | 3   | 3.667      | 4           | (3,4) |
| 2    | 4   | 4.333      | 4           | (4,4) |
| 3    | 5   | 5.0        | 5           | (5,5) |
| 4    | 6   | 5.667      | 6           | (6,6) |
| 5    | 7   | 6.333      | 6           | (7,6) |
| 6    | 8   | 7.0        | 7           | (8,7) |

**Result:** The pixels to be illuminated are (2,3), (3,4), (4,4), (5,5), (6,6), (7,6), and (8,7).

### Example 2: Bresenham's Algorithm

**Problem:** Draw a line from (2, 3) to (8, 7) using Bresenham's algorithm.

**Solution:**

Step 1: Calculate differences
dx = 8 - 2 = 6
dy = 7 - 3 = 4

Step 2: Calculate initial decision parameter
P₀ = 2*dy - dx = 2*4 - 6 = 8 - 6 = 2

Step 3: Generate points (starting from (2, 3), plotting (2,3) first)

| k   | Pk  | xₖ  | yₖ  | Plot  | Pk+1                               |
| --- | --- | --- | --- | ----- | ---------------------------------- |
| 0   | 2   | 2   | 3   | (2,3) | P₀ + 2*dy - 2*dx = 2 + 8 - 12 = -2 |
| 1   | -2  | 3   | 4   | (3,4) | P₁ + 2\*dy = -2 + 8 = 6            |
| 2   | 6   | 4   | 4   | (4,4) | P₂ + 2*dy - 2*dx = 6 + 8 - 12 = 2  |
| 3   | 2   | 5   | 5   | (5,5) | P₃ + 2*dy - 2*dx = 2 + 8 - 12 = -2 |
| 4   | -2  | 6   | 6   | (6,6) | P₄ + 2\*dy = -2 + 8 = 6            |
| 5   | 6   | 7   | 6   | (7,6) | P₅ + 2*dy - 2*dx = 6 + 8 - 12 = 2  |
| 6   | 2   | 8   | 7   | (8,7) | —                                  |

**Result:** The same pixel positions as DDA: (2,3), (3,4), (4,4), (5,5), (6,6), (7,6), (8,7).

### Example 3: Handling a Steep Line

**Problem:** Draw a line from (1, 1) to (3, 7) using Bresenham's algorithm (slope > 1).

**Solution:**

Step 1: Since |dy| > |dx| (6 > 2), we step through y coordinates.

dx = 3 - 1 = 2
dy = 7 - 1 = 6

Step 2: Initial decision parameter
P₀ = 2*dx - dy = 2*2 - 6 = 4 - 6 = -2

Step 3: Generate points

| k   | Pk  | xₖ  | yₖ  | Plot  | Pk+1                               |
| --- | --- | --- | --- | ----- | ---------------------------------- |
| 0   | -2  | 1   | 1   | (1,1) | P₀ + 2\*dx = -2 + 4 = 2            |
| 1   | 2   | 2   | 2   | (2,2) | P₁ + 2*dx - 2*dy = 2 + 4 - 12 = -6 |
| 2   | -6  | 2   | 3   | (2,3) | P₂ + 2\*dx = -6 + 4 = -2           |
| 3   | -2  | 3   | 4   | (3,4) | P₃ + 2\*dx = -2 + 4 = 2            |
| 4   | 2   | 3   | 5   | (3,5) | P₄ + 2*dx - 2*dy = 2 + 4 - 12 = -6 |
| 5   | -6  | 3   | 6   | (3,6) | P₅ + 2\*dx = -6 + 4 = -2           |
| 6   | -2  | 3   | 7   | (3,7) | —                                  |

**Result:** Pixels: (1,1), (2,2), (2,3), (3,4), (3,5), (3,6), (3,7)

## Exam Tips

1. **Understand the core principle**: All line algorithms aim to minimize the error between the ideal mathematical line and the selected pixels. Know how each algorithm achieves this differently.

2. **Memorize the initial decision parameters**: For Bresenham, P₀ = 2\*dy - dx for shallow lines; for Midpoint, the initial d value is derived from the line equation coefficients.

3. **Handle special cases first**: Always check for horizontal lines (dy = 0) and vertical lines (dx = 0) before applying the general algorithm—these have trivial solutions.

4. **Know the comparison criteria**: In Bresenham's algorithm, if P < 0, choose the lower pixel; otherwise, choose the upper pixel. For Midpoint, the comparison is with zero.

5. **Understand the relationship between algorithms**: Bresenham and Midpoint produce identical results and have similar computational complexity, while DDA uses floating-point arithmetic.

6. **Practice coordinate transformations**: Be prepared to handle lines in all octants by swapping endpoints or interchanging x and y coordinates.

7. **Time complexity matters**: Bresenham and Midpoint are O(n) algorithms using only integer arithmetic, making them preferred for practical implementations.

8. **Remember the update formulas**: For Bresenham, if P < 0: P += 2*dy; else: P += 2*dy - 2\*dx. These are frequently asked in exams.
