# **Morphological Image Processing: Preliminaries, Erosion and Dilation, Opening and Closing**

## **12.1 Introduction to Morphological Image Processing**

**Definition:** Morphological image processing is a technique used to analyze and process images by applying mathematical operations to the image. It is based on the idea of morphological transformations, which are defined by set operations.

**Key Concepts:**

- **Morphological transformations:** Mathematical operations that preserve the shape of objects in an image.
- **Binary images:** Images represented as binary arrays, where pixels are either black (0) or white (255).
- **Gray-scale images:** Images represented as arrays of gray-level intensities.

## **12.1.1 Erosion and Dilation**

**Erosion:**
Erosion is an operation that removes small objects or details from an image. It is defined as the intersection of the image with a structuring element.

- **Structuring element:** A small window that slides over the image, performing the morphological operation.
- **Erosion formula:**
  - `Erosion(I, S) = I \` S`

  where `I` is the image, `S` is the structuring element, and `\` denotes the set difference operation.

**Dilation:**
Dilation is an operation that adds small details or objects to an image. It is defined as the union of the image with a structuring element.

- **Structuring element:** A small window that slides over the image, performing the morphological operation.
- **Dilation formula:**
  - `Dilation(I, S) = I \cup S`

  where `I` is the image, `S` is the structuring element, and `\cup` denotes the set union operation.

## **12.1.2 Opening and Closing**

**Opening:**
Opening is a morphological operation that combines erosion and dilation. It is defined as the erosion of the dilation of the image.

- **Opening formula:**
  - `Opening(I, S) = Erosion(Dilation(I, S))`

**Closing:**
Closing is a morphological operation that combines dilation and erosion. It is defined as the dilation of the erosion of the image.

- **Closing formula:**
  - `Closing(I, S) = Dilation(Erosion(I, S))`

## **12.1.3 Hit-or-Miss Transformations**

**Hit-or-Miss Transformations:**
Hit-or-miss transformations are a type of morphological transformation that uses a structuring element to test for specific features in the image.

- **Hit-or-miss transformation formula:**
  - `Hit-or-Miss(I, S) = {x ∈ I | S ⊆ I(x)} or {x ∈ I | S ⊆ I(x)^c}``

  where `I` is the image, `S` is the structuring element, `I(x)` is the value of the image at pixel `x`, and `I(x)^c` is the complement of the image at pixel `x`.

**Example:**
Consider a binary image `I` and a structuring element `S`. The hit-or-miss transformation can be used to find the connected components of `I` that intersect with `S`.

- `Hit-or-Miss(I, S)` returns the set of pixels in `I` that intersect with `S`.

**Key Concepts:**

- **Connected components:** Subsets of pixels that are connected (i.e., have a path of adjacent pixels between any two pixels).
- **Set intersection:** The set of pixels that are common to two or more sets.
- **Set difference:** The set of pixels that are in one set but not in another set.
