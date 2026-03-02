# Color Image Processing

### Chap-6 (6.1-6.8)

### Annexure-II

- **Color Models**
  - RGB (Red, Green, Blue) Model
    - Each pixel is represented by a 3-tuple of intensity values (R, G, B)
    - Values range from 0 to 255
  - CMYK (Cyan, Magenta, Yellow, Black) Model
    - Each pixel is represented by a 4-tuple of intensity values (C, M, Y, K)
    - Values range from 0 to 100
  - YCbCr (Luminance, Blue, Chrominance) Model
    - Used for digital television and video transmission
    - Luminance (Y) represents the brightness of the pixel
    - Blue and chrominance (Cb and Cr) represent the color information

### Key Formulas and Theorems

- **Color Addition**
  - RGB: (R1 + R2, G1 + G2, B1 + B2)
  - CMYK: (C1 + C2, M1 + M2, Y1 + Y2, K1 + K2)
- **Color Subtraction**
  - RGB: (R1 - R2, G1 - G2, B1 - B2)
  - CMYK: (C1 - C2, M1 - M2, Y1 - Y2, K1 - K2)
- **Hue Saturation Value (HSV) Color Model**
  - HSV: (H, S, V)
  - Represents hue, saturation, and value (brightness)
- **YCbCr to RGB Conversion**
  - Y = 0.299 \* R + 0.587 \* G + 0.114 \* B
  - Cb = 128 + 0.168736 \* (R - Y) + 0.331264 \* (G - Y)
  - Cr = 128 + 0.587305 \* (R - Y) + 0.436058 \* (B - Y)

### Important Definitions

- **Pseudocolor Image Processing**: A method of color image processing that uses a fixed palette of colors to represent the image
- **Color Filtering**: A technique used to enhance or suppress specific colors in an image
- **Color Thresholding**: A technique used to segment an image based on the intensity of the colors
