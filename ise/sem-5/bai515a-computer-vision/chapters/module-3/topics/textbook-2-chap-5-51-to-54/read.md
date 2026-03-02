# **Textbook-2: Chap-5 (5.1 to 5.4) - Image Restoration and Reconstruction**

### 5.1: Introduction to Image Degradation

---

Image degradation refers to the process of corrupting or altering an image, resulting in a degraded or distorted representation of the original image.

**Definition:** Image degradation is a process that alters the original image in a way that makes it difficult or impossible to recover the original image.

**Types of Image Degradation:**

- **Noise:** Random fluctuations in the image that can be caused by various factors such as electromagnetic interference, thermal noise, or human error.
- **Blurring:** The spreading of image details due to various factors such as camera shake, atmospheric distortion, or sensor degradation.
- **Obliteration:** The loss of important details in the image due to excessive exposure or camera malfunction.
- **Compression:** The reduction of image data to reduce file size, which can result in loss of image details.

### 5.2: Mathematical Model of Image Degradation

---

The degradation of an image can be modeled using the following equations:

**Noise Model:**

- **Additive Noise:** The image is corrupted by a random noise signal: $y = x + n$, where $x$ is the original image, $n$ is the noise signal, and $y$ is the degraded image.
- **Multiplicative Noise:** The image is corrupted by a random noise signal: $y = x \times n$, where $x$ is the original image, $n$ is the noise signal, and $y$ is the degraded image.

**Blurring Model:**

- **Linear Blurring:** The image is blurred using a linear filter: $y = \sum_{i=0}^{N-1} h_i \times x_i$, where $x$ is the original image, $h$ is the filter, and $y$ is the blurred image.
- **Non-Linear Blurring:** The image is blurred using a non-linear filter: $y = \sum_{i=0}^{N-1} h_i \times x_i^p$, where $x$ is the original image, $h$ is the filter, and $y$ is the blurred image.

### 5.3: Image Restoration

---

Image restoration is the process of recovering the original image from the degraded image.

**Methods of Image Restoration:**

- **Filtering:** Using filters to remove noise and blur from the image.
- **Deconvolution:** Using deconvolution techniques to remove blur from the image.
- **Super-Resolution:** Using super-resolution techniques to improve the resolution of the image.

### 5.4: Image Reconstruction

---

Image reconstruction is the process of generating a new image from the degraded image.

**Methods of Image Reconstruction:**

- **Inpainting:** Filling in missing regions of the image.
- **Image Composition:** Combining multiple images to create a new image.
- **Image Generation:** Generating new images from scratch.

## Key Concepts

- **Image Degradation:** The process of corrupting or altering an image.
- **Noise:** Random fluctuations in the image.
- **Blurring:** The spreading of image details.
- **Obliteration:** The loss of important details in the image.
- **Compression:** The reduction of image data to reduce file size.
- **Image Restoration:** The process of recovering the original image from the degraded image.
- **Image Reconstruction:** The process of generating a new image from the degraded image.
