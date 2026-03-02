python
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# 1. Create and train a simple model
X, y = make_classification(n_samples=100, n_features=4, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 2. Save (Pickle) the model to a file
with open('trained_model.pkl', 'wb') as file: # 'wb' for WRITE Binary
    pickle.dump(model, file)
    print("Model saved successfully!")

# ... Later, in a new session ...

# 3. Load (Unpickle) the model from the file
with open('trained_model.pkl', 'rb') as file: # 'rb' for READ Binary
    loaded_model = pickle.load(file)
    print("Model loaded successfully!")

# 4. Use the loaded model for prediction
new_sample = [[-1.5, 2.4, -0.9, 1.1]]
prediction = loaded_model.predict(new_sample)
print(f"Prediction for new sample: {prediction}")