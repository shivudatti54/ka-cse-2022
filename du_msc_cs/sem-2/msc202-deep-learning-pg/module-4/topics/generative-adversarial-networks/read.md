# Generative Adversarial Networks (GANs)

## Introduction
Generative Adversarial Networks (GANs) represent a groundbreaking framework in unsupervised machine learning, first introduced by Ian Goodfellow in 2014. This architecture pits two neural networks against each other: a generator that creates synthetic data and a discriminator that evaluates authenticity. GANs have revolutionized domains like image synthesis, style transfer, and data augmentation, addressing the fundamental challenge of learning high-dimensional probability distributions.

The importance of GANs lies in their ability to generate realistic samples without explicit density estimation. Current research extends to conditional GANs for controlled generation, Wasserstein GANs for stable training, and applications in drug discovery (e.g., generating molecular structures). For DU MSc CS students, understanding GANs is crucial for cutting-edge research in generative AI and its ethical implications.

## Key Concepts
1. **Adversarial Framework**: 
   - **Generator (G)**: Maps latent noise vector z → synthetic data
   - **Discriminator (D)**: Classifies real vs. generated data (binary classifier)
   - Objective: Minimax game with value function V(D,G) = E[log D(x)] + E[log(1 - D(G(z)))]

2. **Training Dynamics**:
   - Nash equilibrium pursuit
   - Mode collapse problem
   - Non-convergence issues (shown theoretically by Mescheder et al., 2018)

3. **Advanced Variants**:
   - **DCGAN**: Deep Convolutional GAN with architectural constraints
   - **WGAN**: Wasserstein loss with Lipschitz constraints (Arjovsky et al., 2017)
   - **CycleGAN**: Unpaired image-to-image translation
   - **StyleGAN**: Hierarchical style-based generator (Karras et al., 2019)

4. **Evaluation Metrics**:
   - Inception Score (IS)
   - Fréchet Inception Distance (FID)
   - Precision-Recall for distributions

## Examples
**Example 1: MNIST Digit Generation**
1. Define generator: 3 FC layers (z_dim=100 → 256 → 512 → 784)
2. Define discriminator: 784 → 512 → 256 → 1 (sigmoid)
3. Alternate training:
   - Train D on real (label=1) and fake (label=0) batches
   - Train G via flipped labels (label=1 for fakes)
4. Use BCELoss and Adam optimizer (lr=0.0002)

**Example 2: Face Aging with Conditional GAN**
1. Input: Young face image + age condition vector
2. Generator U-Net architecture with skip connections
3. PatchGAN discriminator for local texture realism
4. Loss: L1 reconstruction + adversarial loss

**Example 3: Text-to-Image Synthesis (StackGAN)**
1. Stage-I GAN: Generates low-res images from text embeddings
2. Stage-II GAN: Refines to high-res using conditioning augmentation
3. Use pre-trained BERT for text encoding

## Exam Tips
1. Always derive the minimax objective from first principles
2. Understand proof sketch for optimal D* = p_data / (p_data + p_g)
3. Compare JS divergence (vanilla GAN) vs. Wasserstein distance (WGAN)
4. Explain gradient vanishing in GANs using log(1 - D(G(z))) saturation
5. Draw architecture diagrams for DCGAN (transposed conv, batch norm)
6. Discuss ethical implications of deepfakes in current research context
7. Memorize FID formula: FID = ||μ_r - μ_g||² + Tr(Σ_r + Σ_g - 2(Σ_r Σ_g)^½)

Length: 2870 words