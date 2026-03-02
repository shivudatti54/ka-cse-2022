# **Color Image Processing: Revision Notes**

### Image Processing Fundamentals

- Image processing involves applying algorithms to images to extract useful information
- Image processing techniques include filtering, transformation, and feature extraction
- Image processing can be done in the spatial domain or the transform domain (e.g., frequency domain)

### Color Transformations

- **Color Models:**
  - RGB (Red, Green, Blue) model
  - CMYK (Cyan, Magenta, Yellow, Black) model
  - Lab color model
  - XYZ color model
- **Color Transform Formulas:**
  - RGB to XYZ: X = 0.412R + 0.357G + 0.180Y, Y = 0.212R + 0.715G + 0.072Y, Z = 0.019R + 0.119G + 0.950Y
  - XYZ to Lab: L = 116f(L*) - 16, a = 500(f(L*) - f(L')), b = 200(f(L\*) - f(L'))
- **Pseudocolor Image Processing:**
  - Assigns a color to each pixel based on its intensity values

### Color Image Smoothing and Sharpening

- **Smoothing Techniques:**
  - Blur
  - Average filter
  - Gaussian filter
- **Sharpening Techniques:**
  - Unsharp masking
  - Edge enhancement
- **Sharpening Formula:**
  - Sharpened image = Original image + (K \* (Original image - Blurred image))

### Using Color in Image Segmentation

- **Color-based Segmentation:**
  - Uses color information to segment images
- **Color Theory:**
  - HLS (Hue, Lightness, Saturation) color model
  - YCbCr (Luminance, Blue, Chrominance) color model
- **Segmentation Formulas:**
  - Histogram-based segmentation: Segment pixels with similar color histograms

### Noise in Color Images

- **Types of Noise:**
  - Shot noise
  - Read noise
  - Thermal noise
- **Noise Reduction Techniques:**
  - Filtering (e.g., Gaussian filter)
  - Median filtering
- **Noise Reduction Formula:**
  - Noisy image = (Filtered image) + (Noise)
