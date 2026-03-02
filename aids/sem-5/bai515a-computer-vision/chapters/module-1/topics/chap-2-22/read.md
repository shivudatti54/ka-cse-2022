# Chap-2 (2.2) Image Formation

=====================================================

## Introduction

---

In computer vision, image formation is the process of generating an image from an object or scene. It involves the conversion of light into electrical signals, which are then processed to produce a digital image. In this chapter, we will explore the basics of image formation, including the relationship between light, cameras, and sensors.

### Key Concepts

- **Photometric Image**: A photometric image is a digital representation of the amount of light that falls on a given area of the image.
- **Sensor**: A sensor is an electronic device that converts light into electrical signals.
- **Camera**: A camera is an optical device that captures images using a sensor or film.

## Light and Image Formation

---

Light is the primary source of information for image formation. When light falls on an object, it interacts with the object's surface, resulting in a change in the light's intensity. This change in intensity is captured by the camera's sensor, which converts it into an electrical signal.

### Types of Light

- **Visible Light**: Visible light is the range of light that is visible to the human eye, typically between 400-700 nanometers.
- **Near-Infrared (NIR) Light**: NIR light is a range of light that is not visible to the human eye, typically between 700-1400 nanometers.
- **Far-Infrared (FIR) Light**: FIR light is a range of light that is not visible to the human eye, typically between 1400-3000 nanometers.

### Camera Types

- **CCD (Charge-Coupled Device) Camera**: A CCD camera uses a sensor to capture images.
- **CMOS (Complementary Metal-Oxide-Semiconductor) Camera**: A CMOS camera uses a sensor to capture images.

## Sensor and Camera Principles

---

### Sensor Principles

- **Photodiode**: A photodiode is a type of sensor that converts light into electrical signals.
- **Image Sensor**: An image sensor is a type of sensor that captures images using a photodiode or a complementary photodiode.

### Camera Principles

- **Lens**: A lens is an optical device that focuses light onto a sensor.
- **Aperture**: An aperture is an optical device that controls the amount of light that enters the camera.
- **Shutter**: A shutter is an optical device that controls the duration of light exposure.

### Image Formation Process

1.  **Light Incident**: Light falls on an object, interacting with its surface and resulting in a change in light intensity.
2.  **Lens Focus**: The light is focused onto a sensor using a lens.
3.  **Aperture Control**: The amount of light that enters the camera is controlled by the aperture.
4.  **Shutter Exposure**: The duration of light exposure is controlled by the shutter.
5.  **Sensor Capture**: The sensor captures the electrical signals from the light.
6.  **Digital Image Formation**: The electrical signals are processed and stored as a digital image.

### Example

Suppose we have a camera with a CCD sensor and a 50mm lens. The camera is set to capture an image of a sunny day at 12 pm. The lens focuses the light onto the sensor, and the aperture is set to allow 10% of the available light to enter. The shutter is set to capture the image for 1/1000th of a second. The sensor captures the electrical signals from the light, which are then processed and stored as a digital image.

### Code Example

```python
import numpy as np

# Define the sensor size
sensor_size = 640x480

# Define the lens focal length
focal_length = 50

# Define the aperture
aperture = 0.1

# Define the shutter exposure
shutter_exposure = 1/1000

# Define the light intensity
light_intensity = 1000

# Calculate the image formation parameters
sensor_pixel_size = sensor_size / focal_length
aperture_area = np.pi * (aperture / 2) ** 2
shutter_area = shutter_exposure * sensor_pixel_size

# Print the image formation parameters
print("Sensor Pixel Size:", sensor_pixel_size)
print("Aperture Area:", aperture_area)
print("Shutter Area:", shutter_area)
```

This code example demonstrates how to calculate the image formation parameters for a camera with a CCD sensor and a 50mm lens. The parameters include the sensor pixel size, aperture area, and shutter area.
