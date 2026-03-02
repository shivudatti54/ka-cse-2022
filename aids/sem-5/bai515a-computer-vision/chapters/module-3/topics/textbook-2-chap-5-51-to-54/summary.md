# **Textbook-2: Chap-5 (5.1 to 5.4) - Quick Revision Notes**

### Introduction

---

- Image degradation/restoration process involves removing noise and restoring the original image
- A model of this process is described in the chapter

### 5.1. Image Degradation Models

---

- **Additive Model**: Image degradation is represented as a linear combination of the original image and additive noise
- **Multiplicative Model**: Image degradation is represented as a product of the original image and multiplicative noise
- **Blind Deconvolution**: Removing noise without knowing the degradation model

### 5.2. Image Restoration

---

- **Maximum Likelihood Estimation (MLE)**: Restoring the image by maximizing the likelihood of observing the degraded image
- **Bayesian Approach**: Restoring the image by maximizing the posterior probability of the original image given the degraded image

### 5.3. Deconvolution

---

- **Optimal Deconvolution**: Restoring the image by minimizing the mean squared error between the original and restored images
- **Bayesian Deconvolution**: Restoring the image by minimizing the mean squared error between the original and restored images, subject to a prior distribution on the original image

### 5.4. Image Reconstruction

---

- **Filtering**: Restoring the image by applying a filter to the degraded image
- **Super-Resolution**: Restoring the image by interpolating between multiple degraded images

## **Important Formulas and Definitions**

- **Mean Squared Error (MSE)**: `E[(x - y)^2]`, where `x` is the original image and `y` is the restored image
- **Mean Absolute Error (MAE)**: `E[|x - y|]`
- **Bayesian Estimator**: `E[θ|x] = E[θ|x,θ] / E[x,θ]`

## **Theorems and Resultants**

- **Bayes' Theorem**: `P(A|B) = P(A and B) / P(B)`
- **Maximum Likelihood Estimator**: `E[X] = argmax_P(X) P(X)`

Note: This summary is a concise version of the key points, formulas, and definitions in the chapter. It's meant to be a quick revision guide for exams.
