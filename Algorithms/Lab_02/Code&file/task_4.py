# -*- coding: utf-8 -*-
"""Task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sRGxM9itgH14jeb4-cdcBGOE9mud9LuQ
"""

def maximum_tasks(tasks,person):
    n = len(tasks)

    tasks.sort(key=lambda x: x[1])

    selected_tasks = []
    c = 0
    while c < person:
      tasks.sort(key=lambda x: x[1])
      prev_end_time = -1

      for task in tasks:

        if task not in selected_tasks:
            start_time, end_time = task
            if start_time >= prev_end_time:
                selected_tasks.append(task)
                prev_end_time = end_time
                break
        else:
            continue

      tasks.sort(key=lambda x: x[0])
      for task in tasks:

        if task not in selected_tasks:
            start_time, end_time = task
            if start_time >= prev_end_time:
                selected_tasks.append(task)
                prev_end_time = end_time

        else:
            continue


      c+=1


    return selected_tasks




input_4=open("/content/input4.txt","r")
output_4=open("/content/output4.txt","w")


n = input_4.readline().split()
num = int(n[0])
person = int(n[1])

# print(num)
# print(person)

lst = []

for i in range(num):
    i = input_4.readline().split()
    i = (int(i[0]),int(i[1]))
    #print(i)
    lst.append(i)
#print(lst)


result = maximum_tasks(lst,person)

output_4.write(f"{len(result)}")

input_4.close()
output_4.close()