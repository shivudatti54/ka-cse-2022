r
# Step 1: Load necessary libraries and the data
library(ggplot2)
library(dplyr)
sales_df <- read.csv("sales_data.csv")

# Step 2: Data Exploration & Preprocessing
head(sales_df)
summary(sales_df)
# Check for NA values and handle if any
sales_df <- na.omit(sales_df)

# Step 3: Descriptive Statistics
cat("Mean Sales:", mean(sales_df$Sales), "\n")
cat("Mean Advertising:", mean(sales_df$Advertising), "\n")

# Step 4: Visualization - Scatter Plot to see the relationship
ggplot(sales_df, aes(x = Advertising, y = Sales)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Scatter Plot of Sales vs. Advertising", x = "Ad Budget", y = "Sales")

# Step 5: Statistical Analysis - Correlation and Linear Regression
correlation <- cor(sales_df$Advertising, sales_df$Sales)
cat("Correlation Coefficient:", correlation, "\n")

# Fit a linear model
model <- lm(Sales ~ Advertising, data = sales_df)
summary(model)

# Step 6: Interpretation
# Based on the high correlation coefficient and a significant p-value 
# (e.g., p < 0.05) for the Advertising variable in the model summary,
# we conclude that there is a strong positive relationship between 
# advertising spending and sales.