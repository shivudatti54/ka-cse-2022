# Point Operators

## Overview

Point operators are fundamental image processing techniques transforming each pixel's intensity based solely on its original value, independent of neighbors or spatial location. These efficient O(n) operations form the basis for image enhancement, correction, and analysis tasks.

## Key Points

- **Image Negation**: s = L-1-r creates photographic negative, useful for enhancing detail in dark regions
- **Brightness Adjustment**: s = r + c adds constant to all pixels, requires clamping to valid range (0-255)
- **Contrast Adjustment**: s = α×r multiplies values (α>1 increases, α<1 decreases contrast)
- **Histogram Equalization**: Redistributes intensity values evenly using CDF: s = (L-1) × Σp(j) for improved contrast
- **Thresholding**: Converts grayscale to binary based on threshold T, fundamental for segmentation
- **Gamma Correction**: s = c×r^γ compensates for display nonlinearities (γ<1 brightens darks, γ>1 darkens)
- **Otsu's Method**: Automatically determines optimal threshold by maximizing between-class variance

## Important Concepts

- Output g(x,y) = T[f(x,y)] depends only on input at same location
- Histogram shows frequency distribution of intensity values, reveals image characteristics
- Histogram matching transforms image to match specified target histogram distribution
- Bit-plane slicing decomposes image into constituent bits revealing information hierarchy
- Lookup Tables (LUTs) precompute transformations for efficient implementation

## Notes

- Understand transformation functions for each operation and be able to apply them
- Practice reading histograms to determine appropriate enhancement operations
- Remember data type limitations and need for clamping/clipping values
- Be able to predict visual results of applying operations to different image types
- Know which operation suits specific tasks: thresholding for segmentation, equalization for contrast
- Point operations are highly efficient with O(n) complexity for n pixels
