# Morphological Image Processing: Chap-11(11.1-11.2.2)

### Definitions and Notations

- **Morphological Image Processing**: A technique for image processing that uses mathematical operations to transform images based on the shape and structure of objects in the image.
- **Morphological Operators**: Mathematical operators that manipulate images to achieve specific effects, such as erosion, dilation, opening, and closing.
- **Set Operations**:
  - **Union (A ∪ B)**: The set of elements that are in A, in B, or in both.
  - **Intersection (A ∩ B)**: The set of elements that are in both A and B.
  - **Difference (A - B)**: The set of elements that are in A but not in B.

### Erosion and Dilation

- **Erosion (Erosion)**:
  - Definition: A morphological operation that removes small objects from an image.
  - Formula: Erosion of a binary image I by a structuring element B is defined as:

```r
Erosion(I, B) = B ⊗ I = {x | ∃y ∈ I. (x - y) ∈ B}
```

- **Dilation (Dilation)**:
  - Definition: A morphological operation that adds small objects to an image.
  - Formula: Dilation of a binary image I by a structuring element B is defined as:

```r
Dilation(I, B) = B ⊗ I = {x | ∃y ∈ I. (x + y) ∈ B}
```

- **Opening**:
  - Definition: The combination of erosion and dilation.
  - Formula: Opening of a binary image I by a structuring element B is defined as:

```r
Opening(I, B) = Erosion(Dilation(I, B), B)
```

- **Closing**:
  - Definition: The combination of dilation and erosion.
  - Formula: Closing of a binary image I by a structuring element B is defined as:

```r
Closing(I, B) = Dilation(Erosion(I, B), B)
```

### Important Formulas and Theorems

- **Minkowski's Algorithm**: A method for calculating the opening and closing of a binary image using iterated erosions and dilations.
- **Minkowski's Identity**: A theorem that states that the opening of an image by a structuring element B can be calculated using iterated erosions and dilations:

```r
Opening(I, B) = (I ⊕ B) ⊗ B
```

### Key Points

- Erosion removes small objects from an image.
- Dilation adds small objects to an image.
- Opening and closing are combinations of erosion and dilation.
- Minkowski's Algorithm and theorem can be used to calculate opening and closing.
