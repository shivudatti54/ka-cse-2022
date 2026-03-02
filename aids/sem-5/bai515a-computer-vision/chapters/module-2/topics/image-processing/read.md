# Image Processing

## Introduction

Image processing is a fundamental area of computer science that deals with manipulating digital images to improve their quality, extract useful information, or prepare them for further analysis. In the context of the University of Delhi's Computer Science curriculum, this topic forms a critical component of the broader study of digital image analysis and computer vision. The ability to process images programmatically has become essential across numerous domains including medical imaging, satellite remote sensing, facial recognition systems, autonomous vehicles, and multimedia applications.

The subject of image processing within this module builds upon foundational concepts and prepares students for advanced topics such as Fourier transforms, pyramids and wavelets, and geometric transformations. Understanding the principles of image processing is crucial because digital images are the primary data format in modern computing applications. Every pixel in a digital image represents measurable information that can be transformed through mathematical operations to achieve desired visual or analytical outcomes.

This topic covers both theoretical concepts and practical implementations, aligning with the DU examination pattern that tests conceptual understanding as well as problem-solving abilities. Students must develop a strong grasp of spatial and frequency domain operations, image enhancement techniques, and restoration methods to excel in both internal assessments and end semester examinations.

## Key Concepts

### Digital Image Fundamentals

A digital image is represented as a matrix of pixels, where each pixel contains intensity values. For grayscale images, each pixel typically stores a value between 0 (black) and 255 (8-bit). Color images use multiple channels, most commonly RGB (Red, Green, Blue), where each channel contains intensity values for that particular color component. The spatial resolution of an image is determined by the number of rows and columns, while the bit depth defines the range of possible intensity values.

The coordinate system used in digital image processing places the origin at the top-left corner, with x-coordinate increasing to the right and y-coordinate increasing downward. This is important to remember when implementing geometric transformations and neighborhood operations. The fundamental image processing equation can be expressed as g(x,y) = T[f(x,y)], where f(x,y) is the input image, g(x,y) is the output image, and T is the transformation operator applied to the neighborhood of pixel (x,y).

### Image Enhancement in Spatial Domain

Image enhancement techniques aim to improve the visual appearance of an image or to convert the image into a form better suited for analysis by machine or human interpreters. Spatial domain techniques operate directly on the pixel values, unlike frequency domain methods which work on the Fourier transform of the image.

**Point Processing Operations** are the simplest form of image enhancement where the output value at any location depends only on the input value at that same location. These include:

- **Image Negatives**: Achieved using the transformation s = L - 1 - r, where r is the original intensity, s is the processed intensity, and L is the number of intensity levels. This is particularly useful for enhancing white or gray details in dark regions.

- **Log Transformations**: Given by s = c log(1 + r), where c is a constant. This operation compresses the dynamic range of images with large variations in pixel values, such as in Fourier spectra displays.

- **Power Law (Gamma) Transformations**: Expressed as s = crγ, where c and γ are constants. Different values of γ produce different effects - values less than 1 expand dark regions while values greater than 1 expand bright regions. Gamma correction is extensively used in display devices.

- **Histogram Processing**: Histogram equalization is a technique that distributes intensity values more uniformly across the available range, thereby enhancing image contrast. The probability density function of intensity levels is used to compute the transformation function.

### Histogram Equalization

The histogram of a digital image represents the frequency distribution of intensity levels. For an image with L intensity levels ranging from 0 to L-1, the histogram is computed by counting the number of pixels at each intensity level. Histogram equalization applies a transformation that attempts to produce an image with a uniform histogram.

The transformation function is derived from the cumulative distribution function (CDF) of the original image intensities. If pk(rk) represents the probability of occurrence of intensity level rk, then the cumulative distribution function is given by sk = Σ(pi(ri)) for i = 0 to k. The equalized intensity value is then s k multiplied by (L-1) and rounded to the nearest integer.

This technique is particularly effective for improving the contrast of images that have been acquired under poor lighting conditions. However, it is important to note that histogram equalization may sometimes produce undesirable effects in images with already high contrast or in images with specific color requirements.

### Neighborhood Processing and Spatial Filtering

Neighborhood processing considers a group of pixels surrounding each target pixel. The most common neighborhood is a square region centered on the pixel being processed. The size of the neighborhood (for example, 3x3, 5x5) determines the extent of influence from surrounding pixels.

**Spatial Filtering** applies a convolution operation where a kernel (or mask) is moved across the entire image. For each pixel position, the corresponding neighborhood pixels are multiplied by the kernel coefficients and summed to produce the output value. The kernel is typically an odd-sized square matrix.

**Smoothing Filters** are used to blur images or reduce noise. The most common smoothing filter is the averaging filter (mean filter), which replaces each pixel with the average value of pixels in its neighborhood. A 3x3 averaging filter has all coefficients equal to 1/9. Another important smoothing filter is the median filter, which replaces each pixel with the median value of neighboring pixels. Median filtering is particularly effective for removing salt-and-pepper noise while preserving edges.

**Sharpening Filters** highlight transitions in intensity and enhance edges. The Laplacian filter is a second-order derivative operator defined as ∇²f = ∂²f/∂x² + ∂²f/∂y². For a 3x3 neighborhood, the Laplacian can be implemented using the kernel [0 -1 0; -1 4 -1; 0 -1 0] for the four-connected version or the eight-connected version with diagonal coefficients. The unsharp masking technique involves subtracting a blurred version of the image from the original to enhance edges.

### Image Restoration

Image restoration aims to reconstruct or recover an image that has been degraded by known factors such as motion blur, noise, or sensor imperfections. Unlike enhancement, which is subjective, restoration is based on a degradation model.

The degradation process is typically modeled as g(x,y) = H[f(x,y)] + η(x,y), where g is the degraded image, f is the original image, H is a degradation function, and η represents additive noise. In many cases, H is modeled as a convolution operation, making the degradation process equivalent to g = h * f + η, where h is the point spread function (PSF).

**Noise Models** commonly encountered include Gaussian noise (normal distribution), Rayleigh noise, Erlang (Gamma) noise, Exponential noise, and Salt-and-Pepper noise. Each noise type requires different filtering approaches for effective removal.

**Mean Filters** for noise reduction include the arithmetic mean filter (simple average), geometric mean filter (product of neighborhood values raised to power 1/n), and harmonic mean filter. The contraharmonic mean filter is particularly useful for eliminating salt noise (when Q > 0) or pepper noise (when Q < 0).

### Morphological Image Processing

Morphological operations are based on set theory and are used for extracting image components useful in shape representation and boundary extraction. These operations are particularly important for binary images but can be extended to grayscale images.

**Basic Operations** include:

- **Dilation**: Expands the boundaries of image regions. For binary images, it adds pixels to the boundaries of foreground objects. The structuring element determines the nature and extent of expansion.

- **Erosion**: Shrinks the boundaries of image regions by removing pixels from object boundaries. It eliminates small protrusions and fills small holes.

- **Opening**: Erosion followed by dilation with the same structuring element. It removes small objects and smooths contours while preserving larger shapes.

- **Closing**: Dilation followed by erosion with the same structuring element. It fills small holes and connects nearby objects.

**Applications** of morphological operations include boundary extraction (original minus eroded image), hole filling, extraction of connected components, and morphological skeletonization.

## Examples

### Example 1: Applying Histogram Equalization

Consider a 4x4 grayscale image with the following intensity values:

```
[100, 120, 130, 140]
[110, 125, 135, 145]
[105, 115, 130, 150]
[95,  110, 125, 140]
```

**Step 1**: Count occurrences of each intensity level. Let us assume the unique values and their frequencies are: 95(1), 100(1), 105(1), 110(2), 115(1), 120(1), 125(2), 130(2), 135(1), 140(2), 145(1), 150(1).

**Step 2**: Calculate probability of each level (frequency/total pixels = frequency/16).

**Step 3**: Calculate cumulative probability distribution.

**Step 4**: Apply transformation s = (L-1) × cumulative probability, where L = 256 for 8-bit images.

The result will be a more uniformly distributed histogram, enhancing the contrast of the original image. This method automatically adapts to the input image's histogram distribution.

### Example 2: Applying 3x3 Average Filter

Given a 5x5 image with noise:
```
[10, 12, 15, 12, 10]
[11, 100, 14, 13, 11]
[13, 15, 16, 15, 13]
[12, 14, 15, 100, 12]
[10, 12, 14, 12, 10]
```

For the pixel at position (2,2) with value 100 (center of noise), the 3x3 neighborhood is:
```
[100, 14, 13]
[15,  16, 15]
[14,  15, 100]
```

**Step 1**: Sum all 9 values: 100+14+13+15+16+15+14+15+100 = 302

**Step 2**: Divide by 9: 302/9 = 33.56 ≈ 34

The filtered value at this position becomes 34, significantly reducing the impact of the noisy pixel. Applying this operation to all pixels will smooth the entire image.

### Example 3: Morphological Dilation

Consider a binary image where 1 represents foreground (white) and 0 represents background (black):

```
[0, 0, 0, 0, 0]
[0, 1, 1, 0, 0]
[0, 1, 1, 0, 0]
[0, 0, 0, 0, 0]
```

Using a 3x3 structuring element with all 1s:

**Result**: The foreground region expands by one pixel in all directions:

```
[0, 1, 1, 1, 0]
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 0]
[0, 1, 1, 0, 0]
```

This demonstrates how dilation adds pixels to object boundaries based on the structuring element shape.

## Exam Tips

1. **Understand the difference between image enhancement and restoration**: Enhancement is subjective and aims to improve visual quality, while restoration is objective and tries to recover the original image from a degraded version based on a degradation model.

2. **Remember coordinate system conventions**: In digital image processing, the origin is at the top-left corner with y increasing downward. This is opposite to the standard Cartesian coordinate system used in mathematics.

3. **Know when to use mean vs median filters**: Use arithmetic mean filters for Gaussian noise but expect some blurring. Use median filters for salt-and-pepper noise as they preserve edges better while removing impulse noise.

4. **Master histogram concepts**: Histogram provides the probability distribution of intensity levels. Remember that histogram equalization may not always produce perfect results and can sometimes amplify noise.

5. **Understand morphological operations sequence**: Opening (erosion then dilation) removes small objects while preserving larger shapes. Closing (dilation then erosion) fills small holes and connects nearby objects. Know the order and effects clearly.

6. **Gamma correction is crucial**: Remember that γ < 1 expands dark regions (brightens dark areas), while γ > 1 expands bright regions. Display monitors typically have gamma values around 2.2.

7. **Structuring element matters in morphology**: The size and shape of the structuring element directly affect the output of morphological operations. Larger structuring elements produce more pronounced effects.

8. **Point processing vs neighborhood processing**: Point processing operations like negation or gamma correction consider only the individual pixel value. Neighborhood processing (convolution) considers surrounding pixels to compute the output value.

9. **Be familiar with noise types**: Gaussian noise has a normal distribution, salt-and-pepper noise appears as isolated black and white pixels, and each requires different filtering approaches for effective removal.

10. **Practice numerical problems**: DU examinations often include numerical problems on histogram computation, convolution operations, and morphological operations. Work through multiple examples to develop speed and accuracy.