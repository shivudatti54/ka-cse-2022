r
library(tidyverse)

ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point(aes(color = as.factor(cyl)), size = 3) + # Color points by cylinder
  geom_smooth(method = "lm", se = FALSE) +           # Add a trendline
  labs(title = "Car Weight vs. Fuel Economy",
       x = "Weight (1000 lbs)",
       y = "Miles per Gallon",
       color = "Cylinders") +
  theme_minimal()