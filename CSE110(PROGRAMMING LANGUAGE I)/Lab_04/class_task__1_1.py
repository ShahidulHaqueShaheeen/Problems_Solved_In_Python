# -*- coding: utf-8 -*-
"""Class Task _1.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

st = input()

for i in range(len(st)-1,-1,-1):

    print(st[i],end='')
st = st[::-1]
print()
print(st)
# Using Slicing