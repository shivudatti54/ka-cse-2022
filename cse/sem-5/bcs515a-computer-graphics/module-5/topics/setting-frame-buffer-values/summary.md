# Setting Frame Buffer Values - Summary

## Key Definitions and Concepts

- **Frame Buffer**: A dedicated video memory array that stores pixel values representing the complete image to be displayed on screen
- **Pixel**: The smallest unit of the display, each containing color information stored in the frame buffer
- **Scan Conversion**: The process of converting geometric primitives (lines, circles, polygons) into pixel values in the frame buffer
- **Color Depth**: The number of bits used to represent each pixel's color, determining the total number of possible colors
- **RGB Color Model**: Additive color model using Red, Green, and Blue components to represent colors
- **Alpha Channel**: Additional 8-bit value storing transparency information for each pixel

## Important Formulas and Theorems

- **Memory Offset**: offset = y × width + x (for pixel at screen coordinates x, y)
- **RGB Packing**: packed_pixel = (alpha << 24) | (red << 16) | (green << 8) | blue
- **DDA Line Algorithm**: x(k+1) = x(k) + dx/steps, y(k+1) = y(k) + dy/steps
- **Bresenham Decision Parameter**: p(k+1) = p(k) + 2×dy if p(k) < 0, else p(k) + 2×dy - 2×dx
- **Grayscale Intensity**: I = 0.299×R + 0.587×G + 0.114×B
- **Circle Midpoint Decision**: p = x² + y² - radius² (updated incrementally)

## Key Points

- Frame buffers are organized as 2D arrays mapping directly to screen resolution
- Screen coordinates have origin at top-left with y increasing downward
- Bresenham's algorithm uses only integer arithmetic, making it faster than DDA
- Midpoint circle algorithm exploits 8-way symmetry to reduce computation to one octant
- Anti-aliasing reduces jagged edges by modulating pixel intensities based on distance from ideal primitive
- Color packing into single integers enables efficient memory operations
- Alpha compositing determines how new pixels blend with existing frame buffer content

## Common Mistakes to Avoid

- Confusing screen coordinates (y downward) with mathematical Cartesian coordinates (y upward)
- Forgetting to multiply by bytes-per-pixel when calculating actual memory addresses
- Using floating-point operations in Bresenham's algorithm when only integer operations are needed
- Neglecting boundary conditions when checking loop termination in scan conversion algorithms
- Not considering the coordinate system when implementing polygon filling algorithms

## Revision Tips

- Practice Bresenham's algorithm by manually tracing through several example lines with different slopes
- Remember the eight symmetry points for circles: (x, y), (y, x), (-y, x), (-x, y), (-x, -y), (-y, -x), (y, -x), (x, -y)
- Keep the color packing formula and bit positions clearly in memory
- Focus on understanding why Bresenham's algorithm works rather than just memorizing steps
- Review how DDA and Bresenham algorithms differ in their approach to line drawing
