# Circle Generation Algorithms

## Introduction
In computer graphics, generating smooth and accurate circles is a fundamental task, essential for rendering everything from simple buttons to complex planetary orbits. Unlike lines, circles are non-linear curves, requiring specialized algorithms for efficient pixel-by-pixel plotting. This module explores the mathematical foundation and the primary algorithms used for circle generation, focusing on the **Mid-Point Circle Drawing Algorithm**, an extension of Bresenham's approach for lines.

## The Mathematical Foundation: Circle Equation
A circle is defined as the set of all points that are equidistant (the radius, **r**) from a central point (**x<sub>c</sub>, y<sub>c</sub>**). The standard equation is:

**(x - x<sub>c</sub>)² + (y - y<sub>c</sub>)² = r²**

For simplicity, algorithms often assume the circle is centered at the origin (0,0). The equation then simplifies to:

**x² + y² = r²**

The challenge is to find integer coordinates (x, y) that best satisfy this equation for a given integer radius **r**.

## The Symmetry of a Circle
A key insight that drives efficiency in circle-drawing algorithms is the **eight-way symmetry** of a circle. If a point **(x, y)** is on the circle, then seven other points are also on the circle due to symmetry.
```
        (-y, x) | (y, x)
                 |
    (-x, y)_____|_____(x, y)
                 |
        (-x, -y)| (x, -y)
                 |
        (-y, -x) | (y, -x)
```
This means we only need to calculate the points for one **octant** (a 45-degree segment) of the circle and can simply plot the other seven symmetric points. Most algorithms calculate points for the second octant (from x=0 to x=y) and then use symmetry.

## Mid-Point Circle Drawing Algorithm
This is the most common algorithm for circle generation. It is efficient, uses only integer arithmetic, and is a classic example of a *decision parameter* based algorithm.

### 1. Algorithm Concept
The algorithm starts at point **(0, r)**. For each step, it decides whether the next pixel should be chosen to the **East (E)** or **South-East (SE)** relative to the current pixel. This decision is made based on a **decision parameter (d)**, which is calculated using the circle equation at the midpoint between the two candidate pixels.

### 2. Decision Parameter Derivation
Let's assume we are at point **(x<sub>k</sub>, y<sub>k</sub>)**. The next midpoint to evaluate is between the E and SE pixels.
```
Current Pixel: (xₖ, yₖ)
Candidate Pixels: E = (xₖ+1, yₖ), SE = (xₖ+1, yₖ-1)
Midpoint: M = (xₖ+1, yₖ - 0.5)
```
We define our decision parameter **d** at this midpoint:
**d = f(M) = (xₖ + 1)² + (yₖ - 0.5)² - r²**

*   If **d < 0**, the midpoint is **inside** the circle. We choose pixel E.
*   If **d >= 0**, the midpoint is **on or outside** the circle. We choose pixel SE.

### 3. Iterative Calculation
To avoid floating-point arithmetic, we use an iterative approach to update the decision parameter.

**a) Case 1: If d < 0 (Choose E)**
The next midpoint will be at **(x<sub>k</sub>+2, y<sub>k</sub> - 0.5)**.
The change in the decision parameter, ∆d<sub>E</sub>, is:
**∆d<sub>E</sub> = d<sub>new</sub> - d<sub>old</sub> = [(xₖ+2)² + (yₖ-0.5)² - r²] - [(xₖ+1)² + (yₖ-0.5)² - r²] = (2xₖ + 3)**

**b) Case 2: If d >= 0 (Choose SE)**
The next midpoint will be at **(x<sub>k</sub>+2, y<sub>k</sub> - 1.5)**.
The change in the decision parameter, ∆d<sub>SE</sub>, is:
**∆d<sub>SE</sub> = [(xₖ+2)² + (yₖ-1.5)² - r²] - [(xₖ+1)² + (yₖ-0.5)² - r²] = (2xₖ - 2yₖ + 5)**

### 4. Initial Decision Parameter
At the start point **(0, r)**, the first midpoint is at **(1, r - 0.5)**.
**d<sub>0</sub> = f(1, r - 0.5) = 1² + (r - 0.5)² - r² = 1 + (r² - r + 0.25) - r² = 1.25 - r**

To eliminate the fraction, we can multiply the entire equation by 4. This doesn't change the sign of d and keeps everything integer.
**d<sub>0</sub> = 5 - 4r**  (Since 4 * 1.25 = 5)

### 5. Algorithm Steps (Pseudocode)
1.  Initialize `x = 0`, `y = r`, `d = 5 - 4*r` (or `3 - 2*r` for a common variation).
2.  Plot the symmetric points for (x, y).
3.  While `x < y`:
    a. If `d < 0`:
        `d = d + 4*x + 6`  (Equivalent to 2*(2x + 3))
        `x = x + 1`
    b. Else (`d >= 0`):
        `d = d + 4*(x - y) + 10` (Equivalent to 2*(2x - 2y + 5))
        `x = x + 1`
        `y = y - 1`
    c. Plot the symmetric points for the new (x, y).

## Comparison of Circle Algorithms
| Algorithm | Principle | Advantages | Disadvantages |
| :--- | :--- | :--- | :--- |
| **Direct (Polynomial)** | Calculates y = ±√(r² - x²) for each x | Simple to understand | Slow, uses floating-point, gaps near x=0 |
| **Polar Coordinates** | Uses x = r·cosθ, y = r·sinθ | Accurate, smooth circle | Very slow due to trig calculations |
| **Mid-Point (Bresenham)** | Decision parameter based on midpoint | Fast, integer only, accurate | Slightly more complex logic |

## Example: Drawing a Circle with r=5
Let's trace the Mid-Point algorithm for `r=5`. We use `d0 = 3 - 2*r = 3 - 10 = -7`.
| Step | x | y | d (Decision) | Chosen Pixel | New d Calculation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 5 | -7 (d < 0) | E | d = -7 + 4*0 + 6 = -1 |
| 1 | 1 | 5 | -1 (d < 0) | E | d = -1 + 4*1 + 6 = 9 |
| 2 | 2 | 5 | 9 (d >= 0) | SE | d = 9 + 4*(2-5) + 10 = 9 -12 +10 = 7 |
| 3 | 3 | 4 | 7 (d >= 0) | SE | d = 7 + 4*(3-4) + 10 = 7 -4 +10 = 13 |
| 4 | 4 | 3 | 13 (d >= 0) | SE | d = 13 + 4*(4-3) + 10 = 13+4+10=27 |
| 5 | 5 | 2 | (Stop, x > y) | - | - |

The points calculated for the octant are: (0,5), (1,5), (2,5), (3,4), (4,3), (5,2). The algorithm stops when x >= y.

## Exam Tips
1.  **Memorize the Symmetry:** Always remember you only need to calculate one octant. Forgetting to plot all 8 points is a common mistake.
2.  **Understand `d0`:** Be prepared to derive or explain the initial decision parameter (`5-4r` or `3-2r`). Know that both are valid; `3-2r` is more common in code.
3.  **Integer Arithmetic is Key:** The exam will likely focus on the integer-based Mid-Point algorithm, not the slow trigonometric or polynomial methods.
4.  **Trace an Example:** Be ready to trace the algorithm step-by-step for a small radius (e.g., r=3 or r=4). Draw a small grid and plot the points to visualize the process.
5.  **Comparison:** Be able to write a short comparison between the Mid-Point algorithm and a naive approach, highlighting the advantages of integer calculation and efficiency.