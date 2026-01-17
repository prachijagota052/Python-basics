# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Number of rows and columns in matrix1
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    
    # Number of rows and columns in matrix2
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible (columns of matrix1 == rows of matrix2)
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Matrices cannot be multiplied: incompatible dimensions.")
    
    # Resultant matrix of size (rows_matrix1 x cols_matrix2)
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    
    # Matrix multiplication using nested loops
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):  # or equivalently range(rows_matrix2)
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


# Example matrices
matrix1 = [
    [11, 21, 8],
    [5, 2, 7]
]

matrix2 = [
    [2, 8],
    [5, 1],
    [1, 1]
]

# Multiply the matrices
result = multiply_matrices(matrix1, matrix2)

# Print the result
for row in result:
    print(row)
