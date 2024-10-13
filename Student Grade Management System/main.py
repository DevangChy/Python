# Student Grade Management System

# Crate empty dictionary
student_grade = { }

# Add new Student
def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")

# Update Student info
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated{grade}")
    else:
        print(f"{name} is not found!")

# Delete Student info
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

# View all student
def display_student():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No Data found/added")

# write condition of system
if __name__ == "__main__":
    while True:
        print("\n Student Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            grade = int(input("Enter your grade: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter your name: ")
            grade = int(input("Enter your grade: "))
            update_student(name, grade)
        
        elif choice == 3:
            name = input("Enter your name: ")
            delete_student(name)
        
        elif choice == 4:
            display_student()

        elif choice == 5:
            print("Exiting the program...")
            break
        
        else:
            print("Invalid Choice...")

