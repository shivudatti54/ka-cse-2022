**Textbook-1: Chap- 3 (3.3 - 3.6)**
**Computer Vision**
**Image Processing: More Neighborhood Operators, Fourier Transforms, Pyramids, and Wavelets**

# **3.3 Neighborhood Operators**

Neighborhood operators are used to process local information in an image. They are simple to implement and can be effective in various image processing tasks.

### Definition:

A neighborhood operator is a mathematical function that takes a pixel value and its neighboring pixel values as input and produces an output value.

### Types of Neighborhood Operators:

- **Mean Filter:** calculates the mean of neighboring pixel values and assigns it to the current pixel.
- **Median Filter:** calculates the median of neighboring pixel values and assigns it to the current pixel.
- **Gaussian Filter:** uses a Gaussian distribution to weight neighboring pixel values and calculates their weighted sum.
- **Sobel Operator:** uses a Sobel kernel to detect edges in an image.

### Example:

Suppose we have an image with the following neighboring pixel values:

|     | -   | -   | -   |
| --- | --- | --- | --- |
| -   | 1   | 2   | 3   |
| -   | 4   | 5   | 6   |
| -   | 7   | 8   | 9   |

If we apply a mean filter to the middle pixel value (5), the output would be:

|     | -   | -   | -   |
| --- | --- | --- | --- |
| -   | 2.2 | 3.4 | 4.6 |
| -   | 4.2 | 5.4 | 6.6 |
| -   | 6.2 | 7.4 | 8.6 |

# **3.4 Fourier Transforms**

The Fourier transform is a mathematical tool used to decompose a signal or image into its constituent frequencies.

### Definition:

The Fourier transform is a linear transformation that takes a function as input and produces a new function that contains the same information, but in the frequency domain.

### Types of Fourier Transforms:

- **Discrete Fourier Transform (DFT):** used for discrete-time signals.
- **Fast Fourier Transform (FFT):** an efficient algorithm for computing the DFT.

### Example:

Suppose we have an image with the following pixel values:

|     | 0   | 1   | 0   |
| --- | --- | --- | --- |
| 0   | 1   | 0   | 1   |
| 0   | 0   | 1   | 0   |

If we apply the 2D DFT to the image, we get a frequency-domain representation that shows the distribution of pixel values across different frequencies.

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   | 1   | 0   | 1   |
| 1   | 0   | 1   | 0   |
| 2   | 1   | 0   | 1   |

# **3.5 Image Pyramids**

Image pyramids are a hierarchical representation of an image that can be used for image processing and feature extraction.

### Definition:

An image pyramid is a decomposition of an image into a series of images at different scales, each with a resolution that is a fraction of the original image.

### Types of Image Pyramids:

- **Linear Pyramid:** a pyramid constructed using linear interpolation between adjacent images.
- **Non-Linear Pyramid:** a pyramid constructed using non-linear interpolation between adjacent images.

### Example:

Suppose we have an image with the following pixel values:

|     | 0   | 1   | 0   |
| --- | --- | --- | --- |
| 0   | 1   | 0   | 1   |
| 0   | 0   | 1   | 0   |

If we construct a linear pyramid of three images with resolutions 1/2, 1/4, and 1/8, we get the following images:

Image 1 (1/2 resolution):

|     | 0   | 0   | 0   |
| --- | --- | --- | --- |
| 0   | 1/2 | 1/2 | 1/2 |
| 0   | 1/2 | 1/2 | 1/2 |

Image 2 (1/4 resolution):

|     | 0   | 0   | 0   |
| --- | --- | --- | --- |
| 0   | 1/4 | 1/4 | 1/4 |
| 0   | 1/4 | 1/4 | 1/4 |

Image 3 (1/8 resolution):

|     | 0   | 0   | 0   |
| --- | --- | --- | --- |
| 0   | 1/8 | 1/8 | 1/8 |
| 0   | 1/8 | 1/8 | 1/8 |

# **3.6 Wavelets**

Wavelets are mathematical functions that can be used to represent and analyze images at different scales.

### Definition:

A wavelet is a function that, when convolved with an image, produces a signal that contains the same information as the original image, but at different scales.

### Types of Wavelets:

- **Haar Wavelet:** a simple wavelet that is effective for image compression.
- **Daubechies Wavelet:** a wavelet that is effective for image denoising.

### Example:

Suppose we have an image with the following pixel values:

|     | 0   | 1   | 0   |
| --- | --- | --- | --- |
| 0   | 1   | 0   | 1   |
| 0   | 0   | 1   | 0   |

If we apply a Haar wavelet to the image, we get a signal that contains the same information as the original image, but at different scales.

|     | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | 0   |
| 1   | 0   | 1   |

Note: This is a text-based representation and actual images and signals may vary.
