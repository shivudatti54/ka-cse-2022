r
# Load necessary library
library(caTools)

# Set a seed for reproducibility
set.seed(123)

# Create a split indicator. Here, we split based on the dependent variable 'mpg'
# SplitRatio = 0.8 means 80% of data goes to training.
split <- sample.split(mtcars$mpg, SplitRatio = 0.8)

# Create the training and test sets using the split indicator
training_set <- subset(mtcars, split == TRUE)
test_set <- subset(mtcars, split == FALSE)

# Now, build a model using only the training_set
model <- lm(mpg ~ wt + hp, data = training_set)

# Use the model to make predictions on the test_set (unseen data)
predictions <- predict(model, newdata = test_set)

# Evaluate the model by comparing predictions to actual values in test_set
# A common metric is Mean Squared Error (MSE)
mse <- mean((test_set$mpg - predictions)^2)
print(paste("Mean Squared Error on Test Set:", mse))