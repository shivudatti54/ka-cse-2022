# **Decision by Committee: Ensemble Learning**

### Introduction

Ensemble learning is a type of machine learning approach that involves combining the predictions of multiple models to improve overall performance. In this section, we will explore two popular ensemble learning techniques: boosting and bagging.

### Boosting

---

Boosting is a type of ensemble learning that involves training multiple weak models and combining their predictions to create a strong model. The idea behind boosting is to correct the mistakes of the previous model and use the corrected predictions to train the next model.

#### Adaboost

Adaboost is a popular boosting algorithm that was developed by Yoav Freund and Robert Schapire in 1996. Adaboost works by iterating through multiple models, each of which is trained on a different subset of the training data. The models are trained to minimize the error on the current subset, and the predictions of each model are weighted based on their accuracy.

Here are the key concepts of Adaboost:

- **Weak models**: Adaboost uses multiple weak models, each of which is a simple model that is not very accurate on its own.
- **Weighting**: The predictions of each weak model are weighted based on their accuracy, with the most accurate models receiving the highest weights.
- **Corrections**: The weights of the weak models are updated based on the corrections made by the next model.

Example:

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an Adaboost classifier
clf = AdaBoostClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the classifier
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
```

#### Stumping

Stumping is a technique used in boosting to correct the mistakes of the previous model. A stump is a decision tree that is trained on the most misclassified examples from the previous model. The stump is trained to correct the mistakes of the previous model by changing the boundary between the classes.

Here are the key concepts of stumping:

- **Most misclassified examples**: The most misclassified examples from the previous model are selected and used to train the stump.
- **Decision tree**: The stump is a decision tree that is trained to correct the mistakes of the previous model.
- **Boundary correction**: The stump changes the boundary between the classes to correct the mistakes of the previous model.

### Bagging

---

Bagging, or Bagged Ensemble, is a type of ensemble learning that involves training multiple models on different subsets of the training data and combining their predictions to create a strong model.

#### Subagging

Subagging is a technique used in bagging to correct the mistakes of the previous model. Subagging involves training multiple models on different subsets of the training data and selecting the best-performing model based on its accuracy.

Here are the key concepts of subagging:

- **Different subsets**: Multiple models are trained on different subsets of the training data.
- **Selection**: The best-performing model is selected based on its accuracy.
- **Combination**: The predictions of the selected model are combined with the predictions of the other models to create a strong model.

Example:

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a bagged classifier
clf = BaggingClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the classifier
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
```

### Random Forest

---

Random Forest is a type of ensemble learning that involves training multiple decision trees on different subsets of the training data and combining their predictions to create a strong model.

Here are the key concepts of Random Forest:

- **Decision trees**: Multiple decision trees are trained on different subsets of the training data.
- **Combination**: The predictions of the decision trees are combined to create a strong model.
- **Random subset**: A random subset of the training data is selected for each decision tree.

Example:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the classifier
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
```
