def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get user input for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
result = gcd(num1, num2)

# Print the result
print("The GCD of", num1, "and", num2, "is:", result)
