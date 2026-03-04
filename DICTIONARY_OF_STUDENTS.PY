
STUDENTS_DETAILS= {"Rahul": 85, "Alice": 80, "Mohit": 90}
STUDENT_NAME=input("Enter the student's name: ")
if STUDENT_NAME in STUDENTS_DETAILS :
    MARKS= STUDENTS_DETAILS[STUDENT_NAME]
    print(f"{STUDENT_NAME}'s marks: {MARKS}")
else:
    print("Student not found!!")