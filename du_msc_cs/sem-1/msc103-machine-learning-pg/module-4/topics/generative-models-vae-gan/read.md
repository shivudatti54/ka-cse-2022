# Generative Models: VAEs and GANs

## Introduction
Generative models are machine learning frameworks that learn to model data distributions, enabling the creation of new samples resembling training data. Two landmark architectures in this domain are Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs). VAEs employ probabilistic reasoning to learn latent representations, while GANs use adversarial training between generator and discriminator networks.

These models have revolutionized synthetic data generation with applications ranging from image synthesis (StyleGAN for photorealistic faces) to drug discovery (molecular generation). VAEs excel at structured latent spaces and Bayesian inference, while GANs produce higher-quality samples but face challenges like mode collapse. Current research focuses on hybrid architectures (e.g., VQ-GAN), improved training stability, and applications in multimodal generation.

## Key Concepts
1. **Variational Autoencoders (VAEs)**
   - **Encoder**: Maps input data to parameters of latent distribution (μ, σ)
   - **Latent Space**: Low-dimensional probabilistic representation (q(z|x))
   - **Decoder**: Reconstructs data from latent samples (p(x|z))
   - **ELBO Objective**: Evidence Lower Bound combining reconstruction loss and KL divergence:
     ELBO = 𝔼[log p(x|z)] - KL(q(z|x) || p(z))

2. **GAN Architecture**
   - **Generator (G)**: Transforms noise vector z to data space
   - **Discriminator (D)**: Distinguishes real vs generated samples
   - **Minimax Game**: min_G max_D 𝔼[log D(x)] + 𝔼[log(1 - D(G(z)))]
   - **Advanced Variants**: WGAN (Wasserstein loss), Conditional GANs, StyleGAN

3. **Critical Theoretical Aspects**
   - Mode collapse in GANs
   - Posterior collapse in VAEs
   - Nash equilibrium in adversarial training
   - Disentangled representations (β-VAE)

## Examples

**Example 1: VAE for MNIST Generation**
1. Encoder: CNN mapping 28x28 image to μ, logσ² ∈ ℝ^20
2. Sample z ∼ N(μ, σ²I) using reparameterization trick
3. Decoder: Transpose CNN mapping z to 28x28 reconstruction
4. Loss: BCE(reconstruction, original) + 0.5 * Σ(σ² + μ² - 1 - logσ²)

**Example 2: DCGAN for Face Generation**
1. Generator: 
   Input: z ∈ ℝ^100 → FC → 4x4x512 → Transposed Conv layers → 64x64x3
2. Discriminator:
   CNN with LeakyReLU → Final sigmoid
3. Train with alternating Adam updates (lr=0.0002, β1=0.5)

**Example 3: Solving Mode Collapse**
Problem: GAN generates limited varieties of digits
Solution: Implement Mini-batch Discrimination [Salimans et al. 2016]
- Compute pairwise distances in feature space
- Append statistical features to discriminator input
- Forces generator to produce diverse samples

## Exam Tips
1. Always derive ELBO from KL divergence: KL(q(z|x)||p(z|x)) = log p(x) - ELBO
2. For GANs, understand the implications of JS vs Wasserstein distances
3. Compare VAE/GAN tradeoffs: VAE gives explicit likelihoods but blurry samples; GANs have sharper outputs but unstable training
4. Recent developments to mention: Diffusion Models, Transformer-based generators (e.g., DALL-E)
5. When sketching architectures, label dimensions at each layer
6. For mathematical proofs, practice deriving VAE reparameterization gradient
7. Case study preparation: Memorize 2-3 landmark papers (e.g., Original GAN, β-VAE, StyleGAN2)

Length: 1500-3000 words, MSc CS (research-oriented) postgraduate level