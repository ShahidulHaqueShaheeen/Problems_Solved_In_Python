# -*- coding: utf-8 -*-
"""task_59

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

#  Write a program that can count the number of words in a given string


x = "Shahidul Haque Shaheen"
x = x.split()

#print(x)

c = 0

for i in x:

    c += 1

print("The  number of words in the given string is : ",c)