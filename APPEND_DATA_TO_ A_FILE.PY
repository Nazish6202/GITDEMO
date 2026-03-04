# ASSIGNMENT 4 ,MODULE 5: FILES, EXCEPTIONS, AND ERROR IN PYTHON ,TASK 2: WRITE AND APPEND DATA TO A FILE.
# Step 1: Take user input and write to file
user_input = input("Enter text to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

print("Data successfully written to output.txt.\n")

# Step 2: Take additional user input and append to the same file
additional_input = input("Enter additional text to append: ")

with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')

print("Data successfully appended.\n")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)