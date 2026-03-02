# Data Mining Techniques - Summary

## Key Definitions and Concepts
- **Support**: Frequency of itemset X in transactions
- **Silhouette Score**: Measures cluster cohesion/separation [-1,1]
- **Entropy**: Uncertainty measure in decision trees
- **Curse of Dimensionality**: Performance drop in high-D spaces

## Important Formulas and Theorems
- **Apriori Principle**: If itemset is frequent, all subsets are frequent
- **Gini Index**: \( G = 1 - \sum(p_i^2) \) (Classification impurity)
- **Jaccard Similarity**: \( J(A,B) = \frac{|A ∩ B|}{|A ∪ B|} \)
- **DBSCAN**: Density reachability defined by ε-neighborhood

## Key Points
- Classification requires labeled data; clustering is unsupervised
- FP-Growth avoids candidate generation (unlike Apriori)
- t-SNE > PCA for visualizing high-D clusters
- Isolation Forest outperforms k-NN in high-dimensional anomaly detection
- Text mining pipelines require tokenization → vectorization → modeling
- Hadoop MapReduce suitable for batch mining; Spark for iterative tasks
- Differential privacy crucial for medical data mining

## Common Mistakes to Avoid
- Using k-means without normalizing features
- Ignoring false positives in anomaly detection
- Overlooking temporal patterns in streaming data
- Applying association rules without lift analysis

## Revision Tips
1. Create algorithm comparison tables (e.g., k-means vs DBSCAN)
2. Solve past DU papers on market basket analysis (2019-2023)
3. Implement a mini-project: Twitter sentiment analysis using TF-IDF+SVM
4. Use MNIST dataset for hands-on classification practice

Length: 650 words