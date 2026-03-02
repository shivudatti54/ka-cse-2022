# Image Segmentation: Fundamentals, Point, Line and Edge Detection, Thresholding, and Segmentation by Region

=====================================================

## Fundamentals

- **Image Segmentation**: Division of an image into smaller regions or objects of similar characteristics.
- **Image Representation**: Pixel values, Binary images, and Color images.

## Point Detection

- **Point Detection Algorithms**:
  - **Cornerness Detection**: Measures the "cornerness" of a pixel by using the Laplacian of the gradient magnitude.
  - **Zero-Crossing Detection**: Detects points where the gradient magnitude crosses zero.

## Line Detection

- **Line Detection Algorithms**:
  - **Hough Transform**: Detects lines by finding the points that satisfy the line equation.
  - **Sobel Operator**: Detects horizontal and vertical lines by calculating the gradient magnitude.

## Edge Detection

- **Edge Detection Algorithms**:
  - **Sobel Operator**: Detects edges by calculating the gradient magnitude in the horizontal and vertical directions.
  - **Canny Edge Detection**: A multi-step process that includes Gaussian filtering, non-maximum suppression, and double thresholding.

## Thresholding

- **Thresholding**:
  - **Binary Thresholding**: Converts an image into a binary image by setting pixels above a certain threshold to white and pixels below to black.
  - **Basic Global Thresholding**:
    - **Otsu's Thresholding**: Automatically determines the optimal threshold value.
    - **Fixed Thresholding**: Sets a fixed threshold value.

## Segmentation by Region

- **Segmentation by Region**:
  - **Connected Component Labeling**: Assigns a label to each connected region in the image.

### Important Formulas and Definitions

- **Gradient Magnitude**: √(I_x^2 + I_y^2), where I_x and I_y are the horizontal and vertical gradients.
- **Laplacian**: ∇^2f = ∂^2f/∂x^2 + ∂^2f/∂y^2, where f is the image intensity function.
- **Hough Space**: A 2D space used to store the parameterized equations of lines.

### Important Theorems

- **Linearity**: The linearity of the Sobel operator.
- **Optimality**: Otsu's thresholding is optimal in terms of minimizing the variance of the labeled regions.
