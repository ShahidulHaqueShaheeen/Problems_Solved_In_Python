# -*- coding: utf-8 -*-
"""task_62

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers

O_lst = [1,2,3,4,5,6,7,8,9,10]

lst_E = []
lst_O = []

for i in range(len(O_lst)):

    if O_lst[i] % 2 == 0:
        lst_E.append(O_lst[i])
    else:
        lst_O.append(O_lst[i])

print(f"Even list : {lst_E} \n Odd list : {lst_O}")