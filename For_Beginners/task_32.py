# -*- coding: utf-8 -*-
"""task_32

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Print the first 20 numbers of a Fibonacci series
flag = 0

a  = 0
b = 1

print(a)
print(b)

while True:

    c = a + b
    print(c)
    a = b
    b = c

    flag += 1

    if flag == 18:
        break

