# **Machine Learning II: Graphical Models**

# **Topic 3: Read a Supervised Dataset and Use Bagging and Boosting Techniques to Classify the Dataset**

## **Overview**

In this topic, we will explore the concept of bagging and boosting techniques in machine learning, specifically for classification problems. Bagging and boosting are ensemble methods that combine multiple models to improve the accuracy and robustness of classification predictions.

## **Bagging (Bootstrap Aggregating)**

Bagging is a technique that involves training multiple instances of a model on different subsets of the training data. The goal of bagging is to reduce overfitting by averaging the predictions of multiple models, each trained on a different subset of the data.

## **How Bagging Works**

1. **Bootstrap Sampling**: A random subset of the training data is selected with replacement. This is known as bootstrap sampling.
2. **Model Training**: A model is trained on the bootstrap sample.
3. **Model Ensemble**: The predictions of all models are combined to form an ensemble prediction.

## **Example**

Suppose we have a dataset of 1000 instances with 5 features and we want to classify them as either 0 or 1. We can use bagging to train 10 instances of a model on different subsets of the data.

| Model   | Accuracy |
| ------- | -------- |
| Model 1 | 80%      |
| Model 2 | 85%      |
| Model 3 | 80%      |
| ...     | ...      |

The ensemble prediction is the average of the predictions of all models.

| Instance | Prediction |
| -------- | ---------- |
| 1        | 0.8        |
| 2        | 0.85       |
| ...      | ...        |

## **Boosting**

Boosting is a technique that involves training multiple models sequentially, with each model used to correct the errors of the previous model. The goal of boosting is to improve the accuracy of classification predictions by selectively weighting the importance of each instance in the training data.

## **How Boosting Works**

1. **Model Training**: A model is trained on the entire training data.
2. **Error Calculation**: The errors of each instance are calculated.
3. **Weight Assignment**: The weights of each instance are assigned based on its error.
4. **Model Combination**: The models are combined sequentially, with each model used to correct the errors of the previous model.

## **Example**

Suppose we have a dataset of 1000 instances with 5 features and we want to classify them as either 0 or 1. We can use boosting to train 10 instances of a model sequentially.

| Instance | Weight |
| -------- | ------ |
| 1        | 1.0    |
| 2        | 0.8    |
| ...      | ...    |

The model with the highest weight is used to correct the errors of the previous model.

## **Bagging vs. Boosting**

|                       | Bagging                                            | Boosting                                                                      |
| --------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Goal**              | Reduce overfitting by averaging predictions        | Improve accuracy by selectively weighting importance                          |
| **Model Training**    | Train multiple models on different subsets of data | Train models sequentially, with each model correcting previous model's errors |
| **Error Calculation** | Average errors of all models                       | Calculate errors of individual instances                                      |

## **Conclusion**

In this topic, we have explored the concepts of bagging and boosting techniques in machine learning, specifically for classification problems. Bagging involves training multiple instances of a model on different subsets of the training data, while boosting involves training multiple models sequentially, with each model used to correct the errors of the previous model. By combining the predictions of multiple models, we can improve the accuracy and robustness of classification predictions.

## **Key Concepts**

- Bagging: ensemble method that combines multiple models to improve accuracy and reduce overfitting
- Boosting: ensemble method that trains multiple models sequentially to improve accuracy
- Bootstrap sampling: random subset of training data is selected with replacement
- Model ensemble: predictions of multiple models are combined to form an ensemble prediction
- Weight assignment: weights of each instance are assigned based on its error in boosting
