# -*- coding: utf-8 -*-
"""task_67

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# The max item of each row of a matrix.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
r = 1
for i in matrix:

    max = i[0]
    for j in i:

        if j > max:
            max = j
    print(f"Max value of {r} number row is {max}")
    r +=1

