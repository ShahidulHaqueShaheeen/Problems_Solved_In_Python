# -*- coding: utf-8 -*-
"""task_42

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

'''
Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
'''

n = int(input("Enter your number here : "))

x = int(input("Enter your number here : "))

sum = 1

sq = 0

for i in range(2, n+1):

    sq = x ** i
    print(sq)
    sum = sum + (sq / i)

    sq = 0


print("The sum of nth series is : ",sum)