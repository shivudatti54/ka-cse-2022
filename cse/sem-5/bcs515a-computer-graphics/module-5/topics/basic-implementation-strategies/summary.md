# Quick Reference: Basic Implementation Strategies

## Core Concepts

- **Scan Line Algorithm**: Fills polygons scan line by scan line; uses edge intersection tables; good for solid fills
- **Z-Buffer Method**: Per-pixel depth testing; stores depth per pixel; handles intersecting polygons; industry standard for real-time rendering
- **Painter's Algorithm**: Sorts polygons back-to-front; paints far polygons first; simple but fails with polygon intersections
- **BSP Trees**: Recursively partitions space; enables fast visibility determination; popularized by DOOM (1993)

## Rendering Pipeline Stages

1. **Vertex Processing** → 2. **Primitive Assembly** → 3. **Rasterization** → 4. **Fragment Processing** → 5. **Per-Fragment Operations**

## Hardware vs Software Rendering

- **Software**: CPU-based; portable; slower; used in PDF viewers, boot screens
- **Hardware**: GPU-based; parallel processing; faster; used in games, CAD

## Rendering Modes

- **Immediate Mode**: Draws immediately; stateless; higher CPU overhead
- **Retained Mode**: Maintains scene graph; optimized; lower overhead; modern standard

## Display Lists

- Pre-compile GPU commands; store for repeated execution; reduce CPU-GPU bandwidth

## Key Formulas

- **Z-buffer depth test**: `if (z < z_buffer[x][y]) update pixel`
- **Plane equation**: `Ax + By + Cz + D = 0`
- **BSP traversal**: Front-to-back (painter's) or back-to-front (z-buffer)

## Must-Remember Points

- **Z-buffer is the dominant method** in modern graphics APIs (OpenGL, DirectX)
- **BSP trees provide O(log n) visibility queries** but require preprocessing
- **Modern APIs abandoned immediate mode** for VBOs and shader programs
- **Hardware rendering uses parallel processing** across thousands of GPU cores
- **Painter's algorithm fails** when polygons intersect or have cyclic depth