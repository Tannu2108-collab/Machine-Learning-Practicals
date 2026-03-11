from sklearn.cluster import KMeans
import numpy as np

# Data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4]])

# Model
kmeans = KMeans(n_clusters=2, n_init=10)
kmeans.fit(X)

# Results
print("--- K-Means Results ---")
print(f"Assigned Cluster Labels: {kmeans.labels_}")
print(f"Cluster Centers (Centroids):\n{kmeans.cluster_centers_}")
print(f"Prediction for [0, 0]: Cluster {kmeans.predict([[0, 0]])[0]}")
