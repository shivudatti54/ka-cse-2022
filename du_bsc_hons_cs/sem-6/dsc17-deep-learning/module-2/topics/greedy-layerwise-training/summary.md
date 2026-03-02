# Greedy Layerwise Training - Summary

## Key Definitions and Concepts

- **Greedy Layerwise Training:** A training strategy for deep neural networks where each layer is trained individually in sequence, treating each as a standalone autoencoder that learns to reconstruct the previous layer's output, before supervised fine-tuning.

- **Autoencoder:** A neural network trained to reconstruct its input, consisting of an encoder (compressing input to hidden representation) and decoder (reconstructing input from hidden representation).

- **Stacked Denoising Autoencoders (SDAEs):** Deep autoencoders trained greedily where each layer is a denoising autoencoder that learns robust features by reconstructing clean data from corrupted inputs.

- **Deep Belief Networks (DBNs):** Generative models trained greedily using Restricted Boltzmann Machines (RBMs) stacked together.

- **Fine-tuning:** The final supervised phase where all layers are jointly optimized using backpropagation after greedy pretraining.

## Important Formulas and Procedures

The greedy layerwise algorithm:
1. Train layer 1 as autoencoder: minimize ||x - D₁(E₁(x))||²
2. Freeze layer 1, generate representations: h₁ = E₁(x)
3. Train layer 2 on h₁: minimize ||h₁ - D₂(E₂(h₁))||²
4. Repeat for all layers
5. Add output layer and fine-tune all parameters jointly

## Key Points

- Greedy layerwise training was pioneered by Hinton et al. (2006), enabling successful training of very deep networks

- It addresses the vanishing gradient problem by providing good initializations for each layer

- Pretraining is unsupervised, requiring no labeled data—valuable when labels are expensive

- Each layer learns increasingly abstract hierarchical representations of the data

- The freezing mechanism ensures earlier learned representations are not disrupted

- Fine-tuning after pretraining typically yields significant performance improvements

- While less critical today with ReLU and better optimizers, the approach remains important for certain applications

- Stacked autoencoders and DBNs are the primary architectures using this approach

## Common Mistakes to Avoid

1. **Confusing pretraining and fine-tuning:** Remember greedy pretraining is unsupervised, fine-tuning is supervised.

2. **Forgetting to freeze layers:** The key mechanism is freezing—new layers should not modify previously learned representations.

3. **Skipping fine-tuning:** Pretraining alone is rarely sufficient; fine-tuning is essential for optimal performance.

4. **Applying to shallow networks:** Greedy layerwise training is specifically designed for deep networks where traditional training fails.

## Revision Tips

1. Draw the complete architecture diagram of a stacked autoencoder showing encoder-decoder pairs

2. Write out the step-by-step greedy algorithm from memory

3. Explain in one sentence why greedy pretraining helps with vanishing gradients

4. Compare greedy training to end-to-end backpropagation, listing three differences

5. Remember that modern deep learning frameworks make implementation straightforward—focus on understanding the conceptual framework and algorithm