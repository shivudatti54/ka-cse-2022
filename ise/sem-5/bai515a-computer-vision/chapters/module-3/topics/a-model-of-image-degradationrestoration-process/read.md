# Image Degradation and Restoration Model

## 1. Introduction to Image Degradation

In an ideal world, a digital image would be a perfect representation of the scene it captures. However, during the processes of acquisition, transmission, and storage, images are often corrupted. This corruption is known as **image degradation**. It manifests as a loss of clarity, detail, and color fidelity, often introducing unwanted artifacts like noise and blur.

The goal of **image restoration** is to estimate the original, uncorrupted image from its degraded version. Unlike image _enhancement_, which is subjective and aims to make an image look better, restoration is an objective process that attempts to reverse known or estimated degradation using mathematical models.

## 2. The Image Degradation Model

The relationship between the original scene and the degraded image can be represented by a mathematical model. The most common model assumes the degradation process is linear and position-invariant.

### 2.1 The Mathematical Formulation

The degradation process is modeled by the following equation:

**g(x, y) = h(x, y) ∗ f(x, y) + η(x, y)**

Where:

- **f(x, y)** is the original, undegraded image.
- **h(x, y)** is the **Degradation Function** or **Point Spread Function (PSF)**. This represents the blurring mechanism (e.g., lens defocus, camera motion).
- **∗** denotes the **convolution** operation. Convolution of the image with the PSF is what causes the blur.
- **η(x, y)** is the **Additive Noise** term. This represents random disturbances introduced during the process (e.g., sensor noise, electronic interference).
- **g(x, y)** is the observed, degraded image.

This model is often expressed in the frequency domain for easier computation. Applying the Fourier Transform (denoted by **F**), the convolution operation becomes a multiplication:

**G(u, v) = H(u, v) • F(u, v) + N(u, v)**

Where:

- G, H, F, and N are the Fourier transforms of g, h, f, and η, respectively.
- **H(u, v)** is known as the **Optical Transfer Function (OTF)** or, when considering magnitude only, the **Modulation Transfer Function (MTF)**.

### 2.2 Visualizing the Model with a Block Diagram

The following diagram illustrates the flow of the degradation process:

```
    Original Image
        ↓
    [ Degradation ] → Convolved with PSF (h(x,y)) → Blurred Image
        ↓
    [   Add Noise  ] → Add η(x,y)
        ↓
    Degraded Image (g(x,y))
```

## 3. Components of Degradation

### 3.1 The Point Spread Function (PSF) - `h(x, y)`

The PSF describes how a single point of light is spread out in the image. A perfect, ideal point source would be represented by a Dirac delta function. A real-world system will blur this point.

**Common Types of Blur:**

- **Motion Blur:** Caused by relative motion between the camera and the scene during exposure. The PSF is often a straight line.
- **Out-of-Focus Blur:** Caused by a lens being improperly focused. The PSF is often modeled as a uniform disk (a "pillbox").
- **Atmospheric Turbulence Blur:** Common in long-range aerial imaging, modeled as a Gaussian function.

**Example of a 1D Motion Blur PSF:**

```
A point source [0, 0, 1, 0, 0] is convolved with a motion PSF h = [1/3, 1/3, 1/3].
The result is a blurred line: [0, 1/3, 1/3, 1/3, 0].
```

**ASCII Representation of a Gaussian PSF (2D):**

```
Low Intensity        High Intensity        Low Intensity
     ...                   ...
   ..   ..               .     .
  .       .             .       .
 .         .           .         .
 .         .    →     .    0    .    (A Gaussian "hill")
  .       .             .       .
   ..   ..               .     .
     ...                   ...
```

### 3.2 Additive Noise - `η(x, y)`

Noise is the random variation of brightness or color information in images. It is often statistically characterized.

| Noise Model         | Probability Density Function (PDF)                        | Cause                                                                  | Example                                                                                                                                             |
| :------------------ | :-------------------------------------------------------- | :--------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gaussian**        | `p(z) = (1/√(2πσ²)) * exp(-(z-μ)²/(2σ²))`                 | Electronic circuit noise, sensor noise due to poor illumination        |                                                                                                                                                     |
| **Salt-and-Pepper** | `p(z) = { Pₛ for z = 0 (pepper), Pₚ for z = max (salt) }` | Faulty pixels, analog-to-digital converter errors, transmission errors | ![Salt and Pepper noise: black and white dots scattered on an image](https://upload.wikimedia.org/wikipedia/commons/5/52/Salt-and-pepper_noise.png) |
| **Rayleigh**        | `p(z) = (2/b)(z-a)exp(-(z-a)²/b) for z ≥ a`               | Range imaging                                                          |                                                                                                                                                     |
| **Uniform**         | `p(z) = 1/(b-a) for a ≤ z ≤ b`                            | Least informative, used as a worst-case model                          |                                                                                                                                                     |

## 4. The Image Restoration Process

Restoration is the inverse process of degradation. Given `g(x, y)` and knowledge (or an estimate) of `h(x, y)` and `η(x, y)`, we seek to find an estimate `f̂(x, y)` of the original image.

### 4.1 Inverse Filtering

This is the most straightforward approach. Ignoring the noise term, we can work in the frequency domain:
**F̂(u, v) = G(u, v) / H(u, v)**

**Limitations:**

1.  **Noise Amplification:** If `H(u, v)` is zero or very small at any frequency, the term `N(u, v)/H(u, v)` becomes very large, amplifying noise catastrophically.
2.  **Sensitivity to Blur Model:** Requires precise knowledge of `H(u, v)`.

### 4.2 Wiener Filtering (Minimum Mean Square Error Filter)

This is a more sophisticated and robust approach. The Wiener filter seeks an estimate `f̂` that minimizes the statistical error between the original and the restored image (`E{ (f - f̂)² }`). The frequency domain solution is:

**F̂(u, v) = [ 1/H(u, v) * ( |H(u, v)|² / (|H(u, v)|² + K) ) ] \* G(u, v)**

Where `K` is a constant often approximated by the **noise-to-signal power ratio**. The term in brackets acts as a correction to the inverse filter.

**Advantages:**

- **Handles Noise:** Explicitly accounts for both the blur and the noise.
- **Smooths Output:** Prevents the wild amplification of noise seen in inverse filtering.

### 4.3 Steps for Restoration

A generalized restoration process involves the following steps:

1.  **Model Identification:** Determine the mathematical model of the degradation (`h(x, y)`) and noise (`η(x, y)`). This can be done by:
    - Analysis of the imaging system (e.g., knowing exposure time for motion blur).
    - Blind deconvolution techniques that estimate `h` from the image itself.
2.  **Model Application:** Apply a restoration filter (like Inverse or Wiener) using the identified model.
3.  **Reconstruction:** Obtain the restored image `f̂(x, y)`.

```
    Degraded Image (g(x,y))
        ↓
    [ Estimate H and N ] ← Prior Knowledge / Analysis
        ↓
    [ Apply Restoration Filter ] (e.g., Wiener Filter)
        ↓
    Restored Image Estimate (f̂(x,y))
```

## 5. Exam Tips and Key Takeaways

1.  **Memorize the Model:** The equation `g = h ∗ f + η` is fundamental. Be able to define each component.
2.  **Frequency vs. Spatial Domain:** Understand why restoration is often performed in the frequency domain (convolution becomes multiplication).
3.  **Inverse vs. Wiener Filter:** The key difference is that the Inverse filter ignores noise, while the Wiener filter is designed to handle it. Be prepared to explain the consequences of this difference.
4.  **Know Your Noise:** Be able to identify the PDF and common causes for Gaussian and Salt-and-Pepper noise.
5.  **PSF is Key:** The success of most restoration techniques hinges on accurately estimating or knowing the Point Spread Function.
6.  **Think in Blocks:** Drawing the block diagram for both degradation and restoration will help you visualize and solve problems.
