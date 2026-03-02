# Artificial Intelligence

## Introduction

Artificial Intelligence (AI) stands as one of the most transformative technological developments of the modern era, fundamentally reshaping how computers process information, solve complex problems, and interact with the physical world. At its core, AI enables machines to mimic cognitive functions traditionally associated with human intelligence—including learning, reasoning, problem-solving, perception, and language understanding. The discipline emerged as an academic field in the mid-1950s, with the famous Dartmouth Conference of 1956 often cited as its formal beginning, where pioneers like John McCarthy, Marvin Minsky, and Allen Newell laid the groundwork for machines that could exhibit intelligent behavior.

The significance of AI in contemporary computing cannot be overstated. From voice assistants like Siri and Alexa to recommendation systems on Netflix and Amazon, from autonomous vehicles to medical diagnosis tools, AI permeates nearly every aspect of modern life. For students pursuing Computer Science at the University of Delhi, understanding AI is essential not merely as a technological tool but as a fundamental paradigm shift in computation itself. Traditional programming requires explicit instructions for every step, whereas AI enables systems to learn patterns from data and make decisions without being explicitly programmed for every contingency. This shift from rule-based to data-driven computing represents a fundamental evolution in how we approach problem-solving in computer science.

The relevance of AI extends far beyond technical applications. It raises profound questions about the nature of intelligence, consciousness, and the boundaries between human and machine cognition. As AI systems become more sophisticated, they challenge our understanding of what it means to think, to learn, and to create. For a well-rounded computer science education, studying AI provides not only practical skills but also philosophical depth, preparing students to navigate a world increasingly shaped by intelligent machines.

## Key Concepts

### Foundations of AI

Artificial Intelligence encompasses several foundational concepts that every student must master. The first and perhaps most important is the distinction between weak AI and strong AI. Weak AI, also known as narrow AI, refers to systems designed to perform specific tasks—such as image recognition, natural language processing, or playing chess. These systems operate within predefined boundaries and cannot generalize beyond their training. Strong AI, theoretical in nature, would possess the ability to understand, learn, and apply knowledge across diverse domains, exhibiting general intelligence comparable to human cognition. Current AI technology remains firmly in the weak AI category, though advances in machine learning continue to push boundaries.

The concept of intelligent agents forms another cornerstone of AI study. An intelligent agent is a system that perceives its environment through sensors and acts upon that environment through actuators. This framework, popularized by Russell and Norvig in their seminal textbook, provides a unifying structure for understanding various AI approaches. Agents can range from simple reflex agents that respond directly to stimuli, to model-based agents that maintain internal representations of the world, to goal-based agents that plan actions to achieve specific objectives, and finally to learning agents that improve their performance through experience.

### Problem Solving and Search

One of the core areas of AI involves solving problems through systematic search. State-space search represents problems as graphs where nodes represent states and edges represent transitions between states. Breadth-first search explores all nodes at a given depth before proceeding to deeper levels, guaranteeing the shortest path in unweighted graphs but requiring substantial memory. Depth-first search explores as far as possible along each branch before backtracking, being more memory-efficient but potentially getting stuck in infinite paths if cycles exist. A* search combines the advantages of both by using heuristics—estimated costs to the goal—to guide the search toward promising solutions while maintaining completeness guarantees.

Game playing represents a classic AI application where search becomes essential. Two-player zero-sum games like chess and tic-tac-toe can be represented as game trees where each node represents a board position and branches represent possible moves. The minimax algorithm provides optimal play by assuming both players play optimally, maximizing the agent's minimum payoff. Alpha-beta pruning significantly improves minimax efficiency by eliminating branches that cannot influence the final decision, allowing deep search within practical time constraints.

### Machine Learning Fundamentals

Machine learning represents the dominant paradigm in modern AI, enabling systems to learn from data rather than following explicit programming. Supervised learning involves training models on labeled data—input-output pairs—where the algorithm learns to map inputs to correct outputs. Classification problems require predicting discrete categories (spam or not spam), while regression problems predict continuous values (house prices). Common supervised algorithms include decision trees, which make decisions by learning simple rules from features; support vector machines, which find optimal hyperplanes to separate classes; and neural networks, which learn complex non-linear relationships through interconnected layers of artificial neurons.

Unsupervised learning works with unlabeled data, discovering hidden patterns or structures. Clustering algorithms like k-means group similar data points together, while dimensionality reduction techniques like Principal Component Analysis (PCA) compress high-dimensional data into lower dimensions while preserving essential information. Reinforcement learning represents a third paradigm where an agent learns optimal behavior through trial and error, receiving rewards or penalties for actions in an environment. This approach has achieved remarkable success in game playing (AlphaGo) and robotics, demonstrating how agents can learn sophisticated strategies through experience.

### Neural Networks and Deep Learning

Artificial neural networks draw inspiration from biological neural systems in the brain, consisting of layers of interconnected nodes (neurons) that process information. Each connection has an associated weight that determines signal strength, and during training, these weights adjust to minimize the difference between predicted and actual outputs. The backpropagation algorithm enables efficient training of multi-layer networks by computing gradients of the loss function with respect to weights and adjusting them iteratively.

Deep learning extends neural networks to include multiple hidden layers, enabling the learning of hierarchical representations from raw data. Convolutional Neural Networks (CNNs) excel at image processing through convolutional layers that automatically learn spatial features like edges, textures, and object parts. Recurrent Neural Networks (RNNs) handle sequential data by maintaining hidden states that capture temporal dependencies, making them ideal for time series prediction and natural language processing. Transformers, the architecture behind modern language models like GPT, use attention mechanisms to process entire sequences simultaneously, achieving state-of-the-art results in natural language understanding and generation.

### Knowledge Representation and Reasoning

AI systems require formalisms to represent knowledge about the world. Logical representations use propositions and rules—first-order logic provides expressive power to describe objects, relationships, and quantifications. Production systems encode knowledge as condition-action rules (IF-THEN statements), suitable for expert systems that emulate human expertise in narrow domains. Semantic networks represent knowledge as graphs with nodes for concepts and edges for relationships, offering intuitive visualization but limited inferential power. Frame-based representations organize knowledge into structured objects (frames) with slots for attributes and default values, providing more expressiveness than semantic networks while remaining computationally tractable.

Reasoning mechanisms enable AI systems to derive new knowledge from known facts. Deductive reasoning applies general rules to specific cases, guaranteeing truth preservation when rules are correct. Inductive reasoning generalizes from specific examples to rules, introducing uncertainty but enabling learning from experience. Probabilistic reasoning handles uncertainty through Bayesian networks and probabilistic graphical models, allowing AI systems to make decisions with incomplete or noisy information. Fuzzy logic extends classical logic to handle degrees of truth rather than binary true/false values, useful in control systems and approximate reasoning.

### Natural Language Processing

Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. Tokenization breaks text into individual words or tokens, while part-of-speech tagging identifies grammatical categories. Named entity recognition identifies proper nouns like people, organizations, and locations. Syntactic parsing analyzes grammatical structure, building parse trees that represent sentence composition. Semantic analysis extracts meaning, including sentiment analysis that determines emotional tone and machine translation that converts text between languages.

Modern NLP increasingly relies on large language models trained on vast text corpora. These models learn statistical patterns in language usage, enabling capabilities like question answering, text summarization, and conversational interaction. However, challenges remain in understanding context, handling ambiguity, and ensuring factual accuracy—issues that active research continues to address.

## Examples

### Example 1: Solving the 8-Puzzle with A* Search

Consider the classic 8-puzzle problem where tiles numbered 1-8 are arranged in a 3×3 grid with one empty space. The goal is to arrange tiles in order from 1-8 with the empty space in the bottom-right corner. Starting from a random configuration, we apply A* search to find the optimal solution.

We define the heuristic as the sum of Manhattan distances—each tile's distance from its goal position measured horizontally and vertically. For each state, we generate up to four successors (moving the empty space up, down, left, or right). A* explores states in order of f(n) = g(n) + h(n), where g(n) is the cost from start to current state (number of moves made), and h(n) is the heuristic estimate to goal.

Suppose we start with state: [[1,2,3],[4,5,6],[7,0,8]] where 0 represents empty space. The Manhattan distance for tile 8 is 2 (one right, one down), and all other tiles are in correct positions, giving h(n) = 2. With g(n) = 0, we have f(n) = 2. We expand this state, generating successors with their respective f-values, continuing until we reach the goal state where h(n) = 0 and f(n) equals the optimal path length.

### Example 2: Building a Simple Neural Network for Digit Classification

Imagine building a neural network to recognize handwritten digits (0-9) from 8×8 pixel images. The input layer has 64 nodes (one per pixel with grayscale values 0-255, normalized to 0-1). The output layer has 10 nodes representing digit classes, using softmax activation to produce probability distributions.

Between input and output, we include one hidden layer with 128 neurons using ReLU activation. During forward propagation, each neuron computes a weighted sum of inputs plus bias, applies the activation function, and passes results to the next layer. For training, we use the cross-entropy loss function measuring difference between predicted probabilities and true labels (one-hot encoded). Backpropagation computes gradients through the network, updating weights using gradient descent with a learning rate of 0.01.

Suppose we feed an image of the digit "3." The input layer receives 64 pixel values. Through matrix multiplications and activations, signals propagate to the output layer. If the network outputs [0.05, 0.01, 0.02, 0.85, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01], it predicts "3" with 85% confidence. The loss compares this to the true label [0,0,0,1,0,0,0,0,0,0], and gradients flow backward to adjust weights, gradually improving accuracy through many training iterations.

### Example 3: Designing an Expert System for Medical Diagnosis

An expert system for medical diagnosis uses production rules to simulate a physician's diagnostic reasoning. The knowledge base contains rules like: IF fever AND cough AND fatigue THEN suspect_influenza (0.8); IF headache AND nausea AND sensitivity_to_light THEN suspect_meningitis (0.9); IF chest_pain AND shortness_of_breath AND history_smoking THEN suspect_heart_disease (0.85).

The inference engine uses backward chaining, starting from suspected conditions and working backward to find supporting symptoms. When a user reports "fever" and "cough," the system searches for rules where these appear in the THEN clause, activating influenza suspicion. It then asks follow-up questions about fatigue to confirm or rule out influenza, proceeding systematically through the symptom-disease network.

The system maintains a certainty factor for each diagnosis, combining evidence from multiple rules. If two rules support influenza with certainty factors 0.8 and 0.6, the combined certainty uses the formula: CF_combined = CF1 + CF2 × (1 - CF1) = 0.8 + 0.6 × 0.2 = 0.92. This allows the system to provide ranked diagnoses with confidence levels, assisting rather than replacing human medical judgment.

## Exam Tips

For University of Delhi semester examinations in Artificial Intelligence, students should focus on the following key areas:

Understanding search algorithms thoroughly is essential—you must be able to trace through breadth-first, depth-first, and A* search on example problems, explaining when each is appropriate and analyzing their time and space complexity. Remember that A* search is complete and optimal if the heuristic is admissible (never overestimates cost).

The minimax algorithm and alpha-beta pruning frequently appear in exam questions. Practice drawing game trees, applying minimax to determine optimal moves, and calculating how alpha-beta pruning reduces the number of nodes evaluated. Be prepared to explain how depth limiting relates to practical game-playing programs.

Machine learning concepts require understanding the differences between supervised, unsupervised, and reinforcement learning, including concrete examples of each. Know the basic formulations of classification versus regression problems and common algorithms used for each. The bias-variance tradeoff represents a particularly important concept that explains model generalization.

Neural network questions often ask you to compute forward propagation through simple networks or explain the backpropagation process conceptually. Understand activation functions (sigmoid, ReLU, softmax), the purpose of layers, and how training adjusts weights to minimize loss.

Knowledge representation questions test your ability to represent facts using logical formulas, construct semantic networks from descriptions, and perform inference using forward or backward chaining. Practice converting English statements into formal representations.

Natural language processing coverage typically includes basic concepts like tokenization, parsing, and semantic analysis. Understand the challenges of NLP including ambiguity, context dependence, and the difference between syntactic and semantic analysis.

Application areas of AI—robotics, expert systems, game playing, computer vision, and speech recognition—provide important context. Understand how AI techniques apply in these domains and what distinguishes them from traditional computing approaches.

The historical development of AI, including major milestones and key figures, occasionally appears in examinations. Know the Dartmouth Conference as the founding event, Turing's contribution through the Turing Test, and the significance of expert systems in the 1980s as a major AI application paradigm.