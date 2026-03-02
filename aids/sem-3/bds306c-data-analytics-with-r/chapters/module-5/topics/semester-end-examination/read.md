r
library(dplyr)
total_sales <- sales_data %>%
  mutate(Total_Sales = Q1_Sales + Q2_Sales) %>%
  group_by(Product) %>%
  summarise(Total = sum(Total_Sales))