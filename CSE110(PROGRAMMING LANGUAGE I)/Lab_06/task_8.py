# -*- coding: utf-8 -*-
"""task_8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

def enter_student_info():
    grade_list = []

    for i in range(5):
        name = input("Enter student's name: ")
        gpa = float(input("Enter CSE110 GPA: "))
        student_info = [name, gpa]
        grade_list.append(student_info)

    return grade_list

class_grade_list = enter_student_info()
print(class_grade_list)