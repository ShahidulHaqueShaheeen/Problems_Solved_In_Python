# -*- coding: utf-8 -*-
"""Class Task _1.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

st = input()
index = int(input())


for i in range(index, -1,-1):
    print(st[i],end='')
print(st[index+1:])