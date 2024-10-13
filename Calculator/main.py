# Age calculator and normal calculator

while True:
    print("Choose Calculator")
    print("1. Normal Calculator")
    print("2. Age Calculator")
    print("3. Exite")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        import simple_calculator
        simple_calculator.main()
    
    elif choice == 2:
        import age_calculator
        age_calculator.main()

    elif choice == 3:
        break

    else:
        print("Invalid Input!")