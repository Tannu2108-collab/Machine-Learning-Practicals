import numpy as np
from sklearn.linear_model import LinearRegression

# X: Features (e.g., Area, Rooms, Age)
X = np.array([[1000, 2, 5], [1500, 3, 10], [2000, 4, 15]])
# y: Target (Price)
y = np.array([200, 300, 400])

# Model initialization and training
model = LinearRegression()
model.fit(X, y)

# Prediction for a new house (1200 area, 2 rooms, 6 years old)
new_data = np.array([[1200, 2, 6]])
prediction = model.predict(new_data)

print(f"Predicted Price: {prediction[0]}")
