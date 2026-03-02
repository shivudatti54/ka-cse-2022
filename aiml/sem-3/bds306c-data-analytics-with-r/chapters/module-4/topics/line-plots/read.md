r
# Load the necessary library
library(ggplot2)

# Create some sample time-series data
time <- 1:20
voltage <- cumsum(rnorm(20)) # Simulating a voltage signal

# Create a dataframe
sensor_data <- data.frame(Time = time, Voltage = voltage)

# Create the basic line plot
ggplot(data = sensor_data, aes(x = Time, y = Voltage)) +
  geom_line()