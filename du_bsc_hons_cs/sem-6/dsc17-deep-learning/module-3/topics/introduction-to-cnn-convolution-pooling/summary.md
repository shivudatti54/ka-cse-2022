# CNN: Convolution and Pooling - Summary

## Key Definitions and Concepts

- **Convolutional Neural Network (CNN)**: A deep learning architecture designed for processing grid-like data (images) using localized connections and shared weights.
- **Convolution**: Mathematical operation combining input with a learnable kernel to produce a feature map that highlights specific patterns.
- **Kernel/Filter**: A small weight matrix (typically 3×3 or 5×5) that slides across the input to detect features like edges, textures, or shapes.
- **Feature Map**: The output of convolving an input with a kernel, representing detected features at each spatial location.
- **Stride**: The step size by which the kernel moves across the input; higher stride produces smaller output.
- **Padding**: Adding border pixels (usually zeros) around input to preserve spatial dimensions and capture corner features.
- **Receptive Field**: The region of input that influences a particular output pixel; increases with network depth.
- **Pooling**: Downsampling operation that reduces spatial dimensions while retaining important information.

## Important Formulas and Theorems

- **Output Size Formula**: Output = floor((W - K + 2P) / S) + 1
  - W = input size, K = kernel size, P = padding, S = stride
  
- **Convolution Operation**: Output(i,j) = Σ Σ I(i+m, j+n) × K(m,n)

- **Number of Parameters in Conv Layer**: (K_h × K_w × C_in + 1) × C_out
  - C_in = input channels, C_out = output channels

- **Receptive Field Growth**: Each layer multiplies the receptive field; with 3×3 kernels, stacking N layers gives effective receptive field of (2N+1) × (2N+1)

## Key Points

1. CNNs exploit spatial structure unlike fully-connected networks, reducing parameters dramatically.

2. Early CNN layers detect low-level features (edges, corners); deeper layers detect complex patterns (objects, faces).

3. Padding="same" preserves input dimensions; padding="valid" reduces dimensions.

4. Max pooling is preferred for most tasks as it retains the strongest activations.

5. 1×1 convolutions are used for channel dimension reduction and cross-channel feature learning.

6. Stride=2 is often used instead of pooling for downsampling in modern architectures.

7. Global average pooling eliminates fully-connected layers, reducing overfitting.

## Common Mistakes to Avoid

1. **Confusing kernel and filter**: A kernel is a single weight matrix; a filter is a collection of kernels producing one output channel.

2. **Forgetting padding effect**: Without padding, spatial dimensions shrink rapidly, limiting network depth.

3. **Incorrect output size calculation**: Always use floor division; not all input/kernel/stride combinations produce integer outputs.

4. **Over-padding**: Excessive padding introduces irrelevant zero values, potentially diluting important features.

5. **Ignoring channel dimensions**: Remember that convolutions operate on all input channels simultaneously.

## Revision Tips

1. Practice manual convolution calculations with different kernel sizes and strides until comfortable with the formula.

2. Visualize how 3×3 kernels are equivalent to larger receptive fields when stacked (e.g., two 3×3 layers = one 5×5 receptive field).

3. Draw feature map dimension changes through sample CNN architectures to build intuition.

4. Memorize the output size formula and practice with various input/kernel/padding/stride combinations.

5. Review famous CNN architectures (LeNet, AlexNet, VGG) to see how convolution and pooling are combined in practice.