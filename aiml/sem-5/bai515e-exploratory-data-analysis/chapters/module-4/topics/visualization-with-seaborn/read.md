python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme() # Apply the default theme
sns.scatterplot(data=df, x='rpm', y='torque', hue='engine_type')
plt.title('Torque vs RPM by Engine Type')
plt.show()