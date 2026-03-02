# **Image Segmentation: Fundamentals, Point, Line and Edge Detection, Thresholding**

## **I. Fundamentals**

- Image segmentation is the process of dividing an image into its constituent parts or regions of interest.
- Goal: to group pixels with similar properties or features into meaningful segments.
- Techniques: edge detection, thresholding, region-based segmentation.

## **II. Point, Line, and Edge Detection**

- **Point Detection:**
  - Classic methods: corner detection (e.g., Harris corner detector)
  - Theoretically optimal: features with high gradient magnitude and direction.
- **Line Detection:**
  - Hough Transform: detects lines by fitting equations of lines to pixel data.
  - Theorem: `Local maxima` in gradient magnitude indicate line segments.
- **Edge Detection:**
  - Sobel Operator: detects edge orientation using gradient calculations.
  - Prewitt Operator: detects edge orientation using gradient calculations.
  - Theorem: `Gradient magnitude` of a pixel is proportional to the edge magnitude.

## **III. Thresholding**

- **Basic Global Thresholding:**
  - Converts an image to binary by applying a fixed threshold value.
  - Theorem: `Thresholding value` is typically chosen as 2/3 or 3/2 of the maximum intensity value.
- Formula:
  - `I(x, y) = 0` if `I(x, y) > T`, otherwise `I(x, y) = 255`
  - Where `T` is the threshold value.

## **IV. Segmentation by Region G**

- Region Growing (RG) algorithm:
  - Selects pixels with high similarity to the seed pixel.
  - Expands the region by selecting neighboring pixels until termination condition is met.
  - Theorem: `Local minima` in similarity measure indicate region boundaries.

## **Key Formulas and Definitions:**

- Gradient magnitude: `∂I/∂x` or `∂I/∂y`
- Gradient direction: `tan(θ) = ∂I/∂x / ∂I/∂y`
- Sobel Operator: `Sobel = [1 0 -1; 2 -1 -2; 1 0 -1]`
- Prewitt Operator: `Prewitt = [[-1 0 1; -1 0 1; -1 0 1]]`
- Threshold value: `T = 2/3 * max(I)` or `T = 3/2 * max(I)`
- Region Growing: `σ(x, y) = similarity(x, y, seed)`
