# -*- coding: utf-8 -*-
"""Home Task_1.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

def is_prime(num):

    if num < 2:
        return False

    flag  = True
    for i in range(2,num):

        if num % i == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False

prime_check = is_prime(15)
print(prime_check)