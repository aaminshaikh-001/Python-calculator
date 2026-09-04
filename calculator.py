import math

history = []

while True:
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Show History")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("Thank you for using the calculator!")
        break

    if choice == "8":
        print("\n===== Calculation History =====")

        if history:
            for calculation in history:
                print(calculation)
        else:
            print("No calculations yet.")

        continue

    if choice == "7":
        num = float(input("Enter a number: "))

        if num >= 0:
            result = math.sqrt(num)
            calculation = f"√{num} = {result}"
            print("Result:", result)
            history.append(calculation)
        else:
            print("Error: Square root of a negative number is not possible.")

        continue

    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            calculation = f"{num1} + {num2} = {result}"

        elif choice == "2":
            result = num1 - num2
            calculation = f"{num1} - {num2} = {result}"

        elif choice == "3":
            result = num1 * num2
            calculation = f"{num1} × {num2} = {result}"

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue

            result = num1 / num2
            calculation = f"{num1} / {num2} = {result}"

        elif choice == "5":
            result = num1 ** num2
            calculation = f"{num1} ^ {num2} = {result}"

        elif choice == "6":
            if num2 == 0:
                print("Error: Cannot calculate modulus with zero.")
                continue

            result = num1 % num2
            calculation = f"{num1} % {num2} = {result}"

        print("Result:", result)
        history.append(calculation)

    else:
        print("Invalid choice. Please select a number from 1 to 9.")
        