# **Morphological Image Processing: Chap -9 (9.1-9.5)**

### Key Concepts

- **Morphological Operations**
  - Erosion: Removal of small objects or noise from an image
  - Dilation: Addition of small objects or noise to an image
- **Opening and Closing**
  - Opening: Combination of Erosion and Dilation
  - Closing: Combination of Dilation and Erosion
- **Hit-or-Miss Transform**
  - A morphological operation that performs a specific task based on a template
- **Morphological Gradient**
  - A measure of the rate of change of the image intensity

### Important Formulas and Definitions

- **Erosion Formula**: `Erode(I, B) = min(I \& B)`
- **Dilation Formula**: `Dilate(I, B) = max(I \& B)`
- **Opening Formula**: `Opening(I, B) = Erode(Dilate(I, B), B)`
- **Closing Formula**: `Closing(I, B) = Dilate(Erode(I, B), B)`
- **Hit-or-Miss Transform Formula**: `HIT(I, B) = (I \& B) \& (1 - (I \& B))`
- **Morphological Gradient Formula**: `Morphological Gradient = (Dilate(I, B) - Erode(I, B))`

### Theorems

- **Minkowski's Law**: The sum of the morphological gradients of two images is equivalent to the morphological gradient of their sum.
- **Minkowski's Law for Hit-or-Miss Transform**: The sum of the hit-or-miss transforms of two images is equivalent to the hit-or-miss transform of their sum.

### Important Theorems in Morphology

- **Axiom of Connectedness**: If an object is connected, then its closure is also connected.
- **Axiom of Connectedness for Erosion**: If an object is connected, then its erosion is also connected.

### Important Results in Morphology

- **Hausdorff Distance**: A measure of the difference between two sets.
- **Minkowski Distance**: A measure of the difference between two sets based on their shape.
