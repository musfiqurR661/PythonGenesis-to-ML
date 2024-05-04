import numpy as np
import matplotlib.pyplot as plt

# Load data from text file
X = np.loadtxt("jaint_feats.txt")
centroid_old = np.loadtxt("jain_centers.txt")
centroid_new = np.zeros([2, 2])
# First scatter plot
plt.scatter(X[:, 0], X[:, 1], s=15, color='blue')
plt.scatter(centroid_old[:, 0], centroid_old[:, 1], marker='*', s=350, color='orange')
plt.show()
label = np.empty(X.shape[0], dtype=int)
# Final scatter plot


plt.scatter(X[label == 0, 0], X[label == 0, 1], s=15, color='red')
plt.scatter(X[label == 1, 0], X[label == 1, 1], s=15, color='green')
plt.scatter(centroid_old[0, 0], centroid_old[0, 1], marker='*', s=350, color='red')
plt.scatter(centroid_old[1, 0], centroid_old[1, 1], marker='*', s=350, color='green')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Final Clustering with Centroids')
plt.show()
