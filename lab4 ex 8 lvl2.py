import numpy as np
matrix = np.random.randint(1, 100, (6, 6))
print("The original matrix:")
print(matrix)
def swap_max_elements(matrix, row1, row2):
    max_index1 = np.argmax(matrix[row1])
    max_index2 = np.argmax(matrix[row2])
    matrix[row1][max_index1], matrix[row2][max_index2] = matrix[row2][max_index2], matrix[row1][max_index1]
swap_max_elements(matrix, 0, 1)
swap_max_elements(matrix, 2, 3)
swap_max_elements(matrix, 4, 5)

print("\nthe matrix after replacing the elements:")
print(matrix)