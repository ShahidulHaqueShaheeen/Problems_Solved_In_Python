# -*- coding: utf-8 -*-
"""Class Task_2.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

def is_valid_triangle(x,y,z):

    if x+y > z and y+z > x and z+x > y:
        return True
    else:
        return False


result=is_valid_triangle(7,5,10)
print( result )

result=is_valid_triangle(3,2,1)
print( result )