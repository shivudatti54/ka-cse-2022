python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Assuming 'X' contains features and 'y' contains the target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the unseen test set
test_score = model.score(X_test, y_test)
print(f"Model R^2 score on test set: {test_score:.2f}")