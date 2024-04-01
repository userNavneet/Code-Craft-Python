# Take input from the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform addition
addition = num1 + num2

# Perform subtraction
subtraction = num1 - num2

# Perform multiplication
multiplication = num1 * num2

# Perform division (handling division by zero)
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
