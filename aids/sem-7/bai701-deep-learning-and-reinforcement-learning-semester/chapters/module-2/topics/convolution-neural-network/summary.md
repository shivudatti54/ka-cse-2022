# Convolution Neural Network - Summary

## Key Definitions and Concepts

- CONVOLUTION NEURAL NETWORK (CNN): A deep learning architecture specifically designed for processing grid-like data (especially images) that uses learnable filters to detect spatial features hierarchically.

- CONVOLUTION OPERATION: The mathematical process of applying a kernel (filter) across an input matrix by sliding it and computing element-wise products followed by summation to produce feature maps.

- KERNEL (FILTER): A small learnable matrix (typically 3×3 or 5×5) that detects specific patterns in the input when convolved across the image.

- STRIDE: The number of pixels the kernel moves during convolution at each step, controlling the output spatial dimensions.

- PADDING: Border of zeros added around input to maintain spatial dimensions or enable deeper networks without excessive shrinkage.

- RECEPTIVE FIELD: The region in the input image that affects a particular neuron's output in deeper network layers.

## Important Formulas and Theorems

Output dimension after convolution:
Output = floor((Input - Kernel + 2×Padding)/Stride) + 1

Number of parameters in Conv layer:
(K_h × K_w × C_in + 1) × C_out

ReLU activation: f(x) = max(0, x)

## Key Points

- CNNs exploit spatial locality—neighboring pixels are more related than distant pixels, reducing parameters compared to fully connected networks.

- The convolution operation with learnable kernels automatically discovers useful features from data without manual feature engineering.

- CNN architectures build hierarchical representations: early layers detect edges and textures, deeper layers combine these to recognize complex objects.

- Max pooling provides translational invariance by selecting maximum activations within local regions.

- Stride and padding are crucial hyperparameters affecting output dimensions, computational cost, and information retention.

- Fully connected layers at the network end perform high-level classification by combining features learned by convolutional layers.

- Receptive fields expand as information flows through layers, giving deeper neurons broader spatial context.

## Common Mistakes to Avoid

- Confusing valid padding (no padding, shrinks output) with same padding (maintains input dimensions with stride 1).

- Forgetting to add bias terms when calculating convolution layer parameters.

- Using kernel sizes that are too large without sufficient data, leading to overfitting.

- Applying too much pooling, which loses spatial information necessary for precise localization tasks.

## Revision Tips

- Practice dimension calculations repeatedly until they become automatic—these appear in every exam.

- Draw and trace data flow through a simple CNN, labeling dimensions at each layer to build intuition.

- Memorize the purposes of each layer type and be able to explain why each is necessary.

- Review real-world CNN applications to connect theoretical concepts with practical impact.