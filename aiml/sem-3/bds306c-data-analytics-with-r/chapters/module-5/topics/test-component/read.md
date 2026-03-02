r
# Load necessary library
library(caTools) # For sample.split function

# Load a sample dataset (e.g., mtcars)
data(mtcars)

# Step 1: Split the data (70% for training, 30% for testing)
set.seed(123) # Ensures reproducibility
split <- sample.split(mtcars$mpg, SplitRatio = 0.7)
training_set <- subset(mtcars, split == TRUE)
test_set <- subset(mtcars, split == FALSE)

# Step 2: Train the model on the training data
# Let's predict mileage (mpg) based on weight (wt) and horsepower (hp)
model <- lm(mpg ~ wt + hp, data = training_set)
summary(model)

# Step 3: Make predictions on the test set inputs
predictions <- predict(model, newdata = test_set)

# Step 4: Evaluate the model by comparing predictions to test set actuals
# Create a data frame to view actual vs. predicted
results <- data.frame(Actual = test_set$mpg, Predicted = predictions)
print(results)

# Calculate key regression metrics for the test set
# Mean Absolute Error (MAE)
mae <- mean(abs(results$Actual - results$Predicted))
print(paste('MAE:', mae))

# Root Mean Squared Error (RMSE)
rmse <- sqrt(mean((results$Actual - results$Predicted)^2))
print(paste('RMSE:', rmse))