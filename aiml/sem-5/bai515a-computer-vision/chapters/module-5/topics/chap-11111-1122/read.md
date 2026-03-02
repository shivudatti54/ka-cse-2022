# Chap-11: Morphological Image Processing: Preliminaries, Erosion and Dilation, Opening and Closing

## 11.1 Preliminaries

Morphological image processing is a technique used to process images using mathematical operations that mimic the way the human eye and brain process visual information. This chapter provides the fundamental concepts and operations used in morphological image processing.

### Definition:

Morphological image processing is a non-parametric, non-linear technique that uses mathematical operations to analyze and process images.

### Key Concepts:

- **Morphological operators**: Mathematical operations that analyze and modify images using geometric shapes (e.g., dilations, erosions, openings, and closings).
- **Image features**: Characteristics of an image that can be extracted and analyzed using morphological operations (e.g., shape, size, and orientation).

## 11.2 Erosion and Dilation

Erosion and dilation are two fundamental morphological operations used to process images.

### Erosion:

Erosion is a morphological operation that removes pixels from an image based on the size and shape of a structuring element.

**Definition:** Erosion is the removal of pixels from an image based on the size and shape of a structuring element.

**Mathematical Representation:** Erosion is defined as:

I_e = B \* f(B \* I)

where:

- I_e is the eroded image
- B is the structuring element
- f is the erosion function
- I is the original image

**Example:**

Suppose we have an image of a mountain range and a structuring element that represents a small circle. The erosion operation will remove small areas of the mountain range, creating a smoother image.

### Dilation:

Dilation is a morphological operation that adds pixels to an image based on the size and shape of a structuring element.

**Definition:** Dilation is the addition of pixels to an image based on the size and shape of a structuring element.

**Mathematical Representation:** Dilation is defined as:

I_d = B \* f(B \* I)

where:

- I_d is the dilated image
- B is the structuring element
- f is the dilation function
- I is the original image

**Example:**

Suppose we have an image of a city street and a structuring element that represents a small square. The dilation operation will add small areas to the city street, creating a larger image.

## 11.2.2 Opening and Closing

Opening and closing are two morphological operations used to process images.

### Opening:

Opening is a morphological operation that combines erosion and dilation to remove small objects from an image.

**Definition:** Opening is the combination of erosion and dilation to remove small objects from an image.

**Mathematical Representation:** Opening is defined as:

I_o = (I_d \* B) \* f((I_d \* B) \* I)

where:

- I_o is the opened image
- B is the structuring element
- f is the opening function
- I_d is the dilated image
- I is the original image

### Closing:

Closing is a morphological operation that combines dilation and erosion to fill small holes in an image.

**Definition:** Closing is the combination of dilation and erosion to fill small holes in an image.

**Mathematical Representation:** Closing is defined as:

I_c = (I_e \* B) \* f((I_e \* B) \* I)

where:

- I_c is the closed image
- B is the structuring element
- f is the closing function
- I_e is the eroded image
- I is the original image

**Examples:**

- Opening can be used to remove small objects from an image, such as removing dust or debris from a surface.
- Closing can be used to fill small holes in an image, such as filling in gaps in a road surface.
