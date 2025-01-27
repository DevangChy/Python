# Marks Management System

# add Show Update delete
# roll name term s1 s2 s3 total percentage
import mysql.connector as mydb

# connection to the database
conn = mydb.connect(host="localhost", user="root", password="Devang@2004", database="class")
cur = conn.cursor()

# Function to get Student Roll No
def get_roll():
    while True:
        try:
            roll = int(input("Enter Student Roll No: "))
            return roll
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")

# Function to get Student Name
def get_name():
    return input("Enter Student Name: ")

# Function to get Student term
def get_term():
    return input("Enter Student Term: ")

# Function to Add Student's Marks Details
def add_marks():
    roll = get_roll()
    name = get_name()
    term = get_term()
    s1 = int(input("Enter First Subject Marks: "))
    s2 = int(input("Enter Secon Subject Marks: "))
    s3 = int(input("Enter Third Subject Marks: "))
    total = (s1 + s2 + s3)
    percentage = total / 3
    data = (roll, name, term, s1, s2, s3, total, percentage)
    query = "INSERT INTO marks (roll, name, term, s1, s2, s3, total, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(query, data)
    conn.commit()
    print("Student Marks Added Successfully!")

# Function to Show Student's Marks Details
def show_marks():
    roll = get_roll()
    query = "SELECT * FROM marks WHERE roll = %s"
    cur.execute(query, (roll,))
    marks = cur.fetchone()
    if marks:
        print("Marks Details:")
        print(f"Roll No.: {marks[0]}")
        print(f"Name: {marks[1]}")
        print(f"Term: {marks[2]}")
        print(f"Subject 1 Marks: {marks[3]}")
        print(f"Subject 2 Marks: {marks[4]}")
        print(f"Subject 3 Marks: {marks[5]}")
        print(f"Total Marks: {marks[6]}")
        print(f"Percentage: {marks[7]}")
    else:
        print("Marks Details not found.")

# Function to Update Student's Marks Details
def update_marks():
    print("Enter Roll no. for change Marks data: ")
    roll = get_roll()
    name = get_name()
    term = get_term()
    s1 = int(input("Enter First Subject Marks: "))
    s2 = int(input("Enter Second Subject Marks: "))
    s3 = int(input("Enter Third Subject Marks: "))
    total = (s1 + s2 + s3)
    percentage = total / 3
    data = (name, term, s1, s2, s3, total, percentage, roll)
    query = "UPDATE marks SET name = %s, term = %s, s1 = %s, s2 = %s, s3 = %s, total = %s, percentage = %s WHERE roll = %s"
    cur.execute(query, data)
    conn.commit()
    print("Marks Details Updated Successfully!")
    

# Function to delete student details in database
def delete_marks():
    print("Enter Roll no. for Delete data: ")
    roll = get_roll()
    query = "DELETE FROM marks WHERE roll = %s"
    cur.execute(query, (roll,))
    conn.commit()
    print("Marks Details Deleted Successfully!")
    

# Main function
def main():
    while True:
        print("Marks Details")
        print("1. Add Marks Details")
        print("2. Show Marks Details")
        print("3. Update Marks Details")
        print("4. Delete Marks Details")
        print("5. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_marks()
        elif choice == "2":
            show_marks()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            delete_marks()
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Please try again.")

# Excecution of Main Function
if __name__ == "__main__":
    main()