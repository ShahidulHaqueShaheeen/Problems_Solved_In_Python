# -*- coding: utf-8 -*-
"""task_43

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

'''
The natural logarithm can be approximated by the following series.

(x-1/x)+1/2(x-1/x)**2+1/2(x-1/x)**3+.............1/2(x-1/x)**7

If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.

'''

n = int(input("Enter your number here : "))
x = int(input("Enter your number here : "))

sum = ((x-1)/x)

for i in range(2, n+1):

    sum = sum + (1/2*((x-1)/x)**i)

print("The sum of nth series is : ",sum)