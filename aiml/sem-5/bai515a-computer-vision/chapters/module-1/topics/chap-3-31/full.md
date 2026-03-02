# Chap-3 (3.1) Image Formation: Photometric Image

=====================================================

## 3.1 Introduction

---

In the context of computer vision, an image is a representation of the visual information captured by a camera or other image sensor. The formation of an image is a critical step in the image processing pipeline, as it sets the stage for subsequent image analysis and processing tasks. In this chapter, we will delve into the process of image formation, focusing specifically on photometric images.

## 3.1.1 Historical Context

---

The concept of image formation dates back to the early days of photography. In 1826, Joseph Nicephore Niepce invented the first permanent photograph, capturing a view from his window using a camera obscura. This early technology laid the foundation for modern imaging systems.

In the 20th century, the development of digital imaging revolutionized the field. With the advent of charge-coupled devices (CCDs) and complementary metal-oxide-semiconductor (CMOS) sensors, imaging systems became more efficient, sensitive, and affordable.

## 3.1.2 Image Formation Process

---

The process of image formation involves several stages:

1.  **Light collection**: Light from the scene is collected by the imaging system, which can be a camera lens, a photodiode, or a phototransistor.
2.  **Optical processing**: The light is focused onto a sensor or a detector, where it is converted into an electrical signal.
3.  **Signal processing**: The electrical signal is processed to enhance the image quality, remove noise, and correct for distortions.
4.  **Image formation**: The processed signal is used to form the final image, which can be displayed on a screen, stored on a medium, or used for further processing.

## 3.1.3 Photometric Image Formation

---

A photometric image is a representation of the light intensity or luminance at each point in the image. It is measured in units of power per unit area, such as watts per square meter (W/m²) or candelas per square meter (cd/m²).

The formation of a photometric image involves the following steps:

1.  **Light collection**: Light from the scene is collected by the imaging system.
2.  **Sensor response**: The light is focused onto a sensor, which converts the light into an electrical signal proportional to the light intensity.
3.  **Signal processing**: The electrical signal is processed to enhance the image quality, remove noise, and correct for distortions.
4.  **Image formation**: The processed signal is used to form the final photometric image.

## 3.1.4 Image Formation Equations

---

The formation of an image can be described using several equations:

1.  **Lens equation**: 1/f = 1/do + 1/di, where f is the focal length, do is the object distance, and di is the image distance.
2.  **Sensor response equation**: V = k \* L, where V is the sensor response, k is a constant, and L is the light intensity.
3.  **Image formation equation**: I(x, y) = (1/f) \* L(x, y), where I(x, y) is the image intensity at point (x, y), and L(x, y) is the light intensity at the same point.

## 3.1.5 Applications

---

Photometric images have numerous applications in computer vision, including:

1.  **Image analysis**: Photometric images can be used to analyze the scene, including object recognition, tracking, and segmentation.
2.  **Image processing**: Photometric images can be processed to enhance the image quality, remove noise, and correct for distortions.
3.  **Machine learning**: Photometric images can be used as input data for machine learning algorithms, including classification, regression, and clustering.

## 3.1.6 Case Study

---

Consider a camera that captures a photograph of a scene with a resolution of 1024x768 pixels. The camera has a focal length of 50mm and is positioned 1 meter away from the scene. The light intensity at each point in the image is measured in units of watts per square meter (W/m²).

Using the lens equation, we can calculate the focal length of the camera:

1/f = 1/do + 1/di
1/f = 1/1 + 1/0.48
f ≈ 50mm

Using the sensor response equation, we can calculate the sensor response:

V = k \* L
V = 1024 \* 768 \* 0.1
V ≈ 844,416

The final photometric image is formed using the image formation equation:

I(x, y) = (1/f) \* L(x, y)
I(x, y) = (1/50) \* L(x, y)

## 3.1.7 Further Reading

---

For further reading on the topic of image formation, we recommend the following resources:

1.  **"Computer Vision: Algorithms and Applications"** by Richard Szeliski
2.  **"Image Formation and Image Analysis"** by Hans J. A. Schmitz
3.  **"Photometric Imaging"** by the Society for Optical Engineering (SPIE)

## 3.1.8 Code Snippet

---

Here is a Python code snippet that demonstrates the formation of a photometric image:

```python
import numpy as np

# Define the camera parameters
focal_length = 50  # mm
sensor_resolution = 1024
sensor_distance = 1  # meter

# Calculate the sensor response
sensor_response = np.zeros(sensor_resolution)
for i in range(sensor_resolution):
    for j in range(sensor_resolution):
        sensor_response[i, j] = (1 / focal_length) * (i / sensor_distance + j / sensor_distance)

# Define the light intensity
light_intensity = np.random.rand(sensor_resolution, sensor_resolution)

# Calculate the photometric image
photometric_image = np.dot(sensor_response, light_intensity)

print(photometric_image)
```

This code snippet demonstrates the formation of a photometric image using the sensor response equation and the image formation equation.
