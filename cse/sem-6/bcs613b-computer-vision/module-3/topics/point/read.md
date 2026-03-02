# Point Operations in Computer Vision

## 1. Introduction to Point Operations

**Point operations** (also called **pixel operations** or **intensity transformations**) are the simplest and most fundamental image processing operations. They transform each pixel independently based only on its own intensity value, without considering neighboring pixels.

**Mathematical Definition**: For an input image I(x,y), a point operation produces an output image O(x,y) where:

```
O(x,y) = T[I(x,y)]
```

where T is a transformation function applied to each pixel independently.

**Key Characteristic**: The output pixel value depends **only** on the input pixel value at the same location, not on neighboring pixels.

## 2. Why Point Operations?

Point operations are used to:

- **Enhance visual appearance**: Make images easier to interpret
- **Improve contrast**: Make features more distinguishable
- **Normalize images**: Standardize lighting conditions
- **Prepare for further processing**: Preprocessing step for advanced algorithms
- **Correct acquisition problems**: Fix under/overexposure

**Advantages**:

- Very fast (single pass through image)
- Simple to implement
- Easily parallelizable (can process pixels independently)
- Low computational cost

## 3. Brightness Adjustment

Brightness adjustment uniformly increases or decreases all pixel intensities.

### 3.1 Linear Brightness Adjustment

**Formula**:

```
O(x,y) = I(x,y) + b
```

where b is the brightness offset:

- b > 0: Increases brightness (image lighter)
- b < 0: Decreases brightness (image darker)
- b = 0: No change

**Example**:

```
Input: [50, 100, 150, 200]
b = 30
Output: [80, 130, 180, 230]
```

**Clamping**: Ensure values stay in valid range [0, 255]

```
O(x,y) = clip(I(x,y) + b, 0, 255)
```

### 3.2 Applications

- Correcting underexposed images (add brightness)
- Correcting overexposed images (reduce brightness)
- Normalizing lighting conditions across multiple images

## 4. Contrast Adjustment

Contrast controls the difference between light and dark regions. Higher contrast means greater difference between intensities.

### 4.1 Linear Contrast Stretching

**Formula**:

```
O(x,y) = α × I(x,y)
```

where α is the contrast factor:

- α > 1: Increases contrast (stretches intensity range)
- α < 1: Decreases contrast (compresses intensity range)
- α = 1: No change

**Example**:

```
Input: [50, 100, 150, 200]
α = 1.5
Output: [75, 150, 225, 255] (clamped)
```

### 4.2 Combined Brightness and Contrast

**General linear transformation**:

```
O(x,y) = α × I(x,y) + β
```

where:

- α controls contrast (slope)
- β controls brightness (y-intercept)

**Typical values**:

- α ∈ [0.5, 3.0]
- β ∈ [-127, +127]

### 4.3 Contrast Stretching to Full Range

Expand the image's intensity range to use the full [0, 255] range:

**Formula**:

```
O(x,y) = 255 × (I(x,y) - I_min) / (I_max - I_min)
```

where:

- I_min = minimum intensity in image
- I_max = maximum intensity in image

**Example**:
If image has range [50, 200]:

```
O(x,y) = 255 × (I(x,y) - 50) / (200 - 50)
```

This maps:

- 50 → 0 (darkest)
- 200 → 255 (brightest)

## 5. Image Negative (Inversion)

Creates a photographic negative effect by inverting intensities.

**Formula**:

```
O(x,y) = L - 1 - I(x,y)
```

where L is the number of gray levels (typically 256 for 8-bit images).

**For 8-bit images**:

```
O(x,y) = 255 - I(x,y)
```

**Effect**:

- Dark pixels become bright
- Bright pixels become dark
- 0 → 255, 255 → 0, 128 → 127

**Applications**:

- Medical imaging (enhancing white details in X-rays)
- Film negative digitization
- Artistic effects

## 6. Thresholding

Thresholding converts a grayscale image to a binary image by comparing each pixel to a threshold value.

### 6.1 Basic Thresholding

**Formula**:

```
O(x,y) = { 255 if I(x,y) > T
 { 0 otherwise
```

where T is the threshold value.

**Example**:

```
Input: [30, 80, 120, 200]
T = 100
Output: [0, 0, 255, 255]
```

### 6.2 Types of Thresholding

**1. Binary Thresholding**:

```
O(x,y) = { max_val if I(x,y) > T
 { 0 otherwise
```

**2. Binary Inverse Thresholding**:

```
O(x,y) = { 0 if I(x,y) > T
 { max_val otherwise
```

**3. Truncate Thresholding**:

```
O(x,y) = { T if I(x,y) > T
 { I(x,y) otherwise
```

**4. To-Zero Thresholding**:

```
O(x,y) = { I(x,y) if I(x,y) > T
 { 0 otherwise
```

### 6.3 Threshold Selection Methods

**1. Manual Selection**: User chooses threshold

- Simple but subjective
- Requires trial and error

**2. Otsu's Method**: Automatically finds optimal threshold

- Maximizes between-class variance
- Minimizes within-class variance
- Very popular and effective

**3. Mean/Median**: Use image statistics

```
T = mean(I) or T = median(I)
```

**4. Adaptive Thresholding**: Different thresholds for different regions

- Handles non-uniform illumination
- Computes local threshold for each region

### 6.4 Applications

- Document scanning (text extraction)
- Object segmentation
- Foreground-background separation
- QR code/barcode reading
- Feature extraction

## 7. Histogram Equalization

Histogram equalization improves contrast by redistributing pixel intensities to achieve a more uniform histogram.

### 7.1 Image Histogram

**Definition**: A histogram shows the frequency distribution of intensity values.

**Formula**: For intensity level k:

```
h(k) = number of pixels with intensity k
```

**Normalized histogram** (probability):

```
p(k) = h(k) / (total number of pixels)
```

### 7.2 Why Histogram Equalization?

**Problem**: Images with poor contrast have histograms concentrated in a narrow range.

**Solution**: Spread out intensities to use the full range [0, 255].

**Goal**: Transform histogram to be approximately uniform (flat distribution).

### 7.3 Histogram Equalization Algorithm

**Step 1**: Compute histogram h(k)

**Step 2**: Compute cumulative distribution function (CDF):

```
CDF(k) = Σ(i=0 to k) h(i)
```

**Step 3**: Normalize CDF to [0, 255]:

```
CDF_normalized(k) = (CDF(k) - CDF_min) / (total_pixels - CDF_min) × 255
```

**Step 4**: Map each pixel to new intensity:

```
O(x,y) = CDF_normalized[I(x,y)]
```

### 7.4 Example

**Input image** with 64 pixels and 8 gray levels [0-7]:

| Intensity  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Count h(k) | 10  | 12  | 16  | 10  | 8   | 4   | 2   | 2   |

**Step 1**: Cumulative histogram:

| k   | CDF(k) |
| --- | ------ |
| 0   | 10     |
| 1   | 22     |
| 2   | 38     |
| 3   | 48     |
| 4   | 56     |
| 5   | 60     |
| 6   | 62     |
| 7   | 64     |

**Step 2**: Normalized mapping (to range 0-7):

```
new_value(k) = round((CDF(k) - CDF_min) / (64 - 10) × 7)
```

**Result**: More evenly distributed intensities

### 7.5 Properties

**Advantages**:

- Automatic (no parameters needed)
- Enhances contrast globally
- Brings out hidden details

**Disadvantages**:

- May over-enhance noise
- Can produce unnatural-looking images
- Not suitable for already high-contrast images

**Applications**:

- Medical imaging (X-rays, CT scans)
- Satellite imagery
- Low-light photography enhancement
- Preprocessing for feature extraction

## 8. Gamma Correction

Gamma correction adjusts image brightness in a non-linear way to compensate for display characteristics or enhance specific intensity ranges.

### 8.1 Gamma Transformation

**Formula**:

```
O(x,y) = c × I(x,y)^γ
```

where:

- γ (gamma) is the correction factor
- c is a scaling constant (often 1)

**For normalized intensities [0, 1]**:

```
O = I^γ
```

### 8.2 Gamma Values

- **γ < 1**: Brightens the image (compresses dark regions, expands bright regions)
- γ = 0.5: Significant brightening
- Useful for underexposed images

- **γ = 1**: No change (linear)

- **γ > 1**: Darkens the image (expands dark regions, compresses bright regions)
- γ = 2.0: Significant darkening
- Useful for overexposed images

### 8.3 Applications

- **Display calibration**: Correcting monitor gamma (typically 2.2)
- **Image enhancement**: Revealing details in shadows or highlights
- **HDR imaging**: Tone mapping high dynamic range images
- **Color correction**: Non-linear color adjustments

## 9. Logarithmic Transformation

Compresses the dynamic range of images with large variations in pixel values.

**Formula**:

```
O(x,y) = c × log(1 + I(x,y))
```

where c is a scaling constant.

**Effect**:

- Expands dark pixel values
- Compresses bright pixel values
- Useful for images with wide dynamic range

**Applications**:

- Fourier spectrum display
- Medical imaging (enhancing low-intensity details)
- Astronomical imaging

## 10. Practical Implementation Tips

### 10.1 Clipping Values

Always ensure pixel values stay in valid range:

```python
def clip(value, min_val=0, max_val=255):
 return max(min_val, min(value, max_val))
```

### 10.2 Lookup Tables (LUT)

For efficiency, precompute transformations:

```python
# Create lookup table
LUT = [int(transform(i)) for i in range(256)]

# Apply to image
output = LUT[input_image]
```

**Advantages**:

- Very fast (O(1) per pixel)
- Efficient for video processing
- Easy to combine multiple operations

## 11. Summary Comparison

| Operation     | Formula         | Effect                     | Use Case           |
| ------------- | --------------- | -------------------------- | ------------------ |
| Brightness    | I + b           | Shifts all intensities     | Correct exposure   |
| Contrast      | α × I           | Stretches/compresses range | Enhance visibility |
| Negative      | 255 - I         | Inverts intensities        | Medical imaging    |
| Threshold     | I > T ? 255 : 0 | Binary segmentation        | Extract objects    |
| Histogram Eq. | CDF mapping     | Uniform distribution       | Enhance contrast   |
| Gamma         | I^γ             | Non-linear adjustment      | Display correction |
| Log           | log(1+I)        | Compress dynamic range     | Wide range images  |

## 12. Exam Tips

1. **Understand independence**: Point operations affect each pixel independently
2. **Know formulas**: Brightness (I+b), Contrast (αI), Negative (255-I), Threshold
3. **Histogram equalization**: CDF-based mapping, automatic contrast enhancement
4. **Gamma correction**: γ<1 brightens, γ>1 darkens
5. **Thresholding types**: Binary, inverse, truncate, to-zero
6. **Applications**: Match each operation to its use case
7. **Clipping**: Remember to handle out-of-range values [0, 255]
