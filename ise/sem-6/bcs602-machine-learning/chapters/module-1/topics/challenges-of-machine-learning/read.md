# Types of Machine Learning

## What are Types of Machine Learning?
Types of machine learning classify learning problems by the kind of feedback the model receives during training. The three core types are **supervised learning**, **unsupervised learning**, and **reinforcement learning**, each suited to different data and objectives.

## Key Concepts
### Supervised Learning
Uses **labeled data** (input, output pairs) to learn a mapping from features to targets. Typical tasks are **classification** (predicting categories) and **regression** (predicting numeric values).

**Examples:** spam vs. not spam, house price prediction, disease diagnosis.

### Unsupervised Learning
Uses **unlabeled data** to discover hidden structure, patterns, or groupings. Common tasks include **clustering**, **dimensionality reduction**, and **association rule mining**.

**Examples:** customer segmentation, topic discovery, market basket analysis.

### Reinforcement Learning
An **agent** learns by interacting with an **environment** and receiving **rewards**. The goal is to learn a **policy** that maximizes cumulative reward over time, balancing **exploration** and **exploitation**.

**Examples:** game playing (Chess/Go), robotics control, ad bidding.

## How It Works
1. **Identify the feedback type:** labeled targets (supervised), no targets (unsupervised), or reward signals (reinforcement).
2. **Select an objective:** minimize prediction error, discover structure, or maximize long-term reward.
3. **Choose an algorithm:** e.g., regression/classification, clustering/PCA, or policy/value-based methods.
4. **Train and evaluate:** use task-appropriate metrics (accuracy, silhouette score, or average reward).

## Complexity Analysis (if applicable)
| Operation | Time | Space |
|-----------|------|-------|
| Training | Varies by algorithm (e.g., linear regression vs. deep networks) | Varies by model size and data |
| Inference | Often O(#features) to O(#parameters) | Model storage |

## Real-World Applications
- **Supervised:** credit scoring, image classification, speech recognition
- **Unsupervised:** anomaly detection, compression, clustering users
- **Reinforcement:** robotics, recommendation ranking, resource scheduling

## Summary
- Learning types differ by **feedback signal**: labels, structure, or rewards.
- Each type aligns with distinct tasks, metrics, and algorithms.
- Correctly identifying the learning type guides model choice and evaluation.
