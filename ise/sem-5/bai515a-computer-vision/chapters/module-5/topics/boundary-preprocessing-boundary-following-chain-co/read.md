# **Boundary Preprocessing: Boundary Following and Chain Codes**

## **Introduction**

Boundary preprocessing is an important step in morphological image processing. It involves converting the input image into a more manageable form to facilitate subsequent operations. Two popular techniques used in boundary preprocessing are boundary following and chain codes.

## **Boundary Following**

### Definition

Boundary following is a technique used to extract the boundary of an object in an image. It involves tracing the outermost pixels of the object, which form the boundary.

### Algorithm

1. **Pixel Selection**: Select a pixel at the boundary of the object.
2. **Neighbor Selection**: Select the four neighboring pixels of the selected pixel (up, down, left, right).
3. **Boundary Tracing**: If any of the neighboring pixels are outside the object, add the selected pixel to the boundary list and move to the next neighboring pixel.
4. **Repeat**: Repeat steps 2-3 until no more pixels can be added to the boundary list.

### Example

Suppose we have an image of a circle with a radius of 10 pixels.

```
  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 0
0 5 5 5 5 5 0
0 5 5 5 5 0
0 5 5 5 0
0 5 5 0
0 5 0
0 0
```

The boundary following algorithm extracts the outermost pixels of the circle, which forms the boundary.

### Code

```python
import numpy as np

def boundary_following(image):
    boundary = []
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if image[i, j] == 255 and (image[i-1, j] == 0 or image[i+1, j] == 0 or image[i, j-1] == 0 or image[i, j+1] == 0):
                boundary.append((i, j))
    return boundary
```

## **Chain Codes**

### Definition

Chain codes are a way to represent the connectivity of pixels in an image. They are used to extract the boundary of an object in an image.

### Algorithm

1. **Pixel Selection**: Select a pixel at the boundary of the object.
2. **Neighbor Selection**: Select the four neighboring pixels of the selected pixel (up, down, left, right).
3. **Chain Code Calculation**: Assign a chain code to each neighboring pixel based on its direction (0-7).
4. **Repeat**: Repeat steps 2-3 until no more pixels can be added to the boundary list.

### Example

Suppose we have an image of a circle with a radius of 10 pixels.

```
  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 5 0
0 5 5 5 5 5 5 0
0 5 5 5 5 5 0
0 5 5 5 5 0
0 5 5 5 5 0
0 5 5 5 0
0 5 5 5 0
0 5 5 0
0 5 0
0 0
```

The chain code algorithm extracts the outermost pixels of the circle, which forms the boundary.

### Code

```python
import numpy as np

def chain_codes(image):
    boundary = []
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if image[i, j] == 255 and (image[i-1, j] == 0 or image[i+1, j] == 0 or image[i, j-1] == 0 or image[i, j+1] == 0):
                chain_code = np.zeros(8)
                if image[i+1, j] == 255:
                    chain_code[0] = 1
                if image[i-1, j] == 255:
                    chain_code[1] = 1
                if image[i, j+1] == 255:
                    chain_code[2] = 1
                if image[i, j-1] == 255:
                    chain_code[3] = 1
                if image[i+1, j+1] == 255:
                    chain_code[4] = 1
                if image[i+1, j-1] == 255:
                    chain_code[5] = 1
                if image[i-1, j+1] == 255:
                    chain_code[6] = 1
                if image[i-1, j-1] == 255:
                    chain_code[7] = 1
                boundary.append((i, j, chain_code))
    return boundary
```

## **Comparison of Boundary Following and Chain Codes**

|                              | Boundary Following         | Chain Codes                 |
| ---------------------------- | -------------------------- | --------------------------- |
| **Efficiency**               | Low                        | High                        |
| **Accuracy**                 | High                       | High                        |
| **Computational Complexity** | O(n^2)                     | O(n^2)                      |
| **Applicability**            | Suitable for simple shapes | Suitable for complex shapes |

In conclusion, boundary preprocessing is a crucial step in morphological image processing. Both boundary following and chain codes are effective techniques for extracting the boundary of an object in an image. However, the choice of technique depends on the complexity of the shape and the computational resources available.
