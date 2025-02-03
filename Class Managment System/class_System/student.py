# Student Management System

import mysql.connector as mydb

# connection to the database
conn = mydb.connect(host="localhost", user="root", password="Pass", database="class")
cur = conn.cursor()

# Function to get student roll number
def get_roll():
    while True:
        try:
            roll = int(input("Enter Students Roll No: "))
            return roll
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")

# Function to get student name
def get_name():
    return input("Enter Students Name: ")

# Function to get student email
def get_email():
    return input("Enter Students Email: ")

# Function to get student phone number
def get_phone():
    while True:
        try:
            phone = int(input("Enter Students Phone No: "))
            return phone
        except ValueError:
            print("Invalid input. Please enter a valid phone number.")

# Function to get student address
def get_address():
    return input("Enter Students Address: ")

# Function to add student details in database
def add_student():
    roll = get_roll()
    name = get_name()
    email = get_email()
    phone = get_phone()
    address = get_address()
    data = (roll, name, email, phone, address)
    query = "INSERT INTO student (roll, name, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(query, data)
    conn.commit()
    print("Student Details Added Successfully!")

# Function to show student details in database
def show_student():
    roll = get_roll()
    query = "SELECT * FROM student WHERE roll = %s"
    cur.execute(query, (roll,))
    student = cur.fetchone()
    if student:
        print("Student Details:")
        print(f"Roll No.: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Email: {student[2]}")
        print(f"Phone: {student[3]}")
        print(f"Address: {student[4]}")
    else:
        print("Student not found.")

# Function to update student details in database
def update_student():
    print("Enter Roll no. for change data: ")
    roll = get_roll()
    print("Enter data ")
    name = get_name()
    email = get_email()
    phone = get_phone()
    address = get_address()
    data = (name, email, phone, address, roll)
    query = "UPDATE student SET name = %s, email = %s, phone = %s, address = %s WHERE roll = %s"
    cur.execute(query, data)
    conn.commit()
    print("Student Details Updated Successfully!")
    

# Function to delete student details in database
def delete_student():
    print("Enter Roll no. for Delete data: ")
    roll = get_roll()
    query = "DELETE FROM student WHERE roll = %s"
    cur.execute(query, (roll,))
    conn.commit()
    print("Student Details Deleted Successfully!")
    

# Main function
def main():
    while True:
        print("Student Details")
        print("1. Add Students Details")
        print("2. Show Students Details")
        print("3. Update Students Details")
        print("4. Delete Students Details")
        print("5. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Please try again.")

# Excecution of Main Function
if __name__ == "__main__":
    main()