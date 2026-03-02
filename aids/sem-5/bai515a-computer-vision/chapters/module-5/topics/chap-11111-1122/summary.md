# **Chap-11(11.1-11.2.2) Revision Notes**

## **Definitions**

- **Morphological Image Processing**: A technique used to analyze and manipulate images based on the shape and structure of objects within them.
- **Erosion**: A morphological operation that reduces the size of objects in an image by removing pixels from their boundaries.
- **Dilation**: A morphological operation that increases the size of objects in an image by adding pixels to their boundaries.
- **Opening**: A morphological operation that combines erosion and dilation to remove small objects and details from an image.
- **Closing**: A morphological operation that combines dilation and erosion to remove large objects and details from an image.

## **Theorems and Formulas**

- **Minkowski's Algorithm**: A mathematical formula for calculating the erosion and dilation of an image.
- **Hit-or-Miss Transformation**: A transformation that uses an image and a binary mask to extract specific features from the image.

## **Key Concepts**

- **Morphological operators**: Erosion, dilation, opening, and closing.
- **Binary masks**: Used to extract specific features from an image.
- **Hit-or-Miss transformation**: A transformation that uses an image and a binary mask to extract specific features from the image.
- **Image filtering**: A technique used to modify an image by applying a filter to it.

## **Important Formulas**

- **Erosion**: `Ero(i, j) = min(Ero(e(i, j), e(i+1, j)), Ero(e(i, j), e(i, j+1)))`
- **Dilation**: `Dia(i, j) = max(Dia(d(i, j), d(i+1, j)), Dia(d(i, j), d(i, j+1)))`
- **Opening**: `Op(i, j) = Op(Ero(i, j), Dia(i, j))`
- **Closing**: `Cl(i, j) = Cl(Dia(i, j), Ero(i, j))`

## **Key Points for Revision**

- Understand the definitions of erosion, dilation, opening, and closing.
- Familiarize yourself with Minkowski's Algorithm and the Hit-or-Miss transformation.
- Know how to apply morphological operators to images.
- Understand the importance of binary masks in morphological image processing.
