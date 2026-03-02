# Computer Vision Fundamentals: Digital Images

## 1. What is a Digital Image?

A **digital image** is a numerical representation of a visual scene, stored as a discrete grid of values that computers can process. It is the fundamental data structure in computer vision.

**Formal Definition**: A digital image is a 2D function f(x, y) where x and y are spatial coordinates, and the value of f at any point (x, y) is the intensity or color at that location.

### 1.1 Continuous vs Discrete Images

| Aspect           | Analog (Continuous)              | Digital (Discrete)       |
| ---------------- | -------------------------------- | ------------------------ |
| Spatial domain   | Continuous (infinite resolution) | Discrete (finite pixels) |
| Intensity values | Continuous (infinite levels)     | Discrete (finite levels) |
| Storage          | Film, photographic paper         | Computer memory          |
| Processing       | Chemical/optical                 | Computational            |

**Digitization** is the process of converting continuous images to digital form through:

1. **Sampling**: Discretizing spatial coordinates (x, y)
2. **Quantization**: Discretizing intensity values

## 2. Pixels: The Building Blocks

### 2.1 What is a Pixel?

A **pixel** (picture element) is the smallest addressable unit in a digital image. It represents a single point in the image grid.

**Properties of a pixel**:

- **Location**: (x, y) coordinates in the image grid
- **Value**: Intensity (grayscale) or color (RGB) information
- **Size**: Physical size depends on display/sensor resolution

### 2.2 Image Resolution

**Spatial Resolution**: Number of pixels in an image

- Measured as width × height (e.g., 1920×1080 pixels)
- Higher resolution = more detail, larger file size

**Common Resolutions**:

- VGA: 640×480
- HD: 1280×720
- Full HD: 1920×1080
- 4K: 3840×2160
- 8K: 7680×4320

**Intensity Resolution**: Number of distinct intensity levels

- 8-bit: 256 levels (0-255)
- 16-bit: 65,536 levels
- Higher bit depth = finer gradations, better quality

## 3. Image Types

### 3.1 Binary Images

**Definition**: Each pixel is either 0 (black) or 1 (white)

**Storage**: 1 bit per pixel

**Applications**:

- Document scanning
- Barcode reading
- Shape analysis
- Text recognition

**Example representation**:

```
1 1 1 0 0 1 1 1
1 1 0 0 0 0 1 1
1 0 0 1 1 0 0 1
```

### 3.2 Grayscale Images

**Definition**: Each pixel represents an intensity value

**Storage**: Typically 8 bits per pixel (256 levels)

- 0 = black
- 255 = white
- 1-254 = shades of gray

**Mathematical representation**: I(x, y) ∈ [0, 255]

**Applications**:

- Medical imaging (X-rays, CT scans)
- Surveillance systems
- Texture analysis
- Preprocessing for color images

**Advantages**:

- Smaller file size than color
- Simpler processing
- Sufficient for many applications

### 3.3 Color Images

Color images represent color information at each pixel using different color models.

#### 3.3.1 RGB Color Model

**Most common color representation**

**Components**:

- **R**: Red channel (0-255)
- **G**: Green channel (0-255)
- **B**: Blue channel (0-255)

**Storage**: 24 bits per pixel (8 bits per channel) = 16.7 million colors

**Example**:

- Red = (255, 0, 0)
- Green = (0, 255, 0)
- Blue = (0, 0, 255)
- White = (255, 255, 255)
- Black = (0, 0, 0)
- Yellow = (255, 255, 0)

**Representation**: Color image is a 3D array [height × width × 3]

#### 3.3.2 Grayscale from RGB Conversion

**Common formula**:

```
Gray = 0.299×R + 0.587×G + 0.114×B
```

**Why different weights?**

- Human eyes are most sensitive to green
- Least sensitive to blue
- Weights reflect human perception

### 3.4 Multi-channel Images

Images can have more than 3 channels:

**RGBA**: RGB + Alpha (transparency)

- 32 bits per pixel
- Alpha: 0 = fully transparent, 255 = fully opaque

**Multispectral**: More than 3 spectral bands

- Satellite imagery (infrared, ultraviolet)
- Medical imaging (different wavelengths)

## 4. Color Spaces

Color spaces are mathematical models for representing colors.

### 4.1 RGB (Red, Green, Blue)

**Device-dependent**: Used by cameras, displays

**Advantages**:

- Intuitive for hardware
- Easy color mixing

**Disadvantages**:

- Not perceptually uniform
- Difficult to adjust brightness/saturation separately

### 4.2 HSV (Hue, Saturation, Value)

**Components**:

- **Hue**: Color type (0-360°) - Red=0°, Green=120°, Blue=240°
- **Saturation**: Color purity (0-100%) - 0=gray, 100=pure color
- **Value**: Brightness (0-100%) - 0=black, 100=bright

**Advantages**:

- More intuitive for humans
- Easy to adjust individual properties
- Good for color-based segmentation

**Conversions**:

```
RGB → HSV (non-linear transformation)
HSV → RGB (inverse transformation)
```

**Applications**:

- Color-based object detection
- Image editing tools
- Skin detection (hue is relatively stable)

### 4.3 HSL (Hue, Saturation, Lightness)

Similar to HSV but with different brightness representation:

- **Lightness**: 0=black, 50=pure color, 100=white

### 4.4 YCbCr (Luminance, Chrominance)

**Components**:

- **Y**: Luminance (brightness) - similar to grayscale
- **Cb**: Blue chrominance (blue-yellow difference)
- **Cr**: Red chrominance (red-green difference)

**Advantages**:

- Separates brightness from color
- Human vision more sensitive to Y than Cb/Cr
- Enables better compression (JPEG, video)

**Applications**:

- Video compression (MPEG, H.264)
- JPEG image compression
- Skin detection

### 4.5 LAB (Lightness, A, B)

**Components**:

- **L**: Lightness (0-100)
- **A**: Green-red axis (-128 to +127)
- **B**: Blue-yellow axis (-128 to +127)

**Advantages**:

- Perceptually uniform (equal distance = equal perceived difference)
- Device-independent
- Wide color gamut

**Applications**:

- Color matching
- High-quality image editing
- Color difference measurement

### 4.6 Choosing the Right Color Space

| Task                       | Recommended Color Space | Reason                           |
| -------------------------- | ----------------------- | -------------------------------- |
| Color-based segmentation   | HSV                     | Easy to define color ranges      |
| Skin detection             | YCbCr or HSV            | Separates color from brightness  |
| Image compression          | YCbCr                   | Exploits human visual perception |
| Color matching             | LAB                     | Perceptually uniform             |
| Display rendering          | RGB                     | Native to devices                |
| Professional photo editing | LAB                     | Device-independent, wide gamut   |

## 5. Image Representation in Memory

### 5.1 Matrix Representation

**Grayscale image** (M×N):

```
I = [I(0,0) I(0,1) ... I(0,N-1) ]
 [I(1,0) I(1,1) ... I(1,N-1) ]
 [... ... ... ... ]
 [I(M-1,0) I(M-1,1) ... I(M-1,N-1)]
```

**Color image** (M×N×3):

```
R channel: M×N matrix
G channel: M×N matrix
B channel: M×N matrix
```

### 5.2 Coordinate Systems

**Image coordinates**:

- Origin (0,0) typically at **top-left** corner
- x-axis points **right**
- y-axis points **down**

**Matrix indexing**:

- I[row, column] or I[y, x]
- row corresponds to y-coordinate
- column corresponds to x-coordinate

### 5.3 File Size Calculation

**Formula**: File size = width × height × bits_per_pixel / 8

**Examples**:

- Binary 640×480: 640 × 480 × 1 / 8 = 38,400 bytes ≈ 37.5 KB
- Grayscale 1920×1080: 1920 × 1080 × 8 / 8 = 2,073,600 bytes ≈ 2 MB
- RGB 1920×1080: 1920 × 1080 × 24 / 8 = 6,220,800 bytes ≈ 6 MB

_Note: Actual file sizes are smaller due to compression_

## 6. Image File Formats

### 6.1 Lossless Formats

**PNG (Portable Network Graphics)**:

- Lossless compression
- Supports transparency (alpha channel)
- Good for graphics, screenshots

**BMP (Bitmap)**:

- Uncompressed or minimal compression
- Large file sizes
- Simple format

**TIFF (Tagged Image File Format)**:

- Lossless or lossy
- Professional photography
- Supports multiple layers

### 6.2 Lossy Formats

**JPEG (Joint Photographic Experts Group)**:

- Lossy compression
- Smaller file sizes
- Good for photographs
- Quality controlled by compression level

**WebP**:

- Modern format by Google
- Better compression than JPEG
- Supports transparency

### 6.3 Format Comparison

| Format | Compression  | Transparency | Best Use                      |
| ------ | ------------ | ------------ | ----------------------------- |
| PNG    | Lossless     | Yes          | Graphics, logos, screenshots  |
| JPEG   | Lossy        | No           | Photographs, web images       |
| BMP    | None/minimal | No           | Simple storage, compatibility |
| TIFF   | Both         | Yes          | Professional photography      |
| WebP   | Both         | Yes          | Web images (modern browsers)  |

## 7. Pixel Neighborhoods

### 7.1 4-Connected Neighborhood (N4)

Pixels sharing an edge:

```
 [N]
 [W] [P] [E]
 [S]
```

**Applications**: Region connectivity, simple edge detection

### 7.2 8-Connected Neighborhood (N8)

Pixels sharing edge or corner:

```
[NW] [N] [NE]
[W] [P] [E]
[SW] [S] [SE]
```

**Applications**: Most image processing operations

### 7.3 Distance Metrics

**Euclidean distance** (L2):

```
d = sqrt((x1-x2)² + (y1-y2)²)
```

**Manhattan distance** (L1):

```
d = |x1-x2| + |y1-y2|
```

**Chessboard distance** (L∞):

```
d = max(|x1-x2|, |y1-y2|)
```

## 8. Exam Tips

1. **Understand pixel concept**: Smallest unit, has location and value
2. **Know image types**: Binary, grayscale, color (RGB)
3. **Color space conversions**: RGB to grayscale formula
4. **HSV advantages**: Intuitive for color-based segmentation
5. **File size calculation**: width × height × bits_per_pixel / 8
6. **Coordinate system**: (0,0) at top-left, y-axis down
7. **Color spaces for tasks**: HSV for segmentation, YCbCr for compression
8. **Pixel neighborhoods**: 4-connected vs 8-connected
