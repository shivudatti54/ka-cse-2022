# Morphological Image Processing: Preliminaries, Erosion and Dilation, Opening and Closing

### Definitions

- **Morphology**: A set of operations that preserve the structural properties of images.
- **Erosion**: A morphological operation that removes small objects from an image.
- **Dilation**: A morphological operation that adds small objects to an image.
- **Opening**: A morphological operation that combines erosion and dilation.
- **Closing**: A morphological operation that combines dilation and erosion.

### Important Formulas and Theorems

- **Erosion Formula**: `Eroden(image, structuringElement) = \{y \in Z^+ : \exists x \in Z^+ (x \leq y, \forall i, \forall j, \text{if } \text{image}(x,i) \wedge \text{image}(x,j) \wedge \text{structuringElement}(i,j) \text{ then } \text{image}(y,i) \wedge \text{image}(y,j) \wedge \text{dist}(x,y) \leq 1)\}`
- **Dilation Formula**: `Dilated(image, structuringElement) = \{y \in Z^+ : \exists x \in Z^+ (x \leq y, \forall i, \forall j, \text{if } \text{image}(x,i) \wedge \text{image}(x,j) \wedge \text{structuringElement}(i,j) \text{ then } \text{image}(y,i) \wedge \text{image}(y,j) \wedge \text{dist}(x,y) \geq 1)\}`
- **Opening Formula**: `Opening(image, structuringElement) = Eroden(Dilated(image, structuringElement))`
- **Closing Formula**: `Closing(image, structuringElement) = Dilated(Eroden(image, structuringElement))`

### Key Points

- **Prewitt Operators**: Used to compute the gradient of an image.
- **Sobel Operators**: Used to compute the gradient of an image.
- **Structuring Elements**: Used to define the shape of morphological operations.
- **Morphological Gradient**: A measure of the rate of change of an image.
- **Hit-or-Miss Transform**: A morphological operation used to detect features.
