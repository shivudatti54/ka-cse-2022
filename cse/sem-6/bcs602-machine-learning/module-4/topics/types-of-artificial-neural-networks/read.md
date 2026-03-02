# Types of Artificial Neural Networks

## Introduction

Artificial Neural Networks come in many architectures, each designed for specific types of problems. Understanding the different types, their structures, and suitable applications is essential for choosing the right approach for any given ML task.

## Classification of Neural Networks

Neural networks can be classified based on:

1. **Connection pattern**: Feedforward vs. Recurrent
2. **Learning paradigm**: Supervised vs. Unsupervised vs. Reinforcement
3. **Depth**: Shallow (1-2 layers) vs. Deep (many layers)
4. **Topology**: Fully connected, convolutional, attention-based

## Feedforward Neural Networks (FNN)

### Single-Layer Perceptron

- Simplest neural network: input layer directly connected to output layer
- No hidden layers
- Can only solve linearly separable problems
- Limited to simple classification tasks

### Multilayer Perceptron (MLP)

- One or more hidden layers between input and output
- Fully connected: every neuron connects to every neuron in the next layer
- Uses backpropagation for training
- Universal approximation theorem: can approximate any continuous function

**Architecture**: Input Layer → Hidden Layer(s) → Output Layer

**Applications**: General classification and regression, tabular data, function approximation

### Key Properties

- Information flows in one direction only (input to output)
- No feedback loops or cycles
- Fixed-size input and output

## Convolutional Neural Networks (CNN)

### Architecture

- **Convolutional layers**: Apply learnable filters/kernels to detect features
- **Pooling layers**: Reduce spatial dimensions (max pooling, average pooling)
- **Fully connected layers**: Final classification/regression
- **Activation**: ReLU typically used between layers

### Key Concepts

- **Weight sharing**: Same filter is applied across the entire input
- **Local connectivity**: Each neuron connects to a small region of the input
- **Translation invariance**: Recognizes features regardless of position
- **Hierarchical features**: Early layers detect edges, later layers detect complex patterns

### Applications

- Image classification (ImageNet, medical imaging)
- Object detection (YOLO, Faster R-CNN)
- Image segmentation
- Video analysis
- Some text classification tasks

## Recurrent Neural Networks (RNN)

### Architecture

- Contains feedback connections (loops)
- Maintains a hidden state that serves as memory
- Processes sequences one element at a time
- Same weights applied at each time step

### Mathematical Formulation

hₜ = f(W_hh · hₜ₋₁ + W_xh · xₜ + b_h)
yₜ = g(W_hy · hₜ + b_y)

### Problems with Vanilla RNNs

- **Vanishing gradient**: Gradients diminish over long sequences, losing long-term dependencies
- **Exploding gradient**: Gradients grow uncontrollably

### Applications

- Natural language processing (text generation, translation)
- Speech recognition
- Time series prediction
- Music generation

## Long Short-Term Memory (LSTM)

### Architecture

An advanced RNN with three gates:

- **Forget gate**: Decides what information to discard from cell state
- **Input gate**: Decides what new information to store
- **Output gate**: Decides what to output from cell state

### Advantages Over Vanilla RNN

- Solves the vanishing gradient problem
- Can learn long-term dependencies
- Selective memory: learns what to remember and forget

### Applications

- Machine translation
- Speech synthesis
- Text summarization
- Anomaly detection in time series

## Gated Recurrent Unit (GRU)

- Simplified version of LSTM with two gates (reset and update)
- Fewer parameters than LSTM, faster training
- Comparable performance to LSTM on many tasks
- Better for smaller datasets due to fewer parameters

## Radial Basis Function (RBF) Networks

### Architecture

- Input layer → RBF hidden layer → Linear output layer
- Hidden neurons use radial basis functions (typically Gaussian): φ(x) = exp(-||x - c||² / 2σ²)
- Each hidden neuron measures distance from input to its center

### Properties

- Good for function approximation and interpolation
- Training is often faster than backpropagation
- Two phases: center selection + weight optimization

### Applications

- Pattern recognition
- Time series prediction
- Function approximation

## Self-Organizing Maps (SOM)

### Architecture

- Competitive learning network (unsupervised)
- 2D grid of neurons
- Each neuron has a weight vector matching input dimensionality
- Winner-take-all: closest neuron to input is activated

### Training Process (Kohonen Algorithm)

1. Present input pattern
2. Find the Best Matching Unit (BMU)
3. Update BMU and its neighbors to become more like the input
4. Reduce neighborhood and learning rate over time

### Applications

- Data visualization (mapping high-D to 2D)
- Clustering
- Dimensionality reduction
- Anomaly detection

## Autoencoders

### Architecture

- Encoder: compresses input to a lower-dimensional representation (bottleneck)
- Decoder: reconstructs input from the compressed representation
- Trained to minimize reconstruction error

### Variants

- **Denoising autoencoder**: Learns to remove noise from corrupted inputs
- **Variational autoencoder (VAE)**: Generates new data by learning the data distribution
- **Sparse autoencoder**: Forces sparse activation in the hidden layer

### Applications

- Dimensionality reduction
- Feature learning
- Image denoising
- Generative modeling (VAE)

## Generative Adversarial Networks (GAN)

### Architecture

- **Generator**: Creates synthetic data from random noise
- **Discriminator**: Distinguishes real from generated data
- Trained adversarially: generator tries to fool discriminator

### Applications

- Realistic image generation
- Style transfer
- Data augmentation
- Super-resolution imaging

## Summary Comparison

| Type        | Structure                    | Data Type        | Learning     | Use Case                          |
| ----------- | ---------------------------- | ---------------- | ------------ | --------------------------------- |
| MLP         | Feedforward, fully connected | Tabular          | Supervised   | General classification/regression |
| CNN         | Convolutional + pooling      | Spatial (images) | Supervised   | Image recognition                 |
| RNN/LSTM    | Recurrent with memory        | Sequential       | Supervised   | Text, time series                 |
| RBF         | RBF hidden + linear output   | Any              | Supervised   | Function approximation            |
| SOM         | Competitive grid             | Any              | Unsupervised | Clustering, visualization         |
| Autoencoder | Encoder-decoder              | Any              | Unsupervised | Compression, generation           |
| GAN         | Generator vs. discriminator  | Any              | Adversarial  | Data generation                   |

## Exam Tips

- Know the architecture and key properties of each type
- Be able to match network types to application domains
- Understand why LSTM solves the vanishing gradient problem
- Know the difference between feedforward and recurrent networks
- Be able to compare supervised (MLP, CNN, RNN) vs. unsupervised (SOM, Autoencoder) types
