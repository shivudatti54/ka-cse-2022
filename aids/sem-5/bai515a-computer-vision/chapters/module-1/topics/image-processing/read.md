# Image Processing

## Introduction

Image processing is a fundamental discipline within computer science that deals with the manipulation, analysis, and enhancement of digital images to extract useful information, improve visual quality, or prepare images for further analysis. In the context of computer vision, image processing serves as the critical preprocessing stage that transforms raw image data into a format suitable for higher-level interpretation by vision algorithms. The importance of image processing cannot be overstated in today's technology-driven world, where applications range from medical imaging and satellite remote sensing to smartphone photography and autonomous vehicle navigation.

The history of digital image processing traces back to the 1960s when computers first became powerful enough to handle two-dimensional data. Early applications focused on enhancing images from space missions and medical scans. Today, with the explosion of digital imagery through social media, surveillance systems, and IoT devices, image processing has become an essential skill for computer scientists. For students at the University of Delhi, understanding image processing provides the foundation for advanced topics in computer vision, machine learning, and artificial intelligence.

## Key Concepts

### What is Image Processing?

Image processing refers to the use of algorithms and mathematical operations to perform transformations on digital images. These transformations can be categorized into three main types: image enhancement, image restoration, and image analysis. Image enhancement aims to improve the subjective quality of an image for human viewing, making it more visually appealing or easier to interpret. Image restoration involves removing degradations such as noise, blur, or geometric distortions to recover the original scene. Image analysis extracts quantitative information from images, enabling automated interpretation and decision-making.

### Image Representation

A digital image is represented as a two-dimensional array of pixels (picture elements). For grayscale images, each pixel contains a single intensity value typically ranging from 0 (black) to 255 (white), requiring 8 bits or one byte of storage per pixel. Color images are commonly represented using multiple channels, with the RGB (Red, Green, Blue) model being the most prevalent. In the RGB model, each pixel contains three values representing the intensity of red, green, and blue light, requiring 24 bits or three bytes per pixel. Alternative color spaces such as HSV (Hue, Saturation, Value) and LAB are often used in specific applications because they separate color information from intensity, making certain processing tasks more intuitive.

### Types of Image Processing Operations

Image processing operations are broadly classified into point operations and neighborhood operations. Point operations transform each pixel independently based solely on its own value, without considering neighboring pixels. Examples include brightness adjustment, contrast enhancement, and histogram equalization. These operations are computationally efficient and can be expressed as simple mathematical functions applied to the pixel intensity value.

Neighborhood operations, also known as spatial operations, consider the surrounding pixels when processing each pixel. These operations use kernels or convolution masks that define the neighborhood size and weighting scheme. Common neighborhood operations include smoothing (blur), sharpening, edge detection, and morphological operations. The convolution operation is fundamental to neighborhood processing, where the kernel slides across the entire image, and at each position, the output pixel value is computed as a weighted sum of the input pixels in the neighborhood.

### Image Enhancement Techniques

Image enhancement encompasses various techniques to improve image quality. Histogram equalization is a powerful point operation that redistributes pixel intensities to utilize the full available dynamic range, thereby enhancing contrast. For color images, histogram equalization can be applied to the intensity channel while preserving color information. Adaptive histogram equalization further improves results by computing histograms for small regions of the image, providing better local contrast enhancement.

Spatial filtering uses convolution kernels to achieve different effects. The averaging or mean filter smooths images by replacing each pixel with the average of its neighbors, effectively reducing noise but causing blurring. The Gaussian filter applies a weighted average where pixels closer to the center have higher weights, providing smoother results while preserving edges better than the uniform average. Unsharp masking enhances image sharpness by subtracting a blurred version of the image from the original, effectively boosting high-frequency components.

### Image Restoration

Image restoration aims to reverse degradations that occurred during image acquisition or transmission. Common degradations include motion blur, defocus blur, and noise addition. Geometric operations such as rotation, scaling, and cropping fall under image restoration when used to correct perspective distortions or alignment issues. Deconvolution techniques attempt to reverse the effects of blur by modeling the degradation process and inverting it, though these methods are sensitive to noise and require accurate knowledge of the blur kernel.

### Sampling and Quantization

The process of converting a continuous scene into a digital image involves two fundamental steps: sampling and quantization. Sampling determines the spatial resolution by discretizing the continuous image into a grid of pixels. Higher sampling rates produce images with more pixels and finer detail. Quantization determines the intensity resolution by discretizing the continuous range of brightness values into discrete levels. Standard grayscale images use 8-bit quantization, providing 256 possible intensity levels. Color images typically use 8 bits per channel, resulting in over 16 million possible color combinations.

### Color Image Processing

Processing color images requires understanding color spaces and their properties. The RGB color space is intuitive for display purposes but has limitations when it comes to color-based analysis because the three channels are highly correlated. The HSV color space separates hue (the color type), saturation (the color purity), and value (the brightness), making it easier to perform operations like isolating objects based on color. The LAB color space is designed to be perceptually uniform, meaning that equal changes in values correspond to equal perceptual differences, which is valuable for color-based measurements and matching.

## Examples

### Example 1: Brightness and Contrast Adjustment

Consider a grayscale image represented by intensity function I(x,y). To adjust brightness by adding a constant value b to every pixel, the operation is expressed as O(x,y) = I(x,y) + b. If b is positive, the image becomes brighter; if negative, it becomes darker. To adjust contrast by scaling pixel values around the mean, the operation is O(x,y) = a × (I(x,y) - μ) + μ, where μ is the mean intensity and a is the scaling factor. If a > 1, contrast increases; if 0 < a < 1, contrast decreases.

For an image with pixel values [50, 100, 150, 200], adding 30 to each pixel results in [80, 130, 180, 230], which must be clamped to the valid range [0, 255], giving [80, 130, 180, 230]. For contrast enhancement with a = 1.5 and mean μ = 125: the first pixel becomes 1.5 × (50 - 125) + 125 = 1.5 × (-75) + 125 = -112.5 + 125 = 12.5, approximately 13.

### Example 2: Convolution with a Smoothing Kernel

Apply a 3×3 averaging kernel to a small image patch:

Original 3×3 patch:
```
[10 20 30]
[15 25 35]
[20 30 40]
```

Averaging kernel (all ones divided by 9):
```
[1/9 1/9 1/9]
[1/9 1/9 1/9]
[1/9 1/9 1/9]
```

Convolution result at center pixel: (10+20+30+15+25+35+20+30+40)/9 = 245/9 = 27.22

Similarly, applying a horizontal Sobel edge detection kernel [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] to the same patch: (-1×10 + 0×20 + 1×30) + (-2×15 + 0×25 + 2×35) + (-1×20 + 0×30 + 1×40) = (-10 + 30) + (-30 + 70) + (-20 + 40) = 20 + 40 + 20 = 80, indicating a strong horizontal edge.

### Example 3: Histogram Equalization

Given a 4×4 image with pixel values:
```
[100, 150, 50, 200]
[80, 120, 60, 180]
[90, 130, 70, 190]
[110, 140, 55, 170]
```

Counting frequencies: value 50 appears once, 55 once, 60 once, 70 once, 80 once, 90 once, 100 once, 110 once, 120 once, 130 twice, 140 once, 150 once, 170 once, 180 once, 190 once, 200 once. Cumulative distribution: compute cumulative counts and map to new values in the range [0, 255] using the formula: new_value = floor((cdf(current) - cdf_min) × (L-1) / (N - cdf_min)), where L is 256 and N is 16 pixels.

## Exam Tips

1. UNDERSTAND THE FUNDAMENTAL DIFFERENCE between point operations and neighborhood operations, as this distinction frequently appears in examination questions requiring analysis of computational complexity and effects.

2. MEMORIZE THE CONVOLUTION OPERATION formula: output pixel is the sum of element-wise multiplication of the kernel with the corresponding image neighborhood. Know how boundary conditions (zero padding, replication, reflection) affect the output size.

3. FOR EDGE DETECTION QUESTIONS, remember that Sobel operators compute gradients in horizontal and vertical directions, and the gradient magnitude is calculated using the square root of sum of squares or absolute sum approximation.

4. KNOW THE PROPERTIES OF THE GAUSSIAN KERNEL: it is radially symmetric, separable (can be applied as two one-dimensional convolutions), and approximates the ideal low-pass filter in frequency domain.

5. WHEN ANSWERING QUESTIONS ABOUT COLOR SPACES, explain why HSV is preferred for color-based segmentation while RGB is used for display purposes.

6. UNDERSTAND SAMPLING AND QUANTIZATION effects on image quality: undersampling causes aliasing, and low quantization leads to posterization or banding artifacts.

7. PRACTICE COMPUTING HISTOGRAM EQUALIZATION manually by following the step-by-step procedure: compute histogram, compute cumulative distribution function, apply transformation formula.

8. FOR APPLICATION-BASED QUESTIONS, relate image processing techniques to real-world scenarios like medical imaging (enhancement for diagnosis), satellite imagery (atmospheric correction), and photography (noise reduction, sharpening).