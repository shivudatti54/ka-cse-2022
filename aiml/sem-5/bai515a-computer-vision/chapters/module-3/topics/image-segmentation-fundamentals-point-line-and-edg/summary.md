# **Image Segmentation Revision Notes**

## **Fundamentals**

- Image segmentation is the process of dividing an image into its constituent parts or objects.
- It involves identifying and isolating individual objects or features within an image.
- The goal is to create a binary mask or image where each pixel has a value of either 0 (background) or 255 (foreground).

## **Point Detection**

- Point detection is the process of identifying individual points or features within an image.
- Common techniques:
  - Corner detection (e.g. Harris Corner Detector)
  - Feature detection (e.g. SIFT, SURF)

## **Line and Edge Detection**

- Line and edge detection is the process of identifying lines or edges within an image.
- Common techniques:
  - Canny Edge Detection
  - Sobel Edge Detection
  - Line Detection (e.g. Hough Transform)

## **Thresholding**

- **Global Thresholding**:
  - Definition: assigning a value to each pixel based on its intensity value.
  - Formula: `I(x, y) = 0` if `I(x, y) < T`, `I(x, y) = 255` otherwise.
- **Important Theorem:** The Fundamental Theorem of Thresholding, which states that a binary image can be obtained by applying a threshold to an image.

## **Segmentation by Region G**

- Definition: dividing an image into connected regions or objects.
- Method:
  1.  Initialize a set of pixels with unknown or unvisited status.
  2.  Iterate through the image, marking each pixel as visited.
  3.  Assign a label to each connected region of pixels.

## **Important Formulas and Definitions**

- **Prewitt Operators**: used for edge detection.
- **Sobel Operators**: used for edge detection.
- **Hough Transform**: used for line detection.
- **Region Growing**: used for segmentation by region g.

## **Key Points**

- Image segmentation is a crucial step in image processing and analysis.
- Different techniques can be used depending on the specific application and image characteristics.
- Thresholding and segmentation by region g are commonly used techniques for image segmentation.
