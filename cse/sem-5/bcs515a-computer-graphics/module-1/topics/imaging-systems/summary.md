# Imaging Systems - Summary

## Key Definitions and Concepts

- **Imaging System**: A complete framework for capturing, processing, storing, and displaying visual information in digital form
- **Pixel**: The fundamental unit of a digital image; short for "picture element"
- **Sampling**: Discretization of spatial coordinates to convert continuous images to discrete pixels
- **Quantization**: Discretization of amplitude values to assign discrete intensity levels
- **Spatial Resolution**: Number of pixels in an image, typically expressed as M × N
- **Intensity Resolution**: Number of bits used to represent each pixel's value (bit depth)
- **4-Neighborhood**: Four direct neighbors of a pixel (north, south, east, west)
- **8-Neighborhood**: All eight surrounding pixels including diagonals

## Important Formulas and Theorems

- **Total Pixels**: M × N (rows × columns)
- **Storage (bytes)**: (M × N × bit_depth) / 8
- **Possible Intensity Levels**: 2^b where b is bit depth
- **Grayscale Range**: 0 to 2^b - 1 (for 8-bit: 0-255)
- **Color Combinations (24-bit RGB)**: 2^24 = 16,777,216 colors

## Key Points

- Digital image formation requires both sampling (spatial discretization) and quantization (amplitude discretization)
- Common bit depths: 1-bit (binary), 8-bit (grayscale), 24-bit (true color)
- RGB model uses three bytes per pixel for red, green, and blue channels
- Image resolution directly impacts storage requirements and processing complexity
- Neighborhood concepts are fundamental for image filtering, segmentation, and morphological operations
- JPEG uses lossy compression suitable for photographs; PNG uses lossless compression for graphics
- Higher bit depth provides more intensity levels but increases storage requirements

## Common Mistakes to Avoid

- Confusing spatial resolution with intensity resolution—spatial relates to pixel count, intensity relates to bit depth
- Using Cartesian (x, y) convention instead of image coordinates (row, column) or (y, x)
- Forgetting to convert bits to bytes when calculating storage requirements
- Assuming higher resolution always means better quality—sensor quality and optical parameters also matter

## Revision Tips

- Practice storage calculation problems until automatic—these appear frequently in exams
- Draw pixel neighborhood diagrams to reinforce spatial relationships
- Create a comparison table of image file formats with their characteristics
- Remember that all image processing operations work on the discrete pixel matrix representation
