# Chap-3 (3.1) Image Formation

=====================================================

## 3.1 Photometric Image

---

In computer vision, an image is represented as a collection of pixel values that correspond to the amount of light that enters the camera. This type of image is known as a photometric image.

### Definition

A photometric image is a 2D array of pixel values that represent the amount of light that enters a camera. Each pixel value is typically represented as a color value, which can be specified in various color models such as RGB, YUV, or CMYK.

### Characteristics

- Each pixel value represents the amount of light that enters the camera at that specific location.
- Photometric images are used to represent images that are captured using a camera, where the amount of light is the primary factor in determining the color and intensity of the image.
- Photometric images are typically represented in a digital format, where each pixel value is a numerical representation of the amount of light that enters the camera.

### Example

Consider a camera that captures an image of a sunset. The photometric image of the sunset would represent the amount of light that enters the camera at each pixel location. The pixel values would be higher for the parts of the image that receive more light (i.e., the sun) and lower for the parts that receive less light (i.e., the shadows).

### Key Concepts

- **Pixel value**: The amount of light that enters the camera at a specific location.
- **Color model**: A system for representing color values in a digital image.
- **Photometric image**: A 2D array of pixel values that represent the amount of light that enters a camera.
- **Digital image**: An image that is represented in a digital format.

### Image Formation Process

The formation of a photometric image occurs through the following steps:

1.  **Light absorption**: Light enters the camera and is absorbed by the camera's sensor.
2.  **Conversion to electrical signal**: The absorbed light is converted into an electrical signal by the camera's sensor.
3.  **A/D conversion**: The electrical signal is converted into a digital signal by the camera's analog-to-digital converter.
4.  **Pixel value assignment**: The digital signal is assigned to a specific pixel location in the image.
5.  **Image formation**: The photometric image is formed by combining the pixel values from each pixel location.

### Applications of Photometric Image

Photometric images have a wide range of applications in computer vision, including:

- **Image processing**: Photometric images are used in image processing techniques such as filtering, thresholding, and feature extraction.
- **Computer vision**: Photometric images are used in computer vision applications such as object recognition, scene understanding, and tracking.
- **Medical imaging**: Photometric images are used in medical imaging applications such as medical imaging, radiation therapy, and medical diagnosis.

### Key Formulas

- **Intensity**: I = P / A, where I is the intensity, P is the power of the light source, and A is the area of the sensor.
- **Pixel value**: P = I \* t, where P is the pixel value, I is the intensity, and t is the time the light is absorbed.

### Key Terms

- **Radiance**: The amount of light that enters a camera per unit solid angle.
- **Luminance**: The amount of light that enters a camera per unit area.
- **Color temperature**: The color of light that is emitted by a light source.

By understanding the concepts of photometric images, you can better appreciate the importance of image formation in computer vision and develop a deeper understanding of the techniques and applications used in this field.
