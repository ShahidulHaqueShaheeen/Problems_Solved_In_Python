# -*- coding: utf-8 -*-
"""task_16

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

'''
Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C)      HUMIDITY(%)      WEATHER

      >= 30                             >=90                Hot and Humid
      >= 30                             < 90                 Hot
      <30                                >= 90               Cool and Humid
      <30                                 <90                 Cool

'''
t, h = map(float, input("Enter your temparature and humidity : ").split())

if t >=30 and h >=90:
    print("Weather is Hot and Humid")

elif t >=30 and h <90:
    print("Weather is Hot")

elif t <30 and h >=90:
    print("Weather is Cool and Humid")

else:
    print("Weather is Cool")