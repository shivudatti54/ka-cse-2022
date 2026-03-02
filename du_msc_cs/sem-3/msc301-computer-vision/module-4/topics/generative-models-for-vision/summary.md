# Generative Models for Vision - Summary

## Key Definitions and Concepts
- **GAN**: Adversarial framework with generator/discriminator networks
- **VAE**: Probabilistic autoencoder with latent space regularization
- **Diffusion Model**: Iterative denoising process based on thermodynamic principles
- **ELBO**: Evidence Lower Bound used for variational inference
- **FID**: Fréchet Inception Distance for quality evaluation

## Important Formulas and Theorems
- **GAN Objective**: $\min_G \max_D \mathbb{E}[\log D(x)] + \mathbb{E}[\log(1-D(G(z)))]$
- **VAE ELBO**: $\mathcal{L}(\theta,\phi) = \mathbb{E}_{q_\phi}[\log p_\theta(x|z)] - D_{KL}(q_\phi(z|x)\parallel p(z))$
- **Diffusion Loss**: $\mathbb{E}_{t,x_0,\epsilon}\left[\|\epsilon - \epsilon_\theta(x_t,t)\|^2\right]$
- **Change of Variables**: $\log p(x) = \log p(z) + \log|\det J_{f^{-1}}(x)|$

## Key Points
- GANs excel at sharp image generation but suffer from training instability
- VAEs provide probabilistic latent spaces but may produce blurry samples
- Diffusion models achieve state-of-the-art quality through iterative refinement
- Autoregressive models offer precise likelihood computation but are sequential
- Normalizing flows enable exact likelihood evaluation with invertible transforms
- Evaluation requires both qualitative assessment and quantitative metrics
- Current research focuses on efficiency, controllability, and 3D generation

## Common Mistakes to Avoid
- Confusing VAE's encoder with standard autoencoders
- Neglecting the importance of noise schedules in diffusion models
- Overlooking mode collapse in GAN implementations
- Misinterpreting ELBO as exact likelihood rather than lower bound

## Revision Tips
1. Create comparative tables of model architectures/advantages
2. Practice deriving ELBO from KL divergence
3. Implement simple GAN/VAE in PyTorch/TensorFlow
4. Study seminal papers: "Generative Adversarial Nets" (Goodfellow 2014), "DDPM" (Ho 2020)
5. Explore Hugging Face's Diffusers library for practical implementations