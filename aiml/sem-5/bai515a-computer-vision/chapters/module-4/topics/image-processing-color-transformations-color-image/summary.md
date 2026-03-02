# **Color Image Processing Revision Notes**

## **Image Processing**

- Image processing involves applying algorithms to modify the pixels of an image.
- Types of image processing:
  - Filtering (blurring, sharpening)
  - Transformations (rotation, scaling)
  - Enhancement (contrast, brightness)

## **Color Transformations**

- Color transformation: changing the color space of an image.
- Color models:
  - RGB (Red, Green, Blue)
  - CMYK (Cyan, Magenta, Yellow, Black)
  - HSV (Hue, Saturation, Value)
- Color transformations:
  - Conversion between color models
  - Color space transformations (e.g., from RGB to YCbCr)

## **Color Image Smoothing and Sharpening**

- Image smoothing:
  - Blur: reducing noise and detail
  - Unsharp mask: enhancing contrast and detail
- Image sharpening:
  - Sharpening filters (e.g., Sobel, Kirsch)
  - Unsharp masking

## **Using Color in Image Segmentation**

- Image segmentation: dividing an image into regions of similar color or texture.
- Color-based segmentation:
  - Color histogram analysis
  - Color thresholding
  - Color clustering

## **Noise in Color Images**

- Noise in images: random fluctuations in pixel values.
- Types of noise:
  - Salt and pepper noise
  - Gaussian noise
- Noise reduction techniques:
  - Median filtering
  - Adaptive filtering

## **Important Formulas and Definitions**

- **Luminance**: the brightness of an image, calculated as the weighted sum of the RGB values: I = 0.2126R + 0.7152G + 0.0722B
- **Contrast ratio**: the ratio of the difference between the brightest and darkest pixels to the average brightness
- **Signal-to-noise ratio**: the ratio of the signal (image features) to the noise (random fluctuations)
