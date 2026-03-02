**Module 3: Image Restoration and Reconstruction**

### Introduction

In the world of computer vision, we often deal with images that are imperfect. They can be blurry due to camera shake, noisy from poor lighting or sensor limitations, or even have missing parts. **Image Restoration** and **Reconstruction** are fundamental processes aimed at improving the quality of an image or recovering an original scene from degraded observations. Unlike image enhancement, which is subjective and aims to make an image more visually appealing, restoration is objective and is based on mathematical or probabilistic models of the degradation process. The goal is to reverse the degradation and obtain an estimate of the original, pristine image.

---

### Core Concepts

The entire process of image restoration is modeled by a simple, yet powerful equation:

`g(x, y) = h(x, y) * f(x, y) + η(x, y)`

Where:

- `g(x, y)` is the **degraded (observed) image**.
- `f(x, y)` is the **original, pristine image** (which we wish to recover).
- `h(x, y)` is the **degradation function** or **Point Spread Function (PSF)**. This represents the blurring mechanism (e.g., motion blur, out-of-focus blur).
- `*` denotes the **convolution** operation.
- `η(x, y)` is **additive noise**.

The restoration task is essentially an **inverse problem**: given `g` and knowing (or estimating) `h` and the characteristics of `η`, estimate `f`.

#### 1. Noise Models

The first step is often to address noise. Common noise models include:

- **Gaussian Noise:** Characterized by its mean and variance. It arises from electronic circuit noise and sensor noise due to poor illumination.
- **Salt-and-Pepper Noise:** An impulse noise where pixels are randomly set to either minimum (pepper, black) or maximum (salt, white) intensity. Caused by faulty sensors or analog-to-digital converter errors.

**Example:** Filtering a noisy image. A simple approach is to use **spatial filters**:

- **Mean Filter:** A simple averaging filter. It reduces noise but also blurs edges and fine details.
- **Median Filter:** A non-linear filter excellent for removing salt-and-pepper noise. It replaces a pixel's value with the median of the intensities in its neighborhood, effectively eliminating outliers while preserving edges.

#### 2. Inverse Filtering

This is a direct, but often problematic, approach. In the frequency domain, the degradation model is:
`G(u, v) = H(u, v) * F(u, v) + N(u, v)`

The naive inverse filter estimate `F̂(u, v)` is simply:
`F̂(u, v) = G(u, v) / H(u, v) = F(u, v) + N(u, v)/H(u, v)`

**The Problem:** If `H(u, v)` is zero or very small at any frequency, the term `N(u, v)/H(u, v)` will dominate, amplifying noise to extreme levels and making the restoration useless. This is a classic case of an ill-posed problem.

#### 3. Wiener Filter (Minimum Mean Square Error Filter)

The Wiener filter provides a more robust solution. It overcomes the noise amplification problem of the inverse filter by incorporating statistical knowledge of the noise and the original image. It aims to find an estimate `f̂` that minimizes the mean square error between the original and the restored image (`E{ (f - f̂)² }`).

The Wiener filter in the frequency domain is given by:
`F̂(u, v) = [ 1 / H(u, v) ] * [ |H(u, v)|² / ( |H(u, v)|² + K ) ] * G(u, v)`
where `K` is often approximated as the ratio of the **noise power spectrum** to the **original image power spectrum** (`S_η / S_f`).

**Key Advantage:** The Wiener filter acts as a band-pass filter. At frequencies where `H(u, v)` is large (and thus the signal-to-noise ratio is high), it behaves like an inverse filter. Where `H(u, v)` is small (low signal-to-noise ratio), it attenuates the filter response to suppress noise.

#### 4. Reconstruction from Projections

This is a specialized form of reconstruction, most famously used in **Computed Tomography (CT)**. The concept is to reconstruct a 2D (or 3D) image from a series of 1D projections taken at different angles. The core algorithm for this is the **Filtered Back-Projection (FBP)**.

1.  A single projection is a line integral of the object's attenuation coefficients.
2.  Multiple projections are acquired by rotating the source and detector around the object.
3.  Each 1D projection is filtered (e.g., with a Ram-Lak filter) to correct blurring.
4.  The filtered projections are then "smeared back" (back-projected) across the image plane along the direction they were acquired.
5.  The superposition of all these back-projections from all angles reconstructs the original image.

---

### Key Points & Summary

- **Objective vs. Subjective:** Restoration is an objective process based on models of degradation, unlike enhancement.
- **Degradation Model:** The process is modeled as `g = h * f + η`. Success depends on accurately knowing or estimating `h` and the noise characteristics.
- **Noise Removal:** Simple filters like Mean and Median filters are effective first steps for specific noise types.
- **Inverse Filtering:** A direct but flawed method that amplifies noise severely.
- **Wiener Filter:** A superior, optimal filter that balances inverse filtering with noise suppression based on statistical properties. It is the workhorse of classical image restoration.
- **CT Reconstruction:** Images can be reconstructed from their projections using algorithms like Filtered Back-Projection, which is a cornerstone of medical imaging.
- **Ill-Posed Problem:** Image restoration is inherently an ill-posed inverse problem, often requiring additional constraints (like smoothness) for a stable solution. Modern approaches use **deep learning** to learn the restoration mapping directly from examples of degraded and clean images.
