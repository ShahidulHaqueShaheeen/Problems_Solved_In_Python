# -*- coding: utf-8 -*-
"""task_12

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

r , h = map(float,input("Enter the vlaue of radius and height here : ").split())

vol = 3.14 * (r**2) * h

print("The volume of the cylender is : ",vol)

cost = (vol/1000)*40

print("Your total cost : ",cost)