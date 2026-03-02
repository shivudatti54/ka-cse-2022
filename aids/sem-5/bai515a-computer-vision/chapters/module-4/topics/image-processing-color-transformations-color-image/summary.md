# **Color Image Processing: Quick Revision Notes**

### Image Processing

- **Image Processing**: A set of algorithms used to modify a digital image.
- **Types of Image Processing**:
  - Filtering
  - Transformations (e.g. rotation, scaling)
  - Thresholding
- **Key Concepts**:
  - Image representation (e.g. pixel values, color models)
  - Image operations (e.g. addition, subtraction)

### Color Transformations

- **Color Transformations**: Changes to the color space of an image.
- **Common Color Transformations**:
  - RGB to HSV (Hue, Saturation, Value)
  - RGB to YUV (Luminance, Chrominance)
  - Color lookup tables (LUTs)
- **Formulas**:
  - RGB to HSV: `H = arctan2(S, V)`, `S = V * sqrt(1 - (V^2 / R^2))`
  - RGB to YUV: `Y = 0.299R + 0.587G + 0.114B`, `U = 0.436B - 0.616G + 0.080R`, `V = 0.212B - 0.463G + 0.715R`

### Color Image Smoothing and Sharpening

- **Smoothing**:
  - Reduces noise and detail in an image.
  - Types: Gaussian blur, Median blur
- **Sharpening**:
  - Enhances detail in an image.
  - Types: Unsharp masking, Gaussian sharpening
- **Formulas**:
  - Gaussian blur: `I(x) = (1 / (2πσ^2)) \* ∫∫e^(-(x^2 + y^2) / (2σ^2)) \* f(x, y) dx dy`
  - Unsharp masking: `I(x) = f(x, y) + (α \* (f(x, y) - σ^2 \* ∇^2f(x, y)) + β \* σ^2 \* ∇^2f(x, y))`

### Using Color in Image Segmentation

- **Image Segmentation**: Divides an image into regions of similar color.
- **Methods**:
  - Thresholding
  - Clustering
  - Edge detection
- **Formulas**:
  - Thresholding: `C = (R - μ) / σ`, where `C` is the color difference, `R` is the color value, `μ` is the mean, and `σ` is the standard deviation

### Noise in Color Images

- **Noise**: Random variations in pixel values.
- **Types of Noise**:
  - Shot noise
  - Read noise
  - Thermal noise
- **Formulas**:
  - Shot noise: `σ_R = √(2e \* Δt)`, where `σ_R` is the standard deviation of the read noise, `e` is the elementary charge, and `Δt` is the exposure time.
