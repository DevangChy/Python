# Calculator
# Operation For + , -, *, /, %

def add(num_1, num_2):
    return num_1 + num_2

def sub(num_1, num_2):
    return num_1 - num_2

def mul(num_1, num_2):
    return num_1 * num_2

def div(num_1, num_2):
    if(num_2 == 0):
        print("Value Does not divide by 0 !")
    return num_1 / num_2

def rem(num_1, num_2):
    return num_1 % num_2

def main():
    while True:
        print("Simple Calculator")
        print("1. Addition (+)")
        print("2. Substraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Reminder (%)")
        print("6. Exite")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            num_1 = int(input("Enter First Number: "))
            num_2 = int(input("Enter Second Number: "))
            print(add(num_1, num_2))
        
        elif choice == 2:
            num_1 = int(input("Enter First Number: "))
            num_2 = int(input("Enter Second Number: "))
            print(sub(num_1, num_2))

        elif choice == 3:
            num_1 = int(input("Enter First Number: "))
            num_2 = int(input("Enter Second Number: "))
            print(mul(num_1, num_2))

        elif choice == 4:
            num_1 = int(input("Enter First Number: "))
            num_2 = int(input("Enter Second Number: "))
            print(div(num_1, num_2))

        elif choice == 5:
            num_1 = int(input("Enter First Number: "))
            num_2 = int(input("Enter Second Number: "))
            print(rem(num_1, num_2))

        elif choice == 6:
            break

        else:
            print("invalide Input!")

if __name__ == "__main__":
    main()