# -*- coding: utf-8 -*-
"""Task 01(b).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sRGxM9itgH14jeb4-cdcBGOE9mud9LuQ
"""

input_1=open("/content/input1(b).txt","r")
output_1=open("/content/output1(b).txt","w")

x=input_1.readline().split()
l=int(x[0])
target=int(x[1])
#print(l,target)
arr=input_1.readline().split()
lst=[int(i) for i in arr]
print(lst)

left=0
right=len(lst)-1

while left < right:

    sum=lst[left]+lst[right]

    if sum == target:

        output_1.write(f"{i+1} {j+1}")
        break

    elif sum < target:

        left+=1

    else:

        right-=1


input_1.close()
output_1.close()