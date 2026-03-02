# Opening and Closing

## Overview

Opening and closing are composite morphological operations combining erosion and dilation in specific sequences to smooth object boundaries, remove noise, fill gaps, and extract features while better preserving original object sizes compared to single erosion or dilation.

## Key Points

- **Opening**: A∘B = (A⊖B)⊕B, erosion followed by dilation, removes small objects and protrusions
- **Closing**: A•B = (A⊕B)⊖B, dilation followed by erosion, fills holes and gaps
- **Idempotency**: Opening/closing of already opened/closed image produces no further change
- **Opening Effects**: Smooths boundaries, breaks narrow connections, removes small islands
- **Closing Effects**: Smooths boundaries, fuses narrow breaks, fills small holes
- **Size Preservation**: Opening approximately preserves sizes better than erosion alone
- **Duality**: Opening of A = complement of closing of A^c

## Important Concepts

- Opening eliminates thin protrusions and small objects smaller than SE
- Closing bridges narrow gaps and fills holes smaller than SE
- Both are idempotent: (A∘B)∘B = A∘B and (A•B)•B = A•B
- Applications include noise removal, feature extraction, text processing, particle analysis

## Notes

- Opening ≤ original image ≤ closing (opening removes pixels, closing adds pixels)
- Opening good for removing salt noise, closing good for removing pepper noise
- SE shape determines what features removed/filled: disk for isotropic, line for directional
- Opening-closing or closing-opening sequences used for comprehensive noise removal
