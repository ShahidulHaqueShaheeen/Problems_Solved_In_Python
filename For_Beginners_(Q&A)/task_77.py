# -*- coding: utf-8 -*-
"""task_77

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a function that accepts a string and returns the number of upper case chars and lower case chars as a dictionary

def counter(st):

    dct = {"UpperCase":0,"LowerCase":0}


    for i in st:

        if i.isupper():
            dct["UpperCase"] += 1

        elif i.islower():
            dct["LowerCase"] += 1

    return dct


print(counter("Shahidul Haque Shaheen"))

