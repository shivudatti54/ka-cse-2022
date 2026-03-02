# **Textbook-2: Chap -9 (9.1-9.5) - Morphological Image Processing: Preliminaries, Erosion and Dilation, Opening and Closing, Hit-or-Miss Operation**

## **Key Points**

- **Preliminaries**
  - Morphological operations are image processing techniques that operate on the structural features of an image.
  - Used for noise removal, edge detection, and shape analysis.
- **Erosion and Dilation**
  - **Erosion**: Removal of noise and small objects from an image.
    - Formula: Erosion = Bounding Box Minus Neighborhood
    - Theorem: Erosion is not commutative (order of operations affects result)
  - **Dilation**: Expansion of objects in an image.
    - Formula: Dilation = Neighborhood Minus Bounding Box
    - Theorem: Dilation is commutative (order of operations does not affect result)
- **Opening and Closing**
  - **Opening**: Combination of erosion and dilation.
    - Formula: Opening = Erosion + Dilation
  - **Closing**: Combination of dilation and erosion.
    - Formula: Closing = Dilation + Erosion
- **Hit-or-Miss Operation**
  - Adds or removes pixels based on a given shape.
  * Formula: Hit-or-Miss Operation = Neighborhood (A \* B)
  * Theorem: Hit-or-Miss Operation is commutative (order of operations does not affect result)

## **Important Formulas and Definitions**

- **Neighborhood**: A set of pixels around a given pixel.
- **Bounding Box**: The smallest rectangle that encloses a set of pixels.
- **Hit-or-Miss Operation**: Adds or removes pixels based on a given shape.

## **Theorems**

- Erosion is not commutative.
- Dilation is commutative.
- Opening and closing are associative and commutative.

## **Revision Tips**

- Understand the difference between erosion and dilation.
- Learn the formulas and theorems for each operation.
- Practice applying the operations to different images.
