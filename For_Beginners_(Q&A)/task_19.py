# -*- coding: utf-8 -*-
"""task_19

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

num = int(input("Enter your  4 digits number : "))

check = num

a = num % 10
num = num//10

b = num % 10
num = num//10

c = num % 10
num = num//10

d = num

sum = (a**4)+(b**4)+(c**4)+(d**4)

if sum == check:
    print("The given number is a narcissist number")

else:
    print("The given number is not a narcissist number")