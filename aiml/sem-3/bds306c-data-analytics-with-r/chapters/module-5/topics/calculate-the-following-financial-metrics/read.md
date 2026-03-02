r
# Assuming 'prices' is a vector of closing prices
prices <- c(100, 102, 101, 105)

# Method 1: Using diff()
simple_returns <- diff(prices) / prices[-length(prices)]

# Method 2: Using vectorization
simple_returns <- prices[-1] / prices[-length(prices)] - 1

print(simple_returns)
# Output: [1]  0.02000000 -0.00980392  0.03960396