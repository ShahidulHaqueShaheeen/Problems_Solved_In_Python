# -*- coding: utf-8 -*-
"""task_78

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a dummy program that can perform login and registration using a menu driven program

checker = {}

def user_menu():


    user_input = input('''
    Enter 1 to Register.
    Enter 2 for Login.
    Enter 3 to Exit.

    ''')

    if user_input == '1':
        register()

    elif user_input == '2':
        login()
    else:
        print("Bye")

def register():

    name = input("Enter your name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")

    checker[email] = [name,password]
    print("Registration Successful")
    print()

    user_menu()

def login():

    email = input("Enter your email : ")
    password = input("Enter your password : ")



    for i in checker:

        if email == i:
            flag = 1

            if password == checker[i][1]:
                print("Welcome")
            else:
                print("Wrong password")

        else:
            print("Email is not found")


user_menu()
