# ASSIGNMENT 3, MODULE 4: FUNCTIONS & MODULES IN PYTHON, TASK 2: USING THE MATH MODULE FOR CALCULATION.
from math import sqrt, log, sin, radians
num= input("Enter a number: ")
# check if input is a number or not
if not num.isdigit():
    print("Please enter a valid positive number (not string or negative).")
else:
    num= float(num)
    # sqaure root
    if num < 0:
        print("Square root is not defined for negative numbers.") 
    else:
        print("Square root: ", sqrt(num))
    # Natural logorithm
    if num <= 0:
        print("Natural logorithm is not defined for zero or negative numbers.")
    else:
        print("Logorithm: ", log(num))
    # Sine (in radian)
    print("Sine: ",sin(radians(num)))