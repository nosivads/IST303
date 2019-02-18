# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 2019

CGU IST 303.W SP2019 1
Module 3: BCE 3.3: Team Exercise
"""

#Display menu of choices
print("MENU\n\n1. - List the best musical group ever\n2. - List the best \
sports team ever\n3. - Quit")

#Continue to request input until user enters '3', then 'break' out of the loop
while True:
    response = input("Enter the number for your choice: ")    
    if response == "1":
        print("The Beatles are the best ever")
    elif response == "2":
        print("The Cubs are the best ever")
    elif response == "3":
        print("OK! Hope you learned something")
        break
    else:
        print("That's not one of the choices. Try again.")

