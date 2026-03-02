# Color Transformations

## Overview

Color transformations modify color images by converting between color spaces, adjusting individual channels, or applying functional mappings to color components. These operations enhance images, normalize illumination, or prepare data for specific analysis tasks.

## Key Points

- **Color Space Conversions**: RGB↔HSV, RGB↔YCbCr, RGB↔LAB enable processing in appropriate space for task
- **Channel Operations**: Independent processing of R, G, B or H, S, V channels for targeted adjustments
- **Color Balancing**: White balance, gray world assumption, histogram equalization per channel
- **Gamma Correction**: Nonlinear transformation I_out = I_in^γ compensating for display characteristics
- **Color Transfer**: Match color statistics of target image to reference image

## Important Concepts

- Processing in HSV often better than RGB for illumination-invariant operations
- Color constancy algorithms compensate for different illuminants to obtain invariant descriptors
- Histogram equalization in RGB versus HSV: RGB creates color shifts, HSV preserves hue
- Applications include white balance, color grading, illumination normalization, color-based tracking

## Notes

- Convert to appropriate color space before processing (e.g., HSV for hue-based segmentation)
- Per-channel histogram equalization in RGB can cause color shifts, better in HSV (equalize V only)
- Gamma correction: γ<1 brightens (expands dark values), γ>1 darkens (expands bright values)
- Color constancy important for robust color-based recognition under varying illumination
