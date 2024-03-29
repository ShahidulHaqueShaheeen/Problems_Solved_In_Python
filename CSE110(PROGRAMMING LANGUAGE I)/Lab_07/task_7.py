# -*- coding: utf-8 -*-
"""task_7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

import numpy as np

def flatten(arr):

    temp = temp = np.empty(len(arr) * len(arr[0]), dtype=int)
    idx = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp[idx] = arr[i,j]
            idx += 1
    return temp


arr1 = np.array( [ [1, 2, 3],
[3, 4, 5] ] )
arr2 = flatten(arr1)
print(arr2)