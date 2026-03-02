# Digital Image Fundamentals - Summary

## Key Definitions and Concepts

- **Digital Image**: A two-dimensional function f(x, y) where x and y are spatial coordinates, and f represents intensity at point (x, y). When x, y, and f are all finite discrete quantities, it's a digital image.

- **Pixel**: Short for "picture element," the smallest unit of a digital image. Each pixel has a specific location and intensity value.

- **Sampling**: The process of discretizing spatial coordinates (x, y) in an image. Determines spatial resolution.

- **Quantization**: The process of discretizing intensity values (amplitude f). Determines intensity/bit depth.

- **4-neighborhood**: Four adjacent pixels sharing edges with a central pixel at positions (x±1, y) and (x, y±1).

- **8-neighborhood**: All eight surrounding pixels including diagonals.

## Important Formulas and Theorems

- **Storage Size**: M × N × b bytes, where M×N is image dimension and b is bytes per pixel

- **Intensity Levels**: For n-bit image, possible levels = 2^n

- **Gray Level Range**: 0 to (L-1), where L = number of levels (typically 256 for 8-bit)

- **Nyquist Theorem**: Sampling frequency must be at least twice the highest frequency component

## Key Points

- Digital images are represented as matrices where each element is a pixel value.

- Grayscale images use 8 bits (256 levels), while true color uses 24 bits (16.7 million colors).

- Sampling affects spatial resolution; quantization affects intensity resolution.

- JPEG uses lossy compression; PNG, BMP, GIF use lossless compression.

- Binary images have only 2 levels (black and white).

- RGB model adds Red, Green, Blue channels; grayscale can be derived using luminosity formula.

- Higher resolution means more pixels and better detail but larger file sizes.

## Common Mistakes to Avoid

1. Confusing sampling (spatial discretization) with quantization (intensity discretization).

2. Forgetting to convert between bits and bytes when calculating storage requirements.

3. Assuming all image formats use the same compression method (JPEG is lossy, PNG is lossless).

4. Mixing up 4-neighborhood and 8-neighborhood definitions in connectivity problems.

## Revision Tips

1. Practice storage calculation problems with different image dimensions and bit depths.

2. Draw pixel neighborhoods to visualize 4-connectivity vs 8-connectivity.

3. Remember the relationship: more bits = more gray levels = larger file size.

4. Create a comparison table of image formats with their compression types and typical use cases.
