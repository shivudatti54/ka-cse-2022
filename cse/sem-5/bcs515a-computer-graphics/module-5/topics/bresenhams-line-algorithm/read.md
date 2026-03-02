# Bresenham's Line Algorithm

## Introduction

Bresenham's Line Algorithm is one of the most fundamental and efficient algorithms in computer graphics for drawing straight lines between two points on a raster display. Developed by Jack Bresenham in 1962, this algorithm has become a cornerstone of computer graphics rendering and is extensively used in various applications including CAD software, games, and graphical user interfaces.

The primary challenge in raster graphics is that display devices consist of discrete pixels arranged in a grid, while mathematical lines are continuous. When drawing a line from one pixel to another, we must determine which pixels should be illuminated to best approximate the ideal mathematical line. Bresenham's algorithm solves this problem by using only integer arithmetic and incremental calculations, making it significantly faster than other approaches like the Digital Differential Analyzer (DDA) algorithm. This efficiency stems from the algorithm's ability to avoid expensive floating-point operations, instead relying on simple integer additions, subtractions, and bit shifts.

The algorithm works by calculating the decision parameter at each step to determine whether the next pixel should be placed at position (x+1, y+1) or (x+1, y). This decision is made by comparing the distance between the two possible pixel positions and the actual line, ensuring that the drawn line appears as smooth and accurate as possible. Bresenham's algorithm produces results identical to the direct line equation while being computationally more efficient, which is why it remains the preferred choice for line drawing in hardware implementations and software rendering pipelines.

## Key Concepts

### Basic Principle

Bresenham's algorithm operates on the principle of incremental error calculation. Instead of calculating the exact distance from the line to each candidate pixel, it uses a decision parameter that keeps track of the accumulated error. The algorithm assumes that lines are drawn from point P₀(x₀, y₀) to P₁(x₁, y₁), where x₁ > x₀. The algorithm primarily works in the first octant (slope between 0 and 1), though it can be extended to handle all octants.

The fundamental idea is to start at the starting pixel and then, for each subsequent x-coordinate, choose between two y-positions (y or y+1) based on which one is closer to the true line. To make this determination efficiently, we maintain a decision parameter that tells us whether the error is positive or negative. When the error becomes too large, we increment y; otherwise, we keep y the same.

### The Decision Parameter

For a line with slope m = Δy/Δx, where Δx = x₁ - x₀ and Δy = y₁ - y₀, the algorithm defines an initial decision parameter P₀. For lines in the first octant where Δx > Δy (shallow lines), the parameter is calculated as:

**P₀ = 2Δy - Δx**

At each step k, if Pk < 0, the line is closer to the lower pixel, so we choose yₖ₊₁ = yₖ and calculate:
**Pk₊₁ = Pk + 2Δy**

If Pk ≥ 0, the line is closer to the upper pixel, so we choose yₖ₊₁ = yₖ + 1 and calculate:
**Pk₊₁ = Pk + 2Δy - 2Δx**

This recurrence relation allows us to compute all subsequent decision parameters using only integer additions and subtractions, which is the key to the algorithm's efficiency.

### Algorithm Steps

The complete Bresenham's line drawing algorithm for the first octant follows these steps:

1. **Input**: Receive the starting coordinates (x₀, y₀) and ending coordinates (x₁, y₁).

2. **Calculate differences**: Compute Δx = x₁ - x₀ and Δy = y₁ - y₀.

3. **Initialize variables**: Set the starting pixel at (x₀, y₀) and calculate the initial decision parameter P₀ = 2Δy - Δx.

4. **Plot starting pixel**: Illuminate the pixel at position (x₀, y₀).

5. **Iterate through x-coordinates**: For each pixel position xₖ from x₀ to x₁ - 1:

- If Pk < 0, plot the pixel at (xₖ₊₁, yₖ) and set Pk₊₁ = Pk + 2Δy
- Otherwise, plot the pixel at (xₖ₊₁, yₖ₊₁) and set Pk₊₁ = Pk + 2Δy - 2Δx

6. **Continue until endpoint**: Repeat step 5 until reaching the endpoint at x₁.

### Handling Different Octants

The basic algorithm works for lines in the first octant (0 ≤ slope ≤ 1). To draw lines in all octants, we need to consider symmetry and handle different cases:

For lines where Δx > Δy (shallow lines), the algorithm proceeds as described above. For lines where Δy > Δx (steep lines), we can either swap the roles of x and y, or modify the algorithm to iterate along the y-axis instead. Additionally, the algorithm must handle lines with negative slopes by working from the endpoint with the smaller x-value to the larger one. For completely general lines, we may need to reflect pixels across the axes to ensure the algorithm processes the line in the correct direction.

### Comparison with DDA Algorithm

The Digital Differential Analyzer (DDA) algorithm is another commonly taught line drawing algorithm. While DDA uses floating-point arithmetic and rounds coordinates to the nearest integers, Bresenham's algorithm uses only integer operations. This makes Bresenham's algorithm significantly faster in practice, as integer operations are quicker than floating-point operations on most hardware. Additionally, Bresenham's algorithm produces more accurate results because it minimizes the error between the actual line and the drawn pixels, rather than simply rounding calculated positions.

## Examples

### Example 1: Drawing a Line from (2, 2) to (8, 5)

Let us trace through Bresenham's algorithm for drawing a line from P₀(2, 2) to P₁(8, 5).

**Step 1: Calculate differences**
Δx = 8 - 2 = 6
Δy = 5 - 2 = 3
Slope m = 3/6 = 0.5 (first octant, shallow line)

**Step 2: Initialize decision parameter**
P₀ = 2Δy - Δx = 2(3) - 6 = 6 - 6 = 0

**Step 3: Plot and iterate**

| Step | xₖ  | yₖ  | Pk  | Decision | Next Pixel | Pk₊₁            |
| ---- | --- | --- | --- | -------- | ---------- | --------------- |
| 0    | 2   | 2   | 0   | P₀ ≥ 0   | (3, 3)     | 0 + 6 - 12 = -6 |
| 1    | 3   | 3   | -6  | P₁ < 0   | (4, 3)     | -6 + 6 = 0      |
| 2    | 4   | 3   | 0   | P₂ ≥ 0   | (5, 4)     | 0 + 6 - 12 = -6 |
| 3    | 5   | 4   | -6  | P₃ < 0   | (6, 4)     | -6 + 6 = 0      |
| 4    | 6   | 4   | 0   | P₄ ≥ 0   | (7, 5)     | 0 + 6 - 12 = -6 |
| 5    | 7   | 5   | -6  | P₅ < 0   | (8, 5)     | -6 + 6 = 0      |

**Pixels plotted**: (2,2), (3,3), (4,3), (5,4), (6,4), (7,5), (8,5)

### Example 2: Drawing a Line from (0, 0) to (5, 2)

Let us draw a line from P₀(0, 0) to P₁(5, 2).

**Step 1: Calculate differences**
Δx = 5 - 0 = 5
Δy = 2 - 0 = 2
Slope m = 2/5 = 0.4

**Step 2: Initialize decision parameter**
P₀ = 2Δy - Δx = 2(2) - 5 = 4 - 5 = -1

**Step 3: Plot and iterate**

| Step | xₖ  | yₖ  | Pk  | Decision | Next Pixel | Pk₊₁            |
| ---- | --- | --- | --- | -------- | ---------- | --------------- |
| 0    | 0   | 0   | -1  | P₀ < 0   | (1, 0)     | -1 + 4 = 3      |
| 1    | 1   | 0   | 3   | P₁ ≥ 0   | (2, 1)     | 3 + 4 - 10 = -3 |
| 2    | 2   | 1   | -3  | P₂ < 0   | (3, 1)     | -3 + 4 = 1      |
| 3    | 3   | 1   | 1   | P₃ ≥ 0   | (4, 2)     | 1 + 4 - 10 = -5 |
| 4    | 4   | 2   | -5  | P₄ < 0   | (5, 2)     | -5 + 4 = -1     |

**Pixels plotted**: (0,0), (1,0), (2,1), (3,1), (4,2), (5,2)

### Example 3: Handling Negative Slope (Reflection)

To draw a line from (0, 5) to (5, 2), we can think of this as drawing from (0, 0) to (5, 3) with the y-coordinates reflected. The actual pixels will be (0,5), (1,5), (2,4), (3,4), (4,3), (5,3).

For lines with negative slope, we can transform the coordinates by taking the absolute values and then reflecting the y-coordinates at the end. Alternatively, we can modify the algorithm to handle negative slopes directly by changing the update rules accordingly.

## Exam Tips

1. **Remember the initial decision parameter formula**: P₀ = 2Δy - Δx. This is the most frequently tested concept in exams.

2. **Understand when to increment y**: If Pk < 0, choose the lower pixel (yₖ₊₁ = yₖ); if Pk ≥ 0, choose the upper pixel (yₖ₊₁ = yₖ + 1).

3. **Memorize the update formulas**:

- When Pk < 0: Pk₊₁ = Pk + 2Δy
- When Pk ≥ 0: Pk₊₁ = Pk + 2Δy - 2Δx

4. **Know the difference between shallow and steep lines**: For lines where |Δx| > |Δy|, iterate along the x-axis; otherwise, iterate along the y-axis.

5. **Algorithm works only in first octant**: Remember that the basic algorithm is designed for 0 ≤ slope ≤ 1; you need modifications for other octants.

6. **Integer arithmetic advantage**: Bresenham's algorithm uses only integer operations, making it faster than DDA which uses floating-point calculations.

7. **Be prepared to trace the algorithm**: Most exam questions will ask you to trace through the algorithm step by step, showing the decision parameter at each iteration.

8. **Understand the error interpretation**: The decision parameter Pk represents twice the signed distance between the line and the closer pixel, which is why the algorithm chooses the pixel that minimizes this error.

9. **Endpoint plotting**: Don't forget to plot both the starting point and the ending point pixels.

10. **Comparison questions**: Be prepared to compare Bresenham's algorithm with DDA, focusing on efficiency, accuracy, and type of arithmetic used.
