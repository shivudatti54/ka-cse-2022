# Preliminaries - Morphological Image Processing

## Overview

Morphological image processing preliminaries establish fundamental set theory concepts, binary image representation, structuring element definitions, and basic operations that form the foundation for morphological techniques. Understanding these basics is essential for applying morphological algorithms.

## Key Points

- **Set Representation**: Binary images as sets of foreground pixel coordinates
- **Reflection**: B^ = {-b | b ∈ B}, mirrors SE about origin
- **Translation**: (B)z = {b+z | b ∈ B}, shifts SE by vector z
- **Structuring Element**: Small binary template defining neighborhood shape and operation character
- **Logical Operations**: Union (∪), intersection (∩), complement (^c) on pixel sets
- **Foreground and Background**: Conventionally white (1) = foreground, black (0) = background

## Important Concepts

- Morphological operations fundamentally based on set theory
- SE defines which neighbors participate in operation
- Reflection important for dilation definition
- Translation positions SE at different image locations

## Notes

- Binary image A as set of (x,y) coordinates where pixel = 1
- Reflection B^ mirrors SE: if (1,2) ∈ B, then (-1,-2) ∈ B^
- Translation (B)z moves SE origin to location z
- Standard SEs: 3×3 square, cross (4-connected), disk, line
