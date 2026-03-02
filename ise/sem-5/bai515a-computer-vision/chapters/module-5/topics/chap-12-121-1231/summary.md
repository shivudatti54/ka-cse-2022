# **Chap-12 (12.1-12.3.1) Revision Notes**

## **Morphological Image Processing: Preliminaries**

- **Definition:** Morphological operations are image processing techniques that operate on the shape of objects in an image.
- **Types of Morphological Operations:**
  - Erosion
  - Dilation
  - Opening
  - Closing
  - Hit-or-Miss

## **Erosion (12.1)**

- **Definition:** Erosion is a morphological operation that reduces the size of an object in an image.
- **Formula:** $B = E(A, b)$, where B is the eroded image, A is the original image, and b is the structuring element.
- **Theorem:** The erosion of an object is the intersection of the object with its translation.

## **Dilation (12.2)**

- **Definition:** Dilation is a morphological operation that increases the size of an object in an image.
- **Formula:** $B = D(A, d)$, where B is the dilated image, A is the original image, and d is the structuring element.
- **Theorem:** The dilation of an object is the union of the object with its translation.

## **Opening (12.3)**

- **Definition:** Opening is a morphological operation that combines erosion and dilation.
- **Formula:** $B = O(A, o) = E(E(A, b), d)$, where B is the opened image, A is the original image, and o is the structuring element.
- **Theorem:** The opening of an object is the intersection of the object with its translation.

## **Closing (12.3.1)**

- **Definition:** Closing is a morphological operation that combines erosion and dilation.
- **Formula:** $B = C(A, c) = D(D(A, d), e)$, where B is the closed image, A is the original image, and c is the structuring element.
- **Theorem:** The closing of an object is the union of the object with its translation.
