# Color Image Smoothing and Sharpening

## Overview

Smoothing and sharpening operations enhance color images by reducing noise or emphasizing details while preserving color fidelity. Techniques must consider inter-channel relationships to avoid color artifacts and maintain natural appearance.

## Key Points

- **Component-wise Smoothing**: Apply smoothing filters (Gaussian, median) independently to R, G, B channels
- **Vector Smoothing**: Vector median filter, bilateral filter considering color similarity
- **Component-wise Sharpening**: Laplacian or unsharp masking per channel, may create color shifts
- **Vector Sharpening**: Enhance edges using color gradient magnitude, preserve chromatic information
- **Bilateral Filter**: Edge-preserving smoothing using spatial and range (color) weights
- **Color Artifacts**: Independent channel processing can create false colors at edges

## Important Concepts

- Vector median filter better than component median for preserving color relationships
- Bilateral filter weights pixels by both spatial proximity and color similarity
- Sharpening in HSV (enhance V, preserve H and S) avoids color shifts from RGB sharpening
- Applications include photo enhancement, noise reduction, detail enhancement in color images

## Notes

- Component-wise operations simple but may introduce color artifacts at boundaries
- Vector median: find color pixel minimizing sum of color distances to neighborhood
- Bilateral filter: w = exp(-d²spatial/2σs²) × exp(-d²intensity/2σr²)
- For sharpening without color shift: convert to HSV, sharpen V channel only, convert back to RGB
