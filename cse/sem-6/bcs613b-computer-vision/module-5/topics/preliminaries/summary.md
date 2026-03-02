# Preliminaries of Morphological Image Processing - Summary

## Key Definitions

- **Mathematical Morphology**: A theory for analysis and processing of geometrical structures based on set theory and lattice theory.

- **Structuring Element**: A small binary matrix that defines the neighborhood shape and size for morphological operations.

- **Translation (A)ₜ**: Shifting all points in set A by vector t = {c | c = a + t, for a ∈ A}.

- **Reflection B̂**: Mirroring set B about the origin = {w | w = -b, for b ∈ B}.

- **Binary Image Set**: Representation where foreground pixels are elements of set A and background pixels are not in A.

## Important Formulas

- **Complement**: Aᶜ = {w | w ∉ A}

- **Union**: A ∪ B = {w | w ∈ A or w ∈ B or both}

- **Intersection**: A ∩ B = {w | w ∈ A and w ∈ B}

- **Difference**: A - B = A ∩ Bᶜ = {w | w ∈ A and w ∉ B}

- **Translation**: (A)ₜ = {c | c = a + t, for a ∈ A}

- **Reflection**: B̂ = {w | w = -b, for b ∈ B}

## Key Points

1. Mathematical morphology provides a framework for analyzing image structure through set operations.

2. Binary images are represented as sets where foreground = elements in set, background = elements not in set.

3. The structuring element defines the neighborhood pattern and acts as a "probe" over the image.

4. Translation shifts entire image sets while reflection creates mirrored versions of structuring elements.

5. The origin of the structuring element determines the anchor point for morphological operations.

6. Common structuring element shapes include square, cross, diamond, and circle (approximated).

7. Erosion and dilation are fundamental operations built upon these preliminary concepts.

8. The choice of structuring element shape and size significantly affects morphological operation results.

## Common Mistakes

1. **Confusing translation with reflection**: Translation adds a vector (A + t), reflection negates coordinates (-b).

2. **Forgetting the origin**: Always identify where the origin of the structuring element is located (usually center).

3. **Ignoring empty set handling**: Failing to consider how the empty set behaves in union/intersection operations.

4. **Wrong complement direction**: Remember that complement creates the "opposite" set of all points not in the original.

5. **Assuming symmetric results**: Non-symmetric structuring elements produce different results from their reflections.