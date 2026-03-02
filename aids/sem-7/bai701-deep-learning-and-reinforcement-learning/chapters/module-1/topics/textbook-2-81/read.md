# Textbook 2: 8.1

## Introduction to Deep Learning

### What is Deep Learning?

Deep learning is a subset of machine learning that involves the use of artificial neural networks with multiple layers. These neural networks are designed to mimic the structure and function of the human brain, allowing them to learn complex patterns and relationships in data.

### Key Characteristics of Deep Learning

- **Multiple Layers**: Deep learning models have multiple layers of neurons, which allow them to learn complex patterns and representations of data.
- **Non-Linearity**: Deep learning models often use non-linear activation functions, which allow them to learn non-linear relationships between inputs and outputs.
- **Large Amounts of Data**: Deep learning models typically require large amounts of data to train, as they need to learn from a large number of examples to improve their performance.

### Types of Deep Learning Models

- **Feedforward Neural Networks**: Feedforward neural networks are the simplest type of deep learning model. They consist of multiple layers of neurons, where each layer processes the input data and passes it on to the next layer.
- **Recurrent Neural Networks (RNNs)**: RNNs are a type of deep learning model that are designed to handle sequential data, such as text or time series data. They consist of multiple layers of neurons, where each layer processes the current input data and uses the output from the previous time step to inform its predictions.
- **Convolutional Neural Networks (CNNs)**: CNNs are a type of deep learning model that are designed to handle image data. They consist of multiple layers of neurons, where each layer processes the input image and uses convolutional and pooling operations to extract features.

### Applications of Deep Learning

- **Image Classification**: Deep learning models can be used for image classification tasks, such as recognizing objects in images.
- **Natural Language Processing (NLP)**: Deep learning models can be used for NLP tasks, such as language translation and sentiment analysis.
- **Speech Recognition**: Deep learning models can be used for speech recognition tasks, such as recognizing spoken words and phrases.

### Example of a Deep Learning Model

Here is an example of a simple deep learning model implemented in Python using the Keras library:

```python
from keras.models import Sequential
from keras.layers import Dense

# Create a sequential model
model = Sequential()

# Add a hidden layer with 64 neurons
model.add(Dense(64, activation='relu', input_shape=(784,)))

# Add a hidden layer with 32 neurons
model.add(Dense(32, activation='relu'))

# Add an output layer with 10 neurons
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=128)
```

This model is a simple neural network with two hidden layers and an output layer. It is trained on the MNIST dataset, which consists of 28x28 images of handwritten digits. The model is trained using the Adam optimizer and categorical cross-entropy loss.
