# Morphological Image Processing

## Overview

Morphological operations process images based on shape using structuring elements, fundamental for binary image analysis and applicable to grayscale. Core operations erosion and dilation combine to create opening, closing, and advanced morphological algorithms for shape analysis and feature extraction.

## Key Points

- **Structuring Element (SE)**: Small binary template defining neighborhood shape (common: 3×3 square, cross, disk)
- **Erosion**: Shrinks objects, removes small details, A⊖B = {z | (B)z ⊆ A}
- **Dilation**: Expands objects, fills holes, A⊕B = {z | (B^)z ∩ A ≠ ∅}
- **Opening**: Erosion followed by dilation, A∘B = (A⊖B)⊕B, removes small objects, smooths boundaries
- **Closing**: Dilation followed by erosion, A•B = (A⊕B)⊖B, fills holes, connects nearby objects
- **Hit-or-Miss Transform**: Shape detection by matching foreground and background patterns
- **Morphological Gradient**: Dilation minus erosion highlights object boundaries

## Important Concepts

- Erosion and dilation are dual operations: erosion of A = complement of dilation of A^c
- Opening removes protrusions, closing fills intrusions, both are idempotent
- SE shape and size critical: larger SE removes larger features
- Applications include noise removal, boundary extraction, skeleton extraction, shape analysis

## Notes

- Erosion: SE must fit entirely inside object at that position
- Dilation: SE touches object at that position
- Opening ≤ original ≤ closing (opening removes pixels, closing adds pixels)
- Morphological operations on grayscale use flat or non-flat structuring elements
