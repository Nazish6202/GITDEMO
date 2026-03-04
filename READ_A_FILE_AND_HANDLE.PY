# ASSIGNMENT 4 ,MODULE 5: FILES, EXCEPTIONS, AND ERROR IN PYTHON  ,TASK 1: READ A FILE AND HANDLE ERRORS.
try:
    # Try to open and read the file
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        
        # Read and print each line with line numbers
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.rstrip()}")
            line_number += 1
            
except FileNotFoundError:
    # Handle case when file doesn't exist
    print("Error: the file 'sample.txt' was not found.")