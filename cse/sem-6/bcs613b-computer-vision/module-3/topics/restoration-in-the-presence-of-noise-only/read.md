# **Restoration in the Presence of Noise Only**

## **Introduction**

Image restoration is a crucial process in computer vision that aims to recover the original image from degraded or distorted images. In this topic, we will focus on restoration in the presence of noise only, which is one of the most common types of noise in image degradation.

## **Types of Noise**

- **Gaussian Noise**: Also known as additive white Gaussian noise, this type of noise is characterized by a Gaussian distribution with a mean of 0 and a standard deviation that is proportional to the amplitude of the noise.
- **Additive Noise**: This type of noise is added to an image to degrade it. It can be represented as $I(x) + g(x)$, where $I(x)$ is the original image and $g(x)$ is the noise.
- **Subtractive Noise**: This type of noise is subtracted from an image to degrade it. It can be represented as $I(x) - g(x)$.

## **Mathematical Model**

The mathematical model for image restoration in the presence of noise only can be represented as:

$$
\begin{align*}
I(x) = f(x) + g(x)\\
g(x) & \sim N(0, \sigma^2)
\end{align*}
$$

where $I(x)$ is the original image, $f(x)$ is the forward model (which describes the degradation process), $g(x)$ is the noise, and $\sigma^2$ is the variance of the noise.

## **Restoration Methods**

### 1. **Wiener Filter**

The Wiener filter is a widely used method for image restoration in the presence of Gaussian noise. The filter is based on the Wiener-Khinchin theorem, which states that the optimal filter for removing noise from an image is the one that minimizes the mean squared error between the restored image and the original image.

The Wiener filter is represented as:

$$H(x) = \frac{f^{\dagger}(x)}{f^{\dagger}(x) + \frac{\sigma^2}{\lambda}}$$

where $f^{\dagger}(x)$ is the Wiener filter kernel, $\sigma^2$ is the variance of the noise, and $\lambda$ is a regularization parameter.

### 2. **Maximum a Posteriori (MAP) Estimation**

MAP estimation is a method for image restoration that uses Bayes' theorem to estimate the original image. The MAP estimate is the one that maximizes the posterior probability of the original image given the observed image.

The MAP estimate is represented as:

$$
\begin{align*}
p(y|I) & \propto p(I|y) p(y)\\
\hat{I} & = \arg\max_{I} p(I|y)
\end{align*}
$$

where $y$ is the observed image, $I$ is the original image, and $p(y|I)$ is the likelihood of the observed image given the original image.

## **Advantages and Disadvantages**

### Advantages:

- The Wiener filter is a simple and efficient method for image restoration.
- The MAP estimation method can be implemented using Markov chain Monte Carlo (MCMC) algorithms, which can be useful for large-scale image restoration problems.

### Disadvantages:

- The Wiener filter assumes a Gaussian distribution of the noise, which may not be true in all cases.
- The MAP estimation method can be computationally expensive, especially for large-scale image restoration problems.

## **Conclusion**

Image restoration in the presence of noise only is a crucial problem in computer vision. The Wiener filter and MAP estimation methods are two widely used methods for image restoration, each with its advantages and disadvantages. Understanding the mathematical models and algorithms behind these methods is essential for developing effective image restoration techniques.

**Key Concepts:**

- Image restoration
- Noise models
- Wiener filter
- Maximum a Posteriori (MAP) estimation
- Gaussian noise
- Additive noise
- Subtractive noise

**Example:**

Consider the following image degradation model:

$$I(x) = f(x) + g(x)$$

where $I(x)$ is the original image, $f(x)$ is the forward model, and $g(x)$ is the noise. The noise is represented as a Gaussian distribution with a mean of 0 and a standard deviation of 1.

Suppose we want to use the Wiener filter to restore the image. The Wiener filter kernel is represented as:

$$H(x) = \frac{f^{\dagger}(x)}{f^{\dagger}(x) + \frac{\sigma^2}{\lambda}}$$

where $\sigma^2$ is the variance of the noise and $\lambda$ is a regularization parameter.

To implement the Wiener filter, we need to estimate the forward model $f(x)$ and the noise variance $\sigma^2$. We can use the Maximum a Posteriori (MAP) estimation method to estimate the original image $\hat{I}$.

The MAP estimate is represented as:

$$
\begin{align*}
p(y|I) & \propto p(I|y) p(y)\\
\hat{I} & = \arg\max_{I} p(I|y)
\end{align*}
$$

where $y$ is the observed image and $p(y|I)$ is the likelihood of the observed image given the original image.

Once we have estimated the original image $\hat{I}$, we can use it to restore the image.

**Code:**

Here is some sample code in Python that demonstrates the Wiener filter and MAP estimation methods:

```python
import numpy as np
from scipy import ndimage

# Define the forward model
def f(x):
 return x + np.random.normal(0, 1, size=x.shape)

# Define the noise model
def g(x):
 return np.random.normal(0, 1, size=x.shape)

# Define the Wiener filter kernel
def h(x, lambda_param):
 return (np.linalg.inv(x + lambda_param)) @ x

# Define the MAP estimation method
def mp_map_estimate(y, lambda_param):
 # Estimate the forward model
 f_est = np.linalg.inv(lambda_param) @ y

 # Estimate the noise variance
 sigma2_est = np.var(y)

 # Estimate the original image
 I_est = f_est - g_est

 return I_est

# Simulate an image degradation model
x = np.random.uniform(-10, 10, size=(100, 100))
y = f(x) + g(x)

# Apply the Wiener filter
h_filter = h(x, lambda_param=0.1)
I_est_wiener = h_filter @ y

# Apply the MAP estimation method
I_est_map = mp_map_estimate(y, lambda_param=0.1)

print("Wiener filter estimate:", I_est_wiener)
print("MAP estimation estimate:", I_est_map)
```

Note that this is just a simple example, and in practice, you may need to use more advanced techniques to estimate the forward model, noise variance, and regularization parameter.
