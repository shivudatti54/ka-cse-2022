# Patterns and Classes - Summary

## Definitions

- **Pattern**: A specific spatial arrangement of foreground pixels characterized by geometric and topological properties including size, shape, orientation, and connectivity.

- **Class**: A collection of image pixels sharing common morphological properties; enables categorization of objects within images.

- **Structuring Element**: A predefined binary image used as a probe in morphological operations; determines which patterns can be detected.

- **Hit-or-Miss Transform**: Pattern detection operation $I \otimes S = (I \ominus S_{fg}) \cap (I^c \ominus S_{bg})$ that matches both foreground and background configurations.

## Theorems

- **Hit-or-Miss Detection Theorem**: The transform detects locations where the structuring element's foreground matches the image foreground and background matches the image background.

- **Connected Component Partitioning**: The set of all foreground pixels can be partitioned into disjoint connected components where each pixel belongs to exactly one component.

- **Duality Theorem**: $(I \ominus S)^c = I^c \oplus \hat{S}$ — erosion and dilation are dual with respect to image complement.

- **Idempotence Theorem**: Opening and closing are idempotent: $(I \circ S) \circ S = I \circ S$ and $(I \bullet S) \bullet S = I \bullet S$.

## Formulas

- **Dilation**: $I \oplus S = \{z : \exists s \in S, i \in I \text{ such that } z = i + s\}$

- **Erosion**: $I \ominus S = \{z : \forall s \in S, z + s \in I\}$

- **Opening**: $I \circ S = (I \ominus S) \oplus S$

- **Closing**: $I \bullet S = (I \oplus S) \ominus S$

- **Boundary**: $\partial O = O \setminus (O \ominus S)$

- **Euler Number**: $E = \text{components} - \text{holes}$

## Key Concepts

- **4-Connectivity**: Adjacent pixels sharing edge boundaries (north, south, east, west)

- **8-Connectivity**: All 4-connectivity neighbors plus diagonal neighbors

- **Structuring Element**: Determines detection sensitivity and operation behavior

- **Morphological Operations**: Transform patterns by expanding (dilation), shrinking (erosion), removing small details (opening), or filling holes (closing)