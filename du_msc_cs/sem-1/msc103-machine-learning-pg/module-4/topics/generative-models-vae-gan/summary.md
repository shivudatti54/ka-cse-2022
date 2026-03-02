# Generative Models: VAEs and GANs - Summary

## Key Definitions and Concepts
- **ELBO**: Evidence Lower Bound, VAE training objective combining reconstruction and regularization
- **Reparameterization Trick**: Allows gradient flow through random sampling (z = μ + σ⊙ε)
- **Nash Equilibrium**: State where generator can't improve without discriminator changes
- **Fréchet Inception Distance (FID)**: Quantitative measure of generation quality

## Important Formulas and Theorems
- **VAE ELBO**: 𝔼_{q(z|x)}[log p(x|z)] - KL(q(z|x)||p(z))
- **GAN Loss**: min_G max_D 𝔼[log D(x)] + 𝔼[log(1 - D(G(z)))]
- **Wasserstein Loss**: 𝔼[D(x)] - 𝔼[D(G(z))] + λ𝔼[(||∇D(ẑ)||₂ - 1)²]
- **KL Divergence**: KL(p||q) = ∫ p(x) log(p(x)/q(x)) dx

## Key Points
- VAEs enable principled uncertainty estimation but suffer from blurry samples
- GANs produce sharp outputs but lack explicit density estimation
- Modern GAN stabilization techniques: Spectral normalization, TTUR, R1 regularization
- Disentanglement metrics (β-VAE score) quantify interpretable latent spaces
- Diffusion models combine VAE-like likelihoods with GAN-level quality
- Applications: Data augmentation, anomaly detection, style transfer
- Evaluation requires both quantitative metrics and human assessment

## Common Mistakes to Avoid
- Confusing VAE's latent variables with GAN's noise vectors
- Neglecting gradient clipping in WGAN implementations
- Using BCE loss without considering label smoothing
- Forgetting to set requires_grad=False during generator updates
- Misinterpreting FID scores without class balance consideration

## Revision Tips
1. Create flashcards for key formulas (ELBO, WGAN loss)
2. Practice deriving ELBO from KL divergence step-by-step
3. Implement a simple GAN/VAE in PyTorch with MNIST dataset
4. Study ablation studies from original papers (e.g., effect of β in β-VAE)
5. Memorize 3 key advantages/disadvantages of each model type

Length: 400-800 words