# Boundary Preprocessing (Boundary Following & Chain Codes)

## **Definition and Importance**

- Boundary preprocessing is a technique used in computer vision to analyze and enhance the boundaries of an image.
- It is widely used in various applications, such as object recognition, image segmentation, and feature extraction.

## **Boundary Following**

- **Algorithm:**
  - Start at a pixel on the image boundary.
  - Follow the boundary by moving to adjacent pixels in the same row or column.
  - Continue until the boundary is complete.
- **Advantages:**
  - Simple to implement.
  - Fast processing time.
- **Disadvantages:**
  - May not capture complex boundaries.

## **Chain Codes**

- **Definition:** A chain code is a numerical representation of the direction and order in which pixels follow a boundary.
- **Formula:** The chain code for each pixel is calculated by:
  - Calculating the difference in x-coordinates (dx) and y-coordinates (dy) between the current pixel and the previous pixel.
  - Assigning a chain code (CC) based on the direction of the difference:
    - Top-left (CC = 0)
    - Top-right (CC = 1)
    - Bottom-right (CC = 2)
    - Bottom-left (CC = 3)
  - Repeating the process for each pixel on the boundary.

## **Theorems and Formulas**

- **Thomson Chain Code Theorem:** A chain code can be used to reconstruct the original boundary from a binary image.
- **Chain Code Formula:** The chain code for each pixel can be calculated using the following formula:
  CC = (dx \* dy) / (dx^2 + dy^2)

## **Key Points**

- **Boundary following** is a simple but limited technique for analyzing boundaries.
- **Chain codes** provide a more efficient and accurate representation of boundaries.
- **Thomson Chain Code Theorem** shows that chain codes can be used to reconstruct the original boundary from a binary image.
