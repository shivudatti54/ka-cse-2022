r
# Read a CSV file with a header
my_data <- read.csv("customer_data.csv")

# Read a CSV file without a header, assigning column names
my_data <- read.csv("sensor_readings.csv", header = FALSE, col.names = c("Time", "Voltage", "Current"))