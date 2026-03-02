# **AlexNet Text Book - 1 : Ch 3.2**

## **Training Supervised Deep Learning Networks**

### Introduction

In this chapter, we will delve into the world of supervised deep learning networks, specifically focusing on the AlexNet architecture. We will explore the historical context, key components, and applications of this iconic model.

### Historical Context

The concept of deep learning networks dates back to the 1980s, but it wasn't until the 2012 ImageNet Large Scale Visual Recognition Challenge (ILSVRC) that the stage was set for the development of modern deep learning architectures. AlexNet, proposed by Krizhevsky et al. in 2012, was the first deep learning model to achieve state-of-the-art results on the ILSVRC.

### Key Components

#### Convolutional Neural Networks (CNNs)

CNNs are a type of neural network designed to process data with grid-like topology, such as images. They consist of multiple layers, each performing a specific task:

1. **Convolutional Layers**: Apply filters to the input data to detect local features.
2. **Activation Functions**: Introduce non-linearity to the output of convolutional layers, allowing the model to learn more complex features.
3. **Pooling Layers**: Downsample the feature maps to reduce spatial dimensions and retain important information.
4. **Flatten Layer**: Reshape the feature maps into a one-dimensional vector for feeding into dense layers.

#### Fully Connected Neural Networks (Dense Layers)

Dense layers are used for classification tasks, where the output is a probability distribution over multiple classes. They consist of multiple fully connected layers with an activation function in between.

#### Batch Normalization

Batch normalization is a technique to normalize the input data for each layer, reducing internal covariate shift and improving training stability.

#### ReLU Activation Function

ReLU (Rectified Linear Unit) is a popular activation function, where negative values are set to zero and positive values are passed through unchanged.

### AlexNet Architecture

The AlexNet architecture consists of five convolutional layers, followed by three dense layers, and finally a softmax output layer.

**Diagram: AlexNet Architecture**

```markdown
Conv2D (5x5) -> ReLU -> MaxPool2D (3x3)
Conv2D (3x3) -> ReLU -> MaxPool2D (3x3)
Conv2D (3x3) -> ReLU -> MaxPool2D (3x3)
Conv2D (3x3) -> ReLU -> MaxPool2D (2x2)
Flatten
Dense (512) -> ReLU
Dense (256) -> ReLU
Softmax
```

### Training Supervised Deep Learning Networks

Training a supervised deep learning network involves the following steps:

1. **Data Preprocessing**: Load and preprocess the training data, including resizing images, normalizing pixel values, and creating batches.
2. **Model Initialization**: Initialize the model weights and biases using a random initialization technique, such as Xavier initialization.
3. **Forward Pass**: Pass the input data through the network, computing the output at each layer.
4. **Backward Pass**: Compute the gradients of the loss function with respect to the model parameters using backpropagation.
5. **Optimization**: Update the model parameters using an optimization algorithm, such as stochastic gradient descent (SGD).
6. **Regularization**: Regularize the model to prevent overfitting, using techniques such as dropout and L1/L2 regularization.

### Case Study: Image Classification with AlexNet

Let's consider a case study where we want to train AlexNet to classify images into one of three classes: dogs, cats, and other animals.

**Dataset**: We have a dataset of 100,000 images, with 33,000 images for training, 33,000 images for validation, and 33,000 images for testing.

**Hyperparameters**: We set the learning rate to 0.01, the batch size to 128, and the number of epochs to 15.

**Code**:

```python
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# Load dataset and create data loaders
transform = transforms.Compose([transforms.Resize(256),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                     std=[0.229, 0.224, 0.225])])

trainset = torchvision.datasets.ImageFolder('path/to/train/directory', transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True)

testset = torchvision.datasets.ImageFolder('path/to/test/directory', transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=128, shuffle=False)

# Define AlexNet architecture
class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 96, kernel_size=11)
        self.conv2 = nn.Conv2d(96, 256, kernel_size=5, stride=2)
        self.conv3 = nn.Conv2d(256, 384, kernel_size=3)
        self.conv4 = nn.Conv2d(384, 384, kernel_size=3)
        self.conv5 = nn.Conv2d(384, 256, kernel_size=3)
        self.fc1 = nn.Linear(256*6*6, 4096)
        self.fc2 = nn.Linear(4096, 4096)
        self.fc3 = nn.Linear(4096, 3)

    def forward(self, x):
        x = nn.functional.relu(nn.functional.conv2d(x, self.conv1))
        x = nn.functional.max_pool2d(x, 3)
        x = nn.functional.relu(nn.functional.conv2d(x, self.conv2))
        x = nn.functional.max_pool2d(x, 3)
        x = nn.functional.relu(nn.functional.conv2d(x, self.conv3))
        x = nn.functional.relu(nn.functional.conv2d(x, self.conv4))
        x = nn.functional.relu(nn.functional.conv2d(x, self.conv5))
        x = nn.functional.max_pool2d(x, 2)
        x = x.view(-1, 256*6*6)
        x = nn.functional.relu(nn.functional.fc(x, self.fc1))
        x = nn.functional.relu(nn.functional.fc(x, self.fc2))
        x = nn.functional.log_softmax(nn.functional.fc(x, self.fc3), dim=1)
        return x

# Initialize model and optimizer
model = AlexNet()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Train model
for epoch in range(15):
    for inputs, labels in trainloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# Evaluate model
test_loss = 0
correct = 0
with torch.no_grad():
    for inputs, labels in testloader:
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        test_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()

accuracy = correct / len(testloader.dataset)
print(f'Test Loss: {test_loss / len(testloader)}')
print(f'Test Accuracy: {accuracy:.2f}%')
```

### Further Reading

- Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. In Proceedings of the 26th International Conference on Neural Information Processing Systems (NIPS) (pp. 1097-1105).
- Szegedy, C., Liu, W., Jia, Y., Szeliski, R., & Malisiewski, P. (2015). Going deeper with convolutions. In Proceedings of the 32nd International Conference on Machine Learning (ICML) (pp. 4288-4296).
- Le, Q. V., & Ng, A. Y. (2011). Learning hierarchical representations for visual recognition. In Proceedings of the 24th International Conference on Neural Information Processing Systems (NIPS) (pp. 2348-2356).
