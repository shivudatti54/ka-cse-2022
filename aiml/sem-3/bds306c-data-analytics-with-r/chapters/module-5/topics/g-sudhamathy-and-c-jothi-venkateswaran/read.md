r
# Install and load the required package
install.packages("arules")
library(arules)

# Create a sample transaction dataset (like a list of market baskets)
transactions <- list(
  c("Milk", "Bread", "Butter"),
  c("Milk", "Bread"),
  c("Milk", "Eggs"),
  c("Bread", "Butter", "Jam"),
  c("Milk", "Bread", "Butter", "Jam")
)

# Convert the list into a transaction object format
trans <- as(transactions, "transactions")

# Run the Apriori algorithm
# Set min.support = 0.2 (appears in at least 20% of transactions)
# Set min.confidence = 0.6
rules <- apriori(trans, parameter = list(support = 0.2, confidence = 0.6, minlen = 2))

# Inspect the generated rules, sorted by confidence
inspect(sort(rules, by = "confidence"))