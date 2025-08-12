# Simple Calculator Program

# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Ask the user to input the operation using a letter
print("choose operation")
print("A -Addition")
print("S - Subtraction")
print("M -Multiplication")
print("D -Division")
Operation= input("Enter your choice(A/S/M/D):) ") .upper()

# Perform the operation based on user's input
if Operation == "A":
    result = num1 + num2
    print(f"{num1} A {num2} equals {result}")
elif Operation == "S":
    result = num1 - num2
    print(f"{num1} S {num2} equals {result}")
elif Operation == "M":
    result = num1 * num2
    print(f"{num1} M {num2} equals {result}")
elif Operation == "D":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} D {num2} equals {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter: plus, minus, multiply, or divide.")