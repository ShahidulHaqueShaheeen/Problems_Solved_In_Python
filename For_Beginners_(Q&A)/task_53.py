# -*- coding: utf-8 -*-
"""task_53

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a python program to convert a string to title case without using the title()

st = "hELLo sHAHiduL haQUE sHAHeen"

x = st.split()

y = ''

for i in x:

    y = y + i[0].upper()+i[1:].lower()+' '

print(y)