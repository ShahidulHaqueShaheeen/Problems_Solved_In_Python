# -*- coding: utf-8 -*-
"""Home Task_2.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

def show_palindrome(num):

    for i in range(1,num+1):
        print(i,end="")

    for j in range(num-1,0,-1):
        print(j,end="")

show_palindrome(5)