# Machine Learning at Scale - Summary

## Key Definitions and Concepts

- **Machine Learning at Scale**: Training and deploying ML models on datasets that exceed single-machine capacity, requiring distributed computing infrastructure.

- **Data Parallelism**: Distributing training data across multiple workers, where each worker trains a copy of the model on local data with parameter synchronization.

- **Model Parallelism**: Splitting the model architecture itself across computation nodes, essential for billion-parameter deep learning models.

- **Stochastic Gradient Descent (SGD)**: Optimization algorithm computing gradients on mini-batches rather than full datasets, enabling incremental model updates.

- **Parameter Server**: Distributed architecture decoupling computation (workers) from parameter storage and synchronization (servers), enabling horizontal scaling.

- **Apache Spark MLlib**: Distributed machine learning library providing scalable implementations of classification, regression, clustering, and collaborative filtering algorithms.

- **ML Pipeline**: End-to-end workflow chaining data preprocessing, feature engineering, model training, evaluation, and deployment stages.

## Important Formulas and Theorems

- **Mini-batch SGD Update**: θ(t+1) = θ(t) - η × (1/B) × Σ∇L(xᵢ, yᵢ, θ(t)), where η is learning rate, B is batch size

- **Logistic Regression Loss**: L(θ) = -[y log(h(x)) + (1-y) log(1-h(x))], where h(x) = sigmoid(θᵀx)

- **K-Means Objective**: J = Σ||xᵢ - μ_{cᵢ}||², minimizing within-cluster variance

- **L-BFGS vs SGD**: L-BFGS approximates Hessian for faster convergence per iteration; SGD requires more iterations but cheaper per-iteration computation

## Key Points

- Traditional single-machine ML algorithms fail when datasets exceed memory capacity, necessitating distributed approaches.

- Data parallelism offers simpler implementation but requires efficient gradient synchronization; synchronous SGD ensures consistency at the cost of straggler delays.

- Apache Spark's in-memory computation makes it superior to Hadoop MapReduce for iterative ML algorithms by eliminating repeated disk I/O.

- The spark.ml DataFrame API with Pipeline support is the recommended approach over the older RDD-based MLlib API.

- Feature engineering at scale requires special handling for high-dimensional categorical variables through hashing or embedding techniques.

- Hyperparameter tuning at scale benefits from parallel execution but requires careful resource allocation to avoid cluster overload.

- Production ML systems require MLOps practices including experiment tracking, model versioning, and automated pipeline orchestration.

## Common Mistakes to Avoid

- Confusing data parallelism (splitting data) with model parallelism (splitting model architecture)—these are fundamentally different approaches.

- Using synchronous SGD without accounting for straggler workers—can significantly slow down distributed training.

- Neglecting feature scaling before training SGD-based models—leads to slow or unstable convergence.

- Assuming larger mini-batch sizes always improve performance—they reduce gradient variance but may hurt generalization and increase memory requirements.

- Overlooking data imbalance in distributed training—each partition should maintain representative class distributions.

## Revision Tips

1. Practice implementing at least one algorithm (logistic regression or k-means) in Spark to understand the API and data flow.

2. Draw comparison diagrams between synchronous/asynchronous SGD and data/model parallelism to visualize the differences.

3. Review Spark MLlib documentation for common algorithms' parameters and their default values.

4. Remember that exam questions often ask about tradeoffs—be prepared to explain pros and cons of different approaches rather than just definitions.

5. Connect this topic to previous knowledge of big data infrastructure (Hadoop, Spark) and classical ML algorithms to see the integrated picture.