# import pandas as pd
# import numpy as np
# from sklearn.metrics import accuracy_score
#
# # Load the iris dataset
# iris_data = pd.read_csv("iris.csv")
#
# # Extract features and labels
# X = iris_data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
# y = iris_data['variety.class'].values
#
# # Convert labels to binary: 0, 1
# y = np.where(y == 'Setosa', 0, 1)
#
# # Shuffle the data
# random_indices = np.random.permutation(len(X))
# X_shuffled = X[random_indices]
# y_shuffled = y[random_indices]
#
# print("Shuffled X:")
# print(X_shuffled[:5])  # Print the first 5 rows of shuffled X
# print("\nShuffled y:")
# print(y_shuffled[:5])  # Print the first 5 elements of shuffled y

import pandas as pd

# Load the iris dataset
iris_data = pd.read_csv("../Assignment_3/iris.csv")

# Print the column names
print(iris_data.columns)

