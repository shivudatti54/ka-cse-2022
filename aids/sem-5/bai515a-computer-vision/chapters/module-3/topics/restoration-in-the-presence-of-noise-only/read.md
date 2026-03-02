# **Restoration in the Presence of Noise Only**

## **1. Introduction**

Image restoration is a crucial task in computer vision that involves removing degradations from an image to restore its original state. In this topic, we will focus on the restoration of images in the presence of noise only. Noise can be in the form of random fluctuations or patterns that can degrade the quality of an image.

## **2. Causes of Noise in Images**

- **Random Noise**: Random fluctuations in pixel values that can be represented by a probability distribution.
- **Gaussian Noise**: A type of random noise with a Gaussian distribution.
- **Salt and Pepper Noise**: A type of noise that consists of random black and white pixels.
- **Stationary Noise**: Noise that has a constant probability distribution and remains the same over time.

## **3. Types of Noise Models**

- **Additive Noise**: Noise that is added to the original image.
- **Multiplicative Noise**: Noise that is multiplied with the original image.

## **4. Mathematical Model of Image Restoration**

The mathematical model of image restoration can be represented by the following equation:

I(x) = f(x) + n(x)

where:

- I(x) is the restored image.
- f(x) is the original image.
- n(x) is the noise.

## **5. Denoising Techniques**

- **Filtering**: Filtering is one of the most popular denoising techniques. It involves applying a filter to the image to remove the noise.
  - **Low-Pass Filter**: A low-pass filter removes high-frequency components of the image.
  - **High-Pass Filter**: A high-pass filter removes low-frequency components of the image.
  - **Median Filter**: A median filter replaces each pixel value with the median value of neighboring pixels.
  - **Gaussian Filter**: A Gaussian filter applies a Gaussian distribution to the image to remove noise.
- **Statistical Model-based Methods**: Statistical model-based methods use probability distributions to model the noise and restore the image.
  - **Bayesian Estimation**: Bayesian estimation uses Bayes' theorem to estimate the original image.
  - **Maximum A Posteriori Estimation**: Maximum a posteriori estimation uses the maximum a posteriori estimate to restore the image.
- **Machine Learning-based Methods**: Machine learning-based methods use algorithms to learn the noise patterns and restore the image.
  - **Autoencoders**: Autoencoders use a neural network to learn the noise patterns.
  - **Convolutional Neural Networks**: Convolutional neural networks use a neural network to learn the noise patterns.

## **6. Evaluation Metrics**

- **Mean Squared Error (MSE)**: MSE measures the difference between the restored image and the original image.
- **Peak Signal-to-Noise Ratio (PSNR)**: PSNR measures the ratio of the maximum possible power of a signal to the power of corrupting noise.
- **Structural Similarity Index Measure (SSIM)**: SSIM measures the similarity between the restored image and the original image.

## **7. Conclusion**

Restoration in the presence of noise only is an essential task in computer vision. Different denoising techniques have been developed to remove noise from images. Evaluation metrics are used to measure the performance of denoising techniques. This study material provides a comprehensive overview of the topic and can be used as a reference for researchers and students.
