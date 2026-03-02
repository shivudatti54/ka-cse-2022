# **Chap-2 (2.2) Image Formation: Photometric Image**

## **Introduction**

In the field of Computer Vision, image formation is a crucial step in capturing and processing visual information. In this chapter, we will delve into the concept of photometric image formation, which is the process of converting light into electrical signals that can be processed by a computer.

## **What is Photometric Image Formation?**

Photometric image formation refers to the process of converting light into electrical signals that can be measured and processed by a computer. This process involves the conversion of light waves into voltage signals, which can then be processed and analyzed by a computer.

## **Key Components of Photometric Image Formation**

- **Sensor**: The sensor is the device that converts light into electrical signals. Common types of sensors used in image formation include Charge-Coupled Devices (CCDs) and Complementary Metal-Oxide-Semiconductor (CMOS) image sensors.
- **Optics**: The optics refer to the lenses, mirrors, and other optical components that focus and direct light onto the sensor.
- **Image Formation Process**: The image formation process involves the conversion of light into electrical signals, which is done by the sensor.

## **Types of Photometric Images**

- **Analog Image**: An analog image is a continuous signal that represents the intensity of light at each point in the image.
- **Digital Image**: A digital image is a discrete signal that represents the intensity of light at each point in the image.

## **Key Concepts**

- **Resolution**: The resolution of an image refers to the amount of detail that can be captured by the sensor.
- **Dynamic Range**: The dynamic range of an image refers to the range of light intensities that can be captured by the sensor.
- **Signal-to-Noise Ratio (SNR)**: The SNR of an image refers to the ratio of the signal strength to the noise strength.

## **Example**

A camera captures an image of a scene, which is then converted into an electrical signal by the sensor. The electrical signal is then processed and analyzed by a computer, which uses the signal to reconstruct the original image.

## **Code Example**

Here is an example of how an image can be captured and processed using Python and OpenCV:

```python
import cv2

# Capture an image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

This code captures an image, converts it to grayscale, and displays the resulting image using OpenCV.
