# -*- coding: utf-8 -*-
"""task_15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Checking the two rectangle are overlapping or no

def doOverlap(L1, R1, L2, R2):
    # Check for horizontal overlap
    if L1[0] > R2[0] or L2[0] > R1[0]:
        return False

    # Check for vertical overlap
    if L1[1] < R2[1] or L2[1] < R1[1]:
        return False

    return True


L1 = (0, 10)  # Bottom-left corner of the first rectangle
R1 = (10, 0)  # Top-right corner of the first rectangle
L2 = (5, 5)   # Bottom-left corner of the second rectangle
R2 = (15, 0)  # Top-right corner of the second rectangle

if doOverlap(L1, R1, L2, R2):
    print("Rectangles overlap.")
else:
    print("Rectangles do not overlap.")