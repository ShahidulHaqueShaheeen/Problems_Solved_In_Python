# -*- coding: utf-8 -*-
"""task_38

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write  a program to print the pyramid

r = int(input("Enter your number of rows : "))

for i in range(r):

    for j in range(r-i-1):
        print(end = " ")

    for k in range(i+1):
        print('*', end = " ")

    print()