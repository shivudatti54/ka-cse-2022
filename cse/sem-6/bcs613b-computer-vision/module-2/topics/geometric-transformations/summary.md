# Geometric Transformations

## Overview

Geometric transformations modify the spatial relationships between pixels in images, changing position, orientation, size, and shape. These transformations are fundamental for image registration, alignment, warping, and correcting geometric distortions from cameras and lenses.

## Key Points

- **Translation**: Shifts image by (tx, ty), x'=x+tx, y'=y+ty, preserves shape and size
- **Rotation**: Rotates by angle θ about origin, x'=xcosθ-ysinθ, y'=xsinθ+ycosθ
- **Scaling**: Resizes by factors (sx, sy), x'=sx×x, y'=sy×y, changes size but not position
- **Affine Transformation**: Combines translation, rotation, scaling, shearing, preserves parallel lines
- **Perspective Transformation**: Full 3D projection to 2D, allows arbitrary quadrilateral mapping
- **Interpolation Methods**: Nearest neighbor (fast, blocky), Bilinear (smooth, moderate speed), Bicubic (smoothest, slower)

## Important Concepts

- Forward mapping maps source to destination pixels, backward mapping maps destination to source (preferred)
- Homogeneous coordinates enable matrix representation of all transformations including translation
- Interpolation necessary because transformed coordinates often fall between pixel locations
- Applications include image registration, panorama stitching, lens distortion correction

## Notes

- Practice writing transformation matrices for common operations
- Understand why backward mapping preferred over forward mapping
- Know interpolation trade-offs: nearest (fast/blocky), bilinear (balanced), bicubic (slow/smooth)
- Affine preserves parallelism but not angles or lengths, perspective is most general
