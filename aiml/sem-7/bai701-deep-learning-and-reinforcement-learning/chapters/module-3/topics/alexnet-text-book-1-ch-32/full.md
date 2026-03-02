# **AlexNet Text Book - 1 : Ch 3.2**

## **Introduction**

In this chapter, we will delve into the world of supervised deep learning networks, focusing on the iconic AlexNet architecture. Developed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton in 2012, AlexNet revolutionized the field of image classification by achieving state-of-the-art performance on the ImageNet Large Scale Visual Recognition Challenge (ILSVRC).

## **Historical Context**

The quest for automatic image classification dates back to the 1980s, with the introduction of neural networks in the field of computer vision. However, the advent of deep learning techniques in the 2000s marked a significant turning point. The AlexNet architecture built upon the success of earlier convolutional neural networks (CNNs), such as LeNet-5 and AlexNet's predecessor, AlexNet (2012).

## **Architecture Overview**

AlexNet is a two-stage CNN architecture consisting of:

1. **Convolutional Layer 1**: 96 filters with 11x11 kernels and a stride of 4, followed by a max pooling layer with a stride of 3.
2. **Convolutional Layer 2**: 256 filters with 5x5 kernels and a stride of 1, followed by a max pooling layer with a stride of 3.
3. **Convolutional Layer 3**: 384 filters with 3x3 kernels and a stride of 1.
4. **Fully Connected Layer 1**: 384 neurons with ReLU activation.
5. **Fully Connected Layer 2**: 256 neurons with ReLU activation.
6. **Fully Connected Layer 3**: 128 neurons with ReLU activation.
7. **Output Layer**: 1000 neurons with softmax activation.

## **Training Supervised Deep Learning Networks**

### **Backpropagation Algorithm**

The backpropagation algorithm is the most commonly used optimization technique for training deep neural networks. It consists of two main components:

1. **Forward Pass**: The network is fed with input data, and the output is computed.
2. **Backward Pass**: The error is computed, and the gradients are calculated.

### **Stochastic Gradient Descent (SGD)**

SGD is an optimization algorithm used to minimize the loss function. It works by iteratively updating the model's parameters using a gradient descent update rule.

### **Batch Normalization**

Batch normalization is a technique used to normalize the inputs to each layer, improving the stability and speed of training.

### **Learning Rate Scheduling**

Learning rate scheduling is a technique used to adjust the learning rate during training. It helps prevent overfitting and improves the overall performance of the model.

### **Regularization Techniques**

Regularization techniques, such as dropout and L2 regularization, are used to prevent overfitting and improve the generalization of the model.

## **Case Study: AlexNet on ImageNet**

In 2012, AlexNet achieved a top-5 error of 15.3% on the ILSVRC, surpassing the previous state-of-the-art performance by a significant margin. The success of AlexNet can be attributed to its:

1. **Deep Architecture**: AlexNet has a deep architecture, which allows it to learn complex features from the data.
2. **Large Number of Parameters**: The large number of parameters in AlexNet allows it to learn a wide range of features from the data.
3. **Use of Dropout**: Dropout is used to prevent overfitting and improve the generalization of the model.

## **Applications**

AlexNet has been widely used in various applications, including:

1. **Image Classification**: AlexNet has been used for image classification tasks, such as object recognition and scene understanding.
2. **Image Generation**: AlexNet has been used for image generation tasks, such as generating new images based on existing images.
3. **Image Segmentation**: AlexNet has been used for image segmentation tasks, such as segmenting objects from the background.

## **Conclusion**

In this chapter, we have explored the AlexNet architecture and its role in the development of deep learning. We have also discussed the training process of supervised deep learning networks, including backpropagation, SGD, batch normalization, learning rate scheduling, and regularization techniques. Finally, we have presented a case study on AlexNet's performance on the ILSVRC and its applications in image classification, generation, and segmentation.

**Further Reading**

- Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. In Proceedings of the 25th International Conference on Neural Information Processing Systems (NIPS).
- Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. In Proceedings of the 31st International Conference on International Conference on Machine Learning (ICML).
- Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S. E., Anguelov, D., ... & Rabinovich, A. (2015). Going deeper with convolutions. In Proceedings of the 32nd International Conference on Machine Learning (ICML).
