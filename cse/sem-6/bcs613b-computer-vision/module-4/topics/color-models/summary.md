# Color Models

## Overview

Color models are mathematical representations of colors as tuples of numbers serving different purposes in image processing. Understanding various models (RGB, HSV, YCbCr, LAB) and conversions between them is essential for effective color-based computer vision tasks.

## Key Points

- **RGB**: Additive model (R,G,B 0-255), hardware-oriented, highly correlated components
- **HSV/HSI**: Hue (color 0-360°), Saturation (purity 0-100%), Value/Intensity (brightness), decouples color from brightness
- **YCbCr**: Luminance Y + chrominance Cb,Cr, separates brightness from color, used in JPEG/video compression
- **LAB**: Lightness L + opponent colors a (green-red), b (blue-yellow), perceptually uniform
- **CMY/CMYK**: Subtractive model for printing, C=1-R, M=1-G, Y=1-B, K=black

## Important Concepts

- Model selection depends on task: RGB for display, HSV for segmentation, YCbCr for compression, LAB for matching
- HSV advantages: intuitive color specification, easy brightness adjustment, good for color-based segmentation
- YCbCr exploits human vision being more sensitive to luminance than chrominance for compression
- LAB device-independent and perceptually uniform (equal distances = equal perceived differences)

## Notes

- Practice RGB↔HSV↔YCbCr conversions as frequently tested
- HSV/HSI separates chromatic from achromatic information crucial for illumination-invariant processing
- YCbCr allows chroma subsampling in compression (4:2:0) due to lower human sensitivity
- LAB CIELAB standard for color matching and quality control applications
