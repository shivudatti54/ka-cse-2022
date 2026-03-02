# Z Buffer and List Priority Algorithms

## Introduction
In computer graphics, rendering 3D scenes requires determining the visible surfaces when objects overlap. Two primary approaches address this **visible surface determination** problem: **Z-Buffer Algorithm** (depth buffer) and **List Priority Algorithms**. These are essential topics in the Delhi University BSc (Hons) Computer Science syllabus under the Computer Graphics unit.

---

## Z-Buffer Algorithm

The Z-Buffer algorithm is a **frame-buffer** approach that resolves visibility at the **pixel level**.

- **Working Principle**: Each pixel stores both color and depth (z-value)
- **Comparison**: For each pixel, compare the new polygon's depth with the stored depth
- **Update**: If new z < stored z (closer to viewer), update color and depth buffers
- **Initialization**: All pixels start with maximum depth (background)
- **Advantage**: Handles complex intersecting geometry automatically
- **Disadvantage**: High memory requirement; no object-level processing

**Depth Calculation**: For a polygon plane equation `ax + by + cz + d = 0`, depth is computed using perspective transformation or linear interpolation across vertices.

---

## List Priority Algorithms

These algorithms resolve visibility at the **object/polygon level** before rendering.

### Painter's Algorithm (Painters Algorithm)
- **Concept**: Sort polygons by depth (far to near) and paint in that order
- **Sorting Criteria**: Usually by average z-coordinate or closest vertex
- **Limitation**: Cannot handle intersecting polygons correctly

### Newell's Algorithm
- **Improvement**: Sorts polygons by integrating depth and orientation
- **Sorting Key**: Uses `(z_min + z_max)/2` or performs iterative refinement
- **Advantage**: Better handling of nested surfaces

### Binary Space Partitioning (BSP) Trees
- **Concept**: Recursively divide space using splitting planes
- **Advantage**: Efficient for static scenes; view-independent sorting
- **Application**: Used in Quake engine and real-time rendering

### Scan-Line Algorithm with Depth Sorting
- Combines scan-line conversion with depth-based polygon sorting

---

## Comparison

| Aspect | Z-Buffer | List Priority |
|--------|----------|---------------|
| Memory | High (per pixel) | Lower (per polygon) |
| Complexity | O(n) per pixel | O(n log n) for sorting |
| Intersections | Handled automatically | Problematic |
| Hardware | Widely supported | Less common |

---

## Conclusion
The Z-Buffer algorithm is the **industry standard** due to its simplicity and hardware support in GPUs. List Priority algorithms, though historically significant, are now used mainly for optimization in specific scenarios or when hardware limitations exist. Understanding both approaches is crucial for the Delhi University exam, as questions frequently test knowledge of visible surface determination methods.

*Reference: Unit IV - 3D Graphics (Delhi University NEP 2024 UGCF BSc Computer Science Syllabus)*