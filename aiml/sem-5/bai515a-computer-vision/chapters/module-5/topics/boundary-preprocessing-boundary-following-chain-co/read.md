# Boundary Preprocessing (Boundary Following & Chain Codes)

### Introduction

Boundary preprocessing is an important step in morphological image processing. It involves transforming an image into a more suitable format for image analysis and feature extraction. In this section, we'll focus on boundary following and chain codes, which are two common techniques used for boundary preprocessing.

### Boundary Following

Boundary following is a method used to extract the boundary of an object from an image. It involves tracing the boundary of the object pixel by pixel, starting from a given point.

**How Boundary Following Works:**

1.  Choose a starting point on the boundary of the object.
2.  Mark the current pixel as visited.
3.  Explore all neighboring pixels that are not marked as visited.
4.  If a neighboring pixel is on the boundary, mark it as visited and add it to the boundary list.
5.  Repeat steps 3-4 until all neighboring pixels are marked as visited.
6.  Backtrack to the starting point and remove the starting pixel from the boundary list.

**Example:**

Suppose we have an image with an object (e.g., a circle) and we want to extract its boundary using boundary following.

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   |
| 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| 2   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| 3   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   |
| 4   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   |
| 5   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   |
| 6   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 1   |
| 7   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   |
| 8   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 1   |
| 9   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   |

The resulting boundary list would be:

[0, 1, 2, 3, 4, 5, 6, 7, 8]

### Chain Codes

Chain codes are a numerical representation of the boundary of an object. They are used to describe the direction and magnitude of the boundary at each point.

**How Chain Codes Work:**

1.  The chain code is represented as a sequence of numbers, where each number corresponds to a direction (0-7).
2.  The direction numbers are assigned based on the direction of the boundary at each point.
3.  The chain code is calculated by tracing the boundary of the object and assigning a direction number to each point.

**Example:**

Suppose we have an image with an object (e.g., a circle) and we want to calculate its chain code.

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   |
| 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| 2   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| 3   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   |
| 4   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   |
| 5   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   |
| 6   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 1   |
| 7   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   |
| 8   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 1   |
| 9   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0   |

The resulting chain code would be:

[0, 1, 2, 3, 4, 5, 6, 7, 8]

## Key Concepts

- **Boundary following:** A method used to extract the boundary of an object from an image by tracing the boundary pixel by pixel.
- **Chain codes:** A numerical representation of the boundary of an object, describing the direction and magnitude of the boundary at each point.
- **Direction numbers:** Assigned to each point on the boundary based on its direction.
- **Boundary preprocessing:** An important step in morphological image processing, transforming an image into a more suitable format for image analysis and feature extraction.
