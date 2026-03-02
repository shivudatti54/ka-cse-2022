# Color Fundamentals

## Overview

Color is a powerful descriptor simplifying object identification and extraction in computer vision. Understanding color physics, perception, and mathematical models is essential for effective color image processing, as humans distinguish thousands of color shades versus only dozens of gray shades.

## Key Points

- **Visible Spectrum**: 400nm (violet) to 700nm (red) with human perception based on three cone types (S, M, L)
- **Color Characteristics**: Brightness (intensity), Hue (color family/wavelength), Saturation (color purity/vividness)
- **RGB Model**: Additive model (R,G,B 0-255) for displays, directly corresponds to hardware but not perceptually intuitive
- **CMY/CMYK**: Subtractive model for printing, C=1-R, M=1-G, Y=1-B with Black (K) added
- **HSI Model**: Hue, Saturation, Intensity decouples color from brightness, more aligned with human perception
- **Color Gamut**: Complete subset of colors representable by device/model, varies across devices
- **Color Depth**: Bits per pixel - 8-bit (256 colors), 24-bit (16.7M true color), 32-bit (true color + alpha)

## Important Concepts

- HSI conversion formulas: I = (R+G+B)/3, S = 1-min(R,G,B)/I, H based on angular calculation
- Additive (RGB - light) versus subtractive (CMY - pigment) color mixing principles
- Trichromatic theory: three cone types enable color perception matching imaging systems
- Color gamut differences explain why colors appear differently across devices

## Notes

- Memorize HSI conversion formulas as frequently tested
- Understand advantages of HSI: intensity separation makes it superior for CV tasks versus RGB
- Know color model applications: RGB for display, CMY for printing, HSI for segmentation
- Practice conversions between RGB, CMY, and HSI color representations
- Higher color depth improves quality but increases file size and processing requirements
