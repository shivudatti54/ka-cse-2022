# Color Image Processing: Color Fundamentals

### 1. Introduction to Color Models

- Definition: A color model is a mathematical representation of colors.
- Types:
  - RGB (Red, Green, Blue)
  - CMYK (Cyan, Magenta, Yellow, Black)
  - YUV (Luminance and Chrominance)
  - XYZ (CIE color space)

### 2. Color Spaces

- Definition: A color space is a region of colors that can be represented by a color model.
- Types:
  - RGB color space (used for digital displays)
  - CMYK color space (used for printing)
  - YUV color space (used for video and broadcasting)

### 3. Color Conversion Formulas

- RGB to XYZ:
  - X = 0.412453 _ R + 0.357580 _ G + 0.180423 \* B
  - Y = 0.212671 _ R + 0.715160 _ G + 0.072169 \* B
  - Z = 0.019334 _ R + 0.119193 _ G + 0.950227 \* B
- XYZ to RGB:
  - R = 3.240479 _ X - 1.537150 _ Y - 0.498535 \* Z
  - G = -0.969256 _ X + 1.875992 _ Y + 0.041556 \* Z
  - B = 0.055648 _ X - 0.204043 _ Y + 1.057311 \* Z

### 4. CIE 1931 Color Space

- Definition: A color space that accurately represents the human visual system.
- Formulas:
  - L* = 116 * f(R) - 16
  - a* = 500 * (f(G) - f(R))
  - b* = 200 * (f(B) - f(R))
  - f(X) = X / (X + Y + Z)

### 5. Pseudocolor Image Processing

- Definition: A technique to display a color image using a limited color palette.
- Types:
  - Indexed color
  - Pseudocolor

### 6. Full Color Image Processing

- Definition: A technique to display a color image using a full range of colors.
- Types:
  - RGB color space
  - CMYK color space

### 7. Color Quantization

- Definition: The process of reducing the number of colors in an image.
- Types:
  - Median cut
  - K-means clustering

### 8. Color Matching

- Definition: The process of finding the closest match between two colors.
- Types:
  - Delta-E
  - CIE94

Note: This summary provides a concise overview of the key points in Chapter 6 of the textbook. It is intended for quick revision purposes only.
