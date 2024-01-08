# -*- coding: utf-8 -*-
"""task_80

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a program that prints a chrismastree using a single loop


def tree(h):

    initial_star = 1

    column = h*2 -1

    for i in range(h):

        spaces = (column - initial_star) // 2

        print(spaces * ' ' + initial_star * "*" + spaces * ' ')

        initial_star += 2

    return

print(tree(5))
print(tree(7))


'''
def print_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

tree_height = 5
print_christmas_tree(tree_height)
'''



