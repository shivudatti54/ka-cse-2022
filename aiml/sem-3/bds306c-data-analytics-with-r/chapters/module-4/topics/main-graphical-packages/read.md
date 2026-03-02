r
    # Create a basic scatter plot
    plot(mpg ~ disp, data = mtcars, main = "Base Graphics: MPG vs. Displacement")

    # Add a linear regression line to show trend
    abline(lm(mpg ~ disp, data = mtcars), col = "red")

    # Add a legend
    legend("topright", legend = "Trend Line", col = "red", lty = 1)