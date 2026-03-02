r
# Sample data for 12 months (Jan to Dec 2023)
co2_emissions <- c(315, 320, 325, 330, 335, 340, 345, 340, 335, 330, 325, 320)

# Create a time series object
ts_data <- ts(co2_emissions, start = c(2023, 1), frequency = 12)

# Print the object
print(ts_data)