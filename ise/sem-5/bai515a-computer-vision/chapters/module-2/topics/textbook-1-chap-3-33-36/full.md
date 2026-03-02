**Textbook-1: Chap- 3 (3.3 - 3.6)**

**Image Processing: More Neighborhood Operators, Fourier Transforms, Pyramids, and Wavelets**

**3.3 Neighborhood Operators**

Neighborhood operators are a fundamental concept in image processing. They are used to transform an image into a new representation, often by applying a local operation to a small region of the image.

### Definition

A neighborhood operator is a mathematical function that takes an image as input and produces an output image. The output image is obtained by applying the function to a small region of the input image, known as the neighborhood.

### Types of Neighborhood Operators

There are several types of neighborhood operators, including:

- **Linear Neighborhood Operators**: These operators apply a linear transformation to the pixels in the neighborhood.
- **Non-Linear Neighborhood Operators**: These operators apply a non-linear transformation to the pixels in the neighborhood.
- **Local Autoregressive Model (LAM)**: This operator is a type of non-linear neighborhood operator that uses the neighboring pixels to estimate the value of a pixel.

**Example: Laplacian Operator**

The Laplacian operator is a linear neighborhood operator that is used to detect edges in an image. It is defined as:

∇²f(x) = ∂²f/∂x²

where f(x) is the image function, and x is the spatial coordinate.

The Laplacian operator is applied to a neighborhood of pixels, and the result is a new image where the edges are accentuated.

**Code Example (Python)**

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the Laplacian operator
def laplacian_operator(image):
    height, width = image.shape
    laplacian = np.zeros((height, width))
    for i in range(1, height-1):
        for j in range(1, width-1):
            laplacian[i, j] = (image[i-1, j] - 2 * image[i, j] + image[i+1, j]) + (image[i, j-1] - 2 * image[i, j] + image[i, j+1])
    return laplacian

# Apply the Laplacian operator to an image
image = np.random.rand(100, 100)
laplacian_image = laplacian_operator(image)

# Display the results
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(laplacian_image, cmap='gray')
plt.title('Laplacian Image')
plt.show()
```

**3.4 Fourier Transforms**

The Fourier transform is a mathematical tool used to represent a function as a sum of sinusoids. It is widely used in image processing to perform tasks such as filtering, convolution, and transform.

### Definition

The Fourier transform of a function f(x) is defined as:

F(ω) = ∫∞ -∞ f(x) e^{-iωx} dx

where ω is the frequency variable, and x is the spatial variable.

### Types of Fourier Transforms

There are several types of Fourier transforms, including:

- **Discrete Fourier Transform (DFT)**: This is a discrete version of the Fourier transform that is used for image processing.
- **Fast Fourier Transform (FFT)**: This is an efficient algorithm for computing the DFT.

**Example: Filtering with Fourier Transforms**

The Fourier transform can be used to filter an image. For example, the Butterworth filter can be used to remove high-frequency noise from an image.

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the Butterworth filter
def butterworth_filter(image, cutoff):
    height, width = image.shape
    filter = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            filter[i, j] = np.exp(-((i/height)**2 + (j/width)**2) / (2 * (cutoff**2)))
    return filter

# Apply the Butterworth filter to an image
image = np.random.rand(100, 100)
filter = butterworth_filter(image, 0.1)
filtered_image = np.convolve2d(image, filter, mode='same')

# Display the results
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(filter, cmap='gray')
plt.title('Filter')
plt.subplot(1, 3, 3)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.show()
```

**3.5 Image Pyramids**

Image pyramids are a hierarchical representation of an image, where each level of the pyramid represents a downsampling of the previous level. Image pyramids are widely used in image processing for tasks such as feature extraction and image compression.

### Definition

An image pyramid is defined recursively as follows:

- **Level 0**: The original image
- **Level 1**: Downsample the image by a factor of 2 in both the x and y directions
- **Level 2**: Downsample the image by a factor of 2 in both the x and y directions, and repeat the process

**Example: Image Pyramid Construction**

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the image pyramid construction function
def image_pyramid_image(image):
    pyramid = [image]
    for i in range(3):
        pyramid.append(np.downsample(pyramid[-1], 2))
    return pyramid

# Construct an image pyramid
image = np.random.rand(100, 100)
pyramid = image_pyramid_image(image)

# Display the results
for i in range(len(pyramid)):
    plt.subplot(1, len(pyramid), i+1)
    plt.imshow(pyramid[i], cmap='gray')
    plt.title(f'Level {i}')
plt.show()
```

**3.6 Wavelets**

Wavelets are a mathematical tool used to represent a function as a sum of wave-like functions. They are widely used in image processing for tasks such as image compression and denoising.

### Definition

A wavelet is a mathematical function that is defined as:

w(t) = ∫∞ -∞ h(t - u) f(u) du

where h(t) is the mother wavelet, and f(t) is the function to be waveletized.

### Types of Wavelets

There are several types of wavelets, including:

- **Haar Wavelet**: This is a simple wavelet that is widely used in image processing.
- **Coiflet Wavelet**: This is a more complex wavelet that is used for image denoising.

**Example: Wavelet Denoising**

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the Haar wavelet
def haar_wavelet(image):
    height, width = image.shape
    wavelet = np.zeros((height, width))
    for i in range(1, height-1):
        for j in range(1, width-1):
            wavelet[i, j] = (image[i-1, j] + image[i+1, j]) / 2 - (image[i, j-1] + image[i, j+1]) / 2
    return wavelet

# Denoise an image using Haar wavelets
image = np.random.rand(100, 100) + 0.01 * np.random.randn(100, 100)
denoised_image = haar_wavelet(image)

# Display the results
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image')
plt.show()
```

**Further Reading**

- [Image Processing and Analysis](https://www.amazon.com/Image-Processing-Analysis-Sampling-Techniques/dp/0123737269)
- [Wavelet Analysis and Its Applications](https://www.amazon.com/Wavelet-Analysis-Its-Applications-Fourier/dp/0123733912)
- [Computer Vision: Algorithms and Applications](https://www.amazon.com/Computer-Vision-Algorithms-Applications-Image/dp/0123736447)
