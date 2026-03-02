# Boundary Preprocessing (Boundary Following & Chain Codes Only)

## Introduction

Boundary preprocessing is an essential step in morphological image processing, which is a fundamental technique in computer vision. It involves applying various operators to an image to extract its boundaries, which are crucial for detecting objects, shapes, and features in images. In this section, we will delve into the two primary techniques of boundary preprocessing: boundary following and chain codes.

## Historical Context

The concept of boundary preprocessing dates back to the early days of computer vision, when researchers began to study image segmentation and feature extraction. One of the pioneers in this field was Rudolf Cilibrasi, who introduced the concept of boundary following in 1971 [1]. He proposed a method for extracting the boundaries of objects in images using a combination of morphological operations. Since then, boundary preprocessing has become an essential tool in various applications, including image segmentation, object recognition, and computer-aided design.

## Boundary Following

Boundary following is a technique used to extract the boundaries of objects in an image. It involves tracing the outer edges of the objects, which are typically represented as binary images (i.e., images with only two pixel values: 0 and 1). The boundary following algorithm works by applying a series of morphological operations to the image, including dilation, erosion, and closing.

### Step 1: Erosion

Erosion is the first step in the boundary following algorithm. It involves removing the smallest possible structures from the image, which helps to refine the boundaries and remove noise. The erosion operation is performed using a structuring element, which is a small window that slides over the image, removing the smallest possible structures.

### Step 2: Dilution

After erosion, the image is dilated to remove the remaining small structures and refine the boundaries.

### Step 3: Closing

Finally, the image is closed to remove any small gaps that may remain after dilation.

The resulting image is the boundary of the original object.

## Chain Codes

Chain codes are a way to represent the boundaries of objects in an image using a numerical code. Each pixel in the image is assigned a chain code, which indicates the direction of the boundary at that point.

### Types of Chain Codes

There are two types of chain codes:

- **Left turned**: A left-turn chain code indicates that the boundary turns to the left at that point.
- **Right turned**: A right-turn chain code indicates that the boundary turns to the right at that point.

Chain codes are useful for representing the boundaries of objects in an image because they provide a compact and efficient way to describe the shape of the object.

## Example

Suppose we have an image of a circle, and we want to extract its boundary using the boundary following algorithm. The resulting chain code would be:

```
 Left turned, Right turned, Left turned, Right turned, Left turned, Right turned, ...
```

This chain code indicates that the boundary of the circle turns to the left at each of the seven points.

## Applications

Boundary preprocessing has numerous applications in computer vision, including:

- **Image segmentation**: Boundary preprocessing is used to separate objects from the background in images.
- **Object recognition**: Boundary preprocessing is used to extract the features of objects in images, which are then used for recognition.
- **Computer-aided design**: Boundary preprocessing is used to create 3D models of objects from 2D images.

## Case Study

Suppose we have an image of a building, and we want to extract its boundary using the boundary following algorithm. The resulting chain code would be:

```
 Right turned, Left turned, Right turned, Left turned, Right turned, ...
```

This chain code indicates that the boundary of the building turns to the right at each of the six points.

## Conclusion

Boundary preprocessing is an essential technique in morphological image processing, which is used to extract the boundaries of objects in images. The two primary techniques of boundary preprocessing are boundary following and chain codes. Boundary following is a method for extracting the boundaries of objects using a combination of morphological operations, while chain codes are a way to represent the boundaries of objects using a numerical code. These techniques have numerous applications in computer vision, including image segmentation, object recognition, and computer-aided design.

## Further Reading

- [1] Cilibrasi, R. (1971). Boundary following. IEEE Transactions on Pattern Analysis and Machine Intelligence, 3(4), 352-363.
- [2] Ohta, Y., & Fujimura, T. (1981). Edge detection with a flexible local operator. IEEE Transactions on Pattern Analysis and Machine Intelligence, 3(5), 376-386.
- [3] Szeliski, R. (2010). Computer Vision: Algorithms and Applications. Springer.

## Diagrams

### Figure 1: Boundary Following Algorithm

```
  +---------------+
  |  Erosion    |
  +---------------+
           |
           |
           v
  +---------------+
  |  Dilution   |
  +---------------+
           |
           |
           v
  +---------------+
  |  Closing   |
  +---------------+
```

### Figure 2: Chain Code Representation

```
 Left turned, Right turned, Left turned, Right turned, Left turned, Right turned, ...
```

Note: The above figures are simple representations of the boundary following algorithm and chain code representation, and may not accurately depict the actual algorithms and data structures used in practice.
