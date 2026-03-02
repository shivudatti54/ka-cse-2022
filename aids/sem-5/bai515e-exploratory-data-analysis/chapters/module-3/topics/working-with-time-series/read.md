python
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['power_consumption'])
plt.title('Time Series of Daily Power Consumption')
plt.xlabel('Date')
plt.ylabel('Consumption (MW)')
plt.grid(True)
plt.show()