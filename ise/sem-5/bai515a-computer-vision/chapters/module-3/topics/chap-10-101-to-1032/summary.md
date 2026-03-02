# **Chap-10 Image Restoration and Reconstruction**

## **10.1 Image Degradation Models**

- Image degradation models:
  - Gaussian model: $I(x) = I_0(x) + \epsilon(x) + \sigma^2G(x)$
  - Poisson model: $I(x) = I_0(x) + \epsilon(x)$
  - Non-linear model: $I(x) = f(I_0(x), \epsilon(x))$
- Noise types:
  - Additive white Gaussian noise (AWGN)
  - Multiplicative white Gaussian noise (MWGN)
  - Non-white Gaussian noise

## **10.2 Image Restoration**

- Goal: Estimate the original image $I_0(x)$ from the degraded image $I(x)$
- Restoration techniques:
  - Wiener filter
  - Maximum likelihood estimation (MLE)
  - Bayesian estimation
  - Iterative methods (e.g., TV regularization)

## **10.3 Image Reconstruction**

- Goal: Reconstruct the original image $I_0(x)$ from the degraded image $I(x)$
- Reconstruction techniques:
  - Inverse filtering
  - Maximum likelihood estimation (MLE)
  - Bayesian estimation
  - Machine learning-based methods

## **Important Formulas and Definitions:**

- **Wiener filter**: $W(x) = \frac{\sigma^2 + \lambda}{\sigma^2 + \lambda + |G(x)|^2}$
- **Maximum likelihood estimation**: $\hat{I}_0(x) = \arg\max_{I_0(x)} p(I(x) | I_0(x))$
- **Bayesian estimation**: $\hat{I}_0(x) = \arg\max_{I_0(x)} p(I(x) | I_0(x)) p(I_0(x))$

## **Important Theorems:**

- **Cramer-Rao lower bound**: $\text{Var}(\hat{I}_0(x)) \geq \frac{1}{n \mathcal{I}(I_0(x))}$
- **Maximum likelihood estimation**: $\hat{I}_0(x)$ is the maximum likelihood estimator of $I_0(x)$

Note: This summary covers the key points of Chap-10 (10.1 to 10.3.2) in a concise manner, using Markdown format. It is intended to serve as a quick revision guide before exams.
