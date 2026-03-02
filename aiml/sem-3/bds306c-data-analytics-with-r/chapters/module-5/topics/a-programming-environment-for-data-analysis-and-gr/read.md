r
# Using Base Graphics to plot mtcars
plot(mtcars$wt, mtcars$mpg, main = "Base Plot: Weight vs. MPG", xlab = "Weight", ylab = "Miles per Gallon")
abline(lm(mpg ~ wt, data = mtcars), col = "red") # Add a regression line

# Using ggplot2 for the same plot
library(ggplot2)
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "ggplot2: Weight vs. MPG", x = "Weight", y = "Miles per Gallon")