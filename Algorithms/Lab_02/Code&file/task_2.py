# -*- coding: utf-8 -*-
"""Task_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sRGxM9itgH14jeb4-cdcBGOE9mud9LuQ
"""

def merge(a1, a2):
    merged_arr = []

    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            merged_arr.append(a1[i])
            i += 1
        else:
            merged_arr.append(a2[j])
            j += 1


    merged_arr += a1[i:]
    merged_arr += a2[j:]

    return merged_arr

input_2=open("/content/input2.txt","r")
output_2=open("/content/output2.txt","w")

n1 = int(input_2.readline().strip())
arr1 = input_2.readline().split()
arr1 = [int(i) for i in arr1]

n2 = int(input_2.readline().strip())
arr2 = input_2.readline().split()
arr2 = [int(i) for i in arr2]

sorted_arr = merge(arr1, arr2)

for i in sorted_arr:
    output_2.write(f"{i} ")
#print(sorted_arr)

input_2.close()
output_2.close()