# CNNs for Vision - Summary

## Key Definitions and Concepts

- **Convolution**: Mathematical operation sliding a learnable kernel across input to produce feature maps, providing parameter sharing and translation invariance
- **Receptive Field**: The region in input space affecting a particular neuron output; increases with network depth
- **Feature Maps**: Output of convolving a kernel with input; each kernel learns to detect specific visual patterns
- **Skip Connections**: Identity mappings in ResNet enabling gradient flow in very deep networks
- **Transfer Learning**: Using pretrained model weights as initialization for new tasks, leveraging learned representations

## Important Formulas and Theorems

- **Output Dimension**: $O = \lfloor \frac{I - K + 2P}{S} \rfloor + 1$ where I=input, K=kernel, P=padding, S=stride
- **Parameter Count**: $(K_h \times K_w \times C_{in}) \times C_{out} + C_{out}$ (biases)
- **Receptive Field Growth**: Stack of 3×3 convolutions achieves same receptive field as larger kernels with fewer parameters
- **Effective Receptive Field**: Roughly one-third of theoretical size due to gaussian weighting from successive operations

## Key Points

- CNNs learn hierarchical visual features: edges/textures (early layers) → parts/objects (deep layers)
- LeNet-5 established foundational architecture; AlexNet's 2012 ImageNet win launched deep learning revolution
- VGGNet demonstrated that stacked 3×3 convolutions outperform single larger kernels
- ResNet's residual connections solved the vanishing gradient problem, enabling 100+ layer networks
- Modern architectures optimize accuracy-efficiency tradeoffs through depthwise separable convolutions and compound scaling
- Global Average Pooling reduces overfitting compared to fully connected layers
- Batch normalization accelerates training by normalizing layer inputs; enables higher learning rates
- Data augmentation (random crops, flips, color jittering) provides regularization without additional parameters

## Common Mistakes to Confuse

- Confusing valid padding (output shrinks) with same padding (output preserved)
- Forgetting bias terms when calculating parameter counts
- Equating pooling with strided convolution—pooling is deterministic, convolution is learnable
- Assuming deeper networks always perform better—without skip connections, degradation occurs
- Misunderstanding transfer learning—fine-tuning vs. feature extraction require different learning rates

## Revision Tips

1. Practice dimension calculations until automatic: work through 5-10 examples with different padding/stride combinations
2. Draw architectural diagrams from memory for major networks (LeNet, AlexNet, ResNet)
3. Memorize the key innovation for each architecture year (2012: ReLU/dropout, 2014: 3×3 stacks, 2015: skip connections)
4. Implement a small CNN from scratch in PyTorch/TensorFlow to understand the complete forward/backward pass
5. Review original papers for experimental results—exam questions often ask for specific accuracy improvements or architectural comparisons