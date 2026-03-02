r
# Create sample data (e.g., sine wave)
x <- seq(0, 2*pi, length.out = 50)
y <- sin(x)

# Create a basic line plot
plot(x, y, type = "l", main = "Sine Wave (Base R)", xlab = "Time", ylab = "Amplitude")