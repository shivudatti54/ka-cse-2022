# Deep CNNs: LeNet and AlexNet - Summary

## Key Definitions and Concepts

- **Convolutional Neural Network (CNN)**: A deep learning architecture designed for processing grid-structured data (like images), using convolutional layers that apply learnable filters to detect local patterns through parameter sharing and local connectivity.

- **Feature Map**: The output of a convolutional layer—a 2D array of values produced by applying one filter across the input, representing activation of specific patterns (edges, textures, shapes).

- **Receptive Field**: The region of the input image that influences a particular neuron's output. Deeper layers have larger receptive fields, capturing more global features.

- **ReLU (Rectified Linear Unit)**: Activation function f(x) = max(0,x), introduced in AlexNet to address vanishing gradients and enable faster training.

- **Dropout**: A regularization technique where randomly selected neurons are ignored during training (with probability p=0.5 in AlexNet), preventing co-adaptation of neurons and reducing overfitting.

- **Data Augmentation**: Artificially expanding training data through transformations like random crops, horizontal flips, and color variations—critical for training deep networks like AlexNet.

## Important Formulas and Theorems

- **Convolution Output Size**: $\left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$
  - W = input width/height, K = kernel size, P = padding, S = stride

- **Pooling Output Size**: Same formula as convolution with no padding typically used

- **Parameters per Convolutional Layer**: $(K \times K \times C_{in} + 1) \times N_{filters}$
  - $C_{in}$ = input channels, +1 accounts for bias per filter

- **LeNet-5 Total Parameters**: ~60,000
- **AlexNet Total Parameters**: ~60 million

## Key Points

- LeNet-5 (1998) was the first successful CNN for handwritten digit recognition, demonstrating that backpropagation could train deep networks with 7 layers and ~60K parameters.

- AlexNet (2012) won ILSVRC with 15.3% top-5 error (vs 26.2% runner-up), launching the deep learning revolution by combining 8 layers, 60M parameters, ReLU activation, dropout, and GPU training.

- The key architectural components—convolution for feature extraction, pooling for spatial reduction and invariance, and fully connected layers for classification—remain fundamental in modern CNNs.

- Both architectures demonstrate hierarchical feature learning: early layers detect edges/textures, middle layers combine these into parts, and later layers recognize complete objects.

- Parameter sharing in convolution dramatically reduces parameters compared to fully connected networks (LeNet's 60K vs a fully connected equivalent requiring millions).

- Data augmentation and dropout (introduced in AlexNet) are essential regularization techniques that enable training of very deep networks without severe overfitting.

## Common Mistakes to Avoid

- **Forgetting input channels in parameter calculation**: When calculating convolution parameters, remember to multiply by the number of input channels (3 for RGB images).

- **Confusing padding effects**: No padding (valid padding) reduces spatial dimensions; same padding preserves dimensions. Many students forget to account for padding in output calculations.

- **Ignoring bias terms**: Each filter has one bias term, not just weight parameters. This is a common error in parameter count calculations.

- **Misunderstanding pooling**: Pooling reduces spatial dimensions but keeps depth constant. It does not change the number of channels.

- **Confusing feature maps with neurons**: Feature maps are 2D outputs; each position in a feature map corresponds to one neuron activated by the convolution operation.

## Revision Tips

1. **Draw from memory**: Practice drawing both architectures layer-by-layer with specifications (filter sizes, output dimensions, parameters) from memory.

2. **Calculate manually**: Work through 5-10 convolution and pooling dimension problems until the formulas become automatic.

3. **Create comparison tables**: Prepare a structured table comparing LeNet vs AlexNet across 8-10 dimensions—this is an exam favorite.

4. **Understand "why" not just "what"**: For each innovation (ReLU, dropout, data augmentation), be able to explain the specific problem it solves.

5. **Connect to modern applications**: Link these foundational architectures to ResNet, VGG, YOLO, and transfer learning to demonstrate comprehensive understanding.