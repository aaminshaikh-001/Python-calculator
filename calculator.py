import math

history = []


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


while True:
    print("\n" + "=" * 35)
    print("        PYTHON CALCULATOR")
    print("=" * 35)
    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Power")
    print("6.  Modulus")
    print("7.  Square Root")
    print("8.  Show History")
    print("9.  Factorial")
    print("10. Cube Root")
    print("11. Absolute Value")
    print("12. Clear History")
    print("13. Exit")
    print("=" * 35)

    choice = input("Enter your choice (1-13): ").strip()

    # Exit
    if choice == "13":
        print("\nThank you for using the calculator!")
        break

    # Show History
    if choice == "8":
        print("\n===== Calculation History =====")

        if history:
            for number, calculation in enumerate(history, start=1):
                print(f"{number}. {calculation}")
        else:
            print("No calculations yet.")

        continue

    # Clear History
    if choice == "12":
        if history:
            history.clear()
            print("Calculation history cleared.")
        else:
            print("History is already empty.")

        continue

    # Square Root
    if choice == "7":
        num = get_number("Enter a number: ")

        if num >= 0:
            result = math.sqrt(num)
            calculation = f"√{num} = {result}"
            print("Result:", result)
            history.append(calculation)
        else:
            print("Error: Square root of a negative number is not possible.")

        continue

    # Factorial
    if choice == "9":
        num = get_number("Enter a non-negative integer: ")

        if num < 0 or not num.is_integer():
            print("Error: Factorial requires a non-negative integer.")
        else:
            num = int(num)
            result = math.factorial(num)
            calculation = f"{num}! = {result}"
            print("Result:", result)
            history.append(calculation)

        continue

    # Cube Root
    if choice == "10":
        num = get_number("Enter a number: ")

        result = math.copysign(abs(num) ** (1 / 3), num)
        calculation = f"∛{num} = {result}"
        print("Result:", result)
        history.append(calculation)

        continue

    # Absolute Value
    if choice == "11":
        num = get_number("Enter a number: ")

        result = abs(num)
        calculation = f"|{num}| = {result}"
        print("Result:", result)
        history.append(calculation)

        continue

    # Basic Operations
    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

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
        print("Error: Invalid choice. Please select a number from 1 to 13.")