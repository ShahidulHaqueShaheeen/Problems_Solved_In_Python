# -*- coding: utf-8 -*-
"""Home Task_3.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

def calc_tax(age,salary):

    if age < 18 or salary < 10000:
        return 0
    else:
        if 10000 <= salary <= 20000:
            tax = (salary * 7) / 100
            return tax
        elif 20000 < salary:
            tax = (salary * 14) / 100
            return tax


def calc_yearly_tax():

    sum = 0
    age = int(input())

    for i in range(1,13):

        salary = int(input())
        tax = calc_tax(age,salary)
        print(f"Month{i} tax: {tax}")

        sum += tax
    print(f"Total Yearly Tax: {sum}")

calc_yearly_tax()