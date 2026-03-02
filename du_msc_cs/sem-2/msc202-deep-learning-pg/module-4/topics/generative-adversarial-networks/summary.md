# Generative Adversarial Networks - Summary

## Key Definitions and Concepts
- **Adversarial Training**: Competing networks (G and D) through minimax game
- **Nash Equilibrium**: State where neither player can improve unilaterally
- **Mode Collapse**: Generator produces limited varieties of samples
- **Wasserstein Distance**: Earth-Mover distance used in WGAN

## Important Formulas and Theorems
- **Minimax Loss**: min_G max_D V(D,G) = E[log D(x)] + E[log(1 - D(G(z)))]
- **Optimal Discriminator**: D*(x) = p_data(x) / [p_data(x) + p_g(x)]
- **WGAN Loss**: L = E[D(x)] - E[D(G(z))] + λ·GP (Gradient Penalty)
- **FID Score**: FID = ||μ_r - μ_g||² + Tr(Σ_r + Σ_g - 2(Σ_r Σ_g)^½)

## Key Points
- GANs require careful balancing of generator/discriminator capacities
- Wasserstein GANs enable stable training via Lipschitz constraints
- Conditional GANs enable controlled generation through auxiliary inputs
- Evaluation metrics remain an open research challenge
- GANs have been extended to discrete domains (e.g., text) via reinforcement learning
- Ethical concerns include deepfakes and copyright infringement
- Current research focuses on energy-based models and diffusion-GAN hybrids

## Common Mistakes to Avoid
- Using BatchNorm in both G and D (causes oscillation)
- Ignoring label smoothing and noise injection for stability
- Confusing JS divergence with Wasserstein metrics
- Overlooking the importance of learning rate scheduling

## Revision Tips
1. Practice deriving the optimal discriminator proof step-by-step
2. Compare loss curves of vanilla GAN vs WGAN during training
3. Implement a DCGAN on CIFAR-10 using spectral normalization
4. Study ablation studies from StyleGAN2 paper (CVPR 2020)
5. Explore HuggingFace's Diffusers library for GAN variants

Length: 720 words