# Polygon Filling Algorithms

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Polygon Filling** is a fundamental operation in computer graphics that involves coloring the interior region of a polygon. When we draw a polygon using line segments (edges), the interior remains empty. Polygon filling algorithms determine which pixels inside the polygon boundary should be colored to create solid shapes.

In the context of the **DSE-CG (Discipline Specific Elective - Computer Graphics)** syllabus for Delhi University's NEP 2024 UGCF curriculum, polygon filling is essential for rendering solid objects, creating filled shapes, and producing realistic visualizations. This topic builds upon earlier concepts of raster graphics, line drawing algorithms (DDA, Bresenham), and clipping algorithms.

---

## 2. Real-World Relevance and Applications

Polygon filling algorithms are ubiquitous in modern computer graphics and have numerous practical applications:

- **Computer-Aided Design (CAD)**: Rendering solid components, architectural plans, and mechanical drawings
- **Game Development**: Creating game characters, terrain, and UI elements
- **Geographic Information Systems (GIS)**: Displaying filled regions on maps
- **Medical Imaging**: Visualizing organ segments and anatomical structures
- **User Interfaces**: Button backgrounds, window fills, and icon rendering
- **Image Processing**: Region identification and segmentation
- **Animation**: Frame-by-frame rendering of filled shapes

Understanding these algorithms is crucial for graphics programmers, game developers, and anyone working with 2D/3D visualization software.

---

## 3. Classification of Polygon Filling Algorithms

Polygon filling algorithms can be broadly classified into two categories:

1. **Seed-Based (Area-Filling) Algorithms**
   - Boundary Fill Algorithm
   - Flood Fill Algorithm

2. **Scan-Line (Order-Based) Algorithms**
   - Scan-Line Polygon Fill Algorithm
   - Edge Table Method

---

## 4. Seed Fill Algorithms

Seed fill algorithms are recursive or iterative approaches that start from a **seed point** (a known interior point) and fill outward until reaching the boundary. These algorithms are particularly useful for filling irregular shapes and regions with holes.

### 4.1 Boundary Fill Algorithm

The **Boundary Fill Algorithm** fills a region by starting from a seed pixel and spreading to adjacent pixels that:
- Are not the boundary color
- Have not been filled yet

#### 4-Connected vs 8-Connected Filling

**4-Connected (N,S,E,W)**:
- Checks only 4 neighboring pixels (North, South, East, West)
- Cannot fill diagonally
- May leave gaps in diagonal boundaries
- Faster but less comprehensive

**8-Connected (N,S,E,W,NE,NW,SE,SW)**:
- Checks all 8 neighboring pixels
- Fills complete regions including diagonal connections
- More thorough but slightly slower
- Recommended for complex shapes

#### Algorithm Steps (4-Connected)

```
1. Initialize stack with seed point (x, y)
2. While stack is not empty:
   a. Pop a pixel (x, y) from stack
   b. If pixel is not boundary color and not filled:
      - Color the pixel
      - Push (x+1, y), (x-1, y), (x, y+1), (x, y-1) onto stack
3. Return
```

#### C Implementation of Boundary Fill (4-Connected)

```c
#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>

// 4-connected boundary fill algorithm
void boundaryFill4(int x, int y, int fillColor, int boundaryColor) {
    // Get current pixel color
    int currentColor = getpixel(x, y);
    
    // If current pixel is not boundary and not already filled
    if (currentColor != boundaryColor && currentColor != fillColor) {
        // Fill the current pixel
        putpixel(x, y, fillColor);
        
        // Recursively fill 4-connected neighbors
        boundaryFill4(x + 1, y, fillColor, boundaryColor);
        boundaryFill4(x - 1, y, fillColor, boundaryColor);
        boundaryFill4(x, y + 1, fillColor, boundaryColor);
        boundaryFill4(x, y - 1, fillColor, boundaryColor);
    }
}

// Iterative version to avoid stack overflow for large regions
void boundaryFill4Iterative(int x, int y, int fillColor, int boundaryColor) {
    struct Point {
        int x, y;
    };
    
    struct Point stack[10000];
    int top = -1;
    
    // Push seed point
    stack[++top] = {x, y};
    
    while (top >= 0) {
        struct Point p = stack[top--];
        int currentColor = getpixel(p.x, p.y);
        
        if (currentColor != boundaryColor && currentColor != fillColor) {
            putpixel(p.x, p.y, fillColor);
            
            // Push 4-connected neighbors
            stack[++top] = {p.x + 1, p.y};
            stack[++top] = {p.x - 1, p.y};
            stack[++top] = {p.x, p.y + 1};
            stack[++top] = {p.x, p.y - 1};
        }
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    
    // Draw a polygon (rectangle as boundary)
    rectangle(100, 100, 300, 200);
    
    // Fill with red color using seed point (150, 150)
    boundaryFill4Iterative(150, 150, RED, WHITE);
    
    getch();
    closegraph();
    return 0;
}
```

### 4.2 Flood Fill Algorithm

The **Flood Fill Algorithm** fills a region by replacing a specified **old color** (original color) with a **new color**. Unlike boundary fill, flood fill doesn't require a boundary—it fills all connected pixels of the same original color.

#### Key Differences: Boundary Fill vs Flood Fill

| Aspect | Boundary Fill | Flood Fill |
|--------|--------------|------------|
| Stop Condition | Reaches boundary color | Reaches different color |
| Required Info | Boundary color, fill color | Old color, new color |
| Use Case | Pre-defined boundaries | Color replacement |
| Flexibility | Requires boundary | Works on any region |

#### Algorithm Steps

```
1. Get the color of seed point (oldColor)
2. If oldColor equals newColor, return
3. Initialize stack with seed point
4. While stack is not empty:
   a. Pop pixel (x, y)
   b. If getpixel(x, y) == oldColor:
      - Color pixel with newColor
      - Push all 4 or 8 neighbors
5. Return
```

#### C Implementation of Flood Fill

```c
#include <graphics.h>

void floodFill(int x, int y, int newColor) {
    int oldColor = getpixel(x, y);
    
    // Don't fill if colors are same
    if (oldColor == newColor) return;
    
    struct Point {
        int x, y;
    };
    
    struct Point stack[10000];
    int top = -1;
    
    stack[++top] = {x, y};
    
    while (top >= 0) {
        struct Point p = stack[top--];
        int currentColor = getpixel(p.x, p.y);
        
        if (currentColor == oldColor) {
            putpixel(p.x, p.y, newColor);
            
            // 4-connected neighbors
            stack[++top] = {p.x + 1, p.y};
            stack[++top] = {p.x - 1, p.y};
            stack[++top] = {p.x, p.y + 1};
            stack[++top] = {p.x, p.y - 1};
        }
    }
}
```

### 4.3 Handling Complex Regions

#### Self-Intersecting Polygons

Self-intersecting polygons (also called complex polygons or bowtie shapes) have edges that cross each other. The filling behavior depends on the **fill rule**:

**Even-Odd Rule**: Draw a ray from the point to infinity. If it crosses the polygon boundary an odd number of times, the point is inside; if even, it's outside.

**Winding Number Rule**: Count how many times the polygon winds around the point. A point is inside if the winding number is non-zero.

#### Polygons with Holes

When filling polygons with holes:
1. Identify the outer boundary
2. Identify inner boundaries (holes)
3. Fill the outer region
4. Leave hole regions unfilled (or fill with different color)
5. Alternatively, use even-odd rule which automatically handles holes

---

## 5. Winding Number Rule

The **Winding Number Rule** is a method for determining whether a point lies inside a polygon. It counts the total number of times the polygon edges wrap around the point.

### 5.1 How Winding Number Works

For each edge of the polygon:
1. Determine if the edge crosses a ray extending from the point to infinity
2. If the edge crosses from below to above (relative to the point), add 1
3. If the edge crosses from above to below, subtract 1
4. The final count is the winding number

### 5.2 Algorithm Implementation

```c
// Calculate winding number for a point
int windingNumber(Point p, Polygon poly) {
    int wn = 0;
    int n = poly.numVertices;
    
    for (int i = 0; i < n; i++) {
        Point current = poly.vertices[i];
        Point next = poly.vertices[(i + 1) % n];
        
        // Check if edge crosses the horizontal ray from point
        if (current.y <= p.y) {
            if (next.y > p.y) {
                // Edge is crossing upward
                if (isLeft(current, next, p) > 0) {
                    wn++;
                }
            }
        } else {
            if (next.y <= p.y) {
                // Edge is crossing downward
                if (isLeft(current, next, p) < 0) {
                    wn--;
                }
            }
        }
    }
    
    return wn;
}

// Helper function: tests if point p is left of line v-w
double isLeft(Point v, Point w, Point p) {
    return (w.x - v.x) * (p.y - v.y) - (w.x - p.x) * (w.y - v.y);
}

// Point is inside if winding number is non-zero
bool isInsideWinding(Point p, Polygon poly) {
    return windingNumber(p, poly) != 0;
}
```

### 5.3 Winding Number vs Even-Odd Rule

| Aspect | Winding Number | Even-Odd Rule |
|--------|----------------|---------------|
| Complexity | More complex | Simpler |
| Fill Result | Fills all non-zero regions | Alternates fills |
| Self-intersecting | Correct handling | May produce issues |
| Concave Polygons | Correct | Correct |
| Holes | Handles naturally | Requires special handling |

**Example**: For a star-shaped self-intersecting polygon:
- **Even-Odd Rule**: Alternates between filled and unfilled regions
- **Winding Number Rule**: Fills the entire star (winding number is always non-zero for points inside)

---

## 6. Scan-Line Polygon Fill Algorithm

The Scan-Line algorithm is the most efficient method for filling convex or concave polygons. It processes the polygon **scan line by scan line** (row by row), calculating x-intersections for each scan line.

### 6.1 Algorithm Steps

```
1. Find the minimum and maximum y-coordinates (y_min, y_max) of the polygon
2. For each scan line y from y_min to y_max:
   a. Find all intersections of the scan line with polygon edges
   b. Sort intersections by x-coordinate
   c. Fill pixels between pairs of intersections (1st-2nd, 3rd-4th, etc.)
```

### 6.2 Handling Special Cases

- **Horizontal Edges**: Ignore (don't contribute to intersections)
- **Vertices**: Count each vertex only once
- **Scan Line Passing Through Vertex**: Handle carefully to avoid double-counting

### 6.3 Implementation with Edge Table

```c
struct Edge {
    int y_max;           // Maximum y-coordinate
    float x_min;         // Minimum x-coordinate (at y_min)
    float inverseSlope;  // 1/m
    struct Edge *next;
};

// Scan-line algorithm implementation
void scanLineFill(Polygon poly, int fillColor) {
    // Create edge table
    EdgeTable edgeTable[MAX_Y];
    initializeTable(edgeTable);
    
    // Fill edge table with polygon edges
    int n = poly.numVertices;
    for (int i = 0; i < n; i++) {
        Point p1 = poly.vertices[i];
        Point p2 = poly.vertices[(i + 1) % n];
        
        if (p1.y != p2.y) {  // Skip horizontal edges
            int y_min = (p1.y < p2.y) ? p1.y : p2.y;
            int y_max = (p1.y > p2.y) ? p1.y : p2.y;
            float x_min = (p1.y < p2.y) ? p1.x : p2.x;
            float slope = (float)(p2.x - p1.x) / (p2.y - p1.y);
            
            addEdgeToTable(edgeTable[y_min], y_max, x_min, 1.0/slope);
        }
    }
    
    // Process each scan line
    for (int y = 0; y < MAX_Y; y++) {
        // Get active edges for this scan line
        ActiveEdgeList ael = edgeTable[y];
        
        // Sort by x_min
        sortEdgesByX(ael);
        
        // Fill between pairs
        Edge *ptr = ael;
        while (ptr && ptr->next) {
            // Fill from ptr->x_min to ptr->next->x_min
            for (int x = (int)ptr->x_min; x < (int)ptr->next->x_min; x++) {
                putpixel(x, y, fillColor);
            }
            ptr = ptr->next->next;
        }
    }
}
```

---

## 7. Algorithm Comparison

### 7.1 Performance Analysis

| Algorithm | Time Complexity | Space Complexity | Best For |
|-----------|-----------------|------------------|----------|
| Boundary Fill | O(n) | O(n) stack | Small irregular regions |
| Flood Fill | O(n) | O(n) stack | Color replacement |
| Scan-Line | O(n × m) | O(e) | Large convex/concave polygons |

*Where n = number of pixels, m = scan lines, e = number of edges*

### 7.2 When to Use Which Algorithm

**Use Boundary Fill when:**
- You have a well-defined boundary
- Filling small to medium-sized regions
- Working with shapes drawn with specific boundary colors

**Use Flood Fill when:**
- Replacing one color with another
- Working with regions without explicit boundaries
- Paint bucket operations in image editors

**Use Scan-Line when:**
- Filling large polygons
- Real-time rendering requirements
- Convex or concave polygons
- When you need precise control over fill order

---

## 8. Multiple Choice Questions

### MCQ 1: What is the primary difference between boundary fill and flood fill algorithms?

A) Boundary fill uses recursion while flood fill uses iteration  
B) Boundary fill requires a boundary color while flood fill requires the old color to be replaced  
C) Boundary fill is faster than flood fill  
D) There is no significant difference between them  

**Answer: B**

---

### MCQ 2: In a 4-connected boundary fill algorithm, how many neighboring pixels are checked for each pixel?

A) 4  
B) 8  
C) 16  
D) 2  

**Answer: A**

---

### MCQ 3: Which algorithm is most efficient for filling large convex polygons with many vertices?

A) Boundary Fill  
B) Flood Fill  
C) Scan-Line Fill  
D) All are equally efficient  

**Answer: C**

---

### MCQ 4: The winding number rule for point-in-polygon test:

A) Counts edges crossed by a ray from the point  
B) Counts how many times the polygon winds around the point  
C) Uses only horizontal scan lines  
D) Works only for convex polygons  

**Answer: B**

---

### MCQ 5: In scan-line polygon filling, intersections are paired and filled:

A) Randomly  
B) From left to right  
C) From top to bottom  
D) Based on color  

**Answer: B**

---

## 9. Flashcards

### Flashcard 1

**Q: What is a seed point in polygon filling algorithms?**

A: A seed point is an interior pixel that serves as the starting point for filling. The algorithm begins at this point and spreads outward to fill the entire region.

---

### Flashcard 2

**Q: Why is 8-connected filling more comprehensive than 4-connected filling?**

A: 8-connected filling checks all 8 neighboring pixels (including diagonals), ensuring no gaps are left when filling complex shapes with diagonal boundaries. However, it may accidentally fill through narrow diagonal connections.

---

### Flashcard 3

**Q: How does the scan-line algorithm handle concave polygons?**

A: The scan-line algorithm handles concave polygons by finding all edge intersections for each scan line and pairing them from left to right. Multiple intersection pairs on a single scan line correctly handle the concave portions.

---

### Flashcard 4

**Q: What is the main advantage of the winding number rule over the even-odd rule?**

A: The winding number rule correctly handles self-intersecting polygons and polygons with holes, producing more intuitive fill results. It counts the total "winding" of edges around a point.

---

### Flashcard 5

**Q: Why are horizontal edges ignored in scan-line polygon filling?**

A: Horizontal edges would cause vertices to be counted twice (once for each endpoint), leading to incorrect intersection pairs. Ignoring them ensures proper pairing of intersections.

---

## 10. Key Takeaways

1. **Polygon filling** is essential for rendering solid shapes in computer graphics and forms the foundation for more advanced rendering techniques.

2. **Seed-based algorithms** (Boundary Fill and Flood Fill) start from an interior point and fill outward, useful for irregular shapes but can be slow for large regions.

3. **4-connected** filling checks only N,S,E,W neighbors; **8-connected** checks all 8 neighbors, providing more complete filling at the cost of potential "leakage."

4. **Boundary Fill** requires a defined boundary color, while **Flood Fill** replaces a specified old color throughout a region.

5. **Scan-Line Algorithm** is the most efficient for large polygons, processing one scan line at a time and filling between paired x-intersections.

6. **Winding Number Rule** provides accurate point-in-polygon testing for self-intersecting polygons and holes, while the **Even-Odd Rule** is simpler but may produce unexpected results.

7. **Algorithm selection** depends on polygon size, shape complexity, and real-time requirements.

8. Understanding these algorithms is crucial for graphics programming, CAD applications, game development, and image processing—all relevant for the DSE-CG syllabus and future careers in computer graphics.

---

*Study material prepared in accordance with Delhi University NEP 2024 UGCF syllabus for DSE-CG (Computer Graphics).*