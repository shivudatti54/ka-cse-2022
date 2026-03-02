r
# Create a vector of hypothetical data (e.g., monthly sales figures)
my_data <- c(125, 128, 135, 142, 130, 148, 155, 160, 158, 165, 170, 172,
             178, 182, 190, 195, 185, 200, 210, 215, 208, 220, 225, 230,
             235, 240, 250, 255, 245, 260, 270, 275, 268, 280, 285, 290)

# Convert it to a time series object
my_ts <- ts(my_data, start = c(2021, 1), frequency = 12)

# Print the object
print(my_ts)
# This will show the data with its associated time indices: 2021.000, 2021.083, ...