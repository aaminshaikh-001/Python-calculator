import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Calculator Result ---")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")

print("Power:", num1 ** num2)

if num1 >= 0:
    print("Square Root:", math.sqrt(num1))
else:
    print("Square Root: Not possible for negative numbers")
