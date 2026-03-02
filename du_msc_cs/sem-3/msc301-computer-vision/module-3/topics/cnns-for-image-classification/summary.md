# CNNs for Image Classification - Summary

## Key Definitions and Concepts
- **Convolution**: Element-wise multiplication + summation between kernel and input patch
- **Receptive Field**: Input region affecting a particular neuron
- **Stride**: Step size for kernel traversal
- **Feature Map**: Activation output from a convolutional filter
- **Transfer Learning**: Reusing pre-trained networks for new tasks

## Important Formulas and Theorems
- Convolution Operation: 
  $$(I * K)[i,j] = \sum_{m}\sum_{n} I[i-m, j-n] K[m, n]$$
- ReLU: $f(x) = \max(0, x)$
- Cross-Entropy Loss: 
  $$L = -\frac{1}{N}\sum_{i=1}^N \sum_{c=1}^C y_{i,c} \log(p_{i,c})$$
- Softmax: 
  $$p_i = \frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}$$

## Key Points
- CNNs exploit spatial locality and translation invariance
- Depthwise separable convolutions reduce parameters (MobileNet)
- Residual connections (ResNet) solve vanishing gradient problem
- Global Average Pooling replaces FC layers in modern architectures
- Data leakage in medical imaging requires strict patient-wise splits
- Vision Transformers use patch embeddings instead of convs
- SHAP and LIME methods explain CNN decisions

## Common Mistakes to Avoid
- Using small kernel sizes (1×1) in initial layers → loses spatial context
- Ignoring batch normalization leads to unstable training
- Pooling too aggressively → loss of spatial resolution
- Not using pretrained models when data is limited

## Revision Tips
1. Practice calculating output dimensions: 
   $$W_{out} = \frac{W_{in} - K + 2P}{S} + 1$$
2. Memorize ResNet/VGG architectures diagrams
3. Study attention mechanisms in CNN literature (2020+ papers)
4. Implement Grad-CAM from scratch using PyTorch

Length: 650 words