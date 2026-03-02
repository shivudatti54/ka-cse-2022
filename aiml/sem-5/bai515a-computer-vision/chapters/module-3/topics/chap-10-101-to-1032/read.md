# **Chap-10: Image Restoration and Reconstruction**

## **10.1: Introduction to Image Degradation**

### Definition

Image degradation refers to the process by which an image undergoes a change in its quality, often due to various factors such as noise, blur, or degradation of the image itself.

### Types of Image Degradation

- **Noise**: Random fluctuations in the pixel values, which can be caused by various factors such as thermal noise, shot noise, or quantization noise.
- **Blur**: A loss of sharpness in an image, which can be caused by camera shake, atmospheric effects, or optical aberrations.
- **Compression**: A loss of data due to the use of compression algorithms, which can lead to a decrease in image quality.

### Effects of Image Degradation

- **Artifacts**: Distortions in the image, such as ringing, aliasing, or ghosting.
- **Loss of details**: The degradation of fine details in the image.
- **Reduced contrast**: A decrease in the contrast between different regions of the image.

## **10.2: Mathematical Model of Image Degradation**

### Linear Model of Image Degradation

The linear model of image degradation is a mathematical model that describes the degradation of an image as a linear transformation of the original image.

**Linear Model Equation**

Image degraded = Image original \* H + Noise

where:

- Image degraded: The degraded image.
- Image original: The original image.
- H: The degradation matrix.
- Noise: The noise added to the image.

### Non-Linear Model of Image Degradation

The non-linear model of image degradation is a mathematical model that describes the degradation of an image as a non-linear transformation of the original image.

**Non-Linear Model Equation**

Image degraded = Image original \* f(H) + Noise

where:

- Image degraded: The degraded image.
- Image original: The original image.
- H: The degradation matrix.
- f(H): A non-linear function of the degradation matrix.
- Noise: The noise added to the image.

## **10.3: Image Restoration Techniques**

### 10.3.1: Filter-Based Restoration Techniques

Filter-based restoration techniques use filters to remove noise and blur from an image.

- **Savitzky-Golay Filter**: A low-pass filter that removes high-frequency components from an image.
- **Wiener Filter**: A linear filter that removes noise from an image by minimizing the mean squared error.

### 10.3.2: Model-Based Restoration Techniques

Model-based restoration techniques use mathematical models to describe the degradation of an image and then use these models to restore the image.

- **Maximum likelihood estimation**: A method that estimates the degradation matrix by maximizing the likelihood of the observed image.
- **Least squares estimation**: A method that estimates the degradation matrix by minimizing the difference between the observed image and the restored image.

### Key Concepts

- **Noise**: Random fluctuations in the pixel values.
- **Blur**: A loss of sharpness in an image.
- **Degradation matrix**: A matrix that describes the degradation of an image.
- **Filter-based restoration**: Techniques that use filters to remove noise and blur from an image.
- **Model-based restoration**: Techniques that use mathematical models to describe the degradation of an image and then use these models to restore the image.

### Example

Suppose we have an image that has been degraded by a linear degradation matrix H and added to with noise. We can use the linear model of image degradation to restore the image by solving the following equation:

Image original = (H^(-1) \* Image degraded - H^(-1) \* Noise) \* H

where H^(-1) is the inverse of the degradation matrix H.

### Code

```python
import numpy as np

# Define the degradation matrix H
H = np.array([[0.5, 0.1], [0.1, 0.5]])

# Define the degraded image
Image degraded = np.array([[1, 2], [3, 4]])

# Define the noise
Noise = np.array([[0.1, 0.1], [0.1, 0.1]])

# Calculate the inverse of the degradation matrix H
H_inv = np.linalg.inv(H)

# Calculate the restored image
Image original = (H_inv @ Image degraded - H_inv @ Noise) @ H

print(Image original)
```

This code calculates the inverse of the degradation matrix H and then uses this inverse to restore the image by solving the linear model of image degradation equation.
