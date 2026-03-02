# Decision Tree Learning: Introduction

### Definitions

- **Decision Tree**: A tree-like model of decision making, where each internal node represents a feature or attribute, each branch represents a decision or test, and each leaf node represents a class label or target value.
- **Decision Tree Learning**: A supervised learning algorithm that uses a decision tree to classify data or make predictions.

### Key Concepts

- **Root Node**: The topmost node of the decision tree, representing the initial feature or attribute used for classification.
- **Internal Nodes**: Nodes that represent features or attributes used for classification, and contain child nodes representing the decision or test applied to that feature.
- **Leaf Nodes**: Nodes that represent class labels or target values, and contain the predicted class label or target value.
- **Decision Tree Split**: A split applied to an internal node to separate the data into two subsets based on a feature or attribute.
- **Best Split**: The split that results in the most homogeneous subsets, i.e., subsets with the most similar class labels.

### Important Formulas

- **Information Gain**: A measure of how much information a split provides about the class labels of the data. It is calculated as: I(D) = I(D) + I(D|A), where I(D) is the initial entropy of the data, and I(D|A) is the conditional entropy of the data given the split.
- **Entropy**: A measure of the uncertainty or randomness of the class labels of the data. It is calculated as: H(D) = - ∑ p(x) log2 p(x), where p(x) is the probability of class x.

### Important Theorems

- **Breiman's Theorem**: A theorem that states that decision tree learning can be reduced to a tree search algorithm, where the algorithm explores all possible trees of a given depth and selects the tree with the highest accuracy.
- **Vapnik's Chervonev Theorem**: A theorem that states that decision tree learning can be reduced to a hypothesis space search algorithm, where the algorithm searches for the best hypothesis in the space of possible trees.

### Revision Notes

- Decision tree learning is a supervised learning algorithm that uses a decision tree to classify data or make predictions.
- Decision trees are composed of root nodes, internal nodes, and leaf nodes, and are used to make decisions based on features or attributes.
- The best split is the split that results in the most homogeneous subsets, i.e., subsets with the most similar class labels.
- Information gain and entropy are used to evaluate the quality of splits and to make decisions about which splits to apply.
