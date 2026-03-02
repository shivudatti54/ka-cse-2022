r
# Create some sample data
x <- 1:10
y <- x^2

# High-level plot function creates a scatter plot
plot(x, y, type = "o", col = "blue", pch = 16, main = "Base Graphics Example", xlab = "X-axis", ylab = "Y-axis")

# Low-level function to add a grid
grid()