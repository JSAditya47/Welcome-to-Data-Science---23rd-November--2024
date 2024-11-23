import numpy as np

matrix_a = np.arange(9, dtype= float).reshape(3, 3)
print("Matrix 'Matrix_A' :")
print(matrix_a)

array_b = np.array([10, 10, 10])
print("\nArray 'Array_B':")
print(array_b)

print("\nElement - Wise Addition of 'Matrix_A' and 'Array_B': ")
print(np.add(matrix_a, array_b))

print("\nElement - Wise Subtraction of 'Array_B' from 'Matriz_A': ")
print(np.subtract(matrix_a, array_b))

print("\nElement - Wise Multiplication of 'Matrix_A' and 'Array_B': ")
print(np.multiply(matrix_a, array_b))

print("\nElement - Division of 'Matrix_A' and 'Array_B': ")
print(np.divide(matrix_a, array_b))


