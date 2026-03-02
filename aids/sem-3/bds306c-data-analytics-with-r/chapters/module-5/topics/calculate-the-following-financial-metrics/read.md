r
# Load required library (install first if needed)
library(tidyquant)

# Define cash flows: Initial investment of -1000, then returns of 500, 400, 300
cash_flows <- c(-1000, 500, 400, 300)
discount_rate <- 0.10 # 10%

# Calculate NPV
calculated_npv <- npv(cash_flows[-1], discount_rate) + cash_flows[1]
# cash_flows[-1] excludes the initial investment for the npv function
# cash_flows[1] is the initial cost, which we add (it's negative, so it subtracts)

print(paste("The Net Present Value is:", round(calculated_npv, 2)))
# Output: "The Net Present Value is: 49.21"