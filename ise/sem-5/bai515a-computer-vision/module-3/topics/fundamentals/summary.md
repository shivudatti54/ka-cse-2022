# Computer Vision Fundamentals - Digital Images

## Overview

Digital images are numerical representations of visual scenes stored as discrete grids of pixel values. Understanding image fundamentals including pixels, color spaces, resolution, and representations is essential for all computer vision tasks.

## Key Points

- **Digital Image Definition**: 2D function f(x,y) where x,y are spatial coordinates and f is intensity/color value
- **Pixel (Picture Element)**: Smallest addressable unit with location (x,y) and value (intensity or RGB)
- **Image Types**: Binary (1-bit), Grayscale (8-bit=256 levels), Color RGB (24-bit=16.7M colors)
- **Color Spaces**: RGB (device-dependent), HSV (hue, saturation, value - intuitive), YCbCr (luminance + chrominance - compression), LAB (perceptually uniform)
- **Resolution**: Spatial (width×height pixels) and Intensity (bit depth - 8/16 bits per channel)
- **RGB to Grayscale**: Gray = 0.299×R + 0.587×G + 0.114×B (weights match human eye sensitivity)
- **Pixel Neighborhoods**: 4-connected (edge neighbors) vs 8-connected (edge + corner neighbors)

## Important Concepts

- Image coordinate system: origin (0,0) at top-left, x-axis right, y-axis down
- File size = width × height × bits_per_pixel / 8 (uncompressed)
- HSV separates color from intensity, useful for color-based segmentation
- Different color spaces suit different tasks: HSV for segmentation, YCbCr for compression, LAB for matching

## Notes

- Understand difference between spatial resolution (pixel count) and intensity resolution (bit depth)
- Know RGB to grayscale conversion formula and why green has highest weight (0.587)
- Practice file size calculations for different image types and resolutions
- Memorize color space characteristics and appropriate use cases for each
- Distance metrics: Euclidean (L2), Manhattan (L1), Chessboard (L∞)
