# Image Processing - Summary

## Key Definitions and Concepts

- **Digital Image**: A 2D array of pixels, where each pixel contains intensity information. For grayscale images, values range from 0 (black) to 255 (8-bit). Color images use multiple channels like RGB.

- **Image Enhancement**: Improving image visual quality through techniques like point processing (negation, gamma correction) and spatial filtering (smoothing, sharpening).

- **Image Restoration**: Objective process of recovering an original image from a degraded version using a degradation model g(x,y) = H[f(x,y)] + η(x,y).

- **Histogram**: Graph showing the frequency distribution of intensity levels in an image. Histogram equalization spreads intensity values uniformly to enhance contrast.

- **Spatial Filtering**: Convolution operation using a kernel moved across the image. Smoothing filters (mean, median) reduce noise while sharpening filters (Laplacian) enhance edges.

- **Morphological Operations**: Set-theory based operations using structuring elements. Dilation expands boundaries, erosion shrinks them, opening removes small objects, closing fills small holes.

## Important Formulas and Theorems

- **Image Negative**: s = L - 1 - r (where L is maximum intensity level)

- **Log Transformation**: s = c log(1 + r) (compresses dynamic range)

- **Power Law (Gamma)**: s = cr^γ (γ < 1 expands dark regions, γ > 1 expands bright regions)

- **Laplacian**: ∇²f = ∂²f/∂x² + ∂²f/∂y² (second-order derivative for edge enhancement)

- **Degradation Model**: g(x,y) = h(x,y) * f(x,y) + η(x,y) (convolution with noise)

- **Arithmetic Mean Filter**: g(x,y) = (1/mn) Σ f(x,y) over neighborhood

## Key Points

- Digital image coordinates have origin at top-left with y increasing downward.
- Point processing operations consider only individual pixel values; neighborhood processing considers surrounding pixels.
- Median filter is preferred over mean filter for salt-and-pepper noise as it preserves edges.
- Histogram equalization automatically adjusts contrast but may amplify noise in already high-contrast images.
- Morphological opening (erosion-dilation) smooths contours and removes small objects while preserving larger shapes.
- Morphological closing (dilation-erosion) fills holes and connects nearby objects.
- The choice between enhancement and restoration depends on whether the degradation is known or unknown.
- Gamma correction is essential for display devices; typical monitor gamma is approximately 2.2.
- Structuring element size and shape directly influence morphological operation results.
- Noise type identification is crucial for selecting appropriate restoration filters.

## Common Mistakes to Avoid

1. Confusing image enhancement (subjective improvement) with restoration (objective recovery based on degradation model).

2. Forgetting that the coordinate system in image processing has y increasing downward, not upward as in standard mathematics.

3. Applying mean filters to images with salt-and-pepper noise, which spreads the noise rather than removing it effectively.

4. Using median filters for Gaussian noise when mean filters would be more appropriate.

5. Forgetting to normalize kernel values in spatial filtering (averaging filter coefficients should sum to 1).

6. Confusing the order of operations in morphological opening and closing.

7. Applying histogram equalization to already high-contrast images, which may produce undesirable artifacts.

## Revision Tips

1. Practice computing histograms and applying equalization transformations by hand for small images.

2. Memorize the kernel matrices for common filters (3x3 averaging, Laplacian, Sobel edge detection).

3. Create a comparison table of noise types and recommended filtering approaches.

4. Draw the effect of morphological operations on simple binary shapes to reinforce understanding.

5. Solve previous year DU question papers to understand the exam pattern and important topics.