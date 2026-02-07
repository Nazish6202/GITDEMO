# ASSIGNMENT 3 ,MODULE 4: FUNCTIONS & MODULES IN PYTHON ,TASK 1: CALCULATE FACTORIAL USING PYTHON.
def Factorial():
    num=int(input("Enter a number to find its Facorial: "))
    temp=1
    for i in range (1,num+1):
        temp*=i
    return(f"Factorial of {num} is {temp}")
print(Factorial())