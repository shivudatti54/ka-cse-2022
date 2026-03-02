python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Assume X is our feature matrix containing 'Engine_Size'
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X[['Engine_Size']]) # Creates [Engine_Size, Engine_Size^2]

model = LinearRegression()
model.fit(X_poly, y) # y is CO2_Emissions

# The R² score of the polynomial model will likely be higher than the linear one.
print(r2_score(y, model.predict(X_poly)))