import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("iris.csv")

# Separate features and labels
X = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = data['variety.classnames'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}).values

# Shuffling
indices = np.arange(len(X))
np.random.shuffle(indices)
#print(X)
#print(len(X))

X_shuffled = X[indices]
y_shuffled = y[indices]

# # Print the first few rows of shuffled X and y
# print("Shuffled X:")
# print(X_shuffled[:5])  # Print the first 5 rows of X_shuffled
#
# print("\nShuffled y:")
# print(y_shuffled[:5])  # Print the first 5 elements of y_shuffled

#Train Test Split 80%  20%
split_index = int(0.8 * len(X))
#print(split_index)

# Splitting the data
X_train, X_test = X_shuffled[:split_index], X_shuffled[split_index:]
y_train, y_test = y_shuffled[:split_index], y_shuffled[split_index:]

# Define a function to calculate Euclidean distance
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Define a function to find the most common element in a list
# Define a function to find the most common element in a NumPy array
def most_common(lst):
    return np.argmax(np.bincount(lst))



# Define k
k = 5

# np array to store y predicted test
y_test_predicted = np.zeros(len(X_test))


# For each test sample
for i in range(len(X_test)):
    x_test = X_test[i]

    # Calculate Euclidean distances between x_test and X_train
    distances = np.array([euclidean_distance(x_test, x_train) for x_train in X_train])

    # Find k indices with minimum distances
    min_dist_indices = np.argsort(distances)[:k]

    # Get labels of nearest neighbors
    y_neighbor = y_train[min_dist_indices]

    # Predict the label based on majority vote
    y_test_predicted[i] = most_common(y_neighbor)

# Print the predicted labels
print("Predicted labels for test set:", y_test_predicted)

#accuricy

# Calculate the number of correct predictions
correct_predictions = np.sum(y_test == y_test_predicted)

# Calculate the total number of predictions
total_predictions = len(y_test)

# Calculate the accuracy
accuracy = correct_predictions / total_predictions

# Print the accuracy
print("Accuracy (Test):", accuracy)
