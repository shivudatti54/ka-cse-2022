# Autoencoders — Quick Revision Summary

## Introduction
Autoencoders are **unsupervised neural networks** that learn efficient data codings by forcing the network to reconstruct input data through a compressed bottleneck representation. They are a fundamental deep learning architecture used for representation learning and dimensionality reduction.

---

## Key Concepts

### Architecture
- **Encoder**: Compresses input data into a latent-space representation (bottleneck)
- **Latent Space (Bottleneck)**: Compressed feature representation capturing essential information
- **Decoder**: Reconstructs data from the latent representation back to original dimension

### Working Principle
- Learns to copy input to output while discovering useful features
- Goal: Minimize **reconstruction error** (difference between input and output)
- Forces the network to prioritize important features

### Types of Autoencoders

- **Undercomplete**: Latent dimension < input dimension (prevents overfitting)
- **Overcomplete**: Latent dimension > input dimension (requires regularization)
- **Denoising Autoencoder (DAE)**: Learns to reconstruct clean data from noisy input
- **Variational Autoencoder (VAE)**: Generates new samples using probabilistic latent space
- **Sparse Autoencoder**: Adds sparsity constraint to latent neurons
- **Contractive Autoencoder**: Penalizes sensitivity to input variations

### Loss Function
- **Reconstruction Loss**: L(x, f(g(x))) where g = encoder, f = decoder
- Common metrics: Mean Squared Error (MSE), Binary Cross-Entropy

---

## Applications (As per DU Syllabus)

- **Dimensionality Reduction**: Feature extraction and visualization
- **Anomaly Detection**: Identifying outliers in data
- **Image Denoising**: Removing noise from images
- **Data Generation**: Creating new samples (especially VAE)
- **Recommendation Systems**: Learning user/item embeddings

---

## Important Notes for Exam

- Autoencoders are **self-supervised** (input = target)
- VAEs use **KL-divergence** loss for latent space regularization
- The bottleneck forces **dimensionality reduction** implicitly
- They learn **compressed representations** without labeled data

---

## Conclusion
Autoencoders are powerful unsupervised learning models essential for understanding representation learning in deep learning. Their ability to compress and reconstruct data makes them valuable for both feature learning and generative tasks, forming a core topic in the Delhi University B.Sc. (Hons) Computer Science NEP 2024 UGCF syllabus.