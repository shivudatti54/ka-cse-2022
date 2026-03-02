# Erosion and Dilation

## Overview

Erosion and dilation are fundamental morphological operations that shrink or expand objects in binary images based on structuring element interactions. These dual operations form the basis for all other morphological techniques including opening, closing, and hit-or-miss transforms.

## Key Points

- **Erosion Definition**: A⊖B = {z | (B)z ⊆ A}, result pixel white only if SE fits entirely within object
- **Dilation Definition**: A⊕B = {z | (B^)z ∩ A ≠ ∅}, result pixel white if SE touches object
- **Erosion Effects**: Shrinks objects, removes small details, separates touching objects, smooths concave boundaries
- **Dilation Effects**: Expands objects, fills small holes, connects nearby objects, smooths convex boundaries
- **Duality**: Erosion of A equals complement of dilation of complement (A⊖B)^c = A^c⊕B^
- **Structuring Element**: Shape defines operation character (3×3 square, cross, disk most common)

## Important Concepts

- Erosion removes pixels from object boundaries where SE doesn't fit
- Dilation adds pixels to boundaries where SE overlaps object
- Multiple erosions/dilations compound effect: n erosions = erosion with n-fold enlarged SE
- Grayscale erosion/dilation: minimum/maximum of SE-covered pixels

## Notes

- Erosion: place SE center at each pixel, if SE entirely in foreground → output 1, else 0
- Dilation: place SE center at each pixel, if SE overlaps any foreground → output 1
- SE size critical: larger SE = more aggressive erosion/dilation
- Common SE shapes: square (isotropic), cross (4-connected), line (directional)
