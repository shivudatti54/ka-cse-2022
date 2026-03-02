# **Chap-10 (10.1 to 10.3.2) Image Restoration and Reconstruction**

### Important Concepts

- **Image Degradation**: Any alteration of an image that degrades its quality, such as noise, blur, or distortion.
- **Image Restoration**: The process of restoring an degraded image to its original form.

### Key Points

- **Point Spread Function (PSF)**:
  - Definition: A mathematical function that describes the spread of light or signal through a system.
  - Importance: Used to model image degradation and restoration processes.
- **Line Spread Function (LSF)**:
  - Definition: A mathematical function that describes the spread of light or signal along a line.
  - Importance: Used in image restoration algorithms.
- **Maximum a Posteriori (MAP) Estimation**:
  - Definition: A method of estimating the parameters of a probability distribution given observed data.
  - Importance: Used in image restoration and reconstruction.
- **Bayesian Estimation**:
  - Definition: A method of estimating the parameters of a probability distribution given observed data.
  - Importance: Used in image restoration and reconstruction.

### Formulas and Theorems

- **Blind Deconvolution**: A method of estimating the original image from a degraded image using the PSF.
  - Formula: `x(t) = \int_{-\infty}^{\infty} h(t) y(t) dt`
- **Maximum Likelihood Estimation (MLE)**:
  - Definition: A method of estimating the parameters of a probability distribution given observed data.
  - Formula: `\hat{\theta} = \arg\max_{\theta} p(y|\theta)`
- **Bayes' Theorem**:
  - Definition: A mathematical formula for updating the probability of a hypothesis given new evidence.
  - Formula: `p(\theta|y) = \frac{p(y|\theta)p(\theta)}{p(y)}`

### Important Definitions

- **Noise**: Random fluctuations in the image data.
- **Blur**: A type of image degradation caused by the spreading of light or signal.
- **Distortion**: A type of image degradation caused by changes in the image geometry or orientation.

This summary aims to provide a concise overview of the key concepts, formulas, and theorems covered in Chap-10 (10.1 to 10.3.2) of the Computer Vision module. It is intended to be a quick revision guide before exams.
