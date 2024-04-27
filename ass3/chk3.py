import pandas as pd
import numpy as np

# Load the iris dataset
iris_data = pd.read_csv("../Assignment_3/iris.csv")

# Extract features and labels
X = iris_data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = iris_data['variety.classnames'].values

# Convert labels to binary: 0, 1
y = np.where(y == 'Setosa', 0, 1)

# Combine features and labels
data = np.column_stack((X, y))

# Shuffle the combined dataset
np.random.shuffle(data)

# Separate shuffled data back into X and y
X_shuffled = data[:, :-1]
y_shuffled = data[:, -1]

# Train Test Split (80% train, 20% test)
split_index = int(0.8 * len(X_shuffled))
X_train = X_shuffled[:split_index]
y_train = y_shuffled[:split_index]
X_test = X_shuffled[split_index:]
y_test = y_shuffled[split_index:]

# Algorithm [Test Prediction]
k = 5
y_test_predicted = np.zeros(len(X_test))

for i in range(len(X_test)):
    x_test = X_test[i]
    # Calculate Euclidean distances between x_test and X_train
    distances = np.sqrt(np.sum((X_train - x_test) ** 2, axis=1))
    # Get the indices of the k nearest neighbors
    min_dist_indices = np.argsort(distances)[:k]
    # Get the corresponding labels of the k nearest neighbors
    y_neighbors = y_train[min_dist_indices]
    # Find the value that occurs most in y_neighbors
    y_test_predicted[i] = np.bincount(y_neighbors.astype(int)).argmax()

# Metrics Calculation (Accuracy)
correct_predictions = np.sum(y_test == y_test_predicted)
total_predictions = len(y_test)
accuracy = correct_predictions / total_predictions

# Print the accuracy
print("Accuracy (Test):", accuracy)
