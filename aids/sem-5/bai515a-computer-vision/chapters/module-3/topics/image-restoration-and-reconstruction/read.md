# Image Restoration and Reconstruction

## Introduction

In the world of computer vision, we often deal with images that are imperfect. They can be blurry due to camera shake, contain unwanted noise from a high ISO setting, or even be incomplete with missing pixels. **Image Restoration** and **Reconstruction** are fundamental processes aimed at reversing these degradations to recover the original, clean image. While related to enhancement, which is subjective and aims to improve visual appearance, restoration is an **objective** process based on mathematical or probabilistic models of the degradation and the noise. This module is crucial for applications in medical imaging (e.g., improving MRI scans), satellite image analysis, forensic analysis, and digital archiving.

## Core Concepts

### 1. A Model of the Image Degradation Process

The entire restoration process begins by modeling how the original image was degraded. The most common model is a linear, position-invariant degradation model given by:

`g(x, y) = h(x, y) * f(x, y) + η(x, y)`

Where:
*   `g(x, y)` is the degraded image.
*   `h(x, y)` is the **Point Spread Function (PSF)**, which represents the blurring function (e.g., motion blur, out-of-focus blur).
*   `f(x, y)` is the original, undegraded image.
*   `*` denotes the convolution operation.
*   `η(x, y)` is additive noise (e.g., Gaussian noise, salt-and-pepper noise).

The goal of restoration is to estimate `f(x, y)` given `g(x, y)`, with some knowledge or assumptions about `h(x, y)` and `η(x, y)`.

### 2. Noise Models

A critical step is characterizing the noise that has corrupted the image. Common noise models include:
*   **Gaussian Noise:** Statistical noise characterized by its mean and variance. It is common in electronic sensors due to thermal fluctuations.
*   **Salt-and-Pepper Noise:** Also called impulse noise, it appears as random white ("salt") and black ("pepper") pixels. It can be caused by faulty camera sensors or errors in data transmission.
*   **Rayleigh and Erlang Noise:** Used in specialized imaging scenarios like laser and radar imaging.

Restoration filters are often chosen based on the type of noise present.

### 3. Restoration in the Presence of Noise Only (No Blur)

If the primary degradation is noise (`h(x, y)` is an identity function, meaning no blur), restoration becomes a filtering task.

*   **Mean Filters:** Simple spatial filters that replace a pixel's value with the mean of its neighbors. They reduce noise but also blur edges and details.
    *   **Arithmetic Mean Filter:** Basic averaging.
    *   **Geometric Mean Filter:** Often preserves detail better than the arithmetic mean.
    *   **Harmonic Mean Filter:** Works well for Gaussian noise.
    *   **Contraharmonic Mean Filter:** Effective for salt-and-pepper noise (positive order for pepper noise, negative for salt noise).

*   **Order-Statistics Filters:** Non-linear filters based on ordering the pixel values in a neighborhood.
    *   **Median Filter:** Extremely effective for **salt-and-pepper noise**. It replaces a pixel's value with the median of its neighbors, effectively eliminating outliers while preserving sharp edges.
    *   **Max and Min Filters:** Useful for finding the brightest (max) or darkest (min) points, helpful for removing specific noise types.

*   **Adaptive Filters:** More advanced filters that change behavior based on local image characteristics (e.g., local variance). They provide better noise reduction with less blurring compared to their non-adaptive counterparts.

### 4. Inverse Filtering and Wiener Filtering (Restoring Blur and Noise)

When both blur (`h(x, y)`) and noise are present, we move into the frequency domain.

*   **Inverse Filtering:** A naive approach. It simply divides the Fourier transform of the degraded image `G(u, v)` by the Fourier transform of the blur function `H(u, v)`.
    `F_hat(u, v) = G(u, v) / H(u, v)`
    This method fails catastrophically in the presence of noise because at frequencies where `H(u, v)` is zero or very small, the noise term `N(u, v)` is amplified dramatically.

*   **Wiener Filtering (Minimum Mean Square Error Filter):** A superior, optimal approach. It overcomes the limitations of the inverse filter by incorporating knowledge of the **power spectra of the original image and the noise**. It performs a correction that minimizes the mean square error between the original and the restored estimate. The Wiener filter is given by:
    `F_hat(u, v) = [1 / H(u, v)] * [ |H(u, v)|² / (|H(u, v)|² + S_η(u, v)/S_f(u, v) ) ] * G(u, v)`
    Where `S_η` and `S_f` are the power spectra of the noise and the original image, respectively. In practice, if these are unknown, a constant `K` is often used as an approximation.

### 5. Image Reconstruction

This refers to the process of forming an image from a set of **projections**. The classic example is Computed Tomography (CT) scans in medical imaging, where a 2D cross-sectional "slice" is reconstructed from a series of 1D X-ray projections taken at different angles. The fundamental theorem enabling this is the **Fourier Slice Theorem**. The most common algorithm used for this purpose is the **Filtered Back Projection** algorithm, which essentially smears each projection back across the image plane and sums them to reconstruct the original image.

## Key Points & Summary

*   **Objective:** Image restoration aims to **recover an original image** from a degraded version using mathematical models of the degradation.
*   **Degradation Model:** The process is modeled as `g = h * f + η`, where `h` is the blur (PSF) and `η` is noise.
*   **Noise-Specific Filters:** For noise-only corruption, use spatial filters like the **Median filter** for salt-and-pepper noise and **Mean filters** for Gaussian noise.
*   **Handling Blur:** For images degraded by both blur and noise, **Wiener filtering** is a robust frequency-domain approach that is optimal in the mean square error sense, unlike the unstable Inverse filter.
*   **Reconstruction vs. Restoration:** Reconstruction builds an image from projections (e.g., CT scans), often using the **Filtered Back Projection** algorithm.
*   **Prerequisites:** A solid understanding of **Fourier Transforms**, **convolution**, and **probability** is essential for mastering this topic.