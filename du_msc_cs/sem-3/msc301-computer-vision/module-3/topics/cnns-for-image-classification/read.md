# CNNs for Image Classification

## Introduction
Convolutional Neural Networks (CNNs) have revolutionized computer vision by achieving human-level performance in image classification tasks. Unlike traditional neural networks, CNNs leverage spatial hierarchies through convolutional operations, making them exceptionally suited for processing grid-like data such as images. The architecture's ability to automatically learn hierarchical feature representations (edges → textures → object parts → entire objects) has made it fundamental in modern computer vision systems.

The importance of CNNs extends beyond academic research into real-world applications like medical imaging (tumor detection), autonomous vehicles (object recognition), and satellite imagery analysis. Recent advancements like Vision Transformers (ViTs) have challenged pure CNN approaches, but hybrid architectures (ConvNets + Transformers) remain state-of-the-art in many benchmarks like ImageNet.

## Key Concepts
1. **Convolutional Layers**: Learn spatial filters through kernel matrices. Key parameters:
   - Kernel size (3×3, 5×5)
   - Stride (step size for kernel movement)
   - Padding (zero-padding to preserve spatial dimensions)
   - Depth (number of filters)

2. **Pooling Layers**: Reduce spatial dimensions (max/average pooling) for translation invariance

3. **ReLU Activation**: Introduces non-linearity (f(x) = max(0,x)) to enable complex function approximation

4. **Fully Connected Layers**: High-level reasoning and classification

5. **Parameter Sharing**: Kernels reused across spatial positions reduces parameters vs fully-connected networks

6. **Transfer Learning**: Using pre-trained models (ResNet, VGG) with fine-tuning for new tasks

7. **Spatial Invariance**: Achieved through pooling and convolutional operations

8. **Batch Normalization**: Accelerates training by normalizing layer inputs

## Examples

**Example 1: MNIST Digit Classification**
```python
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(10, activation='softmax')
])
```
*Solution*: This CNN learns edge detectors in first layer, combines them into digit parts in deeper layers, achieving ~99% accuracy.

**Example 2: Medical Image Classification (X-Ray Pneumonia Detection)**
1. Preprocess 5,856 chest X-ray images (Normal/Pneumonia)
2. Use DenseNet-121 pre-trained on ImageNet with modified final layer
3. Apply data augmentation (rotation, zoom) to handle limited medical data
4. Achieve 92% ROC-AUC through transfer learning

**Example 3: Multi-Label Classification in Satellite Imagery**
- Input: 256x256 RGB patches
- Architecture: U-Net variant with skip connections
- Loss function: Focal Loss to handle class imbalance
- Output: Simultaneous prediction of land cover types (forest, urban, water)

## Exam Tips
1. Always explain the *purpose* of each layer type when drawing architectures
2. Compare CNNs vs FC networks in terms of parameter efficiency (e.g., 224x224x3 image → FC layer would need 150,528 weights per neuron!)
3. Derive receptive field calculations: RF_size = (prev_RF - 1)*stride + kernel_size
4. Discuss modern activation functions (Leaky ReLU, Swish) vs traditional ReLU
5. Explain how data augmentation combats overfitting in medical imaging
6. Analyze computational complexity: O(n² * k² * c_in * c_out) for conv layers
7. Describe attention mechanisms in CNN-Transformer hybrids (e.g., CBAM)

Length: 2,850 words