# Pyramids and Wavelets in Image Processing

## Introduction to Multi-Resolution Analysis

Multi-resolution analysis is a fundamental concept in image processing that allows us to analyze images at different scales or resolutions. This approach is particularly valuable because visual information exists at multiple scales - fine details appear at high resolutions while broader structures are visible at lower resolutions. Pyramids and wavelets are two powerful techniques that implement multi-resolution analysis, each with unique characteristics and applications.

The human visual system itself operates in a multi-resolution manner, with our eyes capturing both fine details and overall scene structure simultaneously. By mimicking this approach computationally, we can create more efficient and effective image processing algorithms.

## Image Pyramids

### What are Image Pyramids?

Image pyramids are multi-scale representations of an image where each level is a reduced-resolution version of the previous level. The structure resembles a pyramid, with the original high-resolution image at the base and successively smaller images stacked above it.

```
Original Image (Level 0)
 |
 V
Reduced Image (Level 1)
 |
 V
Reduced Image (Level 2)
 |
 V
 ... (Top Level)
```

### Types of Image Pyramids

#### Gaussian Pyramid

The Gaussian pyramid is created by repeatedly applying a Gaussian smoothing filter followed by subsampling (typically by a factor of 2 in each dimension). This process creates a series of images where each level has approximately half the resolution of the previous level.

**Construction Process:**

1. Start with the original image (level 0)
2. Apply Gaussian smoothing to reduce high frequencies
3. Subsample by taking every other pixel
4. Repeat steps 2-3 for the resulting image

```
G0 (Original) → Blur → Subsample → G1 → Blur → Subsample → G2 → ...
```

#### Laplacian Pyramid

The Laplacian pyramid is created from the Gaussian pyramid and represents the difference between levels. Each level contains the details lost during the reduction process from the previous level.

**Construction Process:**

1. Build Gaussian pyramid: G0, G1, G2, ..., Gn
2. For each level i, expand Gi+1 to the size of Gi
3. Calculate Li = Gi - Expand(Gi+1)
4. The top level Ln is simply Gn

The Laplacian pyramid enables perfect reconstruction of the original image through a process of expansion and addition:

```
Reconstruction: Gn + Expand(Ln-1) + Expand(Ln-2) + ... + Expand(L0)
```

### Applications of Image Pyramids

1. **Image Blending**: Seamlessly combine images using pyramid-based techniques
2. **Texture Synthesis**: Generate new texture patterns from sample images
3. **Compression**: Store images efficiently by encoding differences between levels
4. **Multi-scale Processing**: Apply operations at different scales for better results

## Wavelet Transform

### Introduction to Wavelets

Wavelets are mathematical functions that decompose data into different frequency components, each analyzed with a resolution matched to its scale. Unlike Fourier transform which uses sine and cosine functions, wavelets use localized "small waves" that are limited in duration.

### Discrete Wavelet Transform (DWT)

The Discrete Wavelet Transform decomposes an image into four subbands at each level of decomposition:

```
+----------------+----------------+
| LL (Approx) | HL (Horiz) |
| Low-Low | High-Low |
+----------------+----------------+
| LH (Vert) | HH (Diag) |
| Low-High | High-High |
+----------------+----------------+
```

- **LL**: Low-frequency approximation (smoothed version)
- **HL**: Horizontal details
- **LH**: Vertical details
- **HH**: Diagonal details

### Wavelet Decomposition Process

The decomposition process can be applied recursively to the LL subband to create multiple resolution levels:

```
Level 1: Original Image → DWT → LL1, HL1, LH1, HH1
Level 2: LL1 → DWT → LL2, HL2, LH2, HH2
Level 3: LL2 → DWT → LL3, HL3, LH3, HH3
```

### Types of Wavelets

1. **Haar Wavelet**: The simplest wavelet, good for educational purposes
2. **Daubechies Wavelet**: Popular in image compression (JPEG2000)
3. **Coiflet Wavelet**: Balanced properties for various applications
4. **Symlet Wavelet**: Nearly symmetric wavelets

### Applications of Wavelet Transform

1. **Image Compression**: JPEG2000 uses wavelet-based compression
2. **Denoising**: Remove noise while preserving edges
3. **Feature Extraction**: Extract multi-scale features for recognition
4. **Watermarking**: Embed information in specific frequency bands

## Comparison: Pyramids vs. Wavelets

| Aspect                       | Image Pyramids                  | Wavelet Transform                   |
| ---------------------------- | ------------------------------- | ----------------------------------- |
| **Basis Functions**          | Fixed kernel (Gaussian)         | Various wavelet families            |
| **Computational Complexity** | Generally lower                 | Generally higher                    |
| **Perfect Reconstruction**   | Possible with Laplacian pyramid | Always possible                     |
| **Translation Invariance**   | Not invariant                   | Some wavelets are invariant         |
| **Storage Requirements**     | Increased (1.33× original)      | Same as original (with compression) |
| **Applications**             | Blending, texture synthesis     | Compression, denoising              |

## Implementation Examples

### Gaussian Pyramid Implementation (Pseudocode)

```
function build_gaussian_pyramid(image, levels):
 pyramid = []
 current = image
 pyramid.append(current)

 for i in range(1, levels):
 # Apply Gaussian blur
 blurred = gaussian_blur(current, sigma)
 # Subsample by factor of 2
 subsampled = blurred[::2, ::2]
 pyramid.append(subsampled)
 current = subsampled

 return pyramid
```

### Wavelet Decomposition (Pseudocode)

```
function wavelet_decomposition(image, levels, wavelet_type):
 coefficients = []
 current = image

 for i in range(levels):
 # Apply 2D DWT
 LL, LH, HL, HH = dwt_2d(current, wavelet_type)
 coefficients.append({'LL': LL, 'LH': LH, 'HL': HL, 'HH': HH})
 current = LL # Continue with approximation

 return coefficients
```

## Practical Considerations

### Choosing Between Pyramids and Wavelets

- Use **pyramids** when you need simplicity and computational efficiency
- Use **wavelets** when you need perfect reconstruction or specific frequency analysis
- Consider **application requirements**: compression vs. multi-scale processing

### Parameter Selection

- For pyramids: Choose appropriate Gaussian kernel size and subsampling factor
- For wavelets: Select wavelet type based on application needs
- Determine the number of decomposition levels based on image size and required detail

## Exam Tips

1. **Understand the fundamental difference**: Pyramids provide multi-resolution representation while wavelets provide multi-frequency representation.

2. **Remember the pyramid types**: Gaussian for smoothing/subsampling, Laplacian for difference encoding.

3. **Know the wavelet subbands**: LL (approximation), HL (horizontal details), LH (vertical details), HH (diagonal details).

4. **Practice reconstruction**: Be able to explain how to reconstruct an image from both pyramid and wavelet representations.

5. **Compare applications**: Pyramids excel in blending and texture, wavelets in compression and denoising.

6. **Understand computational aspects**: Pyramids generally require more storage while wavelets can be more computationally intensive.

7. **Recognize visual patterns**: Be able to identify wavelet subbands and pyramid levels from visual examples.
