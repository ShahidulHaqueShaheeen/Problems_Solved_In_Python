# -*- coding: utf-8 -*-
"""Home Task_2.3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

def show_triangle(n):

    for i in range(1,n+1):

        for j in range(1,n-i+1):
            print(".",end=" ")
        for k in range(1,i+1):
            print(k,end=" ")
        for l in range(i-1,0,-1):
            print(l,end=" ")
        for j in range(1,n-i+1):
            print(".",end=" ")
        print()

show_triangle(10)