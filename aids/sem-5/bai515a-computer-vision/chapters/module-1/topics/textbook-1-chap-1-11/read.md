# Computer Vision Study Material: Chap-1 (1.1)

=============================================

## Table of Contents

---

1. [What is Computer Vision?](#what-is-computer-vision)
2. [A Brief History of Computer Vision](#a-brief-history-of-computer-vision)
3. [Image Formation: Photometric Image](#image-formation-photometric-image)

## What is Computer Vision?

---

### Definition

Computer vision is a field of artificial intelligence (AI) that enables systems to interpret and understand visual information from the world around us. It involves the interaction between computers and visual data, with the ultimate goal of extracting meaningful information from images and videos.

### Key Concepts

- **Computer vision**: The process of interpreting visual data to extract meaningful information.
- **Visual data**: Images, videos, and other visual inputs.
- **Computer vision pipeline**: The sequence of steps involved in processing visual data, including image formation, feature extraction, and object recognition.

## A Brief History of Computer Vision

---

### Early Beginnings

The concept of computer vision dates back to the 1950s and 1960s, when the first computer vision systems were developed. These early systems were primarily focused on tasks such as image processing and feature extraction.

### Breakthroughs and Advancements

In the 1970s and 1980s, computer vision experienced significant breakthroughs with the development of new algorithms and techniques. The introduction of the backpropagation algorithm in the 1980s enabled the training of neural networks for image recognition tasks.

### Modern Era

In the 1990s and 2000s, computer vision became a major area of research, with the development of new techniques such as object recognition, tracking, and segmentation. The availability of large datasets and the use of deep learning algorithms have further propelled the field forward.

### Key Milestones

- **1950s-1960s**: Early computer vision systems developed.
- **1970s-1980s**: Breakthroughs in image processing and feature extraction.
- **1990s-2000s**: Development of new techniques such as object recognition and tracking.

## Image Formation: Photometric Image

---

### Definition

A photometric image is a representation of the light reflected by an object, captured by a camera or sensor. It is a measure of the amount of light that is present in an image.

### Key Concepts

- **Intensity**: The amount of light that is present in an image.
- **Gray scale**: A representation of intensity using shades of gray.
- **Color**: A representation of light using colors.
- **Photometric image**: A representation of the light reflected by an object.

### Image Formation Process

1. **Light source**: Light is emitted by a light source, such as a lamp.
2. **Object**: The object reflects light, resulting in a photometric image.
3. **Camera**: The camera captures the photometric image.
4. **Sensor**: The sensor converts the light into an electrical signal.

### Example

Suppose we want to capture a photometric image of a person standing in a room. The light source is a lamp, and the person reflects light onto the camera. The camera captures the reflected light, resulting in a photometric image.

### Code

Below is an example code snippet in Python, using the OpenCV library to capture a photometric image:

```python
import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Capture a frame
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray)

# Wait for a key press
cv2.waitKey(0)

# Release the camera
cap.release()
```

This code captures a frame from the camera, converts it to grayscale, and displays the result. The resulting image is a photometric image, representing the intensity of the light reflected by the object.
