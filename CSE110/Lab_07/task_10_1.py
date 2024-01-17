# -*- coding: utf-8 -*-
"""task_10.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

import numpy as np

def manual_transpose(matrix):
    rows, cols = matrix.shape
    #print(rows,cols)
    transposed_matrix = np.empty((cols, rows), dtype=matrix.dtype)

    for i in range(cols):
        for j in range(rows):
            transposed_matrix[i, j] = matrix[j, i]

    return transposed_matrix

A1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

A2 = np.array([[1, 2, 3, 4],
               [1, 4, 9, 16]])

result1 = manual_transpose(A1)
result2 = manual_transpose(A2)


print("Transposed Array:")
print(result1)

print("Transposed Array:")
print(result2)