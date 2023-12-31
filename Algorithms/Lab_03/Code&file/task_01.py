# -*- coding: utf-8 -*-
"""Task_01.ipynb

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


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    a1 = merge_sort(arr[:mid])
    a2 = merge_sort(arr[mid:])

    arr = merge(a1, a2)
    return arr

input_1=open("/content/input1.txt","r")
output_1=open("/content/output1.txt","w")

n = int(input_1.readline().strip())
arr = input_1.readline().split()
arr = [int(i) for i in arr]


sorted_arr = merge_sort(arr)

for i in sorted_arr:
    output_1.write(f"{i} ")





input_1.close()
output_1.close()