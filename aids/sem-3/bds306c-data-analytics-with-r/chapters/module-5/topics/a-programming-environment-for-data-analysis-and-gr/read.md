r
# Using base R to plot mpg vs. wt from the mtcars dataset
plot(mtcars$wt, mtcars$mpg, main = "Fuel Efficiency vs. Weight", xlab = "Weight (1000 lbs)", ylab = "Miles per Gallon")

# Using ggplot2 for the same plot with a smoother trend line
library(ggplot2)
ggplot(mtcars, aes(x = wt, y = mpg)) +  # Define data and aesthetics
  geom_point() +                        # Add a point geometry
  geom_smooth(method = "lm") +          # Add a linear model smooth line
  labs(title = "Fuel Efficiency vs. Weight", x = "Weight (1000 lbs)", y = "Miles per Gallon")