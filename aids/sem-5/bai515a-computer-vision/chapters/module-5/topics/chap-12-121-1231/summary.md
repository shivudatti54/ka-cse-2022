# Morphological Image Processing: Preliminaries, Erosion and Dilation, Opening and Closing

### Definitions

- **Morphology**: A fundamental technique in image processing that operates on the shape and structure of images.
- **Erosion**: A morphological operation that removes small objects or noise from an image.
- **Dilation**: A morphological operation that adds small objects or noise to an image.
- **Opening**: A morphological operation that combines erosion and dilation to remove small objects and fill holes.
- **Closing**: A morphological operation that combines dilation and erosion to remove large objects and fill small holes.

### Formulas

- **Erosion**:
  - Erosion of a binary image `f` by a structuring element `E`:

```python
f_eroded = min(f, E)
```

- **Dilation**:
  - Dilation of a binary image `f` by a structuring element `E`:

```python
f_dilated = max(f, E)
```

- **Opening**:
  - Opening of a binary image `f` by a structuring element `E`:

```python
f_opened = f_dilated_eroded
```

- **Closing**:
  - Closing of a binary image `f` by a structuring element `E`:

```python
f_closed = f_eroded_dilated
```

### Theorems

- **Theorem 1**: The opening operation is equivalent to the following formula:

```python
f_opened = max(min(f, E), min(E, f))
```

- **Theorem 2**: The closing operation is equivalent to the following formula:

```python
f_closed = min(max(f, E), max(E, f))
```

### Key Points

- Morphological operations are used to process images by modifying their shapes and structures.
- Erosion removes small objects or noise from an image.
- Dilation adds small objects or noise to an image.
- Opening removes small objects and fills holes, while closing removes large objects and fills small holes.
- Theorems provide equivalent formulas for opening and closing operations.
