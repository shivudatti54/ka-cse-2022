

## Table of Contents

- [Module 3: Image Restoration and Reconstruction](#module-3-image-restoration-and-reconstruction)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [2.1 The Degradation Model](#21-the-degradation-model)
  - [2.2 Noise Models](#22-noise-models)
  - [2.3 Restoration Filters](#23-restoration-filters)
  - [2.4 Reconstruction from Projections](#24-reconstruction-from-projections)
- [3. Key Points & Summary](#3-key-points--summary)

Of course. Here is a comprehensive educational content piece on Image Restoration and Reconstruction for engineering students.

# Module 3: Image Restoration and Reconstruction

## 1. Introduction

In the previous modules, we focused on **image enhancement**—subjective techniques to improve visual appearance. **Image Restoration**, by contrast, is an objective process. It aims to recover an image that has been degraded, using a priori knowledge of the degradation process. Think of it as "undoing" damage based on a mathematical model of how that damage occurred. **Image Reconstruction** often deals with creating a 2D image from 1D projections or sparse data, common in medical imaging (like CT scans) and astronomy. This module provides the foundational models and filters used to reverse these degradations.

## 2. Core Concepts

### 2.1 The Degradation Model

Restoration is built upon a model of the degradation process. The fundamental, linear model is represented as:

`g(x, y) = h(x, y) * f(x, y) + η(x, y)`

In the frequency domain, this becomes:

`G(u, v) = H(u, v) . F(u, v) + N(u, v)`

Where:

- `g(x, y)` is the degraded (observed) image.
- `f(x, y)` is the original, undegraded image.
- `h(x, y)` is the **Point Spread Function (PSF)**, which models the degradation (e.g., blur).
- `*` denotes the convolution operation.
- `η(x, y)` is additive noise.
- `H(u, v)` is the **Optical Transfer Function (OTF)**, the Fourier Transform of the PSF.

The goal of restoration is to estimate `f(x, y)` given `g(x, y)` and knowledge (or an estimate) of `H` and `η`.

### 2.2 Noise Models

A key part of degradation is noise. Different types require different approaches:

- **Gaussian Noise:** Statistical noise with a normal distribution. Common in electronic sensors due to thermal fluctuations.
- **Salt-and-Pepper Noise:** Also called impulse noise. Appears as random white ("salt") and black ("pepper") pixels. Caused by faulty sensors or transmission errors.
- **Rayleigh & Erlang Noise:** Used for modeling specific types of non-Gaussian noise in specialized applications.

### 2.3 Restoration Filters

#### A. Inverse Filtering

This is the most straightforward approach. From the frequency domain model, we solve for `F(u, v)`:

`F̂(u, v) = G(u, v) / H(u, v)`

This simply inverts the blur. However, it has a major flaw: it amplifies noise severely wherever `H(u, v)` is small or zero. This makes it impractical for most real-world, noisy images.

#### B. Wiener Filter (Minimum Mean Square Error Filter)

The Wiener filter is a powerful, classical solution that overcomes the noise limitation of the inverse filter. It is designed to find an estimate `f̂` that minimizes the mean square error between the original and restored images (`E{ (f - f̂)² }`).

The Wiener filter in the frequency domain is:

`F̂(u, v) = [ 1 / H(u, v) ] * [ |H(u, v)|² / (|H(u, v)|² + K) ] * G(u, v)`

Where `K` is an approximation of the noise-to-signal power ratio (`S_η(u, v)/S_f(u, v)`).

**Key Advantage:** The Wiener filter acts as a band-pass filter. It inverts the degradation `H(u, v)` where the signal is strong but suppresses the restoration where the noise power dominates the signal power. This prevents the explosive noise amplification seen in the inverse filter.

#### C. Constrained Least Squares Filter

This is another excellent filter that requires less knowledge about the noise than the Wiener filter (which needs its power spectrum). It only requires knowledge of the mean and variance of the noise. It operates by finding a solution that minimizes a linear operator (e.g., a Laplacian for smoothness) applied to the image, subject to the constraint:

`||g - H * f̂||² = ||η||²`

It effectively smoothes out noise while reversing the blur, often producing visually better results than the Wiener filter.

### 2.4 Reconstruction from Projections

This is the cornerstone of **Computed Tomography (CT)**. The core idea is to reconstruct a 2D cross-sectional image (`f(x, y)`) from a set of its 1D line integrals, called projections.

- **The Radon Transform:** This transform calculates the projections of an image along various angles. A single projection is the line integral of `f(x, y)` along a line `L`.
- **The Fourier Slice Theorem:** This theorem states that the **Fourier transform of a parallel projection** of an image at an angle `θ` gives a **slice** of the 2D Fourier transform of the image along the same angle `θ`.
- **Filtered Back-Projection (FBP):** The most common reconstruction algorithm. It works in two steps:
  1.  **Filtering:** Each 1D projection is filtered with a high-pass filter (e.g., a "ramp" filter) to reduce blurring.
  2.  **Back-Projection:** The filtered projections are smeared back across the image plane along the direction they were originally measured. The sum of all these back-projections from all angles forms the reconstructed image.

---

## 3. Key Points & Summary

| Concept                       | Description                                                                                                | Key Takeaway                                                                                |
| :---------------------------- | :--------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Goal**                      | To **objectively** reconstruct an original image from a degraded version using a model of the degradation. | Opposite of subjective enhancement.                                                         |
| **Degradation Model**         | `g = h * f + η`                                                                                            | The mathematical foundation of all restoration. Requires knowledge of `H` (the blur).       |
| **Inverse Filter**            | `F̂ = G / H`                                                                                                | Simple but severely amplifies noise. Not practical.                                         |
| **Wiener Filter**             | Optimal filter minimizing mean square error.                                                               | Considers both the blur (`H`) and the noise power. The standard for robust restoration.     |
| **Constrained Least Squares** | Minimizes a function (e.g., smoothness) subject to a noise constraint.                                     | Requires only noise mean/variance; often produces superior visual results.                  |
| **Reconstruction (FBP)**      | Rebuilding a 2D image from its 1D projections (e.g., CT scans).                                            | Relies on the **Fourier Slice Theorem** and involves **Filtering** and **Back-Projection**. |
