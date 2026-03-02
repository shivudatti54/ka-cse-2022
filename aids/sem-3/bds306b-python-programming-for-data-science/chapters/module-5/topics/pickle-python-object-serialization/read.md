python
import pickle

# Our complex data object (could be a model, a dict, etc.)
data_to_persist = {
    'model_name': 'LinearRegression',
    'version': 1.2,
    'hyperparameters': {'fit_intercept': True},
    'training_dataset': 'dataset_v1.csv'
}

# Serialize and write to a file (Pickling)
with open('trained_model.pkl', 'wb') as file:  # Note the 'wb' mode
    pickle.dump(data_to_persist, file)

# Later... read from the file and reconstruct the object (Unpickling)
with open('trained_model.pkl', 'rb') as file:  # Note the 'rb' mode
    loaded_data = pickle.load(file)

print(loaded_data)
# Output: {'model_name': 'LinearRegression', 'version': 1.2, ...}
print(loaded_data['model_name'])
# Output: LinearRegression