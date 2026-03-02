python
# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Assume `X` contains email features and `y` contains labels (0 for ham, 1 for spam)
# First, split into a temporary set and the final test set (80% temp, 20% test)
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now split the temp set into training and validation (75% of 80% = 60% train, 25% of 80% = 20% validation)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

# Train the model on the training set
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Tune hyperparameters using the validation set (this step is omitted for brevity)
# ...
# Finally, evaluate the final model on the NEVER-USED-BEFORE test set
y_pred = model.predict(X_test)

# Calculate test accuracy
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {test_accuracy:.2f}")

# Get a detailed performance report
print(classification_report(y_test, y_pred))