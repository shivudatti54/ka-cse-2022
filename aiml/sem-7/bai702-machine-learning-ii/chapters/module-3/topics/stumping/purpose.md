### Learning Purpose: Stumping

**1. Why is this topic important?**
Stumping, the process of creating a one-level decision tree (a decision stump), is a fundamental concept in ensemble methods, particularly boosting algorithms like AdaBoost. Understanding stumping is crucial because it serves as the foundational "weak learner" that powerful ensemble models are built upon. It demonstrates how combining many simple, slightly-better-than-random models can lead to highly accurate and robust predictions.

**2. What will students learn?**
Students will learn how to construct a decision stump by identifying the single most informative feature and split point that minimizes error. They will understand the mathematical criterion (e.g., Gini impurity, information gain) used to make this split. Furthermore, they will see how this simple model is weighted and combined sequentially in an ensemble framework to correct the errors of previous models.

**3. How does it connect to other concepts?**
This topic is a direct application and simplification of **Decision Trees** (from Machine Learning I). It is the core building block for **Boosting** techniques (like AdaBoost and Gradient Boosting) covered later in this module. It also contrasts with other ensemble methods such as **Bagging** (e.g., Random Forests), which use fully-grown trees instead of stumps, highlighting a key difference in ensemble strategy.

**4. Real-world applications**
Decision stumps are deployed in ensembles for numerous tasks where model interpretability and computational efficiency are valued. Key applications include:
*   **Medical Diagnosis:** Boosting with stumps helps create efficient models for predicting patient outcomes.
*   **Fraud Detection:** Ensembles of stumps can quickly process transactions to identify fraudulent patterns.
*   **Customer Churn Prediction:** Simple, interpretable rules from stumps help businesses identify key factors leading to customer attrition.