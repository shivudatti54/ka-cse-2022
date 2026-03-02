r
# Creating a data frame for sensor data
sensor_data <- data.frame(
  sensor_id = c(1, 2, 3, 4),
  reading = c(23.5, 26.1, 24.8, 25.3),
  operational = c(TRUE, TRUE, FALSE, TRUE),
  location = c("A", "B", "A", "C")
)
print(sensor_data)