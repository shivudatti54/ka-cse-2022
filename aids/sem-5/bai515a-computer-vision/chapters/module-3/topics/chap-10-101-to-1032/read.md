# Chap-10: Image Restoration and Reconstruction

## 10.1: Introduction to Image Degradation

### Definition

Image degradation refers to the loss of image quality due to various factors such as noise, blur, distortions, and other types of degradations.

### Causes of Image Degradation

- Noise: Random fluctuations in the intensity values of pixels.
- Blur: Loss of sharpness due to motion or other factors.
- Distortions: Changes in the shape or position of objects.
- Compression: Loss of image detail due to reduction in spatial resolution.
- Atmospheric effects: Scattering of light and absorption by the atmosphere.

### Effects of Image Degradation

- Loss of detail and texture.
- Decreased contrast and brightness.
- Changes in color and saturation.
- Decreased sharpness and clarity.

## 10.2: Image Restoration Techniques

### 10.2.1: Filtering Techniques

Filtering techniques are used to remove noise and improve image quality.

- **Median Filter**: Replaces each pixel value with the median value of neighboring pixels.
- **Gaussian Filter**: Replaces each pixel value with the weighted average of neighboring pixels.
- **Bilateral Filter**: Replaces each pixel value with the weighted average of neighboring pixels based on the similarity of neighboring pixels.

### 10.2.2: Deblurring Techniques

Deblurring techniques are used to restore images that are blurred due to motion or other factors.

- **Wiener Filter**: Uses the frequency-domain representation of the image to remove blur.
- **Lucas-Kanade Method**: Uses the gradient of the image to estimate the motion of objects.
- **Non-Linear Deblurring**: Uses non-linear techniques such as total variation minimization to remove blur.

## 10.3: Image Reconstruction Techniques

### 10.3.1: Super-Resolution Techniques

Super-resolution techniques are used to improve the resolution of images.

- **Spatial Domain Methods**: Use techniques such as interpolation and upsampling to increase resolution.
- **Frequency Domain Methods**: Use techniques such as spectral amplification and filtering to increase resolution.

### 10.3.2: 3D Reconstruction Techniques

3D reconstruction techniques are used to create 3D models from 2D images.

- **Structure from Motion (SfM)**: Estimates the 3D structure of objects from motion parallax.
- **Stereo Matching**: Estimates the 3D structure of objects from stereo disparity.
- **Light Field Capture**: Estimates the 3D structure of objects from light field measurements.
