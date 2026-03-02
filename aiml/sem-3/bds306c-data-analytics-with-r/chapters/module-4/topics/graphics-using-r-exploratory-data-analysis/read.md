r
library(ggplot2)
# Histogram
ggplot(mtcars, aes(x = mpg)) +
  geom_histogram(bins = 10, fill = "steelblue", color = "black")

# Density Plot
ggplot(mtcars, aes(x = mpg)) +
  geom_density(fill = "orange", alpha = 0.6)