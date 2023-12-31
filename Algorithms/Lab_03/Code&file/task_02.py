# -*- coding: utf-8 -*-
"""Task_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sRGxM9itgH14jeb4-cdcBGOE9mud9LuQ
"""

def search_max(a1, a2):
    return max(a1, a2)


def find_max(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    a1 = find_max(arr[:mid])
    #print(a1)
    a2 = find_max(arr[mid:])
    #print(a2)
    Max = search_max(a1, a2)

    return Max


input_2=open("/content/input2.txt","r")
output_2=open("/content/output2.txt","w")

n = int(input_2.readline().strip())
arr = input_2.readline().split()
arr = [int(i) for i in arr]


Max = find_max(arr)
output_2.write(f"{Max[0]}")


input_2.close()
output_2.close()