# -*- coding: utf-8 -*-
"""task_20

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

'''
Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).
'''

s = float(input("Enter your Anual salary here : "))

if s > 500000 and s < 1000000:
    tax = (10/100)*s
    temp_salary = s - tax

elif s > 1000000 and s < 2000000:
    tax = (20/100)*s
    temp_salary = s - tax

else:
    tax = (30/100)*s
    temp_salary = s - tax

hra = (10/100)*temp_salary
da = (5/100)*temp_salary
pf = (3/100)*temp_salary

f_salary = (temp_salary - hra - da - pf)/12

print("Montly salary after all sort of deduction is : ",f_salary)