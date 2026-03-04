# ASSIGNMENT 3, MODULE 4: FUNCTIONS & MODULES IN PYTHON, TASK 1: CALCULATE FACTORIAL USING PYTHON.

def factorial(n):
    """
    Calculates the factorial of a non-negative integer recursively.
    """
    if n==0 or n==1: # base case :Factorial of 0 and 1 is 1.
        return 1
    else: # Recursive step : n! = n * (n-1)!
        return n * factorial(n-1) # calls itself with a smaller number
num = input("Enter a number: ")
# check if input is a number or not
if not num.isdigit():
    print("Please enter a valid positive number (not string or negative).")
else:
    num = int(num)
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"Factorial of {num} is",result)            