r
# Example: Create a simple vector of values
categories <- c("A", "B", "C", "D")
values <- c(25, 40, 15, 30)

# Create a basic bar plot
barplot(values,
        names.arg = categories,  # Assign category names
        col = "steelblue",
        main = "Simple Bar Plot (Base R)",
        xlab = "Categories",
        ylab = "Values")