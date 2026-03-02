# **Textbook-2: Chap-5 (5.1 to 5.4) - Image Restoration and Reconstruction**

**Key Points:**

- **5.1 Image Degradation Models**
  - Point Spread Function (PSF)
  - PSF representation: ideal, point spread, and spread function
  - Linear and nonlinear degradation models
- **5.2 Image Restoration Models**
  - Maximum likelihood estimation (MLE)
  - Bayes estimation
  - Wiener filter
  - Regularized least squares
- **5.3 Image Reconstruction**
  - Linear and nonlinear reconstruction models
  - Least squares method
  - Regularization techniques
- **5.4 Image Denoising**
  - Denoising models
  - Blind denoising
  - Deblurring models

**Important Formulas:**

- **Point Spread Function (PSF):**
  - PSF = h(x)
  - PSF = \* (x)
- **Maximum Likelihood Estimation (MLE):**
  - MLE: \* (x) = argmax\_{x \in X} P(x|y)
- **Wiener Filter:**
  - Wiener filter: \* (x) = \* (x) + \* (x)
- **Regularized Least Squares:**
  - Regularized least squares: \* (x) = argmin\_{x \in X} ||y - \* (x)||^2 + \lambda ||x||^2

**Important Definitions:**

- **Linear System:** A system of linear equations
- **Nonlinear System:** A system of nonlinear equations
- **Regularization:** A regularization technique is used to prevent overfitting

**Important Theorems:**

- **Cramer-Rao Lower Bound (CRLB):** The CRLB is a lower bound on the variance of any unbiased estimator.
- **Wiener-Khinchin Theorem:** The Wiener-Khinchin theorem states that a linear system can be represented as a convolution of a random process with a deterministic function.

**Revision Tips:**

- Focus on understanding the different degradation models and restoration models.
- Practice solving problems related to image restoration and reconstruction.
- Review the formulas and theorems mentioned above.
