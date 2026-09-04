import math

while True:
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "8":
        print("Thank you for using the calculator!")
        break

    if choice == "7":
        num = float(input("Enter a number: "))

        if num >= 0:
            print("Square Root:", math.sqrt(num))
        else:
            print("Error: Square root of a negative number is not possible.")

        continue

    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero.")

        elif choice == "5":
            print("Result:", num1 ** num2)

        elif choice == "6":
            if num2 != 0:
                print("Result:", num1 % num2)
            else:
                print("Error: Cannot calculate modulus with zero.")

    else:
        print("Invalid choice. Please select a number from 1 to 8.")