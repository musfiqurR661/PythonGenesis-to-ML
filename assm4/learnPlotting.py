import numpy as np
import matplotlib.pyplot as plt
# Load data from text file
X = np.loadtxt("jaint_feats.txt")
centroid_old = np.loadtxt("jain_centers.txt")
centroid_new = np.zeros([2, 2])

#first scatter
plt.scatter(X[:, 0], X[:, 1], s = 10 , color = 'blue')
plt.scatter(centroid_old[:, 0], centroid_old[:, 1], marker = '*', s = 250, color = 'orange')
plt.show()

# Initialize label array
label = np.empty(X.shape[0]) # X.shape[0] = len(X)
#print(label.shape)

#distance calculation
def distance(point1, point2):
    return np.sqrt(np.sum((point1-point2)**2))

#Kmn
for e in range(100):
    for i in range(X.shape[0]):
        dist = np.zeros(centroid_old.shape[0])
        for j in range(centroid_old.shape[0]):
            dist[j] = distance(X[i], centroid_old[j])
        label[i] = np.argmin(dist)

    #update centroid:
    for j in range(centroid_new.shape[0]):
        centroid_new[j] = np.mean(X[label == j], axis=0)

    #stop condition
    absolute_differences = np.abs(centroid_new - centroid_old)
    max_difference = np.max(absolute_differences)

    if max_difference < 1E-7:
        break
    else:
        centroid_old = centroid_new.copy()

#first scatter
plt.scatter(X[label == 0, 0], X[label == 0, 1], s = 12, color = 'red')
plt.scatter(X[label == 1, 0], X[label == 1, 1], s = 12,  color = 'green')
plt.scatter(centroid_old[0, 0], centroid_old[0, 1], marker = '*', s = 250, color = 'red')
plt.scatter(centroid_old[1, 0], centroid_old[1, 1], marker = '*', s = 250, color = 'green')
plt.show()
