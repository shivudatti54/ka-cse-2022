# **Restoration in the Presence of Noise Only**

### Definitions and Notations

- **Noise**: Random variations in the image data
- **Signal-to-Noise Ratio (SNR)**: Measure of the ratio of signal power to noise power
- **PSNR**: Peak Signal-to-Noise Ratio, defined as:
  \[ PSNR = 20 \log*{10} \left( \frac{max*{I(x)}}{sqrt{M \cdot SNR}} \right) \]
  where $max_{I(x)}$ is the maximum intensity of the image, $M$ is the maximum intensity of the noise-free image

### Theories

- **Maximum Likelihood Estimation (MLE)**: Restore image by minimizing the probability of observing the noisy data
- **Bayesian Estimation**: Use prior knowledge to update the probability of the image parameters
- **Wiener Filter**: Optimal filter for minimizing the mean squared error between the original and restored images

### Formulas

- **Wiener Filter**:
  \[ h(x,y) = \frac{K \cdot G(x,y)}{K + G(x,y)} \]
  where $K$ is the constant to be determined, $G(x,y)$ is the autocorrelation of the image, and $(x,y)$ are the coordinates of the pixel
- **Optimal Restoration**:
  \[ \hat{I}(x,y) = \int*{-\infty}^{\infty} \int*{-\infty}^{\infty} I(x',y') \cdot P(I(x',y')|x,y) \, dx' \, dy' \]
  where $I(x,y)$ is the original image, $P(I(x',y')|x,y)$ is the conditional probability density function

### Important Results

- **Properties of Wiener Filter**:

* It is a linear filter
* It is a minimum mean squared error filter
* It is a maximum likelihood estimator

- **Optimal Restoration**:

* The optimal restoration is the Bayesian estimate of the image parameters
* It is based on the prior knowledge of the image

### Revision Tips

- Understand the definitions and notations
- Familiarize yourself with the theories (MLE, Bayesian Estimation, Wiener Filter)
- Practice deriving the formulas (Wiener Filter, Optimal Restoration)
- Review the important results and their implications
