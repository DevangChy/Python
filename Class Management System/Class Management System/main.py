# class management System

import class_System.marks
import class_System.monitor
import class_System.student


def main():
    while True:
        print("Choose Option For See Class Details")
        print("1. Student Details")
        print("2. Monitor Details")
        print("3. Student's Marks Details")
        print("4. Exite")
        
        choise = int(input("Enter Your Choise:"))

        if choise == 1:
            class_System.student.main()
        
        elif choise == 2:
            class_System.monitor.main()

        elif choise == 3:
            class_System.marks.main()

        elif choise == 4:
            break

        else:
            print("Eneter Valid Input")


if __name__ == "__main__":
    main()