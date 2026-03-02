# **Textbook-2: Chap-5 (5.1 to 5.4)**

## **5.1 Image Degradation Models**

### Introduction

Image degradation refers to the process of reducing the quality of an image due to various factors such as noise, blur, and distortion. In this chapter, we will discuss different models of image degradation and their effects on image quality.

### Types of Image Degradation

- **Additive Noise**: Additive noise is a type of noise that adds to the original image intensity. It can be represented mathematically as: $I(x) + n(x)$, where $I(x)$ is the original image and $n(x)$ is the additive noise.
- **Multiplicative Noise**: Multiplicative noise is a type of noise that multiplies the original image intensity. It can be represented mathematically as: $I(x) \cdot n(x)$, where $I(x)$ is the original image and $n(x)$ is the multiplicative noise.
- **Blur**: Blur is a type of degradation that spreads out the image intensity over a larger area. It can be represented mathematically as: $I(x) \ast h(x)$, where $I(x)$ is the original image and $h(x)$ is the blurring kernel.

### Mathematical Models of Image Degradation

- **Gaussian Noise Model**: The Gaussian noise model is a mathematical model that represents additive noise as a Gaussian distribution. It can be represented mathematically as: $n(x) \sim N(0, \sigma^2)$, where $n(x)$ is the additive noise and $\sigma^2$ is the variance.
- **Rayleigh Noise Model**: The Rayleigh noise model is a mathematical model that represents multiplicative noise as a Rayleigh distribution. It can be represented mathematically as: $n(x) \sim R(0, \sigma^2)$, where $n(x)$ is the multiplicative noise and $\sigma^2$ is the variance.

## **5.2 Image Restoration Techniques**

### Introduction

Image restoration is the process of recovering the original image from a degraded image. In this chapter, we will discuss different techniques for image restoration.

### Techniques for Image Restoration

- **Filtering Techniques**:
  - **Gaussian Filter**: The Gaussian filter is a mathematical model that represents a smoothing filter. It can be represented mathematically as: $I(x) \ast h(x)$, where $I(x)$ is the original image and $h(x)$ is the blurring kernel.
  - **Wiener Filter**: The Wiener filter is a mathematical model that represents an optimal filter for image restoration. It can be represented mathematically as: $I(x) \ast W(x)$, where $I(x)$ is the original image and $W(x)$ is the Wiener filter kernel.
- **Deconvolution Techniques**:
  - **Optimal Deconvolution**: The optimal deconvolution is a mathematical model that represents a method for image restoration using deconvolution. It can be represented mathematically as: $I(x) \ast h^{-1}(x)$, where $I(x)$ is the original image and $h^{-1}(x)$ is the inverse of the blurring kernel.
- **Image Reconstruction Techniques**:
  - **Maximum Likelihood Estimation**: The maximum likelihood estimation is a mathematical model that represents a method for image reconstruction using maximum likelihood estimation. It can be represented mathematically as: $\hat{I}(x) = \arg\max_{I(x)} \mathcal{L}(I(x), y(x))$, where $\hat{I}(x)$ is the reconstructed image and $y(x)$ is the degraded image.

## **5.3 Image Reconstruction Methods**

### Introduction

Image reconstruction methods are techniques used to recover the original image from a degraded image. In this chapter, we will discuss different image reconstruction methods.

### Methods for Image Reconstruction

- **Bayesian Methods**:
  - **Bayesian Filter**: The Bayesian filter is a mathematical model that represents a method for image reconstruction using Bayesian inference. It can be represented mathematically as: $\hat{I}(x) = \arg\max_{I(x)} \mathcal{L}(I(x), y(x))$, where $\hat{I}(x)$ is the reconstructed image and $y(x)$ is the degraded image.
- **Maximum Likelihood Estimation**: The maximum likelihood estimation is a mathematical model that represents a method for image reconstruction using maximum likelihood estimation. It can be represented mathematically as: $\hat{I}(x) = \arg\max_{I(x)} \mathcal{L}(I(x), y(x))$, where $\hat{I}(x)$ is the reconstructed image and $y(x)$ is the degraded image.

## **5.4 Image Restoration Software**

### Introduction

Image restoration software are programs used to restore images from degraded images. In this chapter, we will discuss different image restoration software.

### Software for Image Restoration

- **Adobe Photoshop**: Adobe Photoshop is a popular image editing software that includes tools for image restoration.
- **ImageJ**: ImageJ is a free image processing software that includes tools for image restoration.
- **GIMP**: GIMP is a free and open-source image editing software that includes tools for image restoration.

### Conclusion

---

Image degradation is a common problem in computer vision, and image restoration is an essential technique for recovering the original image. In this chapter, we discussed different models of image degradation, techniques for image restoration, image reconstruction methods, and image restoration software. Understanding these concepts and techniques is crucial for developing effective image restoration systems.
