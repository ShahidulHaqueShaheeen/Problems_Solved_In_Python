# -*- coding: utf-8 -*-
"""Home Task _3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

num = int(input())

divisors = []
flag = True
i = 2

if num < 2:
    flag = False

while i < num:

    if num % i == 0:
        flag = False
        divisors.append(i)
    i += 1

divisors.append(1)

sum = 0
for i in divisors:
    sum +=i

if flag == True:
    print(f"{num} is a prime number")
elif num == sum:
    if num != 1:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a prime or perfect number")

else:
    print(f"{num} is not a prime or perfect number")