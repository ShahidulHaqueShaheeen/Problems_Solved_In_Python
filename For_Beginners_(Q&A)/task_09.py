# -*- coding: utf-8 -*-
"""task_09

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

a1, a2, a3 = map(int, input("Enter three angle here : ").split())

if (a1+a2+a3) == 180 and a1!=0 and a2!=0 and a3!=0:
    print("Yes, they can form a triangle")
else:
    print("No, they can't form a triangle")