python
import plotly.express as px

# Load data
df = px.data.iris()

# Create an interactive scatter plot with tooltips
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species", hover_data=['petal_width', 'petal_length'],
                 title="Interactive Iris Dataset Explorer")
fig.show() # This will display an interactive plot you can hover over and zoom.