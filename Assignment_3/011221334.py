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

# # Print check shuffled X and y
# print("Shuffled X:")
# print(X_shuffled[:)
#
# print("\nShuffled y:")
# print(y_shuffled[:])

#Train Test Split 80%  20%
split_index = int(0.8 * len(X))
#print(split_index)

# Splitting the data
X_train, X_test = X_shuffled[:split_index], X_shuffled[split_index:]
y_train, y_test = y_shuffled[:split_index], y_shuffled[split_index:]


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def most_common(lst):
    return np.argmax(np.bincount(lst))

#KNN implementation

def predict_labels(X_train, y_train, X_test, k=5):
    y_test_predicted = np.zeros(len(X_test))

    for i in range(len(X_test)):
        x_test = X_test[i]
        distances = np.array([euclidean_distance(x_test, x_train) for x_train in X_train])
        min_dist_indices = np.argsort(distances)[:k]
        y_neighbor = y_train[min_dist_indices]
        y_test_predicted[i] = most_common(y_neighbor)

    return y_test_predicted

#chk predected
y_test_predicted = predict_labels(X_train, y_train, X_test)
# print("Predicted labels for test set:", y_test_predicted)


def calculate_accuracy(y_test, y_test_predicted):
    correct_predictions = np.sum(y_test == y_test_predicted)

    total_predictions = len(y_test)

    accuracy = correct_predictions / total_predictions

    return accuracy


accuracy = calculate_accuracy(y_test, y_test_predicted)
print("Accuracy (Test):", accuracy)

