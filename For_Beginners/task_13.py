# -*- coding: utf-8 -*-
"""task_13

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write  a program that will tell whether the given number is divisible by 3 & 6.

num = int(input("Enter your number : "))

if (num % 3 == 0 and num % 6 == 0):
    print("Yes, the given number is divisible by 3 and 6")
else:
    print("No, the given number is not divisible by 3 and 6")