# -*- coding: utf-8 -*-
"""Class Evaluation Task _1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

st = input()

flag = False

for i in st:
    if i != '0' and i != '1':
        flag = True

if flag:
    print("Not a Binary Number")
else:
    print("Binary Number")