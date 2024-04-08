# Take initial values of variables from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Printing initial values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping without using a third variable
a = a + b
b = a - b
a = a - b

# Printing swapped values
print("\nAfter swapping:")
print("a =", a)
print("b =", b)