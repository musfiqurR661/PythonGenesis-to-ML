# Initialize an empty dictionary to represent the matrix
matrix = {}

# Get the size of the matrix from the user
rows = 3
columns = 3

# Populate the dictionary with keys representing row and column indices
for i in range(rows):
    for j in range(columns):
        # Get input value from the user for each element
        value = int(input(f"Enter value for position ({i+1}, {j+1}): "))
        # Use a tuple (i, j) as the key to represent the row and column indices
        matrix[(i, j)] = value

# Print the matrix
print("Matrix:")
for i in range(rows):
    for j in range(columns):
        print(matrix[(i, j)], end="\t")  # Print each element of the matrix
    print()  # Move to the next row
