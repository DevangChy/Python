# Monitor Management System

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

# Function to get student monitor month
def get_months():
    return input("Enter Student Month for monitor Position: ")

# Function to add Monitor Details
def add_monitor():
    roll = get_roll()
    name = get_name()
    months = get_months()
    data = (roll, name, months)
    query = "INSERT INTO monitor (roll, name, months) VALUES (%s, %s, %s)"
    cur.execute(query, data)
    conn.commit()
    print("Monitor Details Added Successfully!")

# Function to show Monitor Details
def show_monitor():
    roll = get_roll()
    query = "SELECT * FROM monitor WHERE roll= %s"
    cur.execute(query, (roll,))
    monitor = cur.fetchone()
    if monitor:
        print("Monitor Details")
        print(f"Roll No.: {monitor[0]}")
        print(f"Name: {monitor[1]}")
        print(f"months: {monitor[2]}")
    else: 
        print("Monitor not found.")

# Function to Update Monitor Details
def update_monitor():
    print("Enter Roll no. for update monitor details: ")
    roll = get_roll()
    print("Enter Details That can be update")
    name = get_name()
    months = get_months()
    data = (name, months, roll)
    query = "UPDATE monitor SET name = %s, months = %s WHERE roll = %s"
    cur.execute(query, data)
    conn.commit()
    print("Monitor Details Update Successfully!")

# Function to Delete Monitor Details
def delete_monitor():
    print("Enter Roll no. for delete monitor details: ")
    roll = get_roll()
    query = "DELETE FROM monitor WHERE roll = %s"
    cur.execute(query, (roll,))
    conn.commit()
    print("Monitor Details Delete Successfully!")

# Main Function
def main():
    while True:
        print("Monitor Details")
        print("1. Add Monitor Details")
        print("2. Show Monitor Details")
        print("3. Update Monitor Details")
        print("4. Delete Monitor Details")
        print("5. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_monitor()
        elif choice == "2":
            show_monitor()
        elif choice == "3":
            update_monitor()
        elif choice == "4":
            delete_monitor()
        elif choice == "5":
            break
        else:
            print("Invalid Choice. Please try again.")

# Excecution of Main Function
if __name__ == "__main__":
    main()