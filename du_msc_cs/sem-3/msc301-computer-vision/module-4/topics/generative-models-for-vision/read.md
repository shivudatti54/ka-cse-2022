# Generative Models for Vision

## Introduction
Generative models have revolutionized computer vision by enabling machines to create realistic synthetic data and understand complex data distributions. These models learn the underlying probability distribution of training data to generate new samples with similar characteristics. For MSc CS students, understanding generative models is crucial as they form the foundation for cutting-edge applications like image synthesis, style transfer, and data augmentation.

The importance of generative models extends beyond mere image generation. They address fundamental challenges in unsupervised learning, enable inverse problem solving in computational photography, and facilitate domain adaptation in transfer learning. Recent advances like Stable Diffusion and DALL-E 2 demonstrate their transformative potential in creative AI applications while raising important questions about model interpretability and ethical implications.

From a research perspective, generative models represent an active area combining deep learning, probability theory, and optimization. The field has evolved from traditional methods like Gaussian Mixture Models to modern architectures such as Generative Adversarial Networks (GANs), Variational Autoencoders (VAEs), and Diffusion Models, each offering unique advantages and theoretical foundations.

## Key Concepts

### 1. Generative Adversarial Networks (GANs)
- **Architecture**: Two neural networks (Generator and Discriminator) in adversarial training
- **Objective Function**: Minimax game $\min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{data}}[\log D(x)] + \mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]$
- **Challenges**: Mode collapse, training instability
- **Advanced Variants**: WGAN, StyleGAN, CycleGAN

### 2. Variational Autoencoders (VAEs)
- **Probabilistic Framework**: Latent variable model with encoder $q_\phi(z|x)$ and decoder $p_\theta(x|z)$
- **Evidence Lower Bound (ELBO)**: $\log p(x) \geq \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - D_{KL}(q_\phi(z|x) \parallel p(z))$
- **Reparameterization Trick**: Enables gradient propagation through random variables

### 3. Diffusion Models
- **Forward Process**: Gradual noising $q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t}x_{t-1}, \beta_t\mathbf{I})$
- **Reverse Process**: Learned denoising $p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t,t), \Sigma_\theta(x_t,t))$
- **Score-Based Learning**: Connects to stochastic differential equations

### 4. Autoregressive Models
- **PixelCNN/RNN**: Factorize image distribution as product of conditional distributions
- **Chain Rule**: $p(x) = \prod_{i=1}^n p(x_i|x_1,...,x_{i-1})$

### 5. Normalizing Flows
- **Invertible Transformations**: Learn bijective mapping $f: \mathcal{X} \leftrightarrow \mathcal{Z}$
- **Change of Variables**: $p_X(x) = p_Z(f(x))|\det J_f(x)|$

## Examples

**Example 1: MNIST Digit Generation with GAN**
1. Define Generator: MLP with input noise dimension 100 → 784 output
2. Define Discriminator: CNN with 784 → 1 (real/fake)
3. Alternate training:
   - Update D: $\nabla_{\theta_d} \frac{1}{m}\sum_{i=1}^m [\log D(x^{(i)}) + \log(1-D(G(z^{(i)})))]$
   - Update G: $\nabla_{\theta_g} \frac{1}{m}\sum_{i=1}^m \log D(G(z^{(i)}))$
4. Monitor Fréchet Inception Distance (FID)

**Example 2: Image Inpainting with VAE**
1. Corrupt input image $x$ with mask $M$
2. Encode to latent $z \sim q_\phi(z|x \odot M)$
3. Decode reconstruction $\hat{x} = p_\theta(x|z)$
4. Loss: $\mathbb{E}[\|(x - \hat{x}) \odot (1-M)\|^2] + \beta D_{KL}(q_\phi \parallel p(z))$

**Example 3: High-Resolution Face Generation with Diffusion**
1. Forward process: 1000-step noise schedule
2. Train U-Net to predict noise $\epsilon_\theta(x_t,t)$
3. Reverse sampling using DDPM:
   $x_{t-1} = \frac{1}{\sqrt{\alpha_t}}(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(x_t,t)) + \sigma_t z$

## Exam Tips
1. Understand the fundamental differences between GANs, VAEs, and Diffusion Models
2. Memorize key equations: GAN minimax loss, VAE ELBO, Diffusion objective
3. Be prepared to compare model advantages: GANs (sharp images) vs VAEs (stable training)
4. Study recent architectures like Stable Diffusion and their latent space operations
5. Practice deriving KL divergence terms in VAEs
6. Understand the role of temperature parameters in sampling
7. Review evaluation metrics: FID, Inception Score, Precision/Recall for distributions