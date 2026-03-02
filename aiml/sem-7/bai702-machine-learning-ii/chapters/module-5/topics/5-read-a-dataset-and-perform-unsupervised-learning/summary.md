# **Unsupervised Learning using SOM Algorithm**

### Introduction

- Self-Organizing Map (SOM) is an unsupervised learning algorithm used for dimensionality reduction and clustering.
- SOM is a type of neural network that maps high-dimensional data to a lower-dimensional representation.

### Key Concepts

- **Map**: A two-dimensional array of weights that represents the lower-dimensional representation of the high-dimensional data.
- **Neurons**: The individual weights in the map that are trained to minimize the distance between the input data and the corresponding neuron.
- **Winner-Take-All**: The neuron with the closest weight to the input data wins and becomes the active neuron.

### SOM Algorithm

- **Training**: The SOM algorithm iteratively updates the weights of the neurons based on the distance between the input data and the corresponding neuron.
- **Map Initialization**: The weights of the neurons are randomly initialized.
- **Competitive Learning**: The neuron with the closest weight to the input data is selected as the winner.

### Important Formulas and Definitions

- **Distance Metric**: The Euclidean distance is commonly used to calculate the distance between the input data and the corresponding neuron.
- **Cost Function**: The mean squared error (MSE) is commonly used as the cost function to minimize during training.
- **Hebbian Learning Rule**: The Hebbian learning rule is a simple learning rule that states: "neurons that fire together, wire together".

### Theorems

- **SOM Convergence Theorem**: The SOM algorithm converges to a stable equilibrium when the training data is sufficiently large and the parameters are properly initialized.
- **SOM Uniqueness Theorem**: The SOM algorithm is unique if the training data is sufficiently large and the parameters are properly initialized.

### Important Theorems and Formulas (continued)

- **Kohonen's Map Initialization Theorem**: The weights of the neurons can be initialized using a technique called Kohonen's map initialization, which minimizes the mean squared error between the weights and the input data.
- **SOM Training Algorithm**: The SOM training algorithm can be summarized as follows:
  1. Initialize the weights of the neurons randomly.
  2. Calculate the distance between the input data and each neuron.
  3. Select the neuron with the closest weight to the input data as the winner.
  4. Update the weights of the winner and its neighbors using the Hebbian learning rule.

### Applications of SOM

- **Data Visualization**: SOM can be used to visualize high-dimensional data in a lower-dimensional space.
- **Clustering**: SOM can be used to cluster similar data points together.
- **Dimensionality Reduction**: SOM can be used to reduce the dimensionality of high-dimensional data.
